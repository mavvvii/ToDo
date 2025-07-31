"""User Profile ViewSet for Version 1 of the API."""

from typing import List, Type
from uuid import UUID

from django.contrib.auth.tokens import default_token_generator
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from users.models import User
from users.serializers import UserDetailSerializerV1


class UserProfileViewSet(GenericViewSet):
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
    permission_classes: List[Type[BasePermission]] = [AllowAny]
    pagination_class: None = None

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
