from rest_framework import serializers
from django_test.models import Parent
from ..child.serializer import ChildSerializer

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

    # child = ChildSerializer()