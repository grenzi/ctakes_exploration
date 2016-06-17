"""
.. module:: corpora
   :synopsis: A useful module indeed.

.. moduleauthor:: gage
"""

from zato.server.service import Service
from contextlib import closing
from sql import cte
import json
from bunch import *
from cteutil import AlchemyEncoder, CteServiceBase
from sqlalchemy.ext.declarative import DeclarativeMeta

class CorporaFetchService(CteServiceBase, Service):
    class SimpleIO:
        output_required = ('status',)
        output_optional = ('data',)

    @staticmethod
    def get_name():
        return 'cte-corpora-list'

    # GET /corpora
    # TODO - implement get one
    def handle_GET(self):
        self.logger.warn("0")
        self.initProcessing()
        data = []
        self.logger.warn("01")

        try:
            self.logger.warn("00")
            with self.getCteSession() as session:
                self.logger.warn("00")
                for c in session.query(cte.Corpus).all():
                    self.logger.warn("00")
                    data.append(AlchemyEncoder.toJsonObj(c))

            if len(data) > 0:
                self.logger.warn("0")
                self.payload.data = data
            else:
                self.logger.warn("1")
                self.payload.data = "sadfasdf "

            self.endProcessing()
        except Exception as e:
            self.payload.status.code = 500
            self.payload.status.msg = "ERR"
            self.payload.status.error = e
            self.payload.data = "asdfasdfasdfasdfasdfasdf "
