"""Module users.models contains the custom user model for the user implementation.

Exported Classes:
- User: Custom user model extending Django's AbstractUser.
    Functions:
    - __str__: Returns the username of the user.

Typical usage:
    from users.models import User
"""

from .user import User

__all__: list[str] = ["User"]
