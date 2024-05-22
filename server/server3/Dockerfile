FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y software-properties-common locales gnupg && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && \
    LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php

RUN apt-get update && apt-get install -y nginx php7.2 php7.2-cli php7.2-fpm php7.2-mysql mysql-server

COPY ./server/src /var/www/html

EXPOSE 80

CMD ["sh", "-c", "service nginx start && tail -f /dev/null"]
