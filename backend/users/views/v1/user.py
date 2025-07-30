"""
User viewsets for API version 1.

This module provides versioned viewsets for handling user-related operations
such as listing all users or retrieving a specific user. Access is restricted
to authenticated users.

Classes:
    UserViewSetV1: ViewSet for listing and retrieving users in API v1.

Example:
    from users.views import UserViewSetV1
"""

from typing import List, Type
from uuid import UUID

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db import IntegrityError
from django.db.models import Q, QuerySet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (
    AllowAny,
    BasePermission,
    IsAuthenticated,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from users.models import User
from users.serializers import RegisterSerializerV1, UserDetailSerializerV1


class UserViewSet(GenericViewSet):
    """User ViewSet handling user details for version 1 of the API.

    This viewset allows authenticated users to retrieve a list of all users or
    fetch a specific user by their ID.

    Attributes:
        queryset (QuerySet): All user objects.
        serializer_class (Type[Serializer]): Serializer used for user details.
        permission_classes (list): List of permission classes required to access the endpoints.
        pagination_class (None): Pagination is disabled for this view.
    Methods:
        get_permissions: Returns the list of permission instances required for the current action.
        get_serializer: Returns the appropriate serializer based on the action.
        list: Returns a list of all users.
        retrieve: Returns a user by their primary key.
        create: Creates a new user if the provided data is valid.
        activate: Activates a user account by clicking the link with the token.
    """

    queryset: QuerySet[User] = User.objects.all()
    serializer_class: Type[UserDetailSerializerV1] = UserDetailSerializerV1
    permission_classes: List[Type[BasePermission]] = [IsAuthenticated]
    pagination_class: None = None

    def get_permissions(self) -> list[BasePermission]:
        """Return the list of permission instances required for the current action.

        For the 'list' and 'retrieve' actions, only authenticated users are allowed.
        For all other actions, the default permission behavior is used.

        Returns:
            list[BasePermission]: A list of permission instances.
        """
        if self.action in ["create"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer(self, *args, **kwargs):
        """Return the appropriate serializer based on the action.

        If the action is 'create', it returns the RegisterSerializerV1.
        Otherwise, it returns the default serializer.

        Returns:
            Type[UserDetailSerializerV1 | RegisterSerializerV1]: The serializer class to use
        """
        if self.action == "create":
            return RegisterSerializerV1(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def list(self, request: Request, *args, **kwargs) -> Response:
        """Return a list of all users.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            Response: A Response object containing serialized user data.
        """
        queryset: QuerySet[User] = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request: Request, pk: UUID, *args, **kwargs) -> Response:
        """Return a user by their primary key.

        Args:
            request (Request): The incoming HTTP request.
            pk (uuid): The primary key of the user to retrieve.

        Returns:
            Response: A Response object containing the user's data or an error message.
        """
        try:
            queryset: QuerySet[User] = self.get_queryset().get(pk=pk)
        except queryset.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request, *args, **kwargs) -> Response:
        """Create a new user with the provided data.

        Args:
            request (Request): The incoming HTTP request containing user data.

        Returns:
            Response: A Response object indicating the result of the user creation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = self.get_queryset().filter(
            Q(username=serializer.validated_data["username"])
            | Q(email=serializer.validated_data["email"])
        )
        if users.exists():
            return Response({"detail": "User already exists."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_user = serializer.save()

            user_id: UUID = new_user.id
            token: str = default_token_generator.make_token(new_user)

            activation_link: str = f"http://localhost:8000/api/v1/users/{user_id}/activate/{token}/"

            send_mail(
                subject="Activate your account",
                message=f"Click the link to activate your account: {activation_link}",
                from_email="noreply@yourdomain.com",
                recipient_list=[new_user.email],
            )

        except (ValidationError, IntegrityError) as e:
            return Response(
                {
                    "detail": "Error occurred during user creation or email sending.",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(
            {
                "detail": "User created successfully.",
                "message": "Check your email to activate your account.",
            },
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=True,
        methods=["get"],
        url_path="activate/(?P<token>[^/.]+)",
        permission_classes=[AllowAny],
    )
    def activate(self, request: Request, pk: UUID, token: str) -> Response:
        """Activates a user account by clicking the link with the token.

        Args:
            request (Request): The incoming HTTP request.
            pk (UUID): The primary key of the user to activate.
            token (str): The activation token from the URL.

        Returns:
            Response: A Response object indicating the activation status.
        """
        try:
            user: User = self.get_queryset().get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "User Does Not Exist."}, status=status.HTTP_404_NOT_FOUND)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"detail": "Account has been activated."}, status=status.HTTP_200_OK)

        return Response({"detail": "Invalid activation link."}, status=status.HTTP_400_BAD_REQUEST)
