FROM debian:jessie

MAINTAINER NGINX Docker Maintainers "docker-maint@nginx.com"

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.9.5-1~jessie

RUN apt-get update && \
    apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \
    rm -rf /var/lib/apt/lists/*
COPY nginx_1.conf /etc/nginx/conf.d/default.conf
COPY index.html /var/www/
COPY about.html /var/www/
COPY dist.tar.gz /var/www/resources/
RUN tar -xvzf /var/www/resources/dist.tar.gz -C /var/www/resources/ && rm -f /var/www/resources/dist.tar.gz

VOLUME ["/var/cache/nginx"]

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
