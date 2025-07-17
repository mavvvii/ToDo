"""
Celery configuration for the ToDo application.

This file sets up the Celery application and configures it to work with Django.
"""

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app: Celery = Celery("todo_celery")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
