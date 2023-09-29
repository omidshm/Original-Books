from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'django-insecure-a1afwr1p5wxne+(%i)puyn7-=_*s&z+zq!#$7ca$xbu!v9dw*x'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore',
        'USER': 'root',
        'PASSWORD': '1212',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}