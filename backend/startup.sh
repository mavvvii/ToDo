#!/usr/bin/bash

set -eu pipefail

echo "[ALERT] Run migrations..."
poetry run python manage.py makemigrations --noinput

echo "[ALERT] Apply migrations..." 
poetry run python manage.py migrate --database=default

echo "[ALERT] Create admin user if none exists..."
poetry run python manage.py createadmin

echo "[ALERT] Collect static files..."
poetry run python manage.py collectstatic --noinput

if [ "$DJANGO_PRODUCTION" = "True" ]; then
  echo "Running production server"
  poetry run uvicorn backend.asgi:application --host 0.0.0.0 --port "8000" --log-level info --workers "4"
else
  echo "Running developing server"
  # poetry run python manage.py runserver 0.0.0.0:8000
  poetry run uvicorn backend.asgi:application --host 0.0.0.0 --port "8000" --reload --reload-dir /workspaces/ToDo_App/backend
fi