"""
User views module.

This module defines versioned viewsets for handling operations related to the User model,
tailored to different API versions.

Exported Classes:
- UserViewSetV1: A viewset for retrieving user details in API version 1. It allows authenticated
  users to list all users or fetch a specific user by ID.

Typical usage example:
    from users.views import UserViewSetV1
"""

from .v1 import LoginViewV1, UserProfileViewSetV1, UserRegisterViewV1

__all__: list[str] = ["LoginViewV1", "UserRegisterViewV1", "UserProfileViewSetV1"]
