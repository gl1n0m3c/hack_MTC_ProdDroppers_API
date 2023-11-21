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


class FriendsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(source="user2.id")
    username = serializers.CharField(source="user2.username")
    image = serializers.ImageField(source="user2.usernewfields.image")

    class Meta:
        model = FriendsAssepted
        fields = ["user_id", "username", "image"]


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
