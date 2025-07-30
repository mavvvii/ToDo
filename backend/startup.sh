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

if [ "$DJANGO_PRODUCTION" = "1" ]; then
  echo "Running production server"
  poetry run gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 4 --log-level info
else
  echo "Running developing server"
  poetry run python manage.py runserver 0.0.0:8000
  # poetry run gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --reload --log-level info
fi
