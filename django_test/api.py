from rest_framework import status, generics
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .models import Album, Track, User, Post
from .serializer import AlbumSerializer, TrackSerializer
from .serializers import UserSerializer, PostSerializer

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, CursorPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import LinkHeaderPagination, CustomPagination as CustomPagination2


class StandardPagination(CursorPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
    ordering = '-created_at'


class CustomPagination(LimitOffsetPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response(
            {
                "status": True,
                "code": status.HTTP_200_OK,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                # 'count': self.page.paginator.count,
                'results': data
            }
        )


class AlbumViewSet(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pass


class TrackViewSet(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    pass

class TrackDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    pass

class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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


class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'content', ]  # field like
    ordering_fields = '__all__'  # order by
    ordering = '-created_at'
    filterset_fields = ['title', ]  # field =
    pass

class PostDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uuid'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
