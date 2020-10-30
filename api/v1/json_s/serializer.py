from rest_framework import serializers
from django_test.models import JsonS

class ListProp(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class AObj(serializers.Serializer):
    prop1 = serializers.CharField()
    listprop = ListProp(many=True)

class JsonStructureSerializer(serializers.Serializer):
    AOBJ = AObj()
    BOBJ = serializers.CharField()

class JsonSSerializer(serializers.ModelSerializer):
    data = serializers.CharField()
    class Meta:
        model = JsonS
        fields = '__all__'

