__version__ = '1.0.0'
VERSION = tuple(map(int, __version__.split('.')))

__all__ = ('AlchemyEncoder','CteServiceBase')

import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from zato.server.service import Service
from contextlib import closing
from bunch import *

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

    @staticmethod
    def toJsonObj(obj):
        a = json.dumps(obj, cls=AlchemyEncoder)
        b = json.loads(a)
        return b

class CteServiceBase():
    req = None
    resp = None
    payload = None
    input = None

    def getCteSession(self):
        db_config_name = 'cte-db-app'
        return closing(self.outgoing.sql.get(db_config_name).session())

    def initProcessing(self):
        self.req = self.request
        self.input = self.request.input
        self.resp = self.response
        self.payload = self.response.payload
        self.payload.status = Bunch()
        self.payload.status.ver = 1
        self.payload.status.code = 200
        self.payload.status.msg = "OK"
        self.payload.status.error = None
        self.payload.status.cid = self.cid

    def endProcessing(self):
        self.logger.info('Response: {}'.format(self.response))
