from allauth.account.views import confirm_email
from django.urls import path, include
from rest_framework import routers
from project.users.views import UserViewSet, django_rest_auth_null

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/account-email-verification-sent/', django_rest_auth_null, name='account_email_verification_sent'),
    path('registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email')
]
