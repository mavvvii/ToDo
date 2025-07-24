"""Defines the Task model."""

import uuid

from django.db import models

from .board import Board


# pylint: disable=too-many-ancestors
class StatusChoices(models.TextChoices):
    """Enumeration for task status choices.

    Attributes:
    TODO (str): Represents a task that is yet to be started.
    IN_PROGRESS (str): Represents a task that is currently being worked on.
    DONE (str): Represents a task that has been completed.
    """

    TODO = "todo", "ToDo"
    IN_PROGRESS = "in progress", "In Progress"
    DONE = "done", "Done"


class Task(models.Model):
    """Task model for managing tasks within a board.

    Attributes:
        id (UUIDField): Unique identifier for the task.
        board_id (UUIDField): The ID of the board to which the task belongs.
        title (str): The title of the task.
        status (str): The current status of the task (e.g., todo, in_progress, done).
        description (str): A detailed description of the task.
        completed (bool): Indicates whether the task is completed.
        created_at (datetime): The date and time when the task was created.
        updated_at (datetime): The date and time when the task was last updated.
        completed_at (datetime): The date and time when the task was completed.
        deleted_at (datetime): The date and time when the task was deleted.
        is_archived (bool): Indicates whether the task is archived.

    Methods:
        __str__: Returns the title of the task.
    """

    id: models.UUIDField = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title: models.CharField = models.CharField(max_length=255, blank=False, null=False)
    board_id: models.ForeignKey = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name="boards"
    )
    status: models.CharField = models.CharField(
        choices=StatusChoices, max_length=20, default="todo"
    )
    description: models.TextField = models.TextField(blank=True, null=True)
    completed: models.BooleanField = models.BooleanField(default=False)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    completed_at: models.DateTimeField = models.DateTimeField(blank=True, null=True)
    deleted_at: models.DateTimeField = models.DateTimeField(blank=True, null=True)
    is_archived: models.BooleanField = models.BooleanField(default=False)

    def __str__(self):
        """Return the title of the task."""
        return self.title
