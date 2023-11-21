from rest_framework.response import Response
from rest_framework.views import APIView

from friends.models import FriendsAssepted, FriendsNotAssepted
from friends.serializers import FriendsSerializer, FriendsWaitingSerializer


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
    def post():
        pass
