#!/usr/bin/bash

# Update package list and install Apache web server
sudo apt update -y
sudo apt install apache2 -y

# Create directory for video page and index file
sudo mkdir -p /var/www/html/video
wget https://raw.githubusercontent.com/Ananyojha/AZ-104-Training/main/index.html
sudo cp ./index.html /var/www/html/video/index.html


