ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-3.10.1}
FROM python:${INSTALL_PYTHON_VERSION}-slim-buster AS base

ENV PYTHONFAULTHANDLER=1 \
	PYTHONUNBUFFERED=1 \
	PYTHONHASHSEED=random \
	PIP_NO_CACHE_DIR=off \
	PIP_DISABLE_PIP_VERSION_CHECK=on \
	PIP_DEFAULT_TIMEOUT=100 \
	POETRY_VERSION=1.1.12

ARG REPOSITORY=https://github.com/ryankanno/py-golf-games
ARG BUILD_DATETIME
ARG VERSION
ARG REVISION
ARG BRANCH

ENV REPOSITORY ${REPOSITORY}
ENV BUILD_DATETIME ${BUILD_DATETIME:-null}
ENV VERSION ${VERSION:-null}
ENV REVISION ${REVISION:-null}
ENV BRANCH ${BRANCH:-main}

LABEL maintainers="Ryan Kanno <ryankanno@localkinegrinds.com>"

LABEL org.opencontainers.image.created="${BUILD_DATETIME}" \
      org.opencontainers.image.title="py-golf-games" \
      org.opencontainers.image.description="Library to help simulate golf games" \
      org.opencontainers.image.authors="ryankanno@localkinegrinds.com" \
      org.opencontainers.image.revision="${REVISION}" \
      org.opencontainers.image.source="${REPOSITORY}" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.licenses="MIT"

SHELL ["/bin/bash", "-exo", "pipefail",  "-c"]

RUN apt-get update && \
    apt-get install --no-install-recommends -y wget python3-pip && \
	apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget -qO- https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python3

ENV PATH="~/.local/bin:${PATH}"

COPY pyproject.toml /pyproject.toml
COPY poetry.lock /poetry.lock

RUN /bin/bash -c "poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi --no-root"

COPY ./py_golf_games /project/py_golf_games

ENV PYTHONPATH "${PYTHONPATH}:/project"

COPY ./entrypoint.sh /entrypoint.sh

# Specify entrypoint and default command
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
