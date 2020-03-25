from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import BlogSerializer, MiniBlogSerializer
from .models import Blog
from rest_framework.response import Response


class BlogsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blog.objects.all()
    serializer_class = MiniBlogSerializer

    def list(self, request, *args, **kwargs):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
