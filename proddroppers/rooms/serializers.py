from rest_framework import serializers

from rooms.models import Rooms


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = (
            Rooms.id.field.name,
            Rooms.name.field.name,
        )
