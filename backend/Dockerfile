FROM python:3.9-alpine

ENV POETRY_VERSION=1.1.2

RUN pip install --upgrade pip &&\
    apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo g++ postgresql-dev zlib libjpeg &&\
    pip install "poetry==$POETRY_VERSION"

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

WORKDIR /code
COPY . /code

RUN poetry config virtualenvs.create false &&\
    poetry install --no-interaction --no-ansi

RUN apk del gcc musl-dev python3-dev libffi-dev openssl-dev cargo g++ py-pip

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 80
