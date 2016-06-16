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

class CorporaDeleteService(CteServiceBase, Service):
    class SimpleIO:
        output_required = ('status','data',)
        input_required=('id',)

    @staticmethod
    def get_name():
        return 'cte-corpora-delete'

    # POST /corpora/{id}/delete
    def handle_POST(self):
        self.handle_DELETE()

    # DELETE /corpora/{id}
    def handle_DELETE(self):
        self.initProcessing()
        data = Bunch()

        with self.getCteSession() as session:
            c = session.query(cte.Corpus).filter_by(id=self.input.id).first()
            if c is not None:
                #delete related rows
                session.query(cte.CorpusMetadata).filter_by(corpusid=self.input.id).delete()
                session.query(cte.CorpusText).filter_by(corpusid=self.input.id).delete()
                session.delete(c)
            self.payload.data = data
            session.commit()

        self.endProcessing()
