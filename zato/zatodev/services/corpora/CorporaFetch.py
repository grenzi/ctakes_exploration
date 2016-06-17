# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
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
        self.initProcessing()
        data = []

        try:
            with self.getCteSession() as session:
                for c in session.query(cte.Corpus).all():
                    data.append(AlchemyEncoder.toJsonObj(c))

            if len(data) > 0:
                self.payload.data = data

            self.endProcessing()
        except Exception as e:
            self.payload.status.code = 500
            self.payload.status.msg = "ERR"
            self.payload.status.error = e
