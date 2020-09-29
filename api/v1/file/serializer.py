from rest_framework import serializers
from django_test.models import FileDetail, File

class FileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileDetail
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    file = FileDetailSerializer()
    class Meta:
        model = File
        fields = '__all__'


