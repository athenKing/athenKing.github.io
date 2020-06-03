---
layout: post
title: How to set a gogs server on a remote server?
date: 2019-10-09 19:29:35 +0800
categories: Engineering-Pieces
---


## Buy the domain name lets-do-it.online


## Install go language for gogs installtion

<!-- sudo add-apt-repository ppa:longsleep/golang-backports -->

sudo apt-get update
sudo apt-get install golang-go


## Download gogs binary file

wget https://dl.gogs.io/0.11.53/gogs_0.11.53_linux_amd64.tar.gz

**move file to proper location like this**

tar -C /usr/lib -xzf gogs_0.11.53_linux_amd64.tar.gz

**install git**

apt-get install git

**install mysql-server**

apt-get install mysql-server

by setting phase,set root password to be root123


**Before running gogs successfully,firstly we create a new database**


## after setting up the gogs, we need to install nginx to proxypass port 80 to 3000 like this


### Firstly install nginx

sudo apt-get update
sudo apt-get install nginx

### Then set nginx set up,set the whole config file 

sudo vi /etc/nginx/sites-available/default

like this 

server {
    listen 80;

    server_name lets-do-it.online;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}


## To set gogs attachment size to upload large file

in path /gogs/conf/app.ini add configuration as below:
[attachment]

FILE_SIZE = 200(MB)
FILE_NUMS = 5 (Files count to upload by the same time)