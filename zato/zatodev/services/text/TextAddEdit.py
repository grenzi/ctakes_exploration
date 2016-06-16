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

class CorpusTextEditService(CteServiceBase, Service):
    class SimpleIO:
        output_required = ('status','data',)
        input_optional = ('id','name',)
        input_required=('content','corpusid',)
        default_value = -1

    @staticmethod
    def get_name():
        return 'cte-corpustext-addedit'

    # do we need to add PUT /CorpusText/{id}??
    # POST /corpus/{id}/text/add
    # POST /corpus/{id}/text/{id}/update
    def handle_POST(self):
        self.initProcessing()

        o = cte.CorpusText(id=self.input.id, corpusid=self.input.corpusid, name=self.input.name, content=self.input.content)

        data = Bunch()

        with self.getCteSession() as session:
            if o.id == -1 or o.id is None:
                o.id = None
                session.add(o)
            else:
                o = session.merge(o)
            session.flush()

            data.id = o.id
            data.corpusid = o.corpusid

            self.payload.data = data
            session.commit()

        self.endProcessing()

