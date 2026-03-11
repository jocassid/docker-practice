FROM python:3.14.2-alpine3.23

LABEL description="Simple Django app to experiment with networking"

COPY project /app


WORKDIR /app

# Set environment variables
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

ENV DJANGO_SETTINGS_MODULE=main.settings

# Upgrade pip
RUN pip install --upgrade pip

## run this command to install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN ./manage.py migrate

## Expose the Django port
#EXPOSE 8000
#
## Run Django’s development server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["ash"]