from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django_test.models import Parent
from .serializer import ParentSerializer

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, CursorPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
# from .pagination import LinkHeaderPagination, CustomPagination as CustomPagination2

class ParentViewSet(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', ]  # field like
    ordering_fields = '__all__'  # order by
    ordering = '-name'
    filterset_fields = ['name', ]  # field =

    @swagger_auto_schema(
        tags=['Parent'],
        operation_description='',
        operation_id='List Parent',
        operation_summary='Test',
    )
    # def get(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset().all())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Parent'],
        operation_description='',
        operation_id='Create Parent',
        operation_summary='Test',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ParentDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    @swagger_auto_schema(
        tags=['Parent'],
        operation_description='',
        operation_id='Get Parent by ID',
        operation_summary='Test',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Parent'],
        operation_description='',
        operation_id='Put Parent by ID',
        operation_summary='Test',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Parent'],
        operation_description='',
        operation_id='Patch Parent by ID',
        operation_summary='Test',
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Parent'],
        operation_description='',
        operation_id='Delete Parent by ID',
        operation_summary='Test',
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
