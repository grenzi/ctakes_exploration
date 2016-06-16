#!/bin/bash
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m'

ZATOEXTRAPATHS=/opt/zato/2.0.7/zato_extra_paths
echo ""
printf "${YELLOW} tail -f $ZATODIR/server1/logs/server.log to watch zato side\n"
printf "${BLUE}...stopping zato${NC}\n"
$ZATODIR/zato-qs-stop.sh >/dev/null

printf "${BLUE}...copying lib files to zato include directory${NC}\n"
sudo mkdir -p $ZATOEXTRAPATHS/sql
sudo chown vagrant $ZATOEXTRAPATHS/sql
cp ./sql/*.py $ZATOEXTRAPATHS/sql
sudo cp -R ./lib/* $ZATOEXTRAPATHS

printf "${BLUE}...starting zato${NC}\n"
find $ZATODIR | grep pid | xargs rm 2>/dev/null
$ZATODIR/zato-qs-start.sh
#netstat -al | grep LIST


printf "${BLUE}...deploying from conf files (will take a couple seconds as zato starts up)${NC}\n"
echo "...Dbs"
zato enmasse $ZATODIR/server1/ --input /vagrant/zatodev/configs/dbs.json  --import --replace-odb-objects
echo "...Outgoing service links"
zato enmasse $ZATODIR/server1/ --input /vagrant/zatodev/configs/outgoing.json  --import --replace-odb-objects
echo "...Corpora"
zato enmasse $ZATODIR/server1/ --input /vagrant/zatodev/services/corpora/Corpora.json  --import --replace-odb-objects
echo "...Text"
zato enmasse $ZATODIR/server1/ --input /vagrant/zatodev/services/text/Text.json  --import --replace-odb-objects

printf "${YELLOW}done. run ./deploy.sh next${NC}\n"

#todo - get host ip:
# netstat -rn | grep "^0.0.0.0 " | cut -d " " -f10 (but actually seems to be one low on last byte segment. idk.

