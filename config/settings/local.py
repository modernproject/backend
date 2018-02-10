from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_WHITELIST = (
    'localhost',
)

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default='ip_address')
