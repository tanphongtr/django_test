from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status, generics
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .models import Album, Track, User, Post, BaseUser
from .serializer import AlbumSerializer, TrackSerializer
from .serializers import UserSerializer, PostSerializer, BaseUserSerializer, LoginSerializer

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

    @swagger_auto_schema(
        tags=['User'],
        operation_description='2222',
        operation_id='Get User list',
        operation_summary='Test',
    )
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)
        pass

    @swagger_auto_schema(
        tags=['User'],
        operation_description='2222',
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
        return super().get(request, *args, **kwargs)

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
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'content', ]  # field like
    ordering_fields = '__all__'  # order by
    ordering = '-created_at'
    filterset_fields = ['title', ]  # field =
    pass


class PostDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uuid'
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BaseUserViewSet(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    pass


class LoginViewSet(generics.GenericAPIView, ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['username']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
