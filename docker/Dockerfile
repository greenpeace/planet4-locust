FROM gcr.io/planet-4-151612/ubuntu:latest

MAINTAINER Raymond Walker <raymond.walker@greenpeace.org>

RUN apt-fast update \
    && apt-fast install -y --no-install-recommends \
        build-essential \
        libc6-dev \
        libgdbm-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        libxslt-dev \
        libzmq3-dev \
        python \
        python-dev \
        python-pip \
        python-setuptools \
    && pip install pyzmq locustio pyquery\
    && apt-get autoremove -yqq \
    && rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/* \
    && rm -fr /usr/share/man/* /usr/share/doc/* /usr/share/locale/* /var/cache/apt/apt-fast

COPY . /app/

EXPOSE 8089 5557 5558

ENV \
    CACHE_BUSTER="false" \
    LOCUST_MASTER="" \
    LOCUST_MODE="standalone" \
    LOCUST_FILE="/app/locustfile.py" \
    LOCUST_OPTIONS="" \
    INSECURE_SSL="" \
    TARGET_URL="https://docker.p4.greenpeace.org"
