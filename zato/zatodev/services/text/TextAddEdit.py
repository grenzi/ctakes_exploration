# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from zato.server.service import Service
from contextlib import closing
from sql import cte
import json
from bunch import *
from cteutil import AlchemyEncoder, CteServiceBase
from sqlalchemy.ext.declarative import DeclarativeMeta

class CorpusTextEditService(CteServiceBase, Service):
    class SimpleIO:
        output_required = ('status',)
        output_optional = ('data',)
        input_optional = ('id','name',)
        input_required=('content','corpusid',)
        default_value = -1

    @staticmethod
    def get_name():
        return 'cte-corpustext-addedit'

    # POST /corpus/{id}/text/add
    # POST /corpus/{id}/text/{id}/update
    def handle_POST(self):
        self.initProcessing()
        data = Bunch()

        try:
            o = cte.CorpusText(id=self.input.id, corpusid=self.input.corpusid, name=self.input.name,
                               content=self.input.content)

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
        except Exception as e:
            self.payload.status.code = 500
            self.payload.status.msg = "ERR"
            self.payload.status.error = e
            self.payload.data = None
