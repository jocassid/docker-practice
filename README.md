<style>
    /*  PyCharm doesn't seem to like external stylesheets */
    table.commands > thead > tr > th:nth-of-type(1){
        width: 40%;
    }

</style>

# docker-practice

Notes from online sources are in this readme.  Notes from books are in
https://docs.google.com/document/d/17vFd-ejqFVAITu_Bfn8Mj_L7LJjvmxhtjEwPI_VEy9M/edit?tab=t.0

## Practice Dockerfiles

| Dockerfile Directory   | Description                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------|
| dockerfile0            | Very simple docker file.  Takes Ubuntu container and runs a `echo` command                          |
| dockerfile1            | Ubuntu image where I install python, copy a `hello-world.py` script into container and run it       |
| dockerfile2            | Un-modified Ubuntu image, used to practice learn how to access shell within container               |
| dockerfile3_flask_page | Docker file for a container with a simple Flask page.  Also experiments with base & dev Dockerfiles |
| dockerfile4_volumes    | Experiment w/ Docker volumes                                                                        |

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

## Dockerfiles

A brief summary of Docker File instructions, for details 
check https://docs.docker.com/reference/dockerfile/

<table class="commands">
    <thead>
        <tr>
            <th style="width: 20%">Instruction</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>FROM</code></td>
            <td>
                <code>FROM</code> indicates the base image to use for your 
                container.  All images are built from a base image.</td>
        </tr>
        <tr>
            <td><code>WORKDIR</code></td>
            <td>
                Set current working directory for <code>RUN</code>, 
                <code>CMD</code>, etc.  Working dir may be changed as the 
                makefile runs.
            </td>
        </tr>
        <tr>
            <td><code>COPY</code></td>
            <td>
                Copy files from the host filesystem to the container 
                filesystem
            </td>
        </tr>
        <tr>
            <td><code>ADD</code></td>
            <td>
                Like <code>COPY</code>, but automatically extracts tarballs 
                and can fetch files via URL
            </td>
        </tr>
        <tr>
            <td><code>RUN</code></td>
            <td>Run command as **container (not image)** is being built</td>
        </tr>
        <tr>
            <td><code>CMD</code></td>
            <td>Defines a command to be run when the container runs.  
                Example: <code>CMD ["python", "my_script.py", "arg1", 
                "arg2"]</code>  Note that <code>CMD</code> arguments are in 
                double quotes</td>
        </tr>
        <tr>
            <td><code>ENTRYPOINT</code></td>
            <td>
                With <code>CMD</code>, <code>docker run ls</code> will run 
                the <code>ls</code> command.  This is a way to override the 
                <code>CMD</code>.  <code>ENTRYPOINT</code> allows you to 
                pass args to the executable.  Example <code>ENTRYPOINT 
                ["curl", "-s"]</code>
            </td>
        </tr>
        <tr>
            <td><code>ENV</code></td>
            <td>Set environment variable.  Examples:
                <ul>
                    <li><code>ENV DJANGO_SETTINGS_MODULE main.settings</code></li>
                    <li><code>ENV FOO=bar PLACEHOLDER=yadayada</code></li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><code>VOLUME</code></td>
            <td>
                Create a "directory" that persists beyond the runtime of the 
                container.  This "directory" is managed by Docker and not a 
                regular directory in the Host filesystem.  Example 
                <code>VOLUME /var/logs/nginx</code>
            </td>
        </tr>
        <tr>
            <td><code>EXPOSE</code></td>
            <td>Opens port on container.  Example <code>EXPOSE 43/tcp</code></td>
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

## Docker Commands `docker` ...

### `build` ...
<table class="commands">
    <thead>
        <tr>
            <th>Arguments</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>.</code></td>
            <td>Simplest build command.  Context is current directory.  Output 
            of build command includes a sha256 hash (The image ID) which can be used in 
            command similar to <code>docker run sha256:dfed...29fc</code></td>
        </tr>
        <tr>
            <td><code>-f Dockerfile.v1 .</code></td>
            <td><code>-f</code> option allows you to specify a docker file.  
            Otherwise, docker will look for a Dockerfile in the current directory</td>
        </tr>
        <tr>
            <td><code>-t jocassid/hello_world .</code></td>
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

### `image` ...

`images` is an alias for `images`.  You can use `docker image` and 
`docker images` interchangeably

<table class="commands">
    <thead>
        <tr>
            <th>Subcommand</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>ls "foo*"</code></td>
            <td>List images with tags that begin with foo</td>
        </tr>
        <tr>
            <td><code>ls --all</code></td>
            <td>Show all images (default is to only show images that are tagged)</td>
        </tr>
        <tr>
            <td><code>pull postgres:16.11-alpine3.23</code></td>
            <td>Download postgres image from docker hub</td>
        </tr>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
    </tbody>
</table>

### `container` ...

Unlike `docker image` and `docker images`, there isn't a `docker containers` alias 

<table class="commands">
    <thead>
        <tr>
            <th>arguments</th>
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

### `tag` ...

<table class="commands">
    <thead>
        <tr>
            <th>Arguments</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>IMAGE_ID TAG_NAME</code></td>
            <td>Assigns a tag name to an image after it has been built.  Example 
            <code>docker tag sha256:45ce...ffca dockerfile1_img</code></td>
        </tr>
        <tr>
            <td><code></code></td>
            <td></td>
        </tr>
    </tbody>
</table>


### `volume` ...

<table class="commands">
    <thead>
        <tr>
            <th>Subcommand</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>create</code></td>
            <td>Creates volume with a name that's a long hexadecimal string <b style="color:red">Don't do this!</b></td>
        </tr>
        <tr>
            <td><code>create --name=log_dir --label='Some metadata</code></td>
            <td>Create volume, give it a name and label it with some metadata.  Note Docker 
            doesn't like double quotes around the label</td>
        </tr>
        <tr>
            <td><code>rm VOLUME_NAME</code></td>
            <td><b>Note:</b> If you don't specify a name when the volume is 
            created, you'll get random hexadecimal name and will have to 
            provide the ENTIRE name when removing the volume</td>
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
            <td><code>docker run -it IMAGE</code></td>
            <td>
                Access a shell within the container.  This combines the 
                <code>-i</code>, <code>--interactive</code> and
                <code>-t</code>, <code>--tty</code> options.
            </td>
        </tr>
        <tr>
            <td><code>docker run -d -p 8080:80 IMAGE</code></td>
            <td><code>-d</code>, <code>--detach</code> options runs the 
                container in the background.  <code>-p</code>, 
                <code>--publish</code>maps port 8080 on the host to 
                port 80 on the container.</td>
        </tr>
        <tr>
            <td><code>docker run --name NAME IMAGE</code></td>
            <td>By default, Docker assigns a random name to the container.  
                This can be overridden with the <code>--name</code> option.
                Example: <code>docker run --name production_database 
                database:latest</code></td>
        </tr>
        <tr>
            <td><code>docker run -v $HOME:/host-home IMAGE bash</code></td>
            <td>Mount's the user's home directory as /host-home</td>
        </tr>
        <tr>
            <td><code></code></td>
            <td></td>
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




