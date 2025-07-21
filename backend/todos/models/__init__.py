"""Module todos.models contains the data models for the ToDo application.

It includes the Task and Board models, which are used to manage tasks and boards
within the application.

Exported Classes:
- Board: Board model using models.Model to define the board structure.
    Functions:
    - __str__: Return the title of the board.
- Task: Task model using models.Model to define the task structure.
    Functions:
    - __str__: Return the title of the task.

Typical usage:
    from todos.models import Task
    from todos.models import Board
"""

from .boards import Board
from .tasks import Task

__all__ = [
    "Task",
    "Board",
]
