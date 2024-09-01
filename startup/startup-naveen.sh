#!/bin/bash

echo "deb http://deb.debian.org/debian bullseye main" > /etc/apt/sources.list
echo "deb http://deb.debian.org/debian bullseye-updates main" >> /etc/apt/sources.list
echo "deb http://security.debian.org/debian-security bullseye-security main" >> /etc/apt/sources.list

# Update package lists and install python3 and python3-pip
apt-get update
apt-get install python3 python3-pip -y --allow-unauthenticated

