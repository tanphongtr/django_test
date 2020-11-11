from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django_test.models import TestSerializer
from .serializers import (
    Test1Serializer,
    Test1GetSerializer,
)


class TestSerializer1ViewSet(generics.ListCreateAPIView):
    queryset = TestSerializer.objects.all()
    serializer_class = Test1Serializer

    @swagger_auto_schema(
        tags=['Test Serializers'],
        operation_description='',
        operation_id='Create Get',
        operation_summary='Test',
        responses=Test1GetSerializer()
    )
    def get(self, request, *args, **kwargs):
        self.serializer_class = Test1GetSerializer
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Test Serializers'],
        operation_description='',
        operation_id='Create Post',
        operation_summary='Test',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)