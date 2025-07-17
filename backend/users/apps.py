"""
Configuration for the Users application.

This file defines the application configuration for the Users app.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration class for the Users application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
