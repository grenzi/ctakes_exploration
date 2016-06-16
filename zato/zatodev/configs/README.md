# export / import
to export after manual addition in web admin run
```
sudo /opt/zato/current/bin/zato enmasse $ZATODIR/server1 --export-odb --input ~/in.json
```

see [zato documenation here](https://zato.io/docs/admin/guide/enmasse.html)


to import run

```
zato enmasse $ZATODIR/server1/   --import --replace-odb-objects --input /vagrant/zatodev/cte/corpora/Corpora.json
```

[go.sh](../go.sh) runs the imports

