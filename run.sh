#!/bin/bash

service mariadb start
mysql < mysql_init.sql
mkdir /app/logs/nginx/
touch /app/logs/nginx/access.log
touch /app/logs/nginx/error.log
service nginx start
uwsgi --ini /app/uwsgi.ini