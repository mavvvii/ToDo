"""Cookie Token Refresh View."""

from django.conf import settings
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenRefreshView


class CookieTokenRefreshView(TokenRefreshView):
    """View to handle token refresh requests with cookie support.

    Methods:
        get_serializer: Returns the serializer class for the current action.
        post: Handles the POST request to refresh tokens and set cookies.
    """

    def get_serializer(self, *args, **kwargs):
        """Get the serializer class for the current action.

        Args:
            args: Positional arguments for the serializer.
            kwargs: Keyword arguments for the serializer.

        Raises:
            InvalidToken: If the refresh token is not provided in the request data or cookies.

        Returns:
            TokenRefreshSerializer: An instance of the TokenRefreshSerializer.
        """
        if "data" in kwargs and "refresh" not in kwargs["data"]:
            refresh_from_cookie: str = self.request.COOKIES.get("refresh_token")
            if not refresh_from_cookie:
                raise InvalidToken("No refresh token provided.")
            kwargs["data"]["refresh"] = refresh_from_cookie
        return super().get_serializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Handle POST requests for token refresh.

        Args:
            request (Request): The request object containing the refresh token.

        Returns:
            Response: A response object with the new access and refresh tokens.
        """
        serializer: TokenRefreshSerializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            return Response({"detail": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        access_token: str = serializer.validated_data.get("access")
        csrf_token: str = get_token(request)

        response: Response = Response(serializer.validated_data, status=status.HTTP_200_OK)

        response.set_cookie(
            key=settings.SIMPLE_JWT["ACCESS_TOKEN_NAME"],
            value=access_token,
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTPONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            max_age=int(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds()),
        )

        response.set_cookie(
            key=settings.SIMPLE_JWT["CSRF_TOKEN_NAME"],
            value=csrf_token,
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["CSRF_COOKIE_HTTPONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            max_age=(int(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds())),
        )

        return response
