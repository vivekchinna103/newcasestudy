"""
Django settings for casestudy project.

Generated by 'django-admin startproject' using Django 4.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
STATIC_URL = 'static/'
STATICFILES_STORAGE= 'whitenoise.storage.CompressedManifestStaticFilesStorage'
BASE_DIR= Path(__file__).resolve(strict=True).parent.parent 
MEDIA_URL= '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,"media") 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9xh#z!zcn4+rtti@44+m-*a8vnk2wf3mgrvd6q^#c_n%t6bi1z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'CaseStudyApp.apps.CasestudyappConfig',
    'rest_framework',
    'storages'
]
CORS_ORIGIN_ALLOW_ALL= True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'casestudy.urls'

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

WSGI_APPLICATION = 'casestudy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        "NAME": "case-study-db",
        "USER": "dbadmin",
        "PASSWORD": "db@admin12345",
        "HOST": 'case-study-poc.database.windows.net',
        'Trusted_Connection': 'yes',
        'OPTIONS': {
           'driver': 'ODBC Driver 18 for SQL Server',}
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
STATIC_URL = 'static/'
MEDIA_URL ='/media/'
STATICFILES_STORAGE= 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_ROOT= os.path.join(BASE_DIR,"media")
STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles')
DEFAULT_FILE_STORAGE = 'casestudy.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'casestudy.custom_azure.AzureStaticStorage'


MEDIA_LOCATION = "cases"

AZURE_ACCOUNT_NAME = "cases1967"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'