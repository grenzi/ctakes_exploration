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

## Service Template
(todo - create a script to create this...)

```
from __future__ import absolute_import, division, print_function, unicode_literals
import os.path
from zato.server.service import Service
from contextlib import closing
from sql import cte
import json
from bunch import *
from cteutil import AlchemyEncoder, CteServiceBase
from sqlalchemy.ext.declarative import DeclarativeMeta
import sys

# if you want to use a sqlalchemy object
# (see zatodev/sql/* files)
# from sql import modelname

# todo set the class name
class RestExB(Service):
    class SimpleIO:
        # TODO define inputs below usingn input_optional and input_required
        output_optional = ('data',)
        input_optional = ('id',)
        # input_required = ('id',)

    @staticmethod
    def get_name():
        # TODO fill in name in the format cte.service.noun.verb
        # verb should be one of these if applicable:
        #   Create
        #   Delete
        #   Edit
        #   GetByID
        #   GetList
        return 'cte.service.noun.verb'

    @staticmethod
    def get_channels():
        # TODO fill in the information to expose this service (right now just JSON over http
        # verb should be one of these if applicable. hypens should be removed for urls
        #   create
        #   delete
        #   edit
        #   get-by-id
        #   get-list
        return [{'name': u'cte.noun.get-list', 'method': u'GET', 'path': u'/api/noun/getlist',},
                {'name': u'cte.noun.create', 'method': u'POST', 'path': u'/api/noun/create',}]

    @staticmethod
    def after_add_to_store(logger):
        from cteutil import ChannelUtils
        logger.info('Configuring {}'.format(RestExB.get_name()))
        cu = ChannelUtils(logger)
        cu.configure_service_file(os.path.realpath(__file__))

    #todo - make stub handle examples for get/create/delete/etc
    def handle(self):
        self.initProcessing()
        data = Bunch()

        try:
            with self.getCteSession() as session:
                c = session.query(cte.Corpus).filter_by(id=self.input.id).first()
                self.payload.data = AlchemyEncoder.toJsonObj(c)
                session.commit()

            self.endProcessing()
        except Exception as e:
            self.payload.status.code = 500
            self.payload.status.msg = "ERR"
            self.payload.status.error = e
            self.payload.data = None


# so there are two ways to automatically run the configuration
# 1. just execute the file (original plan)
# 2. just deploy it (how cool is that?!?
def configure_service_on_zato():
    sys.path.append(os.environ['ZATOEXTRAPATHS'])
    from cteutil import ChannelUtils
    cu = ChannelUtils()
    cu.configure_service_file(os.path.realpath(__file__))


if __name__ == "__main__":
    configure_service_on_zato()

```

