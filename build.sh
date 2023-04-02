#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip poetry
poetry install
poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate
