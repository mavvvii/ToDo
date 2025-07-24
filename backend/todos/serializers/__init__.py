"""
Board and Task serializers module.

This module provides versioned serializers for the Board and Task models,
used in different API versions.

Exported Classes:
- BoardSerializerV1: Serializer for board details in version 1 of the API.
- TaskSerializerV1: Serializer for task details in version 1 of the API.

Typical usage example:
    from users.serializers import UserDetailSerializerV1
    serializer_class = BoardSerializerV1

    from todos.serializers import TaskSerializerV1
    serializer_class = TaskSerializerV1
"""

from .v1 import BoardSerializerV1, TaskSerializerV1

__all__ = [
    "BoardSerializerV1",
    "TaskSerializerV1",
]
