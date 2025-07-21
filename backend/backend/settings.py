"""Django settings for the backend ToDo application.

This module contains the settings and configurations for the Django application,
including database connections, installed apps, middleware, and other configurations.
"""

import os
from datetime import timedelta
from pathlib import Path
from typing import Any

BASE_DIR: Path = Path(__file__).resolve().parent.parent


SECRET_KEY: str | None = os.environ.get("DJANGO_SECRET_KEY")
DEBUG: bool = os.environ.get("DJANGO_PRODUCTION", "False") == "True"

assert SECRET_KEY, "SECRET_KEY environment variable must be set"

ALLOWED_HOSTS: list[str] = ["*"]

REDIS_HOST: str = os.environ.get("REDIS_HOST", "redis_container")
REDIS_PORT: str = os.environ.get("REDIS_PORT", "6379")
REDIS_DB: str = os.environ.get("REDIS_DB", "0")

CELERY_BROKER_URL: str = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

CELERY_RESULT_BACKEND: str = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

CELERY_ACCEPT_CONTENT: list[str] = ["application/json"]
CELERY_TASK_SERIALIZER: str = "json"
CELERY_RESULT_SERIALIZER: str = "json"

INSTALLED_APPS: list[str] = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "celery",
    "users",
    "todos",
]

MIDDLEWARE: list[str] = [
    "whitenoise.middleware.WhiteNoiseMiddleware",  # For serving static files
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF: str = "backend.urls"

TEMPLATES: list[dict[str, Any]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION: str = "backend.wsgi.application"


DATABASES: dict[str, dict[str, str | None]] = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DJANGO_DATABASE_NAME"),
        "USER": os.environ.get("DJANGO_DATABASE_USER"),
        "PASSWORD": os.environ.get("DJANGO_DATABASE_PASSWORD"),
        "HOST": os.environ.get("DJANGO_DATABASE_HOST"),
        "PORT": os.environ.get("DJANGO_DATABASE_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK: dict[str, Any] = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "1000/day",
        "user": "10000/day",
    },
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "DEFAULT_VERSION": "v1",
    "ALLOWED_VERSIONS": [
        "v1",
    ],
}

SIMPLE_JWT: dict[str, timedelta] = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(weeks=4),
}

LANGUAGE_CODE: str = "en-us"
TIME_ZONE: str = "UTC"
USE_I18N: bool = True
USE_TZ: bool = True

STATIC_URL: str = "static/"
STATIC_ROOT: str = "static/"

AUTH_USER_MODEL = "users.User"

DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"
