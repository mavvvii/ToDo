"""Views for version 1 of the API .

Exported Classes:
- UserViewSetV1: A viewset for retrieving user details in API version 1. It allows authenticated
  users to list all users or fetch a specific user by ID.
"""

from .detail import UserViewSet as UserViewSetV1

__all__ = [
    "UserViewSetV1",
]
