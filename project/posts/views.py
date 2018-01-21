from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny

from project.posts.models import Post
from project.posts.serializers import PostSerializer, PostListSerializer
from project.posts.permissions import IsAvailableArticle

class PostViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing posts.
    """
    queryset = Post.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action is 'list':
            permission_classes = [IsAuthenticatedOrReadOnly]
        elif self.action is 'metadata':
            permission_classes = [AllowAny]
        elif self.action is 'retrieve':
            permission_classes = [IsAvailableArticle]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action is 'list':
            return PostListSerializer
        else:
            return PostSerializer

