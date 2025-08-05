"""Register Serializer for User Registration."""

from typing import Type

from rest_framework import serializers
from users.models import User


class RegisterSerializer(serializers.Serializer):
    """Serializer for user registration.

    Provides serialization and validation logic for user registration
    used in version 1 of the API.

    Attributes:
        username (str): Username used for login.
        email (str): User's email address.
        password (str): Password for the user account.
    """

    username: serializers.CharField = serializers.CharField()
    email: serializers.EmailField = serializers.EmailField()
    password: serializers.CharField = serializers.CharField()

    class Meta:
        """Meta options for RegisterSerializer."""

        fields = ["username", "email", "password"]

    def create(self, validated_data):
        """Create a new user instance with the validated data.

        Args:
            validated_data (dict): Data validated by the serializer.

        Returns:
            User: The created user instance.
        """
        user: Type[User] = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        """Update method is not implemented for registration serializer."""
        raise NotImplementedError("Update method is not implemented for registration serializer.")
