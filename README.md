# Horizon Blog

By: Leonard

Position: Software Engineer

### Requirements:

Django: 4.2

Python: ^3.11

Postgres: 15.3

Poetry: Dependency Management

Docker Container

### Development Setup

Setup environment variables:

```bash
cp sample.env .env
```

Run Docker:

```bash
docker-compose up --build
```

Note: if docker build fails re-run it again. Postgres was not ready yet in first build

Visit Page:

`http://localhost:8080/blog/`

`http://localhost:8080/admin/`


Note: python commands should be run inside the docker container
### Create Super User

```bash
python manage.py createsuperuser
```

### Run test

```bash
python manage.py test
```