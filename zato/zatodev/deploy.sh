#!/bin/bash
cp ./services/*.py $ZATODIR/server1/pickup-dir
tail -f $ZATODIR/server1/logs/server.log