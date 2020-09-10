from rest_framework import serializers
from ..models import BaseUser
from .UserInfoSerializer import UserInfoSerializer


class BaseUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = BaseUser
        fields = '__all__'

    def create(self, validated_data):
        user = BaseUser.objects.create(
            # id=validated_data['id']
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
