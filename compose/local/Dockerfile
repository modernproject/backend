FROM python:latest

RUN set -ex && pip install pipenv --upgrade

ENV PYTHONUNBUFFERED 1

RUN set -ex && mkdir /backend
ADD . /backend
WORKDIR /backend

RUN set -ex && pipenv install --deploy --system
