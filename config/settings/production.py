from .base import *

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

SECRET_KEY = env.str('DJANGO_SECRET_KEY')
