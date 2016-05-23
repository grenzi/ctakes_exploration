#!/usr/bin/env bash
#ok - maybe docker is the best thing in the world, i just can't get
#shared folders to work. leaving this here for posterity.
#also, just discovered that they have a vagrant flavor =)

docker-machine start dockdev
docker-machine env dockdev
eval "$(docker-machine env dockdev)"

myip=`docker-machine ip dockdev | sed -n 1p`
echo $myip

#shared folder = mount to opt/docker on vm
mydir=`pwd`
#shared folder portion is  -d -P --name zato -v $mydir:/opt/docker
docker run -i -t k3_s3:latest /bin/bash

#launch zato
docker run -it -p 22 -p 6379:6379 -p 8183:8183 -p 17010:17010 -p 17011:17011 \
        -p 11223:11223 zatosource/zato-2.0.7-quickstart:env /bin/bash -c "/opt/zato/start.sh" \
        -d -P -name zato -v $mydir:/opt/docker


#login as root
#docker ps
#(get id)
#docker exec -i -t 8a6974be89a0 /bin/bash