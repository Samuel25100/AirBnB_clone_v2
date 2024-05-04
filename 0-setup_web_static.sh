#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt update && sudo apt install nginx -y

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

cont="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

sudo chown -R ubuntu:ubuntu /data/

echo "$cont" > /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo ufw allow 'Nginx HTTP'

sudo sed -i '/listen 80 default_server/a\\n\t\tlocation /hbnb_static {\n\t  alias /data/web_static/current/;\n\t\t  autoindex off;\n\t\t}' /etc/nginx/sites-enabled/default

sudo service nginx restart
