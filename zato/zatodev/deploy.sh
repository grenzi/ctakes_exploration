#!/bin/bash
#MYSQLHOST=$(/sbin/ip route | awk '/default/ { print $3 }')
#echo ZATOPASS SHOULD BE SET IN THE ENVIRONMENT.
#admininvokepass=$(echo "SELECT \`password\` FROM zato.sec_base where name = 'admin.invoke' limit 1" | mysql zato -uzatoapp -pzatoapp -h$MYSQLHOST)
#admininvokepass=782fd57d201a4ff39918c09f100cd3f4
#echo 'export ZATOPASS='"$admininvokepass"
#rm $ZATODIR/server1/pickup-dir/* 2>/dev/null
find ./services -name "*.py" -not -name "__init__*" | xargs -i cp {} $ZATODIR/server1/pickup-dir/
ls -l $ZATODIR/server1/pickup-dir

#remove comment below to tail logs for a little while.
#tail -f $ZATODIR/server1/logs/server.log & P=$! ; sleep 5; kill -9 $P
