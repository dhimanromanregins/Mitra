"""
Django settings for Mitra project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d428@iu6&#y1@)zrb=1r&d8kd@kq_w2=%%a(l+_o&m1rkck7as'




# Application definition

INSTALLED_APPS = [
     'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mitraapp',
     'rest_framework',
    'rest_framework_api_key',
    'corsheaders',
    'registration',
    'videoupload',
    'userlist',
    'report',
    'videolist',
    'statusapp',
    'relationship'
    # 'chatapp'

]
#from decouple import config

# API_KEY = "tb2V8II2"
# API_KEY_CUSTOM_HEADER = "HTTP_X_API_KEY"
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework_api_key.permissions.HasAPIKey',
#     ],
#     # Other DRF settings...
# }
# REST_FRAMEWORK_API_KEY = {
#     'DEFAULTS': {
#         'DEFAULT_AUTHENTICATION_CLASSES': (
#             'rest_framework_api_key.authentication.DefaultAPIKeyAuthentication',
#         ),
#         'DEFAULT_KEY': 'your_default_api_key_here',
#     },
# }
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ],
#     # Other settings...
# }

import os
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# this middleware for authentication
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
# ]
MIDDLEWARE = [
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

]
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
# }

ROOT_URLCONF = 'Mitra.urls'
CORS_ORIGIN_ALLOW_ALL = True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
STATIC_URL = 'static/'

WSGI_APPLICATION = 'Mitra.wsgi.application'

# settings.py



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgresqladmin',
#         'PASSWORD': 'Siance@123',
#         'HOST': 'sspmitra.postgres.database.azure.com',
#         'PORT': '5432',  # The default PostgreSQL port
#     }
# #       'custom_user_db': {
# #         'ENGINE': 'django.db.backends.postgresql',
# #         'NAME': 'postgres',
# #         'USER': 'postgresqladmin',
# #         'PASSWORD': 'Siance@123',
# #         'HOST': 'chatdb.postgres.database.azure.com',
# #         'PORT': '5432',  # The default PostgreSQL port
# #     },
#  }









# DATABASE_ROUTERS = [
#     'Mitra.custom_user_router.CustomUserRouter',
# ]



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'defaultdb',
        'USER': 'vultradmin',
        'PASSWORD': 'AVNS_9kb5IW7kOfkbLYcH5Xs',
        'HOST': 'vultr-prod-653ca7f5-d140-4221-9802-209c3156704e-vultr-prod-8ba8.vultrdb.com',  # Replace with your PostgreSQL server's address if necessary
        'PORT': '16751',          # Leave empty to use the default PostgreSQL port (usually 5432)
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Backend Database',
#         'USER': 'vultradmin',
#         'PASSWORD': 'AVNS_9kb5IW7kOfkbLYcH5Xs',
#         'HOST': 'localhost',  # Replace with your PostgreSQL server's address if necessary
#         'PORT': '16751',          # Leave empty to use the default PostgreSQL port (usually 5432)
#     }
# }
AUTH_USER_MODEL = 'registration.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'














import os
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#DEBUG = True
#ALLOWED_HOSTS = []

DEBUG = True

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#216 219 212 database 221
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your SMTP server hostname
EMAIL_PORT = 587  # Port for TLS (587 for TLS, 465 for SSL)
EMAIL_USE_TLS = True  # Use TLS encryption
EMAIL_HOST_USER = 'srutee03@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'yswq okhi enmt vgzo'


import os
# from storages.backends.azure_storage import AzureStorage
#
#
# # AZURE_ACCOUNT_NAME = 'csg10032002fb0ba2aa'
# # AZURE_ACCOUNT_KEY = '6ofACEdLTIu0s4CnDRTRmsfrrtGQMC1kCn5Rz4KLx4KWY3ChKUDAqtkSHoccwphTybD+GeuCjrZ7+AStmLP0bw=='
# # AZURE_CONTAINER = 'filecont'
# #
# # DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
# # AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
# #
# # MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_CONTAINER}/'


# settings.py

import boto3
#
# # Vultr Object Storage credentials
# VULTR_HOSTNAME = "blr1.vultrobjects.com"
# VULTR_ACCESS_KEY = "3M5ECKPL2BBJUK7C2IPG"
# VULTR_SECRET_KEY = "Q60vtZGsZkJ7P7dwfHdJzzNHT3E4RzjeI0dlYEbU"
# VULTR_BUCKET_NAME = "your-new-bucket"  # Replace with your bucket name
#
# # Initialize the Boto3 S3 client
# session = boto3.session.Session()
# VULTR_S3_CLIENT = session.client('s3', region_name=VULTR_HOSTNAME.split('.')[0], endpoint_url=f"https://{VULTR_HOSTNAME}",
#                                  aws_access_key_id=VULTR_ACCESS_KEY, aws_secret_access_key=VULTR_SECRET_KEY)

# import vultr
#
# # Vultr Object Storage settings
# VULTR_API_KEY = 'ZDO4X43RG77KPCPOIW5G3GWO5LJ75KD6HHYA'
# VULTR_OBJECT_STORAGE_NAME = 'MitraStorage'
# VULTR_CONTAINER = 'storagemi'
#
# # Initialize the Vultr client
# vultr_client = vultr.Vultr(VULTR_API_KEY)
#
# # List your Vultr Object Storage instances
# object_storage_instances = vultr_client.object_storage.list()
#
# # Find the Object Storage instance with the name "MitraStorage"
# instance_id = None
# for instance in object_storage_instances:
#     if instance['label'] == VULTR_OBJECT_STORAGE_NAME:
#         instance_id = instance['object_storage_id']
#         break
#
# if instance_id:
#     # Upload a file to the chosen instance
#     file_path = 'path_to_your_local_file.txt'
#     object_name = 'my_uploaded_file.txt'
#
#     with open(file_path, 'rb') as file:
#         vultr_client.object_storage.upload(instance_id, VULTR_CONTAINER, object_name, file)
#
#     # List objects in your instance
#     objects = vultr_client.object_storage.list_objects(instance_id, VULTR_CONTAINER)
#
#     # Delete an object from the instance
#     object_name_to_delete = 'my_uploaded_file.txt'
#     vultr_client.object_storage.delete_object(instance_id, VULTR_CONTAINER, object_name_to_delete)
# else:
#     print(f"Object Storage instance '{VULTR_OBJECT_STORAGE_NAME}' not found.")
#
# settings.py
#
# import vultr
#
# # Vultr Object Storage settings
# VULTR_API_KEY = 'ZDO4X43RG77KPCPOIW5G3GWO5LJ75KD6HHYA'
# VULTR_OBJECT_STORAGE_NAME = 'MitraStorage'
# VULTR_CONTAINER = 'your-new-bucket'
#
# # Vultr Object Storage URL
# VULTR_CUSTOM_DOMAIN = f'{VULTR_OBJECT_STORAGE_NAME}.objectstorage.vultr.com'
# MEDIA_URL = f'https://{VULTR_CUSTOM_DOMAIN}/{VULTR_CONTAINER}/'
#
# # Initialize the Vultr client
# vultr_client = vultr.Vultr(VULTR_API_KEY)

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#change the database, 276-83 and urls-40-41 comment this
# settings.py

# # Use S3 for media storage
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_STORAGE_BUCKET_NAME = 'your-new-bucket'  # Replace with your bucket name
# AWS_S3_REGION_NAME = 'blr1.vultrobjects.com'
# AWS_ACCESS_KEY_ID = '3M5ECKPL2BBJUK7C2IPG'
# AWS_SECRET_ACCESS_KEY = 'Q60vtZGsZkJ7P7dwfHdJzzNHT3E4RzjeI0dlYEbU'



# settings.py
# settings.py

# settings.py

AWS_ACCESS_KEY_ID = '3M5ECKPL2BBJUK7C2IPG'
AWS_SECRET_ACCESS_KEY = 'Q60vtZGsZkJ7P7dwfHdJzzNHT3E4RzjeI0dlYEbU'
AWS_STORAGE_BUCKET_NAME = 'your-new-bucket'  # Replace with your Vultr Object Storage bucket name
AWS_S3_ENDPOINT_URL = 'https://blr1.vultrobjects.com'  # Use your Vultr Object Storage endpoint

# Use the Vultr S3Boto3Storage backend
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'





