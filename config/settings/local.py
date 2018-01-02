from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_NAME'),
        'USER': env.str('POSTGRES_USER'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.int('POSTGRES_PORT'),
    }
}

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default='ip_address')
