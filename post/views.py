from django.db.models import query
from django.shortcuts import render
from .models import Post 
from rest_framework import generics,permissions
from .serializers import PostSerialzer
# Create your views here.

class PostList (generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class PostDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    