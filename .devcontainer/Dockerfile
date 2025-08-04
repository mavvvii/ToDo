ARG PYTHON_VERSION=3.12

FROM mcr.microsoft.com/devcontainers/python:${PYTHON_VERSION}

ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && \
    apt-get install -y curl docker.io git ruby && \
    pip install -U \
        pip \
        setuptools \
        poetry \
        toml
