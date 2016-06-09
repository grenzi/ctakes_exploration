#!/bin/bash
$ZATODIR/zato-qs-stop.sh
cd configs
zato-deploy
cd ..
find $ZATODIR | grep pid | xargs rm
$ZATODIR/zato-qs-start.sh
netstat -al | grep LIST


