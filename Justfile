#!/usr/bin/env just --justfile

set quiet

uv := 'uv'

[private]
default:
    just --list

# Remove build artifacts (build, dist, .egg)
[private]
clean-build:
    rm -fr build/
    rm -fr dist/
    rm -fr .eggs/
    find . -name '*.egg-info' -exec rm -fr {} +
    find . -name '*.egg' -exec rm -f {} +

# Remove Python artifacts (.pyc, .pyo, __pycache__)
[private]
clean-pyc:
    find . -name '*.pyc' -exec rm -f {} +
    find . -name '*.pyo' -exec rm -f {} +
    find . -name '*~' -exec rm -f {} +
    find . -name '__pycache__' -exec rm -fr {} +

# Remove test artifacts (.tox, .coverage, coveragexml)
[private]
clean-test:
    rm -fr .tox/
    rm -f .coverage
    rm -f coverage.xml
    rm -fr htmlcov/

# Remove docs
[private]
clean-docs:
    rm -fr .tox/docsout

# Remove build, Python, test artifacts, and docs
clean: clean-docs clean-build clean-pyc clean-test

# Check code coverage with current Python
coverage:
    {{uv}} run pytest --cov --cov-config=pyproject.toml --cov-append --cov-report term-missing --doctest-modules -ra -q -n auto
    {{uv}} run coverage report -m
    {{uv}} run coverage html
    open htmlcov/index.html

# Generate Sphinx documentation (tox:docs)
[no-quiet]
docs: clean-docs
    just tox run -e docs

# Package
dist: clean
    {{uv}} build

# Install package to current Python's site-package
install: clean
    {{uv}} install

# Lint (tox:lint)
lint:
    just tox run -e lint

# Lint fix (tox:lint-fix)
lint-fix:
    just tox run -e lint-fix

# Runs tests (tox:tests)
tests:
    just tox run-parallel -m tests

# Runs pre-commit (tox:pre-commit)
pre-commit:
    just tox run -e pre-commit

# Runs tox
tox *TOX_ARGS:
    {{uv}} run tox {{TOX_ARGS}}

# Runs watchexec
watch *JUST_RECIPE:
    watchexec -r -e py -- "just {{JUST_RECIPE}} && toastify send '🚀 just {{JUST_RECIPE}}' 'just {{JUST_RECIPE}} was successful' --icon info || toastify send '❌ just {{JUST_RECIPE}}' 'just {{JUST_RECIPE}} failed' --icon error"
