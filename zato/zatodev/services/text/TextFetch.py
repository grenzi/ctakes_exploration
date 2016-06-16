"""
.. module:: CorpusText
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

class CorpusTextFetchService(CteServiceBase, Service):
    class SimpleIO:
        output_required = ('status','data',)
        input_required = {'corpusid',}
        input_optional = ('id',)
        default_value = -1

    @staticmethod
    def get_name():
        return 'cte-corpustext-fetch'

    # GET /corpus/{id}/text
    # GET /corpus/{id}/text/{id}
    def handle_GET(self):
        self.initProcessing()

        data = []
        with self.getCteSession() as session:
            for c in session.query(cte.CorpusText).filter(corpusid=self.input.id).all():
                data.append(AlchemyEncoder.toJsonObj(c))

        if len(data)>0:
            self.payload.data = data

        self.endProcessing()