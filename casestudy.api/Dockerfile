# Dockerfile

# Pull base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python casestudy/manage.py makemigrations
RUN python casestudy/manage.py migrate
RUN python casestudy/manage.py loaddata casestudy/capital_call/fixtures/initial_data.json
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "./casestudy", "casestudy.wsgi", "--access-logfile", "'-'", "--error-logfile", "'-'" ]
