from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import FriendsAssepted, FriendsNotAssepted
from users.serializers import (
    FriendsSerializer,
    FriendsWaitingSerializer,
    UserSerializer,
)


class DetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)
        return Response(UserSerializer(user).data)


class FriendsAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        friends = FriendsAssepted.objects.get_friends(pk)

        serializer = FriendsSerializer(friends, many=True)

        return Response(serializer.data)


class FriendsWaitingAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        friends = FriendsNotAssepted.objects.get_friends(pk)

        return Response(FriendsWaitingSerializer(friends).data)


class FriendsAddAPI(APIView):
    def post():
        pass
