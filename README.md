# 📝 ToDo Web App

A full-stack web application to manage your daily tasks, built with Django and Vue.

- Backend: Django REST Framework + Celery + PostgreSQL + Redis + Poetry
- Frontend: Vue.js + TailwindCSS + TypeScript
- DevOps Setup: Docker, DevContainers, pre-commit hooks

## Project Structure

- `backend/` — Django REST API with PostgreSQL, Celery,

    Redis and Poetry for dependency management

- `frontend/` — Vue.js, TypeScript and TailwindCSS

- `.devcontainer/` — Dev containers setup with Docker Compose

```bash
├── backend
│   └── devcontainer.json
├── docker-compose.yml
└── frontend
    └── devcontainer.json
```

- `docs/` — Include documetation project like ADR, App Functionality

```bash
├── ADR
│   ├── ADR-0001-tech-stack.MD
│   ├── ADR-0002-backend-interface-asgi-vs-wsgi.MD
│   └── ADR-0003-hosting-choice.MD
└── App_Functionality.MD
```

## 🚀 Getting Started

To run the full project, follow these steps:

Clone the repository:

```bash
git clone https://github.com/mavvvii/ToDo.git
cd ToDo
```

Copy the example environment file:

```bash
cp .env-example .env
```

> **⚠️ WARNING:**  For production, remember to update the
.env file with your production settings.

Running the project

via Docker Compose:

From the root directory, run the following command to build
and start the development environment:

```bash
docker compose up --build -d
```

via Dev Containers in Visual Studio Code:

1. Open the project folder by pressing F1,
   then type File: Open Folder and select the "ToDo" directory.

1. Press F1 again, type Dev Containers:
   Rebuild and Reopen in Container... and select it.

1. Choose which container you want to work in — backend or frontend.

1. The container will open, and you can start developing inside it.

1. To switch to the other container:

   1. Press `F1`, type **Remote: Close Remote Connection**

   1. Then open the folder again (**File: Open Folder**)

   1. Finally, use **Dev Containers: Reopen in Container**

## Environment Variables Overview

### Django Settings

These variables control the core behavior of the Django backend.

```bash
DJANGO_SECRET_KEY=django-insecure-jfks0k02kf920kfs0oi2k
```

> **⚠️ WARNING:** You must change this in production.

```bash
DJANGO_PRODUCTION=False
```

> **⚠️ WARNING:** Set to True when running in production mode.

### Django Database Settings

Used by Django to connect to the PostgreSQL database.

```bash
DJANGO_DATABASE_NAME=todo_postgres
DJANGO_DATABASE_USER=postgres
DJANGO_DATABASE_PASSWORD=postgres
DJANGO_DATABASE_HOST=db_container
DJANGO_DATABASE_PORT=5432
```

These values should match the configuration in your docker-compose.yml
 file for the db_container service.

### Django Admin Auto-Creation

Optional environment variables to automatically create an admin account during development.

```bash
DJANGO_ADMIN_USER=
DJANGO_ADMIN_EMAIL=
DJANGO_ADMIN_PASSWORD=
```

If none of these are provided, a default admin account will be created with:

- Username: admin

- Email: admin@example.com

- Password: admin

> **⚠️ WARNING:** Be sure to change or set these values before deploying to production.

### PostgreSQL Container Configuration

These values are used by the PostgreSQL Docker image to initialize the database.

```bash
POSTGRES_DB=todo_postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

These values must match the Django database settings above.

### Redis Configuration

Redis is used as a message broker for Celery.

```bash
REDIS_HOST=
REDIS_PORT=
REDIS_DB=
```

During development, you can leave these empty. Redis will auto-connect
via internal service name redis_container in Docker.

> **⚠️ WARNING:** In production, set the full host and port
to connect to an external Redis server.

---

## 🔧 Running the Servers

### Backend (ASGI + Uvicorn)

### Backend Development

Backend with Uvicorn (ASGI) and hot-reload for development

This setup is intended for local development and automatically restarts
the server when you make changes to the code.

```bash
uvicorn app.asgi:application --host 0.0.0.0 --port 8000 --reload
```

### Backend Production

In production, the backend running via Uvicorn with 4 worker processes
and without reload.

This improves performance and is more suitable for deployment.

```bash
uvicorn app.asgi:application --host 0.0.0.0 --port 8000 --workers 4
```

### Frontend (Vue)

### Frontend Development

The frontend is built with Vue and runs in development mode using npm.
It starts a local server on port 3000.

```bash
npm run dev
```

### Frontend Production

For production, the frontend is built using.

```bash
npm run build
```

---

## Git Flow Workflow

### Branch

#### Include Branches

- **main** – always production‑ready; only tagged releases.

- **develop** – integration branch for features before release.  

   - **feature/** – new feature branches, e.g. `feature/user-auth`.

   - **release/** – prepare a release, e.g. `release/v1.2.0`.  

   - **hotfix/** – urgent fixes on production, e.g. `hotfix/critical-bug`.  

#### Branch Naming Conventions

- Features: `feature/your-short-description`

- Releases: ` release/X.Y.Z`

Where:

X - Major

Y - Minor

Z - Patch

– Hotfixes: `hotfix/short-description`

### Install Git Flow to local developing

#### OSX - Homebrew

```bash
brew install git-flow
```

#### OSX - Macports

```bash
ports install git-flow
```

#### Linux

```bash
apt-get install git-flow
```

#### Windows (Cygwin)

```bash
wget -q -O - --no-check-certificate \
  https://github.com/nvie/gitflow/raw/develop/contrib/gitflow-installer.sh |
```

[Source](https://skoch.github.io/Git-Workflow/)

### Common Git Flow Commands

```bash
# Start a new feature

git flow feature start my-feature

# Finish a feature (merges into develop and deletes branch)

git flow feature finish my-feature

# Start & finish a release

git flow release start 1.2.0
git flow release finish 1.2.0

# Create a hotfix

git flow hotfix start critical-fix
git flow hotfix finish critical-fix
```

---

## Pre-commit Hooks

This project uses pre-commit hooks to keep the
code clean, consistent, and safe.

Enabled hooks:

- [pre-commit-hooks](
    https://github.com/pre-commit/pre-commit-hooks
    ): basic sanity checks
- [markdownlint](
    https://github.com/markdownlint/markdownlint
    ): checks formatting and style in Markdown files
- [pydocstyle](
    https://github.com/pycqa/pydocstyle
    ): enforces docstring conventions (PEP 257)
- [flake8](
    https://github.com/pycqa/flake8
    ): checks Python code for style issues and errors (PEP 8)
- [pylint](
    https://github.com/pylint-dev/pylint
    ): deep static analysis for Python code
- [black](
    https://github.com/psf/black
    ): automatic Python code formatter
- [mypy](
    https://github.com/pre-commit/mirrors-mypy
    ): static type checker for Python
- [isort](
    https://github.com/pycqa/isort
    ): automatically sorts Python imports
- [bandit](
    https://github.com/PyCQA/bandit
    ): scans for common security issues in Python code

This project uses pre-commit version >=4.2.0 <5.0.0.

---

## Related Documentation

- [App Functionality](./docs/App_Functionality.MD)
- [Architecture Decision Records](./docs/ADR/)
- [Backend README](./backend/README.md)
- [Frontend README](./frontend/README.md)

---

## Authors

[mavvvii](https://github.com/mavvvii)

## License

[Mit License](https://choosealicense.com/licenses/mit/)
