FROM opensuse/leap:15.0

RUN zypper refresh && \
    zypper install -y apache2 apache2-prefork php7 php7-mysql mariadb && \
    zypper clean --all

COPY ./server/src /srv/www/htdocs

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
