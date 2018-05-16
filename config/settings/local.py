from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_WHITELIST = (
    'localhost',
)

# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default='ip_address')
ALLOWED_HOSTS = ['*',]

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
