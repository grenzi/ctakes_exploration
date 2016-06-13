"""
.. module:: corpora
   :synopsis: A useful module indeed.

.. moduleauthor:: gage
"""

from zato.server.service import Service
import sys
from contextlib import closing
from sql import cte

class CorporaList(Service):
    class SimpleIO:
        output_required = ('corpora', 'cid')

    @staticmethod
    def get_name():
        return 'cte-corpora-list'

    def handle(self):
        a  = '\n'.join(sys.path)
        self.logger.info(a)
        db_config_name = 'cte-db-app'
        corpora = []

        with closing(self.outgoing.sql.get(db_config_name).session()) as session:
            for c in session.query(cte.Corpus).all():
                a = dict([('id', c.idCorpus), ('name', c.name)])
                corpora.append(a)

        self.response.payload.corpora = corpora
        self.response.payload.cid = self.cid
        self.logger.info('Response: {}'.format(self.response))