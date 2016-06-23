
# Info

- these are the name suffixes that zato uses to assign input value types
  for simpleio services

From their website [here](https://zato.io/docs/progguide/sio.html)


### Datatypes
Zato uses a few conventions when deciding when to convert request and response parameters between various datatypes. This can be helpful because otherwise all the request parameters could've been strings - this is true for both JSON and XML but doubly so for the latter.

- If a parameter's name is 'id' it will be converted to an integer
- If a parameter ends with '_id', '_size' or '_timeout' it will be converted to an integer
- If a parameter begins with 'is_', 'needs_', 'should_' it will be converted to a bool

Name	Notes
AsIs	A pass-through marker, no conversions will be performed even though normally one would've been attempted
Boolean	Converted to a bool object
CSV	Converted to/from comma-separated values
Dict	Converted to a dictionary
Integer	Converted to an integer
List	Converted to a list
ListOfDicts	Converted to a list of dictionaries
Opaque	Similar to AsIs but works with arbitrarily nested structures as well
Unicode	Converted to a unicode object


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




