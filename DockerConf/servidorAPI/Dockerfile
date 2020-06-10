FROM python:3-alpine

ARG COLLECTION
ARG USERNAME
ARG PASSWORD
ARG HOST
ARG PORT
ARG AUTHSOURCE
ARG DB

RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev
RUN apk add --no-cache pcre

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install update
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python setconf.py host:${HOST} port:${PORT} username:${USERNAME} password:${PASSWORD} authsource:${AUTHSOURCE} db:${DB} collection:${COLLECTION}

CMD ["uwsgi", "--ini", "./wsgi.ini"]