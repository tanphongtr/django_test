from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django_test.models import Child
from .serializer import ChildSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from ..auth.authentication import _TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, CursorPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
# from .pagination import LinkHeaderPagination, CustomPagination as CustomPagination2

class ChildViewSet(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    authentication_classes = [_TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', ]  # field like
    ordering_fields = '__all__'  # order by
    ordering = '-name'
    filterset_fields = ['name', ]  # field =

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                required=False,
                description='Token <token>'
            ),
        ],
        tags=['Child'],
        operation_description='',
        operation_id='List Child',
        operation_summary='Test',
    )
    # def get(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset().all())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Child'],
        operation_description='',
        operation_id='Create Child',
        operation_summary='Test',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ChildDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    @swagger_auto_schema(
        tags=['Child'],
        operation_description='',
        operation_id='Get Child by ID',
        operation_summary='Test',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Child'],
        operation_description='',
        operation_id='Put Child by ID',
        operation_summary='Test',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Child'],
        operation_description='',
        operation_id='Patch Child by ID',
        operation_summary='Test',
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Child'],
        operation_description='',
        operation_id='Delete Child by ID',
        operation_summary='Test',
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
