"""
Custom User model for the application.

This model extends Django's AbstractUser to include additional fields.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model extending Django's AbstractUser."""

    bio: models.TextField = models.TextField(max_length=2048, blank=True, null=True)
    email: models.EmailField = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self) -> str:
        """Return the username of the user."""
        return self.username
