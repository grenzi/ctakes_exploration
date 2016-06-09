#!/bin/bash
echo "don't forget to change the pubapi password in zato here http://localhost:9000/zato/security/basic-auth/?cluster=1"
$ZATODIR/zato-qs-stop.sh
cd configs
zato-deploy
cd ..
find $ZATODIR | grep pid | xargs rm
$ZATODIR/zato-qs-start.sh
netstat -al | grep LIST


