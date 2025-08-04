"""Serializers for version 1 of the API .

Exported Classes:
- UserDetailSerializerV1: Serializer for user details in version 1 of the API.
- RegisterSerializerV1: Serializer for user registration in version 1 of the API.
- LoginSerializerV1: Serializer for user login in version 1 of the API.
"""

from .login import LoginSerializer as LoginSerializerV1
from .register import RegisterSerializer as RegisterSerializerV1
from .user import UserDetailSerializer as UserDetailSerializerV1

__all__: list[str] = [
    "UserDetailSerializerV1",
    "RegisterSerializerV1",
    "LoginSerializerV1",
]
