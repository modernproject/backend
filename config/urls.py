from django.urls import include, path
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import verify_jwt_token
from .routers import DefaultRouter

from project.posts.urls import router as posts_router
from project.users.urls import router as users_router

router = DefaultRouter()
router.extend(posts_router)
router.extend(users_router)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('verify_token/', verify_jwt_token),
    path('', include('project.users.urls')),
    path('', include('project.api_registration.urls')),
    path('docs/', include_docs_urls(title='Modern Project'))
]
