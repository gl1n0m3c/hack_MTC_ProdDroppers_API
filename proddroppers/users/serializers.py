from django.contrib.auth.models import User
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
        return [friend.user2.username for friend in obj]


class FriendsWaitingSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField()

    class Meta:
        model = FriendsAssepted
        fields = ["friends"]

    def get_friends(self, obj):
        return [friend.user2.username for friend in obj]
