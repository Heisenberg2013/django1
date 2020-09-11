from django.shortcuts import render
# include many views under one thus view sets.
# Create your views here.
from rest_framework import viewsets
from .serializers import PostSerializers
from .models import Post

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializers # specifying the  serializer class from which to take the JSON response from
    queryset = Post.objects.all() # picks all objects of class posts and puts into query set
