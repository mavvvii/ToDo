"""
Board and Task views module.

This module defines versioned viewsets for handling operations related to the Board and Task models,
tailored to different API versions.

Exported Classes:
- BoardViewSetV1: ViewSet for CRUD operations on boards.
- TaskViewSetV1: ViewSet for CRUD operations on tasks.

Typical usage example:
    from users.views import UserViewSetV1
"""

from .board import BoardViewSet as BoardViewSetV1
from .task import TaskViewSet as TaskViewSetV1

__all__ = [
    "BoardViewSetV1",
    "TaskViewSetV1",
]
