from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission: write allowed only to the author of the post.
    Read allowed to anyone.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of the post
        return obj.author == request.user or getattr(obj.author, "username", None) == request.user.username


class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD API for posts:
      GET    /api/blog/posts/
      POST   /api/blog/posts/
      GET    /api/blog/posts/{id}/
      PUT    /api/blog/posts/{id}/
      PATCH  /api/blog/posts/{id}/
      DELETE /api/blog/posts/{id}/
    """
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as author
        serializer.save(author=self.request.user)
