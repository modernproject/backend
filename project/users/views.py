from django.contrib.auth import get_user_model
from project.users.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
