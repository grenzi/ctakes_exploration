# prod server setup
```
zato quickstart create --odb_host 162.243.212.81 --odb_port 3306 --odb_user zato --odb_db_name zato --odb_password zato --cluster_name cte_prod --servers 1 /opt/zatoprod mysql 162.243.212.81 6379
zato update password $ZATODIR/web-admin/ admin
```

## in ~/.bashrc
```
export JAVA_HOME=/usr/lib/jvm/java-7-oracle
export ZATODIR=/opt/zatoprod
export ZATOEXTRAPATHS=/opt/zato/2.0.7/zato_extra_paths
```


