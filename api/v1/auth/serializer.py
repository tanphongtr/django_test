from rest_framework import serializers
from django.contrib.auth.models import (
    User,
    Group,
    GroupManager,
    Permission,
    ContentType,
)
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    # content_type = ContentTypeSerializer()
    class Meta:
        model = Permission
        fields = '__all__'

class AuthGroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True, )
    class Meta:
        model = Group
        fields = '__all__'

class ContentTypeSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True, )
    # permissionss = serializers.CharField()
    class Meta:
        model = ContentType
        fields = '__all__'