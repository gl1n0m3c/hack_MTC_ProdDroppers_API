from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            User.objects.get(username=request.data["email"])
        except User.DoesNotExist:
            user = User.objects.create(
                username=request.data["email"],
                email=request.data["email"],
            )
            user.set_password(request.data["password"])
            user.save()
            return Response(
                {
                    "success": ["True"],
                    "description": ["Регистрация прошла успешно"],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": ["False"],
                "description": ["Такая почта уже зарегистрирована"],
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class LoginUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = authenticate(
            username=request.data["username"],
            password=request.data["password"],
        )
        if user is None:
            return Response(
                {
                    "success": ["False"],
                    "description": ["Неверный логин или пароль"],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "success": ["True"],
                "description": ["Авторизация прошла успешно"],
            },
            status=status.HTTP_200_OK,
        )


class ChangePasswordView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.data["id"])
        except User.DoesNotExist:
            return Response(
                {
                    "success": ["False"],
                    "description": ["Такого пользователя нету"],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        auth_user = authenticate(
            username=user.username,
            password=request.data["old_password"],
        )
        if auth_user is None:
            return Response(
                {
                    "success": ["False"],
                    "description": ["Неверный пароль"],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.set_password(request.data["new_password"])
        user.save()
        return Response(
            {
                "success": ["True"],
                "description": ["Пароль успешно изменен"],
            },
            status=status.HTTP_200_OK,
        )
