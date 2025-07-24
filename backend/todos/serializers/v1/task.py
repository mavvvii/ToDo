"""Serializer for Task model in version 1 of the API."""

from typing import Type

from rest_framework import serializers
from todos.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializers for task.

    Provides serialization and validation logic for the Task model
    used in version 1 of the API.

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
        create: Create a new task instance.
        update: Update an existing task instance.
    """

    class Meta:
        """Meta options for TaskSerializer.

        Attributes:
            model (Type[Task]): The Task model to serialize.
            fields (str): All fields of the Task model.
            read_only_fields (list[str]): Fields that are read-only and cannot be modified.
        """

        model: Type[Task] = Task
        fields: str = "__all__"
        read_only_fields: list[str] = ["id", "created_at", "updated_at"]

    def create(self, validated_data: dict) -> Task:
        """Create a new task instance.

        Args:
            validated_data (dict): The validated data for creating a task.

        Returns:
            Task: The created task instance.
        """
        return Task.objects.create(**validated_data)

    def update(self, instance: Task, validated_data: dict) -> Task:
        """Update an existing task instance.

        Args:
            instance (Task): The task instance to update.
            validated_data (dict): The validated data for updating the task.

        Returns:
            Task: The updated task instance.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
