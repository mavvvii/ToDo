"""
User serializers module.

This module provides versioned serializers for the User model, used in different API versions.

Exported Classes:
- UserDetailSerializerV1: Serializer for user details in version 1 of the API.
- RegisterSerializerV1: Serializer for user registration in version 1 of the API.

Typical usage example:
    from users.serializers import UserDetailSerializerV1

    serializer_class = UserDetailSerializerV1

    -----------------------------------------------------
    from users.serializers import RegisterSerializerV1

    serializer_class = RegisterSerializerV1
"""

from .v1 import RegisterSerializerV1, UserDetailSerializerV1

__all__ = [
    "UserDetailSerializerV1",
    "RegisterSerializerV1",
]
