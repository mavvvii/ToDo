"""Serializers for version 1 of the API .

Exported Classes:
- UserDetailSerializerV1: Serializer for user details in version 1 of the API.
"""

from .detail import UserDetailSerializer as UserDetailSerializerV1

__all__ = [
    "UserDetailSerializerV1",
]
