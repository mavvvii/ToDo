ARG PYTHON_VERSION=3.11

FROM mcr.microsoft.com/vscode/devcontainers/python:${PYTHON_VERSION}

ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=2.1.3
# ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /workspaces/ToDo_App/backend/

RUN apt-get update && \
    apt-get install -y \
    curl \
    libpq-dev \
    ruby-full \
    git-flow

USER vscode
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

ENV PATH="/home/vscode/.local/bin:$PATH"

USER root
COPY poetry.lock pyproject.toml README.md ./

USER vscode
RUN poetry install --with dev --no-root

USER root
COPY . /workspaces/ToDo_App/backend/

RUN chmod +x startup.sh

USER vscode
ENTRYPOINT ["sh", "./startup.sh"]
