from rest_framework import serializers
from .models import (Post,
                     About,
                     Tag,
                     Service,
                     Blog,
                     Home)


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read = ['created', 'update']


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read = ['created', 'update']


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read = ['created', 'update']


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read = ['created', 'update']


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read = ['created', 'update']


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        read = ['created', 'update']



