from .models import Album, Track
from rest_framework import serializers

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer()

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('tracks')
    #     album = Album.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album
    def create(self, validated_data):
        track_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        Track.objects.create(album=album, **track_data)
        return album