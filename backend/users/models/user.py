"""Defines the User model extending Django's AbstractUser with additional fields."""

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model with additional fields for enhanced user profiles.

    Attributes:
        id (UUIDField): Unique identifier for the user.
        username (str): The username of the user.
        password (str): The hashed password of the user.
        last_login (datetime): The last login time of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        is_staff (bool): Indicates whether the user can log into the admin site.
        is_active (bool): Indicates whether the user account is active.
        date_joined (datetime): The date and time when the user account was created.
        bio (str): A short biography of the user.
        is_superuser (bool): Indicates whether the user has all permissions without explicitly
                             assigning them.
        groups (ManyToManyField): Groups the user belongs to, which provides permissions.
        user_permissions (ManyToManyField): Specific permissions granted to the user.

    Methods:
        __str__: Returns the username of the user.
    """

    id: models.UUIDField = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio: models.TextField = models.TextField(max_length=2048, blank=True, null=True)
    email: models.EmailField = models.EmailField(unique=True, blank=False, null=False)
    is_active: models.BooleanField = models.BooleanField(default=False)

    REQUIRED_FIELDS: list[str] = ["email", "password"]

    def __str__(self) -> str:
        """Return the username of the user."""
        return self.username
