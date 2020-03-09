FROM ubuntu:18.04
RUN apt-get update && \
  apt-get install -y build-essential python3.7 python3.7-dev tox
COPY . /app
WORKDIR /app
