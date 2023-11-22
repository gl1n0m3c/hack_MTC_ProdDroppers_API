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


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = (
            NewUser.id.field.name,
            NewUser.username.field.name,
        )
