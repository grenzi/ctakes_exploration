#!/bin/bash
zato enmasse $ZATODIR/server1/ --input /vagrant/zatodev/configs/dbs.json  --import --replace-odb-objects
rm $ZATODIR/server1/pickup-dir/* 2>/dev/null
find ./services -name "*.py" -not -name "__init__*" | xargs -i cp {} $ZATODIR/server1/pickup-dir/
ls -l $ZATODIR/server1/pickup-dir
#find $ZATODIR/server1/pickup-dir/* | xargs -i touch {}
tail -f $ZATODIR/server1/logs/server.log