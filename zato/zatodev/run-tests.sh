#!/usr/bin/env bash
echo "clearing db"
IP=$(/sbin/ip route | awk '/default/ { print $3 }')
mysql -uytex -pytex -h$IP -e "delete FROM cte.CorpusText; ALTER TABLE cte.CorpusText AUTO_INCREMENT = 1; "
mysql -uytex -pytex -h$IP -e "delete FROM cte.Corpus; ALTER TABLE cte.Corpus AUTO_INCREMENT = 1; "

echo "running tests"
apitest run /vagrant/zatodev/tests