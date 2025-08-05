"""Register Serializer for User Login."""

from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """Serializer for user login.

    Provides serialization and validation logic for user login
    used in version 1 of the API.

    Attributes:
        username (str): Username used for login.
        password (str): Password for the user account.
        remember_me (bool): Indicates whether to remember the user session.
    """

    username: serializers.CharField = serializers.CharField()
    password: serializers.CharField = serializers.CharField()
    remember_me: serializers.BooleanField = serializers.BooleanField(required=False, default=False)

    def update(self, instance, validated_data):
        """Update method is not implemented for LoginSerializer."""
        raise NotImplementedError("`update()` must be implemented.")

    def create(self, validated_data):
        """Create method is not implemented for LoginSerializer."""
        raise NotImplementedError("`create()` must be implemented.")
