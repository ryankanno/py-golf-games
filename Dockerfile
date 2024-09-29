# syntax=docker/dockerfile:1.9
FROM python:3.11-slim-buster AS base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random

FROM base AS builder

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.11 \
    UV_PROJECT_ENVIRONMENT=/app

SHELL ["/bin/bash", "-exo", "pipefail",  "-c"]

RUN apt-get update -qy \
    && apt-get install -qyy \
    -o APT::Install-Recommends=false \
    -o APT::Install-Suggests=false \
    ca-certificates \
	&& apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml /_project/
COPY uv.lock /_project/

RUN --mount=type=cache,target=/root/.cache <<EOT
    uv venv
EOT

# install deps
RUN --mount=type=cache,target=/root/.cache <<EOT
    cd /_project
    uv sync --locked --no-dev --no-install-project
EOT

COPY . /src

# install application
RUN --mount=type=cache,target=/root/.cache <<EOT
    cd /src
    uv sync --locked --no-dev --no-editable
EOT

FROM base AS final

SHELL ["/bin/bash", "-exo", "pipefail",  "-c"]

ENV PATH=/app/bin:$PATH

RUN <<EOT
    groupadd -r app
    useradd -r -d /app -g app -N app
EOT

ENTRYPOINT ["/bin/bash", "/docker-entrypoint.sh"]
STOPSIGNAL SIGINT

RUN <<EOT
    apt-get update -qy
    apt-get install -qyy \
    -o APT::Install-Recommends=false \
    -o APT::Install-Suggests=false
    apt-get clean
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EOT

COPY docker-entrypoint.sh /

COPY --from=builder --chown=app:app /app /app

USER app
WORKDIR /app
