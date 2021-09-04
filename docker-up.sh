#!/bin/bash

#docker-compose up -d

docker run -d \
--name=dyn-dns-checker \
-e TZ=America/Denver \
-v ./dynamic-url-python.py:/dynamic-url-python.py \
-v ./makevenv.sh:/makevenv.sh \
--restart=unless-stopped \
raychorn/ubuntu_focal_all_pythons:latest-3.9.6
