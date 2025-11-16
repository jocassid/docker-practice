# docker-practice

Notes from online sources are in this readme.  Notes from books are in
https://docs.google.com/document/d/17vFd-ejqFVAITu_Bfn8Mj_L7LJjvmxhtjEwPI_VEy9M/edit?tab=t.0



## Terminology

| Term      | Definition                                        |
|-----------|---------------------------------------------------|
| image     | the collection of software and configuration data |
| container | the running image                                 |


Get a shell on a linux container
```bash
# -i    interactive
# -t    allocate a pseudo-tty
# --rm  Automatically remove the container and its associated anonymous volumes when it exits
# --name  Specify name for container (my_ubuntu_container in this example)
docker run -it --rm --name my_ubuntu_container my_ubuntu_image
```



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

## Volumes and Bind Mounts Oh My

Docker volumes are stored under /var/lib/docker/volumes/

* [Article on differences between Volumes and Bind Mounts](https://dev.to/caffinecoder54/docker-volumes-vs-bind-mounts-when-to-use-each-1ah4) 
It recommends using volumes for database service.  Consensus seems to be volumes for production and bind mounts for 
development where you want code changes to have immediate effect (i.e. developer's code lives in a binds mount) 

## Docker Documentation

* [Volumes](https://docs.docker.com/engine/storage/volumes/)
* [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/)
* A discussion re postgres and docker https://wiki.postgresql.org/wiki/DockerizingPostgres




