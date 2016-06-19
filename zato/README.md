## configuring the vm
- vagrant init, up
- right now the shell script doesn't quite work but all the commands
  are correct
- you sould be able to copy / paste lines from the [Vagrant File](Vagrantfile)
- after you do this, the VM should have forwarded ports, so just use these addresses:
  - [web admin](http://localhost:9000/zato) (user/password admin/admin)
  - todo: put in load balancer for invoking

## first run
- run
```
vagrant ssh
$ZATODIR/zato-qs-start.sh
```
- if there's anything wrong, you won't see listening ports: ```netstat -al | grep LIST```
- run ```$ZATODIR/zato-qs-stop.sh```

## subsequent times
```
vagrant ssh
cd /vagrant/zatodev
./go.sh
```


## hot deploy of modified services
```
./deploy.sh
```

## misc
- testing info [here](https://zato.io/docs/2.0/test/apitest/index.html)
- adding a new service
  - create under zatodev/services/domain/etc
  - use template
  - if you call external webservice, add entry to [outgoings.conf](zatodev/configs/outgoings.conf)
  - add service .py file / directory / glob to [deploy.conf](zatodev/configs/deploy.conf)
  - add a plain http channel [channels.conf](zatodev/configs/channels.conf)
  - (don't forget to run go.sh on the vagrant box to create these if needed)
- right now, using https://pypi.python.org/pypi/sqlacodegen for generating the sqlalchemy defs

