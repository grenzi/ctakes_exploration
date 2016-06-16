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

class CorpusTextDeleteService(CteServiceBase, Service):
    class SimpleIO:
        output_required = ('status','data',)
        input_required=('id','corpusid',)

    @staticmethod
    def get_name():
        return 'cte-corpustext-delete'

    # POST /corpus/{id}/text/{id}/delete
    def handle_POST(self):
        self.handle_DELETE()

    # DELETE /corpus/{id}/text/{id}
    def handle_DELETE(self):
        self.initProcessing()
        data = Bunch()

        with self.getCteSession() as session:
            c = session.query(cte.CorpusText).filter_by(id=self.input.id,corpusid=self.input.corpusid).first()
            if c is not None:
                session.delete(c)
            session.commit()
            self.payload.data = data

        self.endProcessing()
