from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from django.http import HttpResponse

from .models import Album, User
from .serializer import AlbumSerializer, UserSerializer, UserDetailSerializer

from drf_yasg.utils import swagger_auto_schema

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg import openapi

from rest_framework.pagination import PageNumberPagination, CursorPagination

from django_filters.rest_framework import DjangoFilterBackend


from rest_framework import filters

class StandardPagination(CursorPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    # max_page_size = 10
    ordering = '-created_at'

class AlbumViewSet(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pass

class UserViewSet(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['username',] # field like
    ordering_fields = '__all__' # order by
    ordering = '-created_at'
    filterset_fields = ['username',] # field =
    
    @swagger_auto_schema(
        # manual_parameters=[
        #     openapi.Parameter(
        #         name='Authorization',
        #         in_=openapi.IN_HEADER,
        #         type=openapi.TYPE_STRING,
        #         required=True,
        #         description='Basic <token>'
        #     ),
        # ],
        tags=['User'],
        operation_description='GET /articles/today/',
        operation_id='List User',
        operation_summary='Test',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['User'],
        operation_description='POST /articles/today/',
        operation_id='Create User',
        operation_summary='Test',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    pass

class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        tags=['User'],
        operation_description='',
        operation_id='Get User by Id',
        operation_summary='Test',
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['User'],
        operation_description='',
        operation_id='Put User by Id',
        operation_summary='Test',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=['User'],
        operation_description='',
        operation_id='Patch User by Id',
        operation_summary='Test',
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=['User'],
        operation_description='',
        operation_id='Delete User by Id',
        operation_summary='Test',
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    pass
