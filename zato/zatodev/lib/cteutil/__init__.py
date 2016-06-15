__version__ = '1.0.0'
VERSION = tuple(map(int, __version__.split('.')))

__all__ = ('AlchemyEncoder','CteServiceBase')

import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from zato.server.service import Service

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

