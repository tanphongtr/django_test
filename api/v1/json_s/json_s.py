from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_test.models import File, JsonS
from .serializer import (
    JsonStructureSerializer,
    JsonSSerializer,
)
from rest_framework import filters
from rest_framework.pagination import (
    PageNumberPagination,
    CursorPagination,
    LimitOffsetPagination,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser


class JsonSViewSet(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser, )
    queryset = JsonS.objects.all()
    serializer_class = JsonSSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    # search_fields = ['name', ]  # field like
    ordering_fields = '__all__'  # order by
    # ordering = '-name'
    # filterset_fields = ['name', ]  # field =


    @swagger_auto_schema(
        tags=['Json S'],
        operation_description='',
        operation_id='Json S',
        operation_summary='Test',
    )
    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_201_CREATED)

        # jsons_serializer = JsonStructureSerializer(data=data)

        # if jsons_serializer.is_valid():

        #     serializer = self.get_serializer()

        #     serializer.save(data=data)

        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(jsons_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        print('=====', args)
        return super().post(request, *args, **kwargs)
