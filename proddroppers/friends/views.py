from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from friends.models import FriendsAssepted, FriendsNotAssepted
from friends.serializers import FriendsSerializer, FriendsWaitingSerializer


error_response = {
    "success": False,
    "description": ["Ты отправил мне какую-то дичь"],
}


def checker(request):
    try:
        receiver = request.data["receiver"]
        sender = request.data["sender"]

        if not (isinstance(receiver, int) and isinstance(sender, int)):
            raise ValueError

        user1 = User.objects.get(pk=sender)
        user2 = User.objects.get(pk=receiver)
    except (User.DoesNotExist, KeyError, ValueError):
        return (None, None, None, None)
    return (sender, receiver, user1, user2)


class FriendsAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        friends = FriendsAssepted.objects.get_friends(pk)

        serializer = FriendsSerializer(friends, many=True)

        return Response(serializer.data)


class FriendsWaitingAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        friends = FriendsNotAssepted.objects.get_friends(pk)

        serializer = FriendsWaitingSerializer(friends, many=True)

        return Response(serializer.data)


class FriendsAddAPI(APIView):
    def post(self, request, *args, **kwargs):
        sender, receiver, user1, user2 = checker(request)
        if user1 is None:
            return Response(error_response)

        friends = FriendsAssepted.objects.get_friends(sender)
        friends_waiting_user1 = FriendsNotAssepted.objects.get_friends(sender)
        friends_waiting_user2 = FriendsNotAssepted.objects.get_friends(
            receiver,
        )

        for friend in friends:
            if friend.user2.id == receiver:
                return Response(
                    {
                        "success": False,
                        "description": [
                            "Вы уже добавили этого пользователя в друзья!",
                        ],
                    },
                )

        for friend in friends_waiting_user1:
            if friend.user1.id == receiver:
                return Response(
                    {
                        "success": False,
                        "description": [
                            "Этот пользователь уже отправил вам заявку!",
                        ],
                    },
                )

        for friend in friends_waiting_user2:
            if friend.user1.id == sender:
                return Response(
                    {
                        "success": False,
                        "description": [
                            "Вы уже отправили заявку этому пользователю!",
                        ],
                    },
                )

        FriendsNotAssepted.objects.create(
            user1=user1,
            user2=user2,
        )

        return Response(
            {
                "success": True,
                "description": ["Ваша заявка успешно отправлена!"],
            },
        )


class FriendsAsseptAPI(APIView):
    def post(self, request, *args, **kwargs):
        sender, receiver, user1, user2 = checker(request)
        if user1 is None:
            return Response(error_response)

        friends = FriendsNotAssepted.objects.get_friends(receiver)

        for friend in friends:
            if friend.user1.id == sender:
                friend.delete()
                FriendsAssepted.objects.create(
                    user1=user1,
                    user2=user2,
                )
                return Response(
                    {
                        "success": True,
                        "description": ["Заявка принята!"],
                    },
                )
        return Response(
            {
                "success": False,
                "description": [
                    "Этот пользователь не отправлял вам запрос в друзья!",
                ],
            },
        )


class FriendsRejectAPI(APIView):
    def post(self, request, *args, **kwargs):
        sender, receiver, user1, user2 = checker(request)
        if user1 is None:
            return Response(error_response)

        friends = FriendsNotAssepted.objects.get_friends(receiver)

        for friend in friends:
            if friend.user1.id == sender:
                friend.delete()
                return Response(
                    {
                        "success": True,
                        "description": ["Заявка отклонена!"],
                    },
                )
        return Response(
            {
                "success": False,
                "description": [
                    "Этот пользователь не отправлял вам запрос в друзья!",
                ],
            },
        )


class FriendsDeleteAPI(APIView):
    def post(self, request, *args, **kwargs):
        sender, receiver, user1, user2 = checker(request)
        if user1 is None:
            return Response(error_response)

        friends_sender = FriendsAssepted.objects.get_friends(pk=sender)

        for friend in friends_sender:
            if friend.user2.id == receiver:
                friend.delete()

                return Response(
                    {
                        "success": True,
                        "description": ["Пользователь удален!"],
                    },
                )
        return Response(
            {
                "success": False,
                "description": ["Этот пользователь не является вашим другом!"],
            },
        )
