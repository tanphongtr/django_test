from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from django_test.models import Post
from .serializers import PostSerializer

class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pass