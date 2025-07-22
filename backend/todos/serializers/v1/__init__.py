"""Serializers Board and Task for version 1 of the API .

Exported Classes:
- BoardSerializerV1: Serializer for board details in version 1 of the API.
- TaskSerializerV1: Serializer for task details in version 1 of the API.
"""

from .board import BoardSerializer as BoardSerializerV1
from .task import TaskSerializer as TaskSerializerV1

__all__ = [
    "BoardSerializerV1",
    "TaskSerializerV1",
]
