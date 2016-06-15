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

class CorporaEditService(CteServiceBase, Service):
    class SimpleIO:
        output_required = ('status','data',)
        input_optional = ('id',)
        input_required=('name', 'description')
        default_value = -1

    @staticmethod
    def get_name():
        return 'cte-corpora-addedit'

    # do we need to add PUT /corpora/{id}??
    # POST /corpora/add
    # POST /corpora/{id}/update
    def handle_POST(self):
        self.initProcessing()

        o = cte.Corpus(id=self.input.id, name=self.input.name, description=self.input.description)

        # self.logger.info(json.dumps(o, cls=AlchemyEncoder))
        data = Bunch()

        with self.getCteSession() as session:
            if o.id == -1:
                del self.request.input.id
                mo = session.add(o)
            else:
                o.id = self.request.input.id
                mo = session.merge(o)
            session.flush()

            data.id = mo.id
            data.name = mo.name
            data.description = mo.description

            self.payload.data = data
            session.commit()

        self.endProcessing()

