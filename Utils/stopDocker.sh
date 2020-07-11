docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images dev* -q);rm -rf /tmp/hfc-*
