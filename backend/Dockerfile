ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION}

ENV POETRY_VERSION=2.1.3

RUN pip install poetry==$POETRY_VERSION

WORKDIR /app

COPY pyproject.toml poetry.lock README.md /app/

RUN poetry install --no-root

COPY . /app/

RUN chmod +x startup.sh

ENTRYPOINT ["sh", "./startup.sh"]
