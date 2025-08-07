"""User Login View for Version 1 of the API."""

from typing import Type

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.middleware import csrf
from rest_framework import status
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from users.serializers import LoginSerializerV1


class LoginView(APIView):
    """User Login View handling user authentication for version 1 of the API.

    Attributes:
        permission_classes (list): List of permission classes required to access the endpoints.
        serializer_class (Type[Serializer]): Serializer used for user login.

    Methods:
        post: Authenticates a user with the provided credentials and returns tokens.
        _get_tokens_for_user: Generates JWT tokens for the authenticated user.
        _user_validation_alerts: Validates the user and returns appropriate error messages.
    """

    permission_classes: list[Type[BasePermission]] = [AllowAny]
    serializer_class: Type[LoginSerializerV1] = LoginSerializerV1

    def _get_tokens_for_user(self, user: User) -> dict[str, str]:
        """Generate JWT tokens for the authenticated user.

        Args:
            user (User): The authenticated user object.

        Returns:
            dict[str, str]: A dictionary containing the refresh and access tokens.
        """
        refresh: RefreshToken = RefreshToken.for_user(user)

        return {
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),
        }

    def _user_validation_alerts(self, username: str | None) -> dict[str, str] | None:
        """Validate user credentials and return appropriate error messages.

        Args:
            username (str | None): The username provided by the user.

        Returns:
            dict[str, str] : A dictionary containing error details if validation fails.
        """
        user_model: Type[User] = get_user_model()

        try:
            user: User = user_model.objects.get(username=username)
            if not user.is_active:
                return {
                    "detail": "This account is not active!!",
                    "status": status.HTTP_403_FORBIDDEN,
                }
            return {
                "detail": "Invalid username or password!!",
                "status": status.HTTP_401_UNAUTHORIZED,
            }
        except user_model.DoesNotExist:
            return {"detail": "This user does not exist!!", "status": status.HTTP_401_UNAUTHORIZED}
        return None

    # pylint: disable=R1710
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Handle user login.

        Args:
            request (Request): The incoming HTTP request containing user credentials.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Response object containing the authentication tokens and CSRF token.
        """
        serializer: LoginSerializerV1 = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username: str | None = serializer.validated_data.get("username", None)
        password: str | None = serializer.validated_data.get("password", None)
        remember_me: bool = serializer.validated_data.get("remember_me", False)

        user: User | None = authenticate(username=username, password=password)

        csrf_token: str = csrf.get_token(request)

        if user is not None:
            if user.is_active:
                user_tokens: dict[str, str] = self._get_tokens_for_user(user)

                response: Response = Response(
                    {"tokens": user_tokens, "csrf_token": csrf_token, "remember_me": remember_me},
                    status=status.HTTP_200_OK,
                )

                response.set_cookie(
                    key=settings.SIMPLE_JWT["ACCESS_TOKEN_NAME"],
                    value=user_tokens["access_token"],
                    secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTPONLY"],
                    samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                    max_age=int(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds()),
                )

                response.set_cookie(
                    key=settings.SIMPLE_JWT["REFRESH_TOKEN_NAME"],
                    value=user_tokens["refresh_token"],
                    secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTPONLY"],
                    samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                    max_age=(
                        int(
                            settings.SIMPLE_JWT[
                                "REFRESH_TOKEN_LIFETIME_REMEMBER_ME"
                            ].total_seconds()
                        )
                        if remember_me
                        else None
                    ),
                )

                response.set_cookie(
                    key=settings.SIMPLE_JWT["CSRF_TOKEN_NAME"],
                    value=csrf_token,
                    secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    httponly=settings.SIMPLE_JWT["CSRF_COOKIE_HTTPONLY"],
                    samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                    max_age=(
                        int(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds())
                        if remember_me
                        else int(settings.SIMPLE_JWT["CSRF_TOKEN_LIFETIME"].total_seconds())
                    ),
                )

                response.data = {
                    "detail": "Login successfully",
                    "data": response.data,
                }
                return response

        else:
            response_data: dict[str, str] | None = self._user_validation_alerts(username)
            if response_data is None:
                return Response(
                    {"detail": "Invalid credentials."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response({"detail": response_data["detail"]}, status=response_data["status"])
