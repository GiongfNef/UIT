FROM python:3.8
MAINTAINER Dhyey

RUN apt-get update \
  && apt-get install -y gcc socat \
  && pip3 install pycryptodome sympy inputimeout \
  && rm -rf /var/lib/apt/lists/* \
  && useradd -m chal

WORKDIR /opt/chal

COPY server.py .

RUN chmod 777 /opt/chal && chmod 777 /opt/chal/*

USER chal
CMD ["socat", "-T300", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:/usr/local/bin/python3 /opt/chal/server.py,pty,echo=0"]