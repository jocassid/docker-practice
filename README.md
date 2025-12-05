
# docker-practice

Notes from online sources are in this readme.  Notes from books are in
https://docs.google.com/document/d/17vFd-ejqFVAITu_Bfn8Mj_L7LJjvmxhtjEwPI_VEy9M/edit?tab=t.0

## Practice Dockerfiles

| Dockerfile Directory | Description                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------|
| dockerfile0          | Very simple docker file.  Takes Ubuntu container and runs a `echo` command                    |
| dockerfile1          | Ubuntu image where I install python, copy a `hello-world.py` script into container and run it |
| dockerfile2          | Un-modified Ubuntu image, used to practice learn how to access shell within container         | 

## Terminology

| Term      | Definition                                        |
|-----------|---------------------------------------------------|
| image     | the collection of software and configuration data |
| container | the running image                                 |


## Installation

Packages I needed to install to get this working:
* docker.io
* docker-buildx
                                |

## Docker Commands in General

* docker commands typically need `sudo` to run
* `--help` will display help for `docker` and it's various sub-commands
* `docker image --help` help on `image` sub-command
* `docker image ls --` help on `image ls` 


| Dockerfile Instructions | Description                                                                                                                                                       |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VOLUME`                | Create a "directory" that persists beyond the runtime of the container.  This "directory" is managed by Docker and not a regular directory in the Host filesystem |
| `EXPOSE`                | Opens port on container                                                                                                                                           |

## Build Commands
<style>
    /*  PyCharm doesn't seem to like external stylesheets */
    table.commands > thead > tr > th:nth-of-type(1){
        width: 40%;
    }

</style>
<table class="commands">
    <thead>
        <tr>
            <th>Command</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>docker build .</code></td>
            <td>Simplest build command.  Context is current directory.  Output 
            of build command includes a sha256 hash (The image ID) which can be used in 
            command similar to <code>docker run sha256:dfed...29fc</code></td>
        </tr>
        <tr>
            <td><code>docker build -f Dockerfile.v1 .</code></td>
            <td><code>-f</code> option allows you to specify a docker file.  
            Otherwise, docker will look for a Dockerfile in the current directory</td>
        </tr>
        <tr>
            <td><code>docker build -t jocassid/hello_world .</code></td>
            <td>Build an image tagging it as  jocassid/hello_world</td>
        </tr>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
    </tbody>
</table>

## Image Commands

`images` is an alias for `images`.  You can use `docker image` and 
`docker images` interchangeably

<table class="commands">
    <thead>
        <tr>
            <th>Command</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>docker image "foo*"</code></td>
            <td>List images with tags that begin with foo</td>
        </tr>
        <tr>
            <td><code>docker image --all</code></td>
            <td>Show all images (default is to only show images that are tagged)</td>
        </tr>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
    </tbody>
</table>

## Container Commands

Unlike `docker image` and `docker images`, there isn't a `docker containers` alias 

<table class="commands">
    <thead>
        <tr>
            <th>Command</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
    </tbody>
</table>

## Tag Commands

<table class="commands">
    <thead>
        <tr>
            <th>Command</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>docker tag IMAGE_ID TAG_NAME</code></td>
            <td>Assigns a tag name to an image after it has been built.  Example 
            <code>docker tag sha256:45ce...ffca dockerfile1_img</code></td>
        </tr>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
    </tbody>
</table>


## Run Commands

<table class="commands">
    <thead>
        <tr>
            <th>Command</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
    </tbody>
</table>


### Get a shell on a linux container
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




