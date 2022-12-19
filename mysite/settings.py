"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qcv1s!6id0lsd652tzs-ddaz0_lw3*a&tj5d^3t_*!y_c#rr1-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '*'
]
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',  # for localhost (REACT Default)
    'http://192.168.0.50:3000',  # for network 
    'http://localhost:8080',  # for localhost (Developlemt)
    'http://192.168.0.50:8080',  # for network (Development)
    'http://uit.techdoor.space:80',
)

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',  # for localhost (REACT Default)
    'http://103.75.185.190:4444',  # for network 
    'http://localhost:8080',  # for localhost (Developlemt)
    'http://192.168.0.50:8080',  # for network (Development)
    'http://uit.techdoor.space:80',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'course',
    'minio_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'mydb',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': '103.75.185.190',
        'PORT': '5003',
    }   
    
}
import os
# S3 Storage MINIO

DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
MINIO_STORAGE_ENDPOINT = 'http://103.75.185.190:9000/'
MINIO_STORAGE_ACCESS_KEY = 'ROOTNAME'
MINIO_STORAGE_SECRET_KEY = 'CHANGEME123'
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'second-bucket'
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
# MINIO_STORAGE_STATIC_BUCKET_NAME = 'local-static'
# MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
