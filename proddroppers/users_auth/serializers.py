from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "password2",
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
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {
                    "success": "False",
                    "description": "Поля паролей не совпадают.",
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
