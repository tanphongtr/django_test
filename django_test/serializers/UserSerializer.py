from rest_framework import serializers
from ..models import User, UserInfo
from .UserInfoSerializer import UserInfoSerializer

class UserSerializer(serializers.ModelSerializer):
    profile = UserInfoSerializer()
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        UserInfo.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        print('UPDATE')
        profile_data = validated_data.pop('profile')

        print('profile_data => ', profile_data)

        print('instance => ', instance)

        profile = instance.profile

        print('profile => ', profile)

        instance.username = validated_data.get('username', instance.username)
        profile.first_name = profile_data.get('first_name', profile.first_name)
        # instance.email = validated_data.get('email', instance.email)
        instance.save()
        profile.save()

        return instance
