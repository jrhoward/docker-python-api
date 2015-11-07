#!/bin/bash

container_name='ngnix-proxy'
image_name='ngnix-proxy'
container=`docker ps -a | grep " $container_name "`

if [ ! -z "$container" ]; then
  docker stop $container_name && docker rm $container_name
fi

docker build --tag=$image_name .

docker run -itd  --name $container_name --restart=always  -p 80:80  $image_name
