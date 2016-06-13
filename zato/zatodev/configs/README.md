# about zato config import and export
sudo /opt/zato/current/bin/zato enmasse $ZATODIR/server1 --export-local  --input ~/in.json
sudo /opt/zato/current/bin/zato enmasse $ZATODIR/server1 --export-odb --input ~/in.json

see [zato documenation here](https://zato.io/docs/admin/guide/enmasse.html)

netstat -nr, although see other.
10.211.55.1

zato enmasse $ZATODIR/server1/   --import --replace-odb-objects --input /vagrant/zatodev/cte/corpora/Corpora.json

zato enmasse $ZATODIR/server1/ --input /vagrant/zatodev/cte/corpora/Corpora-List.json  --import --replace-odb-objects
