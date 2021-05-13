from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ada234567yhgvcxsaq123456ygvcs!@##'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',

]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

INTERNAL_IPS = ('127.0.0.1',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hospital_referal',
        'USER': 'root',
        'PASSWORD': 'Nep@l1234',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
