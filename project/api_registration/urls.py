from django.urls import path, include
from project.api_registration.views import django_rest_auth_null, VerifyEmailView

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/account-email-verification-sent/', django_rest_auth_null, name='account_email_verification_sent'),
    path('password-reset/confirm/<str:uidb64>)/<str:token>/', django_rest_auth_null, name='password_reset_confirm')
]
