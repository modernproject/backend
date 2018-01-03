from django.urls import include, path
from rest_framework import routers
from project.posts.views import PostViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
