#!/usr/bin/env bash
#sets up webservers for deployment of webstatic

sudo apt-get -y update
sudo apt-get -y install nginx
#make the neccesary directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#make a fake index html
sudo echo 'Hey there am now learning to deploy' | sudo tee /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/;
SERVER_CONFIG="\
server {
	listen 80;
	listen [::]:80 default_server;
	server_name vitalisalexia.tech;
	location /hbnb_static {
		alias /data/web_static/current/;
	}
}\
"
sudo echo -e "$SERVER_CONFIG" | sudo tee /etc/nginx/sites-enabled/default
sudo nginx -s reload
