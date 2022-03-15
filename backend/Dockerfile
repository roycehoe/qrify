FROM python:3.9-alpine

ENV POETRY_VERSION=1.1.2

RUN pip install --upgrade pip &&\
    apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo g++ postgresql-dev zlib-dev libjpeg jpeg-dev &&\
    pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY . /code

RUN poetry config virtualenvs.create false &&\
    poetry install --no-interaction --no-ansi

RUN apk del gcc musl-dev python3-dev libffi-dev openssl-dev cargo g++ py-pip

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 80
