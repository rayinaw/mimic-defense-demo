FROM debian:latest

# Install Apache and ModSecurity
RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-security2 \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Enable ModSecurity and configure it
RUN a2enmod security2 && \
    echo "Include /etc/modsecurity/modsecurity.conf" >> /etc/apache2/apache2.conf

# Create the directory for ModSecurity custom rules
RUN mkdir -p /etc/modsecurity/custom_rules

# Copy the modsecurity.conf and entrypoint.sh
COPY modsecurity.conf /etc/modsecurity/modsecurity.conf
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80 9090
