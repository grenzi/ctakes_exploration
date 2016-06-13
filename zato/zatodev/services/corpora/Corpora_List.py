"""
.. module:: corpora
   :synopsis: A useful module indeed.

.. moduleauthor:: gage
"""

from zato.server.service import Service
from contextlib import closing
from sql import cte
import json


class CorporaList(Service):
    class SimpleIO:
        output_required = ('corpora', 'cid')
        output_optional = ('franken', 'furter')

    @staticmethod
    def get_name():
        return 'cte-corpora-list'

    def handle(self):
        db_config_name = 'cte-db-app'
        corpora = []

        with closing(self.outgoing.sql.get(db_config_name).session()) as session:
            for c in session.query(cte.Corpus).all():
                a = dict([('id', c.idCorpus), ('name', c.name), ('description', c.description)])
                #self.logger.info('adding ' + json.dumps(a))
                corpora.append(a)

        self.response.payload.corpora = corpora
        self.response.payload.cid = self.cid
        self.logger.info('Response: {}'.format(self.response))
