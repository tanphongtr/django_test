from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django_test.models import File
from .serializer import FileSerializer

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, CursorPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
# from .pagination import LinkHeaderPagination, CustomPagination as CustomPagination2

class FileViewSet(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    # search_fields = ['name', ]  # field like
    ordering_fields = '__all__'  # order by
    # ordering = '-name'
    # filterset_fields = ['name', ]  # field =

    @swagger_auto_schema(
        tags=['Files'],
        operation_description='',
        operation_id='List Files',
        operation_summary='Test',
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Files'],
        operation_description='',
        operation_id='Create Files',
        operation_summary='Test',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
