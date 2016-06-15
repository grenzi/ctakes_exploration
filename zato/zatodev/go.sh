#!/bin/bash
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m'

ZATOEXTRAPATHS=/opt/zato/2.0.7/zato_extra_paths
echo ""
printf "${YELLOW} tail -f $ZATODIR/server1/logs/server.log to watch zato side\n"
printf "${BLUE}...stopping zato${NC}\n"
$ZATODIR/zato-qs-stop.sh >/dev/null

printf "${BLUE}...deploying from conf files${NC}\n"
cd configs
#zato-deploy
cd ..

printf "${BLUE}...copying shared files${NC}\n"
sudo mkdir -p $ZATOEXTRAPATHS/sql
sudo chown vagrant $ZATOEXTRAPATHS/sql
cp ./sql/*.py $ZATOEXTRAPATHS/sql
sudo cp -R ./lib/* $ZATOEXTRAPATHS

printf "${BLUE}...starting zato${NC}\n"
find $ZATODIR | grep pid | xargs rm 2>/dev/null
$ZATODIR/zato-qs-start.sh
#netstat -al | grep LIST

printf "${BLUE}...run deploy.sh next${NC}\n"



#todo - get host ip:
# netstat -rn | grep "^0.0.0.0 " | cut -d " " -f10 (but actually seems to be one low on last byte segment. idk.

