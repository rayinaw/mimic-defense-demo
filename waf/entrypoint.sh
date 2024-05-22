#!/bin/bash

# Enable ModSecurity
sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/' /etc/modsecurity/modsecurity.conf

# Start Apache
apachectl -D FOREGROUND
