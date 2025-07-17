# Backend ToDo Web App

Django REST Framework + Celery + PostgreSQL + Redis + Poetry

---

## Project Structure

- `backend/`

```text
├── backend
│   ├── asgi.py
│   ├── celery.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── startup.sh
├── static
│   ├── admin
│   ├── jazzmin
│   ├── rest_framework
│   └── vendor
├── todos
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   ├── serializers
│   │   └── __init__.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── models
│   │   │   └── __init__.py
│   │   ├── serializers
│   │   │   └── __init__.py
│   │   └── views
│   │       └── __init__.py
│   ├── urls.py
│   └── views
│       └── __init__.py
└── users
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── management
    │   ├── commands
    │   │   ├── createadmin.py
    │   │   ├── __init__.py
    │   ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   └── user.py
    ├── serializers
    │   └── __init__.py
    ├── tests
    │   ├── __init__.py
    │   ├── models
    │   │   └── __init__.py
    │   ├── serializers
    │   │   └── __init__.py
    │   └── views
    │       └── __init__.py
    ├── urls.py
    └── views
        └── __init__.py
```

## Dependency Management

Project using Poetry version 2.1.3 for dependency management.

### Add a new package

```bash
# Allow >=2.0.5, <3.0.0 versions
poetry add package-name^2.0.5

# Allow >=2.0.5, <2.1.0 versions
poetry add package-name~2.0.5

# Allow >=2.0.5 versions, without upper bound
poetry add "package-name>=2.0.5"

# Allow only 2.0.5 version
poetry add package-name==2.0.5
```

## Script to Run backend [startup.sh]

### Run Django Migrations

```bash
poetry run python manage.py makemigrations --noinput
poetry run python manage.py migrate --database=default
```

### Create Admin User Automatically

```bash
poetry run python manage.py createadmin
```

### Collect Static Files

```bash
poetry run python manage.py collectstatic --noinput
```

### Start the Application Server

In poduction:

```bash
poetry run uvicorn backend.asgi:application \
--host 0.0.0.0 --port 8000 --workers 4
```

In development:

```bash
poetry run uvicorn backend.asgi:application --host 0.0.0.0 --port 8000 --reload
```

## Run Manually Pre-commit Hooks

In the backend directory, run the following command:

```bash
poetry run pre-commit run --all-files --config ../.pre-commit-config.yml
```

## Run Tests

## Useful Resources

- [Django Docs](https://docs.djangoproject.com/en/5.2/)

- [DRF Docs](https://www.django-rest-framework.org/)

- [Celery Django Docs](
    https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html
    )
- [Postgresql Dosc](https://www.postgresql.org/docs/)

- [Redis Docs](https://redis.io/docs/latest/)

- [Poetry Docs](https://python-poetry.org/docs/)
