#!/bin/bash
rm $ZATODIR/server1/pickup-dir/* 2>/dev/null
cat /dev/null >| file $ZATODIR/server1/logs/server.log
find ./cte -name "*.py" -not -name "__init__*" | xargs -i cp {} $ZATODIR/server1/pickup-dir/
ls -l $ZATODIR/server1/pickup-dir
find $ZATODIR/server1/pickup-dir/* | xargs -i touch {}
tail -f $ZATODIR/server1/logs/server.log