FROM ubuntu:latest
LABEL author="jocassid"
LABEL description="Simple Dockerfile"
RUN apt-get update
RUN apt-get install -y python3
COPY hello-world.py /opt
COPY cwd_file.txt .
CMD ["python3", "/opt/hello-world.py"]