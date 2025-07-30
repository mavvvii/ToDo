"""Views for version 1 of the API .

Exported Classes:
- UserViewSetV1: A viewset that handles user-related operations in API version 1.
"""

from .user import UserViewSet as UserViewSetV1

__all__ = [
    "UserViewSetV1",
]
