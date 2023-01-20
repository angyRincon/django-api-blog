from rest_framework import serializers
from ..models import Post
from users.api.serializers import UserGetSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserGetSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']
