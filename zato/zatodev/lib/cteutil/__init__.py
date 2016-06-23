__version__ = '1.0.0'
VERSION = tuple(map(int, __version__.split('.')))

__all__ = ('AlchemyEncoder','CteServiceBase', 'ChannelUtils')

import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from zato.server.service import Service
from zato.client import AnyServiceInvoker
import ast
import os.path
from contextlib import closing
from bunch import *


def load_from_file(filepath, expected_class):
    import imp
    class_inst = None

    mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

    if file_ext.lower() == '.py':
        py_mod = imp.load_source(mod_name, filepath)

    elif file_ext.lower() == '.pyc':
        py_mod = imp.load_compiled(mod_name, filepath)

    if hasattr(py_mod, expected_class):
        class_inst = getattr(py_mod, expected_class)()

    return class_inst

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


class ChannelUtils:
    def __init__(self, logger=None):
        try:
            self.address = 'http://localhost:11223'
            self.path = '/zato/admin/invoke'
            self.auth = ('admin.invoke', os.environ["ZATOPASS"])
            self.client = AnyServiceInvoker(self.address, self.path, self.auth)
            self.channeldict = None
            self.loggerobj = logger
        except KeyError:
            print "Please set the environment variable ZATOPASS"
            self.log('Please set the environment variable ZATOPASS')
            sys.exit(1)

    def get_channels(self):
        self.channeldict = {}

        payload = {"cluster_id": 1, "connection": "channel", "transport": "plain_http"}
        response = self.client.invoke('zato.http-soap.get-list', payload=payload)

        if response.ok:
            d = response.data
            for c in d:
                self.channeldict[c[ u'name']]=c[ u'id']
            return self.channeldict
        else:
            self.log('ERROR getting channel dictionary')
            return {}

    def delete_channel(self, id):
        self.channeldict = {}

        payload = {"id": id}
        response = self.client.invoke('zato.http-soap.delete', payload=payload)

        if response.ok:
            pass
        else:
            print(response.details)
            return {}

    def add_channel(self, channelname, servicename, url, method, skipifexists=False):
        if self.channeldict is None:
            self.get_channels()

        if skipifexists == False and channelname in self.channeldict:
            self.delete_channel(id=self.channeldict[channelname])

        payload = {}
        payload[u'connection'] = u'channel'
        payload[u'name'] = channelname
        payload[u'cluster_id'] = 1
        payload[u'transport'] = u'plain_http'
        payload[u'url_path'] = url
        payload[u'service'] = servicename
        payload[u'method'] = method
        payload[u'data_format'] = u'json'
        payload[u'is_active']=True
        payload[u'is_internal']=False

        response = self.client.invoke('zato.http-soap.create', payload=payload)

        if response.ok:
            pass
        else:
            print(response.details)
            return {}

    def log(self, msg):
        if self.loggerobj is not None:
            self.loggerobj.info(msg)
        else:
            print msg

    def configure_service_file(self, filepath):
        source = ''
        self.log('Processing {}'.format(filepath))
        with open(filepath, 'r') as f:
            source = f.read()
        p = ast.parse(source)

        classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
        for classname in classes:
            if classname != 'SimpleIO':
                classobj = load_from_file(filepath, classname)

                namemethod = getattr(classobj, 'get_name')
                servicename = namemethod()

                channelmethod = getattr(classobj, 'get_channels')
                channels = channelmethod()

                for channel in channels:
                    self.log('Adding channel {}'.format(channel['name']))
                    self.add_channel(channel['name'], servicename, channel['path'], channel['method'])

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
        self.input = self.request.input or None
        self.resp = self.response
        self.payload = self.response.payload
        self.payload.status = Bunch()
        self.payload.status.ver = 1
        self.payload.status.code = 200
        self.payload.status.msg = "OK"
        self.payload.status.info = None
        self.payload.status.error = None
        self.payload.status.cid = self.cid
        #self.log_input("-----------------------input:")

    def endProcessing(self):
        #self.log_output("-----------------------output:")
        pass

    def errorHandler(self, e):
        self.payload.status.code = 500
        self.payload.status.msg = "ERR"
        self.payload.status.error = e
        self.payload.data = None

