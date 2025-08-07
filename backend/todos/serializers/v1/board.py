"""Serializer for version 1 of the API."""

from typing import Type

from rest_framework import serializers
from todos.models import Board


class BoardSerializer(serializers.ModelSerializer):
    """Serializers for board.

    Provides serialization and validation logic for the Board model
    used in version 1 of the API.

    Attributes:
        id (UUIDField): Unique identifier for the board.
        title (str): The title of the board.
        user_id (ForeignKey): The user who owns the board.
        description (str): A description of the board.
        created_at (datetime): The date and time when the board was created.
        updated_at (datetime): The date and time when the board was last updated.
        is_archived (bool): Indicates whether the board is archived.
    Methods:
        create: Create a new board instance.
        update: Update an existing board instance.
    """

    class Meta:
        """Meta options for BoardSerializer.

        Attributes:
            model (Type[Board]): The Board model to serialize.
            fields (str): All fields of the Board model.
            read_only_fields (list[str]): Fields that are read-only and cannot be modified.
        """

        model: Type[Board] = Board
        fields: str = "__all__"
        read_only_fields: list[str] = ["id", "created_at", "updated_at", "user_id"]

    def create(self, validated_data: dict) -> Board:
        """Create a new board instance.

        Args:
            validated_data (dict): Data to create the board instance.

        Returns:
            Board: The created board instance.
        """
        return Board.objects.create(**validated_data)

    def update(self, instance: Board, validated_data: dict) -> Board:
        """Update an existing board instance.

        Args:
            instance (Board): The board instance to update.
            validated_data (dict): Data to update the board instance.

        Returns:
            Board: The updated board instance.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
