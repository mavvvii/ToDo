"""Views for version 1 of the API .

Exported Classes:
- UserViewSetV1: A viewset that handles user-related operations in API version 1.
"""

from .cookie_token_refresh import CookieTokenRefreshView as CookieTokenRefreshViewV1
from .login import LoginView as LoginViewV1
from .profile import UserProfileViewSet as UserProfileViewSetV1
from .register import UserRegisterView as UserRegisterViewV1

__all__ = [
    "LoginViewV1",
    "UserProfileViewSetV1",
    "UserRegisterViewV1",
    "CookieTokenRefreshViewV1",
]
