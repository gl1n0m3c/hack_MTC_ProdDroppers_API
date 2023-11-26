from rest_framework import serializers


class MusicSerializer(serializers.Serializer):
    music_id = serializers.IntegerField(source="id")
    name = serializers.CharField()
    artist_name = serializers.CharField(source="albom.artist")
    image = serializers.ImageField(source="albom.image")
    file = serializers.FileField(source="music_file")
