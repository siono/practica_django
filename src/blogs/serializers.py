from django.contrib.auth.models import User
from datetime import datetime
from blogs.models import Blog, Post
from rest_framework import serializers

class BlogOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class BlogsListSerializer(serializers.ModelSerializer):

    user = BlogOwnerSerializer(read_only=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    posts_count = serializers.CharField(source='get_count_post')

    class Meta:
        model = Blog
        fields = ('id','user','url','name','description','posts_count')


class PostListSerializer(serializers.ModelSerializer):

    publication_date = serializers.DateTimeField(default=datetime.now())
    author = serializers.CharField(source='get_author')

    class Meta:
        model = Post
        fields = ('title','summary','body','multimedia','author','publication_date')

class PostDetailSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source='get_author')
    blog = serializers.StringRelatedField(many=False)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ('title','summary','body','multimedia','author','publication_date','created_at','modified_at','blog','categories')