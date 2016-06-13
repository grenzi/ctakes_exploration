#!/bin/bash
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo ""
printf "${YELLOW} don't forget to change the pubapi password to pubapi in zato here http://localhost:9000/zato/security/basic-auth/?cluster=1${NC}\n"
printf "\n${BLUE}...stopping zato${NC}\n"
$ZATODIR/zato-qs-stop.sh

printf "\n${BLUE}...deploying from conf files${NC}\n"
cd configs
#zato-deploy
cd ..

printf "\n${BLUE}...copying shared files${NC}\n"
sudo mkdir -p /opt/zato/2.0.7/zato_extra_paths/sql
sudo chown vagrant /opt/zato/2.0.7/zato_extra_paths/sql
cp ./sql/*.py /opt/zato/2.0.7/zato_extra_paths/sql
sudo cp -R ./lib/bunch /opt/zato/2.0.7/zato_extra_paths

printf "${BLUE}...starting zato${NC}\n"
find $ZATODIR | grep pid | xargs rm 2>/dev/null
$ZATODIR/zato-qs-start.sh
netstat -al | grep LIST

printf "${BLUE}...running deploy.sh next${NC}\n"
source ./deploy.sh


#todo - get host ip:
# netstat -rn | grep "^0.0.0.0 " | cut -d " " -f10 (but actually seems to be one low on last byte segment. idk.

