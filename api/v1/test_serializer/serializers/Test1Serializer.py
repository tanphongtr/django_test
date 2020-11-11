from django_test.models import child
from rest_framework import serializers, fields
import json
from django_test.models import TestSerializer

class ListAsJsonField(fields.ListField):
    """
    Converts an incoming list of string values to json.
    This field is _very_ primitive, lots of edge cases may break it.
    """
    child = fields.CharField(min_length=1) # always use a char field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, data):
        """Convert to our output representation.  Assumes input is always valid json now"""
        return json.loads(data)

    def to_internal_value(self, data):
        """Convert to the internal value -> database (and validated_data)"""
        return json.dumps(data)

class Test1Serializer(serializers.ModelSerializer):
    props1 = serializers.ListField(child=serializers.CharField())
    # props1 = serializers.ListField(child=serializers.CharField())
    # props1 = ListAsJsonField()

    class Meta:
        model = TestSerializer
        fields = '__all__'

    def validate_props1(self, props1):
        print("========================", props1)
        props1 = json.dumps(props1)
        return props1

class Test1GetSerializer(serializers.ModelSerializer):
    props1 = serializers.JSONField(source='props1_json')
    # props1 = ListAsJsonField()

    class Meta:
        model = TestSerializer
        fields = '__all__'
