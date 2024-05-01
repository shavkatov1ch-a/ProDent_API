from django.shortcuts import render
from .models import (Post,
                     Tag,
                     About,
                     Service,
                     Blog)
from .serializers import *
from rest_framework import generics


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializers


class ServiceAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers


class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class HomeAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers