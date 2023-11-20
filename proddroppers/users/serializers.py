from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from users.models import FriendsAssepted, FriendsNotAssepted


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            User.id.field.name,
            User.username.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
            User.email.field.name,
        )


class FriendsSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField()

    class Meta:
        model = FriendsNotAssepted
        fields = ["friends"]

    def get_friends(self, obj):
        username = self.context["username"]
        result = list()
        for friend in obj:
            if friend.user1.username == username:
                result.append(
                    {"id": friend.user2.id, "name": friend.user2.username}
                )
            else:
                result.append(
                    {"id": friend.user1.id, "name": friend.user1.username}
                )
        return result


class FriendsWaitingSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField()

    class Meta:
        model = FriendsAssepted
        fields = ["friends"]

    def get_friends(self, obj):
        result = list()
        for friend in obj:
            result.append(
                {"id": friend.user1.id, "name": friend.user1.username}
            )
        return result
