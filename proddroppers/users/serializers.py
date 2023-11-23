from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import NewUser


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            User.id.field.name,
            User.username.field.name,
            User.email.field.name,
        )


class UsersSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(source="id")
    username = serializers.CharField()
    image = serializers.ImageField(source="new_fields.image")

    class Meta:
        model = NewUser
        fields = ["user_id", "username", "image"]
