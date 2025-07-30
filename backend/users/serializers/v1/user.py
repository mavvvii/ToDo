"""Serializer for version 1 of the API."""

from typing import Type

from django.conf import settings
from rest_framework import serializers
from users.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailed user information.

    Provides serialization and validation logic for the User model
    used in version 1 of the API.

    Attributes:
        id (UUID): Unique identifier for the user.
        username (str): Username used for login.
        email (str): User's email address.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        is_active (bool): Indicates if the user account is active.
        is_staff (bool): Indicates if the user has staff privileges.
    """

    class Meta:
        """Meta options for UserDetailSerializer."""

        model: Type[User] = settings.AUTH_USER_MODEL
        fields: str = "__all__"

        read_only_fields: list[str] = ["id", "username", "email"]
