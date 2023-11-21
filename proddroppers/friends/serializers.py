from rest_framework import serializers

from friends.models import FriendsAssepted, FriendsNotAssepted


class FriendsSerializer(serializers.Serializer):
    friend_id = serializers.IntegerField(source="user2.id")
    username = serializers.CharField(source="user2.username")
    image = serializers.ImageField(source="user2.new_fields.image")

    class Meta:
        model = FriendsAssepted
        fields = ["friend_id", "username", "image"]


class FriendsWaitingSerializer(serializers.ModelSerializer):
    friend_id = serializers.IntegerField(source="user1.id")
    username = serializers.CharField(source="user1.username")
    image = serializers.ImageField(source="user1.new_fields.image")

    class Meta:
        model = FriendsNotAssepted
        fields = ["friend_id", "username", "image"]
