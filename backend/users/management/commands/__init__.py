"""
Command to create a superuser if one does not already exist.

This command checks if a superuser exists in the database. If none exists,
it creates one using environment variables for username, email, and password.

Environment variables used:
- DJANGO_ADMIN_USER
- DJANGO_ADMIN_EMAIL
- DJANGO_ADMIN_PASSWORD

This is intended to be used as a Django management command, typically in automated deployments.
"""
