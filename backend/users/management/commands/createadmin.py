"""
Command to create a superuser if one does not already exist.

This command checks if a superuser exists in the database, and if not,
creates one using environment variables for username, email, and password.
It is intended to be run as a management command in a Django application.
"""

import os
import sys
from typing import Type

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.management.base import BaseCommand

UserModel: Type[AbstractUser] = get_user_model()


class Command(BaseCommand):
    """Command to create a superuser if one does not already exist."""

    def handle(self, *args, **options) -> None:
        """Create a superuser if one does not already exist."""
        if UserModel.objects.using("default").filter(is_superuser=True).count() == 0:
            username: str = os.environ.get("DJANGO_ADMIN_USER", "admin")
            email: str = os.environ.get("DJANGO_ADMIN_EMAIL", "admin@example.com")
            password: str = os.environ.get("DJANGO_ADMIN_PASSWORD", "admin")
            sys.stdout.write(f"Creating account for {username} \n")

            admin = UserModel.objects.create_superuser(
                username=username, email=email, password=password
            )
            admin.save()
        else:
            sys.stdout.write(
                "There can be only one administrator account! Can not create the other one. \n"
            )
