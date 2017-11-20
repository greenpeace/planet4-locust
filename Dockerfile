FROM gcr.io/planet-4-151612/ubuntu:develop

RUN apt-get update \
  && apt-get install -y \
    build-essential \
    libncursesw5-dev \
    libreadline-dev \
    libssl-dev \
    libgdbm-dev \
    libc6-dev \
    libsqlite3-dev \
    libxml2-dev \
    libxslt-dev \
    python \
    python-dev \
    python-setuptools \
  && easy_install locustio pyzmq \
  && apt-get autoremove -yqq \
  && rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/* \
  && rm -fr /usr/share/man/* /usr/share/doc/* /usr/share/locale/* \


EXPOSE 8089 5557 5558

ENV \
    LOCUST_MASTER="" \
    LOCUST_MODE="standalone" \
    SCENARIO_FILE="/app/locustfile.py" \
    TARGET_URL=""
