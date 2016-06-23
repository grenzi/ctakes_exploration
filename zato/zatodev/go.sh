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

printf "${BLUE}...deploy services${NC}\n"
rm $ZATODIR/server1/pickup-dir/* 2>/dev/null
find ./services -name "*.py" -not -name "__init__*" -print | tee | xargs -i echo cp {} $ZATODIR/server1/pickup-dir

printf "${BLUE}...deploying from conf files (will take a couple seconds as zato starts up)${NC}\n"
echo "...Dbs"
#get gateway ip address (assume db server on host os)
# this works on a windows host -->
export IP=$(/sbin/ip route | awk '/default/ { print $3 }')
#export IP=gages-mbp
echo "......setting DB IP to host IP: $IP"
sed "s/__MYSQLHOST__/$IP/g" ./configs/dbs.json > ./tempdb.json
#cat ./tempdb.json
zato enmasse $ZATODIR/server1/ --input ./tempdb.json  --import --replace-odb-objects
rm ./tempdb.json

echo "...Outgoing service links"
#zato enmasse $ZATODIR/server1/ --input /vagrant/zatodev/configs/outgoing.json  --import --replace-odb-objects

printf "${YELLOW}done.${NC}\n"


#todo - get host ip:
# netstat -rn | grep "^0.0.0.0 " | cut -d " " -f10 (but actually seems to be one low on last byte segment. idk.

