FROM fedora:37

# Install necessary packages
RUN dnf install -y wget gcc gcc-c++ make php php-mysqlnd mariadb

# Install Caddy
RUN wget https://github.com/caddyserver/caddy/releases/download/v2.4.6/caddy_2.4.6_linux_amd64.tar.gz && \
    tar -zxvf caddy_2.4.6_linux_amd64.tar.gz && \
    mv caddy /usr/local/bin/ && \
    rm -rf caddy_2.4.6_linux_amd64.tar.gz

# Copy the web application files
COPY ./server/src /srv/www

# Copy the Caddyfile configuration
COPY ./server/server2/Caddyfile /etc/caddy/Caddyfile

EXPOSE 80

CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
