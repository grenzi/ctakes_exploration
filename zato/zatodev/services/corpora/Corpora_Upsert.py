"""
.. module:: corpora
   :synopsis: A useful module indeed.

.. moduleauthor:: gage
"""

from zato.server.service import Service
import sys
from contextlib import closing
from sql import cte

class CorporaUpsert(Service):
    class SimpleIO:
        output_required = ('cid')
        output_optional = ('id', 'error')
        input_required = ('name')
        input_optional = ('description')


    @staticmethod
    def get_name():
        return 'cte-corpora-upsert'

    def handle(self):
        db_config_name = 'cte-db-app'
        req = self.request
        if req is None:
            pass
        else:
            #update
            with closing(self.outgoing.sql.get(db_config_name).session()) as session:
                for c in session.query(cte.Corpus).all():
                    a = dict([('id', c.idCorpus), ('name', c.name)])
                    corpora.append(a)

        self.response.payload.corpora = corpora
        self.response.payload.cid = self.cid
        self.logger.info('Response: {}'.format(self.response))