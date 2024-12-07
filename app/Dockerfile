# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
EXPOSE 8000
WORKDIR /app

# INSTALL DEPENDENCIES
RUN apk update
RUN apk add \
    pkgconfig \
    gcc \
    musl-dev \
    bash \
    mariadb-dev

# INSTALL NEEDED PACKAGES SPECIFIED IN REQUIREMENTS
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# RUN SERVER 
ENTRYPOINT [ "python3" ]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]