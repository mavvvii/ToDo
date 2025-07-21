"""
User serializers module.

This module provides versioned serializers for the User model, used in different API versions.

Exported Classes:
- UserDetailSerializerV1: Serializer for user details in version 1 of the API.

Typical usage example:
    from users.serializers import UserDetailSerializerV1

    serializer_class = UserDetailSerializerV1
"""

from .v1 import UserDetailSerializerV1

__all__ = [
    "UserDetailSerializerV1",
]
