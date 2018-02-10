FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
ADD . /backend

RUN pip install -Ur /backend/requirements/production.txt
