"""
Configurations for the Todos application.

This file defines the application configuration for the Todos app.
"""

from django.apps import AppConfig


class TodosConfig(AppConfig):
    """Configuration class for the Todos application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "todos"
