#!/bin/bash

# add a system user with restricted abilities
useradd -r fortune

# default port is 5000
CONTAINER_PORT=${1:-5000}

#See app.py file. This is the token for integrating fortune with slack.
TOKEN=${1:-"A_SLACK_TOKEN"}

#create the container name based on the port it is listening on.
#This allows us to run multiple containers on the same box
container_name="fortune-api_${CONTAINER_PORT}"
image_name='fortune-api'
container=`docker ps -a | grep " $container_name"`

#If the container already exists stop and remove it.
if [ ! -z "$container" ]; then
  docker stop $container_name && docker rm $container_name
fi

docker build --tag $image_name .

# The container will only listen on the internal 172... interface
#Ngnix is used expose the container(s) to the outside world
docker run -itd -e "TOKEN=$TOKEN" -u="`id -u fortune`" --name $container_name\
 --restart=always -p 172.17.42.1:${CONTAINER_PORT}:5000 $image_name
