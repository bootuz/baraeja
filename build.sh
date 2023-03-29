#!/usr/bin/env bash
# exit on error
set -o errexit

pip install poetry
python -m pip install --upgrade pip poetry
python -m poetry install
poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate