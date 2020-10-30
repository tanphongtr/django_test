from rest_framework import serializers
from django_test.models import Post

class PostSerializer(serializers.ModelSerializer):
    test = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

    def get_test(self, arg):
        # print('=============================', self)
        print(arg, self.context['request'].user)
        return 1

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'