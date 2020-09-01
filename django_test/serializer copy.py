from .models import User, UserInfo, Album, Track
from rest_framework import serializers

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'
        # exclude = ('password', )
        # read_only_fields = ('username','created_at', 'updated_at', )

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('password', )

# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = ['order', 'title', 'duration']

# class AlbumSerializer(serializers.ModelSerializer):
#     # tracks = serializers.SlugRelatedField(
#     #     many=True,
#     #     read_only=True,
#     #     slug_field='title'
#     # )

#     tracks = TrackSerializer(many=True, read_only=True,)

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album