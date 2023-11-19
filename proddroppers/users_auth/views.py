from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework import generics


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
