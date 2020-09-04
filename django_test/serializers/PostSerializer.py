from ..models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(format="%s")
    class Meta:
        model = Post
        fields = '__all__'