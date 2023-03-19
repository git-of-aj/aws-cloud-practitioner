#!/bin/bash

# Update package list and install Apache web server
sudo apt update -y
sudo apt install apache2 -y

# Create directory for video page and index file
sudo mkdir -p /var/www/html/video
echo "<iframe width="560" height="315" src="https://www.youtube.com/embed/teHR00DpX2E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>" > index.html

