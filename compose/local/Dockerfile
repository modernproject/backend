FROM lambci/lambda:build-python3.6

RUN set -ex && pip install pipenv --upgrade

ENV PYTHONUNBUFFERED 1

ADD . /var/task
WORKDIR /var/task

RUN set -ex && pipenv install --deploy --system
