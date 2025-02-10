import os
import datetime
import logging

from pathlib import Path

import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config.SECRET_KEY

DEBUG = config.DEBUG

RECAPTCHA_PUBLIC_KEY = config.RECAPTCHA_PUBLIC_KEY
RECAPTCHA_PRIVATE_KEY = config.RECAPTCHA_PRIVATE_KEY

ALLOWED_HOSTS = [
    'arma72.com', 'www.arma72.com', 'arma72.ru', 'www.arma72.ru',
    'www.mc.yandex.ru', 'mc.yandex.ru',
    '66.249.66.162',  # Googlebot
]

COOKIE_EXPIRES_TIMEDELTA = datetime.timedelta(days=365)
BASKET_COOKIES_RANDOM_STRING_LENGTH = 32
NOT_ALLOWED_COUNTRIES = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'main',
    'shop',
    'CRM',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'arma.middlewares.blockipmiddleware.BlockIPMiddleware',
    'arma.middlewares.shop.BasketCookiesMiddleware',
]

ROOT_URLCONF = 'arma.urls'

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
                'arma.context_processors.base_dependencies'
            ],
            'libraries': {
                'filters': 'arma.templatetags.filters',
            }
        },
    },
]

WSGI_APPLICATION = 'arma.wsgi.application'


# Logging
LOG_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s\n%(exc_info)s"
        },
        "simple": {
            "format": "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s\n%(exc_info)s"
            # "format": "[%(levelname)s] %(message)s"
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOG_DIR, "django.log"),
            "maxBytes": 5 * 1024 * 1024,  # 5MB
            "backupCount": 10,  # Храним до 10 архивных логов
            "formatter": "verbose",
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOG_DIR, "django_errors.log"),
            "maxBytes": 5 * 1024 * 1024,  # 5MB
            "backupCount": 10,
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["error_file"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    },
    'mys': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config.DB_NAME,
        'USER': config.DB_USER,
        'PASSWORD': config.DB_PASS,
        'HOST': config.DB_HOST,
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # Принудительно задаём режим SQL
        },
    }
}

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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

START_TIME_AT_THE_COMPANY = datetime.time(hour=8, minute=0)
END_TIME_AT_THE_COMPANY = datetime.time(hour=22, minute=0)

USE_I18N = True

USE_TZ = True

# CRSF
CSRF_TRUSTED_ORIGINS = [
    'https://arma72.com', 'https://www.arma72.com', 'https://arma72.ru', 'https://www.arma72.ru',
    'https://www.mc.yandex.ru', 'https://mc.yandex.ru',
    'http://66.249.66.162', 'https://66.249.66.162' # Googlebot
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

MEDIA_ROOT = 'media/'
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
