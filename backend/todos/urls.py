"""
URL configuration for the 'todos' app.

This module defines the URL patterns for the todos application,
mapping URL paths to their corresponding view functions or classes.

"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from todos.views import BoardViewSetV1, TaskViewSetV1

ToDosRouterV1 = DefaultRouter()
ToDosRouterV1.register(r"boards", BoardViewSetV1, basename="boards_v1")

boards_router = NestedDefaultRouter(ToDosRouterV1, r"boards", lookup="board")
boards_router.register(r"tasks", TaskViewSetV1, basename="tasks_v1")

urlpatterns = [
    path("v1/", include(ToDosRouterV1.urls)),
    path("v1/", include(boards_router.urls)),
]
