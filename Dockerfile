FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /code
COPY . .

# This is a special case. We need to run this script as an entry point:
COPY ./docker_runserver.sh /
RUN chmod +x /docker_runserver.sh

ENTRYPOINT ["./docker_runserver.sh"]
