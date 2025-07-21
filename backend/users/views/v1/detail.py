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

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from users.models import User
from users.serializers import UserDetailSerializerV1


class UserViewSet(GenericViewSet):
    """User ViewSet handling user details for version 1 of the API.

    This viewset allows authenticated users to retrieve a list of all users or
    fetch a specific user by their ID.

    Attributes:
        queryset (QuerySet): All user objects.
        serializer_class (Type[Serializer]): Serializer used for user details.
        permission_classes (list): List of permission classes required to access the endpoints.
        pagination_class (None): Pagination is disabled for this view.
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
        if self.action in ["list", "retrieve"]:
            return [IsAuthenticated()]
        return super().get_permissions()

    def list(self, request: Request, *args, **kwargs) -> Response:
        """Return a list of all users.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            Response: A Response object containing serialized user data.
        """
        queryset: QuerySet[User] = self.get_queryset()
        serializer: UserDetailSerializerV1 = UserDetailSerializerV1(queryset, many=True)
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
