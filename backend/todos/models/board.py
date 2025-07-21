"""Defines the Board model."""

import uuid

from django.db import models
from users.models import User


class Board(models.Model):
    """Board model for organizing tasks.

    Attributes:
        id (UUIDField): Unique identifier for the board.
        title (str): The title of the board.
        user_id (ForeignKey): The user who owns the board.
        description (str): A description of the board.
        created_at (datetime): The date and time when the board was created.
        updated_at (datetime): The date and time when the board was last updated.
        is_archived (bool): Indicates whether the board is archived.

    Methods:
        __str__: Returns the title of the board.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boards")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Return the title of the board."""
        return self.title
