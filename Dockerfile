FROM fedora:31
RUN dnf install -y gcc python3 python3-devel python3-tox
COPY . /app
WORKDIR /app
