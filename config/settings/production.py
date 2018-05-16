from .base import *

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
