"""
Board viewsets for API version 1.

This module provides versioned viewsets for handling board-related operations
such as listing all boards or retrieving a specific board. Access is restricted
to authenticated users.

Classes:
    BoardViewSetV1: ViewSet for listing and retrieving boards in API v1.

Example:
    from todos.views import BoardViewSetV1
"""

from typing import List, Type
from uuid import UUID

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from todos.models import Board
from todos.serializers import BoardSerializerV1


# pylint: disable=too-many-ancestors
class BoardViewSet(ModelViewSet):
    """Board ViewSet handling board for version 1 of the API.

    This viewset allows authenticated users to do CRUD operations on boards.

    Attributes:
        queryset (QuerySet[Board]): All board objects.
        serializer_class (BoardSerializerV1): Serializer used for board details.
        permission_classes (list[BasePermission]): List of permission classes
                                                   required to access the endpoints.
    Methods:
        get_queryset: Returns the queryset of boards filtered by the authenticated user.
        list: Returns a list of all boards.
        retrieve: Returns a board by their primary key.
        create: Creates a new board.
        update: Updates an existing board.
        destroy: Deletes a board.
    """

    queryset: QuerySet[Board] = Board.objects.all()
    serializer_class: Type[BoardSerializerV1] = BoardSerializerV1
    permission_classes: List[Type[BasePermission]] = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Board]:
        """Return the queryset of boards filtered by the authenticated user.

        Args:
            None

        Returns:
            QuerySet[Board]: A queryset of boards owned by the authenticated user.
        """
        return self.queryset.filter(user_id=self.request.user.id, is_archived=False)

    def list(self, request: Request, *args, **kwargs) -> Response:
        """Return a list of all boards.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            Response: A Response object containing serialized board's data.
        """
        boards: QuerySet[Board] = self.get_queryset()
        if not boards.exists():
            return Response({"detail": "No boards found."}, status=status.HTTP_404_NOT_FOUND)

        serializer: BoardSerializerV1 = self.get_serializer(boards, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        """Return a board by their primary key.

        Args:
            request (Request): The incoming HTTP request.
            pk (uuid): The primary key of the board to retrieve.

        Returns:
            Response: A Response object containing the board's data or an error message.
        """
        try:
            pk: UUID | None = kwargs.get("pk")
            board: Board | None = self.get_queryset().get(pk=pk)
        except Board.DoesNotExist:
            return Response({"detail": "Board not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer: BoardSerializerV1 = self.get_serializer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request, *args, **kwargs) -> Response:
        """Create a new board.

        Args:
            request (Request): The incoming HTTP request containing the board data.

        Returns:
            Response: A Response object containing the created board's data or an error message.
        """
        serializer: BoardSerializerV1 = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request: Request, *args, **kwargs) -> Response:
        """Update an existing board.

        Args:
            request (Request): The incoming HTTP request containing the updated board data.
            pk (uuid): The primary key of the board to update.

        Returns:
            Response: A Response object containing the updated board's data or an error message.
        """
        try:
            pk: UUID | None = kwargs.get("pk")
            board: Board | None = self.get_queryset().get(pk=pk)
        except Board.DoesNotExist:
            return Response({"detail": "Board not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer: BoardSerializerV1 = self.get_serializer(board, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        """Delete a board.

        Args:
            request (Request): The incoming HTTP request.
            pk (uuid): The primary key of the board to delete.

        Returns:
            Response: A Response object indicating the result of the deletion.
        """
        try:
            pk: UUID | None = kwargs.get("pk")
            board: Board = self.get_queryset().get(pk=pk)
        except Board.DoesNotExist:
            return Response({"detail": "Board not found."}, status=status.HTTP_404_NOT_FOUND)

        board.delete()
        return Response(
            {"detail": "Board deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )
