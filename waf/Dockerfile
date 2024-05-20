FROM ubuntu:latest

RUN apt-get update && apt-get install -y apache2 libapache2-mod-security2 curl netcat-traditional

COPY modsecurity.conf /etc/modsecurity/modsecurity.conf
COPY crs-setup.conf /etc/modsecurity/crs-setup.conf
COPY rules /etc/modsecurity/rules
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]

EXPOSE 80 9090
