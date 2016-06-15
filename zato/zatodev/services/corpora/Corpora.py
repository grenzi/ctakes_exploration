"""
.. module:: corpora
   :synopsis: A useful module indeed.

.. moduleauthor:: gage
"""

from zato.server.service import Service
from zato.server.service import AsIs, Boolean, Integer, Unicode, ListOfDicts

from contextlib import closing
from sql import cte
import json
from bunch import *
from cteutil import AlchemyEncoder
from sqlalchemy.ext.declarative import DeclarativeMeta


# class CteServiceBase(Service):
#     req = None
#     resp = None
#     payload = None
#
#     def __getCteSession(self):
#         db_config_name = 'cte-db-app'
#         return closing(self.outgoing.sql.get(db_config_name).session())
#
#     def __initProcessing(self):
#         self.req = self.request
#         self.resp = self.response
#         self.payload = self.response.payload
#         self.payload.cid = self.cid
#
#     def __endProcessing(self):
#         self.logger.info('Response: {}'.format(self.response))

class CorporaService(Service):
    class SimpleIO:
        output_required = ('cid',)
        output_optional = ('corpora', 'error')

    req = None
    resp = None
    payload = None

    def __getCteSession(self):
        db_config_name = 'cte-db-app'
        return closing(self.outgoing.sql.get(db_config_name).session())

    def __initProcessing(self):
        self.req = self.request
        self.resp = self.response
        self.payload = self.response.payload
        self.payload.cid = self.cid

    def __endProcessing(self):
        self.logger.info('Response: {}'.format(self.response))

    @staticmethod
    def get_name():
        return 'cte-corpora'


    # GET /corpora
    def handle_GET(self):
        self.__initProcessing()

        corpora = []
        with self.__getCteSession() as session:
            for c in session.query(cte.Corpus).all():
                corpora.append(AlchemyEncoder.toJsonObj(c))

        if len(corpora)>0:
            self.payload.corpora = corpora



    # PUT /corpora/{id}
    # POST /corpora/add
    # POST /corpora/{id}/update
    def handle_POST(self):
        self.response.payload.cid = "D1EF"
        self.response.payload.name = "123"
        db_config_name = 'cte-db-app'
        # req = self.request
        # resp = self.response

        #id is optional. direct assignment gives empty string

        self.logger.warn("--------------------------------")


        self.logger.info('Request: {}'.format(self.request))

        o = cte.Corpus(id=self.request.id, name=self.request.input.name, description=self.request.input.description)
        self.logger.info(json.dumps(o, cls=AlchemyEncoder))
        with closing(self.outgoing.sql.get(db_config_name).session()) as session:
            if o.id == -1:
                del self.request.input.id
                mo = session.add(o)
            else:
                o.id = self.request.input.id
                mo = session.merge(o)
            self.logger.warn(json.dumps(mo, cls=AlchemyEncoder))
            session.flush()

            self.response.payload.name = mo.name
            self.response.payload.id = mo.id
            self.response.payload.description = mo.description
            session.commit()

        self.response.payload.cid = self.cid
        self.logger.info('Response: {}'.format(self.response))

