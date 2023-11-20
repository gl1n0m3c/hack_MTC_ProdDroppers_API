from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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
        user = get_object_or_404(User, pk=pk)
        friends = FriendsAssepted.objects.get_friends(pk)

        context = {"username": user.username}
        return Response(FriendsSerializer(friends, context=context).data)


class FriendsWaitingAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        friends = FriendsNotAssepted.objects.get_friends(pk)

        return Response(FriendsWaitingSerializer(friends).data)


class FriendsAddAPI(APIView):
    def post():
        pass
