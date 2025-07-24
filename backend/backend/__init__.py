"""
Main package for the backend application.

This package includes configuration for Celery, which is used for asynchronous task processing.
"""

from .celery import app as celery_app

__all__ = ["celery_app"]
