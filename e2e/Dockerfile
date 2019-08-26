FROM ubuntu:18.04

ENV LANG C.UTF-8
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update -y && apt-get install -y curl && apt-get autoremove

ADD wait-for-it.sh /usr/bin/wait-for-it
RUN chmod a+x /usr/bin/wait-for-it

ADD . /pah-fm/e2e
WORKDIR /pah-fm/e2e
