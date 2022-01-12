"""
Django settings for digit_phone project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import tempfile
from pathlib import Path
from pathlib import Path
from typing import List

import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.contrib import messages
from django.contrib.messages import constants as message_constants
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()
SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
ALLOWED_HOSTS: List[str] = ['127.0.0.1', 'dnigne.herokuapp.com', '192.168.1.5', 'localhost']
# ALLOWED_HOSTS = []

# Application definition


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

OWN_APPS = [
    ## internal apps
    'blog.apps.BlogConfig',
    'core.apps.CoreConfig',
    'home.apps.HomeConfig',
    'user.apps.UserConfig',
    'phone',


]

THIRD_PARTY_APPS = [

    'mptt',
    # 'rest_framework',
    # 'corsheaders',
    'crispy_forms',
    'tinymce',
    # 'parler',
    # 'social_django',
    # 'whitenoise.runserver_nostatic',
    # 'formtools',
    # 'notification',
    # 'channels',
    # "bootstrap4",
    # "bootstrap_datepicker_plus",
    'import_export',
    # 'fontawesome-free',

]

INSTALLED_APPS += THIRD_PARTY_APPS + OWN_APPS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'digit_phone.urls'
DJANGO_NOTIFICATIONS_CONFIG = {'USE_JSONFIELD': True}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'digit_phone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
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

TIME_ZONE = 'Egypt'

USE_I18N = True
USE_L10N = True  # use localization
USE_TZ = True
gettext = lambda s: s
MODELTRANSLATION_LANGUAGES = ('en', 'ar')

LANGUAGES = (
    ('en', _('English')),
    ('ar', _('Arabic')),

)
LANGUAGE_COOKIE_NAME = 'django_language'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
CSS_LOCATION = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, "upload")
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

CORS_ORIGIN_ALLOW_ALL = True
MESSAGE_LEVEL = message_constants.DEBUG
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PAGINATE_BY = 10

MAIL_USE_SSL = True
EMAIL_USE_TLS = False
EMAIL_PORT = 465
EMAIL_HOST = 'ydoob.com'
EMAIL_HOST_USER = 'noreply@ydoob.com'
EMAIL_HOST_PASSWORD = '3q7wq5t9nuYBZxr'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_EMAIL_FROM = 'no-reply@ydoob.com'
# email stuff
# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_PORT='587'
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_HOST_USE = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# DEFAULT_EMAIL_FROM = env('DEFAULT_EMAIL_FROM')

#########User Authentication ############
AUTH_USER_MODEL = 'user.User'
SOCIAL_AUTH_USER_MODEL = 'user.User'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, picture.type(large), link, age_range'
}
SOCIAL_AUTH_FACEBOOK_AUTH_EXTRA_ARGUMENTS = {
    # 'auth_type': 'reauthenticate',
}

SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
    # 'access_type': 'offline',
    # 'approval_prompt': 'force',
}

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['first_name', 'email']
SOCIAL_AUTH_ADMIN_SEARCH_FIELDS = ['username', 'first_name', 'email']

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated usersaaa.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',

    ]
}
