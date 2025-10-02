# docker-practice

Practice at deploying Django apps w/ Docker

* https://betterstack.com/community/guides/scaling-python/dockerize-django/


```bash
docker run \
  --rm \
  --name django-todo-db \
  --env POSTGRES_PASSWORD=admin \
  --env POSTGRES_DB=django_todo \
  --volume django-pg-data:/var/lib/postgresql/data \
  --publish 5432:5432 \
  postgres:bookworm
```