# setup performed on server box

- mysql schema and user creation

```
export ZATODIR=/opt/zatoenv/ca
mkdir -p $ZATODIR

zato create odb --store-config --odb_host 162.243.212.81 --odb_port 3306 --odb_user zato --odb_db_name zato --odb_password zato mysql


zato create cluster --store-config --odb_host 162.243.212.81 --odb_port 3306 --odb_user zato --odb_db_name zato --odb_password zato --tech_account_password Nusiv4321# mysql 162.243.212.81 80 81 localhost 6379 cte_cluster admin

mkdir -p /opt/zatoenv/ca &&
zato ca create ca /opt/zatoenv/ca

mkdir -p $ZATODIR/load_balancer_agent &&
zato ca create lb_agent $ZATODIR/ca/ load_balancer_agent

mkdir -p $ZATODIR/server1 &&
zato ca create server $ZATODIR/ca/ cte_cluster server1

mkdir -p $ZATODIR/web_admin &&
 zato ca create web_admin $ZATODIR/ca/
```

zato quickstart create --odb_host 162.243.212.81 --odb_port 3306 --odb_user zato --odb_db_name zato --odb_password zato --cluster_name cte_prod --servers 1 /opt/zatoprod mysql 162.243.212.81 6379