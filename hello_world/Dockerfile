
# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY hello.py .

# Run the Python script when the container starts
CMD ["python", "hello.py"]

# Build the image using this command
# docker build -t hello-python .
# No files get generated in this directory, but image will be created wherever docker stores images

# run the container with the following command:
# docker run hello-python