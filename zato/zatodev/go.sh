#!/bin/bash
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo ""
printf "${YELLOW} don't forget to change the pubapi password in zato here http://localhost:9000/zato/security/basic-auth/?cluster=1${NC}\n"
printf "\n${BLUE}...stopping zato${NC}\n"
$ZATODIR/zato-qs-stop.sh

printf "\n${BLUE}...deploying from conf files${NC}\n"
cd configs
zato-deploy
cd ..

printf "\n${BLUE}...copying shared files${NC}\n"
#copy shared files - assume ZATODIR is at same level as zato
sudo mkdir -p $ZATODIR/../zato/current/bin/zato_extra_paths
sudo chown vagrant $ZATODIR/../zato/current/bin/zato_extra_paths
cp ./sql/*.py $ZATODIR/../zato/current/bin/zato_extra_paths

printf "${BLUE}...starting zato${NC}\n"
find $ZATODIR | grep pid | xargs rm 2>/dev/null
$ZATODIR/zato-qs-start.sh
netstat -al | grep LIST

printf "${BLUE}...all done. run deploy.sh next${NC}\n"

