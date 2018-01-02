FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
ADD . /backend

RUN pip install -Ur /backend/requirements/local.txt
