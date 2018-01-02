from django.urls import include, path
from django.contrib import admin
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verify_token/', verify_jwt_token),
    path('', include('project.users.urls')),
]
