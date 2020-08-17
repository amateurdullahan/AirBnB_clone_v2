#!/usr/bin/env bash
# task 0
sudo apt-get install nginx
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/current
mkdir -p /data/web_static/releases/test
echo "Wangxian OTP" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test
chown -R ubuntu:ubuntu /data
sed '/^\tserver_name*/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart 
