from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django_test.models import Post
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
)
from rest_framework import filters
from rest_framework.pagination import (
    PageNumberPagination,
    CursorPagination,
    LimitOffsetPagination,
)
from django_filters.rest_framework import DjangoFilterBackend
# from .pagination import LinkHeaderPagination, CustomPagination as CustomPagination2

from rest_framework.exceptions import (
    APIException,
    MethodNotAllowed,
    PermissionDenied,
    NotFound,
)
from drf_yasg import openapi

class StandardPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
    ordering = '-created_at'

class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    # print('======', queryset.query)
    serializer_class = PostSerializer
    pagination_class = StandardPagination
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ['title', 'content', ]  # field like
    ordering_fields = '__all__'  # order by
    ordering = '-created_at'
    filterset_fields = ['title', ]  # field =

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='List Post',
        operation_summary='Test',
        security=[],
    )
    # def get(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset().all())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='Create Post',
        operation_summary='Test',
        # request_body=openapi.Schema(
        #     type=openapi.TYPE_OBJECT,
        #     required=['username'],
        #     properties={
        #         'username': openapi.Schema(type=openapi.TYPE_STRING)
        #     },
        # ),
    )
    def post(self, request, *args, **kwargs):
        self.serializer_class = PostCreateSerializer
        return super().post(request, *args, **kwargs)


class PostDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uuid'
    queryset = Post.objects.all()
    # print('======', list(queryset))
    
    serializer_class = PostSerializer

    serializers = {
        'list':    PostSerializer,
        'detail':  PostCreateSerializer,
        # etc.
    }

    def get_object(self):
        try:
            instance = super().get_object()
        except:
            raise NotFound(detail="LKDLSKLKSLD")
        return instance

    def get_serializer_class(self):
        from pprint import pprint
        pprint ( '=====A', self.request.method )
        return self.serializers.get(
            self.action,
            self.serializers['default']
        )

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='Get Post by ID',
        operation_summary='Test',
    )
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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
