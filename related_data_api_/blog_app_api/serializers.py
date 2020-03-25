from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(read_only=True, source="user.user_name")

    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_content', 'user', 'user_name')
        # extra_kwargs = {'user': {'read_only': True}}
        # depth = 1


class MiniBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
