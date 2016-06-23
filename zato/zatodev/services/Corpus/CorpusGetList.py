from __future__ import absolute_import, division, print_function, unicode_literals
import os.path
from zato.server.service import Service
from contextlib import closing
from sql import cte
import json
from bunch import *
from cteutil import AlchemyEncoder, CteServiceBase
from sqlalchemy.ext.declarative import DeclarativeMeta
import sys


class CorpusGetListService(CteServiceBase, Service):
    class SimpleIO:
        output_optional = ('data',)

    @staticmethod
    def get_name():
        return 'cte.service.Corpus.GetList'

    @staticmethod
    def get_channels():
        return[
            {'name': u'cte.corpus.get-list.GET', 'method': u'GET', 'path': u'/api/corpus/get-list'},
        ]

    @staticmethod
    def after_add_to_store(logger):
        from cteutil import ChannelUtils
        logger.info('Configuring {}'.format(CorpusGetListService.get_name()))
        cu = ChannelUtils(logger)
        cu.configure_service_file(os.path.realpath(__file__))

    def handle(self):
        self.initProcessing()
        data = Bunch()

        try:
            with self.getCteSession() as session:
                for c in session.query(cte.Corpus).all():
                    data.append(AlchemyEncoder.toJsonObj(c))

            if len(data) > 0:
                self.payload.data = data

            self.endProcessing()
        except Exception as e:
            self.errorHandler(e)


# this is run when the file is run in CLI. if you add things here, also put in after_add_to_store above
def configure_service_on_zato():
    sys.path.append(os.environ['ZATOEXTRAPATHS'])
    from cteutil import ChannelUtils
    cu = ChannelUtils()
    cu.configure_service_file(os.path.realpath(__file__))


if __name__ == "__main__":
    configure_service_on_zato()
