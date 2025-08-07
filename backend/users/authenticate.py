"""Custom authentication class that enforces CSRF protection."""

from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import CSRFCheck
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomCookiesAuthentication(JWTAuthentication):
    """Custom authentication class that enforces CSRF protection.

    Methods:
        _enforce_csrf: Enforces CSRF validation on the request.
        authenticate: Authenticates the user and enforces CSRF validation.
    """

    def _enforce_csrf(self, request: Request) -> None:
        """Enforces CSRF validation on the request.

        Args:
            request (Request): The incoming HTTP request.

        Raises:
            PermissionDenied: If CSRF validation fails.
        """
        check = CSRFCheck(get_response=lambda request: None)
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        if reason:
            raise exceptions.PermissionDenied(f"CSRF Failed: {reason}")

    def authenticate(self, request: Request):
        """Authenticate the user and enforces CSRF validation.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            tuple[AuthUser, Token]: A tuple containing the authenticated user and the token.
        """
        header = self.get_header(request)

        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE"]) or None
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        self._enforce_csrf(request)
        return self.get_user(validated_token), validated_token
