from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from django_test.models import Post
from .serializers import PostSerializer

class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects

    print(queryset.query)
    serializer_class = PostSerializer

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='List Post',
        operation_summary='Test',
    )
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().all())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='Create Post',
        operation_summary='Test',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class PostDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uuid'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='Get Post by ID',
        operation_summary='Test',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='Put Post by ID',
        operation_summary='Test',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='Patch Post by ID',
        operation_summary='Test',
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='Delete Post by ID',
        operation_summary='Test',
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)