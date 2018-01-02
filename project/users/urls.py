from django.conf.urls import url, include
from rest_framework import routers
from project.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls'))
]
