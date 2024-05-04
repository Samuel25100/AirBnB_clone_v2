#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt update && sudo apt install nginx -y

sudo mkdir -p /data/web_static/releases/test/

content="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" 
sudo chown -R ubuntu:ubuntu /data/

echo "$content" > /data/web_static/releases/test/index.html

sudo mkdir /data/web_static/current

sudo ln -s -f /data/web_static/current /data/web_static/releases/test/

sudo chown -R ubuntu:ubuntu /data/

sudo ufw allow 'Nginx HTTP'

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
