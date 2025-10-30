from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all()
    )

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
