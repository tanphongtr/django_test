from rest_framework import serializers
from ..models import BaseUser


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = (
            'username',
            'password',
        )
