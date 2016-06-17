# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from zato.server.service import Service
from contextlib import closing
from sql import cte
import json
from bunch import *
from cteutil import AlchemyEncoder, CteServiceBase
from sqlalchemy.ext.declarative import DeclarativeMeta

class CorporaEditService(CteServiceBase, Service):
    class SimpleIO:
        output_required = ('status',)
        output_optional = ('data',)
        input_optional = ('id',)
        input_required=('name', 'description',)
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

        # self.logger.info(json.dumps(self.input))
        # self.logger.info(json.dumps(o, cls=AlchemyEncoder))
        data = Bunch()

        try:
            with self.getCteSession() as session:
                if o.id == -1 or o.id is None:
                    o.id = None
                    session.add(o)
                else:
                    o = session.merge(o)
                session.flush()

                data.id = o.id
                data.name = o.name
                data.description = o.description

                self.payload.data = data
                session.commit()

            self.endProcessing()

        except Exception as e:
            self.payload.status.code = 500
            self.payload.status.msg = "ERR"
            self.payload.status.error = e
            self.payload.data = None
