"""
URL configuration for the 'users' app.

This module defines the URL patterns for the users application,
mapping URL paths to their corresponding view functions or classes.

URL configuration for users project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

Typical usage example:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import URLResolver, include, path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSetV1

UsersRouterV1: DefaultRouter = DefaultRouter()
UsersRouterV1.register(r"users", UserViewSetV1, basename="v1")

urlpatterns: URLResolver = [
    path("v1/", include(UsersRouterV1.urls), name="users_v1"),
]
