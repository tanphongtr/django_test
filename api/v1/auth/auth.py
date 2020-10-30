from rest_framework.authtoken import views
from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import (
    Group,
    Permission,
    ContentType,
)
from .serializer import (
    AuthSerializer,
    AuthGroupSerializer,
    PermissionSerializer,
    ContentTypeSerializer,
)

class AuthViewSet(generics.CreateAPIView):
    serializer_class = AuthTokenSerializer

    @swagger_auto_schema(
        tags=['Auth'],
        operation_description='',
        operation_id='Login',
        operation_summary='Test',
        responses={
            200: AuthSerializer(),
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
                'user': user.username
            }
        )
    pass

class PermissonViewSet(generics.ListCreateAPIView):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()

class AuthGroupViewSet(generics.ListCreateAPIView):
    serializer_class = AuthGroupSerializer
    queryset = Group.objects.all()

class ContentTypeViewSet(generics.ListCreateAPIView):
    serializer_class = ContentTypeSerializer
    queryset = ContentType.objects.all()