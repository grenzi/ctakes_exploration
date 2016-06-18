# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from zato.server.service import Service
from contextlib import closing
from sql import cte
import json
from bunch import *
from cteutil import AlchemyEncoder, CteServiceBase
from sqlalchemy.ext.declarative import DeclarativeMeta

class CorpusTextFetchService(CteServiceBase, Service):
    class SimpleIO:
        output_required = ('status',)
        output_optional = ('data',)
        input_required = ('corpusid',)
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

        try:
            with self.getCteSession() as session:
                if self.input.id == -1 or self.input.id is None:
                    for t in session.query(cte.CorpusText).filter(corpusid=self.input.corpusid).all():
                        data.append(AlchemyEncoder.toJsonObj(t))
                else:
                    t = session.query(cte.Corpus).filter_by(id=self.input.id, corpusid=self.input.corpusid).first()
                    data.append(AlchemyEncoder.toJsonObj(t))

            self.payload.data = data
            self.endProcessing()
        except Exception as e:
            self.payload.status.code = 500
            self.payload.status.msg = "ERR"
            self.payload.status.error = e
            self.payload.data = None
