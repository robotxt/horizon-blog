FROM python:3.11

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY app/ /app
COPY pyproject.toml poetry.lock /app/

RUN pip install --upgrade pip poetry setuptools
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

RUN DJANGO_SECRET_KEY=abcd python3 manage.py collectstatic