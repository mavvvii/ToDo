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
from users.views import LoginViewV1, UserProfileViewSetV1, UserRegisterViewV1

user_profile_router_v1 = DefaultRouter()
user_profile_router_v1.register(
    r"profile",
    UserProfileViewSetV1,
    basename="user-profile-v1",
)


urlpatterns: URLResolver = [
    path(
        "v1/auth/login/",
        LoginViewV1.as_view(),
        name="user-login-v1",
    ),
    path(
        "v1/auth/register/",
        UserRegisterViewV1.as_view(),
        name="user-register-v1",
    ),
    path(
        "v1/",
        include(user_profile_router_v1.urls),
    ),
]
