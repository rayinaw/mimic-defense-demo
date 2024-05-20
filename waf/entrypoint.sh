#!/bin/bash

# Start Apache in the background
apachectl -D FOREGROUND &

# Create a simple server to receive rules
while true; do
  nc -l -p 9090 -c 'cat > /etc/modsecurity/rules/custom_rules.conf && apachectl graceful'
done
