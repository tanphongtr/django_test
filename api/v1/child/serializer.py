from rest_framework import serializers
from django_test.models import Child
from ..parent.serializer import ParentSerializer

class ChildSerializer(serializers.ModelSerializer):
    parent = ParentSerializer()
    class Meta:
        model = Child
        fields = '__all__'

class ChildCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'