from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )

    def validate(self, attrs):
        users = User.objects.all()
        for u in users:
            if attrs["email"] == u.email:
                raise serializers.ValidationError(
                    {
                        "success": "False",
                        "description": "Такая почта уже зарегистрирована!",
                    },
                )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["email"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    def validate(self, attrs):
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )
        if user is None:
            raise serializers.ValidationError(
                {
                    "success": "False",
                    "description": "Неверный логин или пароль",
                },
            )
        return attrs

    def create(self, validated_data):
        return authenticate(
            username=validated_data["username"],
            password=validated_data["password"],
        )
