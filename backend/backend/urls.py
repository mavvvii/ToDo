"""
URL configuration for backend project.

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

from typing import Union

from django.contrib import admin
from django.urls import (
    URLPattern,
    URLResolver,
    include,
    path,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

api_urls_v1: URLPattern = [
    path("api/", include(("users.urls", "v1"), namespace="users")),
]

documentation_urls_v1: list[URLPattern] = [
    path(
        "api/v1/schema/",
        SpectacularAPIView.as_view(),
        name="schema-v1",
    ),
    path(
        "api/v1/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema-v1"),
        name="schema-v1-swagger-ui",
    ),
    path(
        "api/v1/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema-v1"),
        name="schema-v1-redoc",
    ),
]

urlpatterns: list[Union[URLPattern, URLResolver]] = [
    *api_urls_v1,
    *documentation_urls_v1,
    path("admin/", admin.site.urls, name="admin_site"),
]
