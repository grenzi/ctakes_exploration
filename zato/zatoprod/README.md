# prod server setup
```
zato quickstart create --odb_host 162.243.212.81 --odb_port 3306 --odb_user zato --odb_db_name zato --odb_password zato --cluster_name cte_prod --servers 1 /opt/zatoprod mysql 162.243.212.81 6379
zato update password $ZATODIR/web-admin/ admin

sudo /opt/zato/current/bin/zato quickstart create --odb_host gages-MBP --odb_port 3306 --odb_user zato --odb_db_name zato --odb_password zato --cluster_name cte_dev --servers 1 /opt/zatodev mysql localhost 6379

```

## in ~/.bashrc
```
export JAVA_HOME=/usr/lib/jvm/java-7-oracle
export ZATODIR=/opt/zatoprod
export ZATOEXTRAPATHS=/opt/zato/2.0.7/zato_extra_paths
```


# servers
sudo apt-get install -y mysql-server-5.6
NLPMySql 104.236.93.209
NLPDemo 162.243.212.81

CREATE USER 'ytexapp'@'%' IDENTIFIED BY 'ytex';
CREATE USER 'umlsapp'@'%' IDENTIFIED BY 'umls';
CREATE USER 'cteapp'@'%' IDENTIFIED BY 'cteapp';

CREATE DATABASE IF NOT EXISTS umls CHARACTER SET utf8 COLLATE utf8_unicode_ci;
GRANT ALL PRIVILEGES ON umls.* TO 'umlsapp'@'%';
GRANT SELECT on umls.* to 'ytexapp'@'%';

CREATE DATABASE IF NOT EXISTS ytex CHARACTER SET utf8;
GRANT ALL PRIVILEGES ON ytex.* TO 'ytexapp'@'%';

CREATE DATABASE IF NOT EXISTS cte CHARACTER SET utf8;
GRANT ALL PRIVILEGES ON cte.* TO 'cteapp'@'%';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';

FLUSH PRIVILEGES;
