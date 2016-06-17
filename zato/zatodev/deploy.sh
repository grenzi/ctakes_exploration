#!/bin/bash
rm $ZATODIR/server1/pickup-dir/* 2>/dev/null
find ./services -name "*.py" -not -name "__init__*" | xargs -i cp {} $ZATODIR/server1/pickup-dir/
ls -l $ZATODIR/server1/pickup-dir

#remove comment below to tail logs for a little while.
#tail -f $ZATODIR/server1/logs/server.log & P=$! ; sleep 5; kill -9 $P
IP=$(/sbin/ip route | awk '/default/ { print $3 }')
mysql -uytex -pytex -h$IP -e "delete FROM cte.CorpusText; ALTER TABLE cte.CorpusText AUTO_INCREMENT = 1; "
mysql -uytex -pytex -h$IP -e "delete FROM cte.Corpus; ALTER TABLE cte.Corpus AUTO_INCREMENT = 1; "