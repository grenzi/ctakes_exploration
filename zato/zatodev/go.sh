#!/bin/bash
$ZATODIR/zato-qs-stop.sh
#cp -R /vagrant/zatoenv $ZATODIR
./config.py
find $ZATODIR | grep pid | xargs rm
$ZATODIR/zato-qs-start.sh