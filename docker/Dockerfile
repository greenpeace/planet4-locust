FROM gcr.io/planet-4-151612/ubuntu:develop

MAINTAINER Raymond Walker <raymond.walker@greenpeace.org>

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        libc6-dev \
        libgdbm-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        libxslt-dev \
        python \
        python-dev \
        python-setuptools \
    && easy_install \
        locustio \
        pyzmq \
        pyquery \
    && apt-get autoremove -yqq \
    && rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/* \
    && rm -fr /usr/share/man/* /usr/share/doc/* /usr/share/locale/*

COPY . /app/

EXPOSE 8089 5557 5558

ENV \
    LOCUST_MASTER="" \
    LOCUST_MODE="standalone" \
    LOCUST_FILE="/app/locustfile.py" \
    LOCUST_OPTIONS="" \
    INSECURE_SSL="" \
    TARGET_URL="https://docker.p4.greenpeace.org"
