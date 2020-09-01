from ..models.user_info import UserInfo
from rest_framework import serializers

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        # exclude = ('user', )
        fields = ['first_name', 'last_name']
