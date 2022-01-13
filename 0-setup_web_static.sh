#!/usr/bin/env bash
# all all all all

apt-get update -y
apt-get install nginx -y
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu /data
sudo chgrp -R ubuntu /data
sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default
service nginx restart
