from django.contrib.auth.models import User

from blogs.models import Blog, Post
from rest_framework import serializers

class BlogOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class BlogsListSerializer(serializers.ModelSerializer):

    user = BlogOwnerSerializer(read_only=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title','summary','multimedia','publication_date')