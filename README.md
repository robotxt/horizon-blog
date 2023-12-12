# Horizon Blog

By: Leonard

Position: Software Engineer

---

### Requirements:

Django: 4.2

Python: ^3.11

Postgres: 15.3

Poetry: Dependency Management

Docker Container

---

### Development Setup

> Using docker for development setup and poetry for dependency management. Instead of sqlite I used Postgres for the application database which is ideal for production. I added .env files which contains the environment variables.
> 

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

---

Note: python commands should be run inside the docker container

### Create Super User

```bash
python manage.py createsuperuser
```

### Run test

> I created a factory using [factory_boy](https://factoryboy.readthedocs.io/en/stable/) to create dummy blogs data when running the test. Created only 1 test case to check the status code of the GET request and check if the blog are in descending order and contains titles
> 

```bash
python manage.py test
```

### Models

**BaseDateModel**: Created a model abstract where we can use if have different models. This contains date like: created_at, updated_at and deleted_at.

**Blog**: This model contains a primary_key which is a UUID type. I used UUID type so we don’t need to have sequencial ID which is really predictable if we used it to the URL.

### Views

BlogView: View that renders the blogs.html. This handles the list of blogs that are created before the current time

BlogDetailView: View that renders the blog.html which handles the blog details. It just displays title, content and published_date