#!/usr/bin/env bash
#sets up webservers for deployment of webstatic
mkdir -p /data/web_static/releases/test;
echo 'Hello World!' > /data/web_static/releases/test/index.html;
if [ -L /data/web_static/current ]; then
	rm /data/web_static/current;
ln -s /data/web_static/releases/test/ /data/web_static/current;
chown ubuntu /data/;
SERVER_CONFIG="\
htpp{
	server {
		listen 80;
		listen [::]:80 default_server;
		server_name vitalisalexia.tech;

		location /hbnb_static {
		alias /data/web_static/current/;
		}
	}
}\
"
echo -e "$SERVER_CONFIG" | tee /etc/nginx/sites-enabled/default;
nginx -s reload;
