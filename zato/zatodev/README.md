# CTE Core Codebase

## about
blue creek uses zato.io to expose its services. This lets us scale out as
necessary by adding servers to the pool, and also provides high availablity
via its built in clustering and load balancing capabilities.

services are written in python. configuration values are stored in zato.
service endpoint information, sqlalchemy connectinos, etc, are stored in
that configuration.

## scripts used for doing development
- [go.sh](go.sh): should be run from Vagrant VM.
  - starts Zato
  - calls zato-deploy to create endpoints, etc, stored in the
    [configs](configs) subdirectory
  - calls netstat and greps for LISTENing ports so you can see that zato
    started OK
- [deploy.sh](deploy.sh): should be run from Vagrant VM.
  - copies service files from the cte subfolder here to the
    vagrant deploy directory, where zato will hot-deploy the updates
- [test.sh](test.sh): can be run from either host or guest OS. will
  probably work better on guest
  - runs zato's unit testing (apitest) against items in the [test](test) folder
- [sql/generate-sql.sh](./sql/generate-sql.sh) calls sqlacodegen to generate the
  SqlAlchemy type files for the CTE, UMLS, and YTEX databases
- TODO - get those into the zato extra paths folders or make a cte package
  or something similar
- [cte and subfolders] these are the actual implementations of the services
- [../doc](../doc/) not sure why I put this up a level in the tree, but want this to have
  our service documentation. it's a sphinx project, so ```make html``` builds it.
  that said, given the [../doc/source/conf.py](../doc/source/conf.py)
- if line endings get wonko (windows style) run ```find -type f | xargs sed -i -e 's/^M//'```

## why the api is structured the way it is and isn't that cool new REST format with fancy methods, etc
todo: put explanation here, SIO, SOAP, etc. also cover adding additoinal channels later (maybe)
