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


class CorpusEditService(CteServiceBase, Service):
    class SimpleIO:
        output_optional = ('data',)
        input_required = ('name', 'description','id')

    @staticmethod
    def get_name():
        return 'cte.service.Corpus.Edit'

    @staticmethod
    def get_channels():
        return[
            {'name': u'cte.corpus.edit.POST', 'method': u'POST', 'path': u'/api/corpus/edit'},
        ]

    @staticmethod
    def after_add_to_store(logger):
        from cteutil import ChannelUtils
        logger.info('Configuring {}'.format(CorpusEditService.get_name()))
        cu = ChannelUtils(logger)
        cu.configure_service_file(os.path.realpath(__file__))

    def handle(self):
        self.initProcessing()
        data = Bunch()

        try:
            o = cte.Corpus(id=self.input.id, name=self.input.name, description=self.input.description)
            with self.getCteSession() as session:
                o = session.merge(o)
                session.flush()

                data.id = o.id
                data.name = o.name
                data.description = o.description

                self.payload.data = data
                session.commit()

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
