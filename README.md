# docker-practice

## Terminology

| Term      | Definition                                        |
|-----------|---------------------------------------------------|
| image     | the collection of software and configuration data |
| container | the running image                                 |


## How-to Postgresql

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

## Docker Documentation

* https://docs.docker.com/engine/storage/volumes/
* A discussion re postgres and docker https://wiki.postgresql.org/wiki/DockerizingPostgres


