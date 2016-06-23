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


class ${noun}${verb}Service(CteServiceBase, Service):
    class SimpleIO:
        output_optional = ('data',)
        input_optional = ('id',)
        # input_required = ('id',)

    @staticmethod
    def get_name():
        return 'cte.service.${noun}.${verb}'

    @staticmethod
    def get_channels():
        return[
        % for method in channelmethods:
            {'name': u'cte.${channelnoun}.${channelverb}', 'method': u'${method}', 'path': u'/api/${channelnoun}/${channelverb}'},
        % endfor
        ]

    @staticmethod
    def after_add_to_store(logger):
        from cteutil import ChannelUtils
        logger.info('Configuring {}'.format(${noun}${verb}Service.get_name()))
        cu = ChannelUtils(logger)
        cu.configure_service_file(os.path.realpath(__file__))

    #todo - make stub handle examples for get/create/delete/etc
    def handle(self):
        self.initProcessing()
        data = Bunch()

        try:
            with self.getCteSession() as session:
                c = session.query(cte.Corpus).filter_by(id=self.input.id).first()
                self.payload.data = AlchemyEncoder.toJsonObj(c)
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
