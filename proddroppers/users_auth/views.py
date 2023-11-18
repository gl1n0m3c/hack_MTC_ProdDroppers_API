from django.contrib.auth.models import User
from rest_framework import generics

from users_auth.serializers import UserSerializer


def logout(request):
    pass


def sign_up(request):
    pass


def login(request):
    pass


class Test(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
