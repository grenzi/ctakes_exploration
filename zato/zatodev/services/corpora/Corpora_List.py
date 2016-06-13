"""
.. module:: corpora
   :synopsis: A useful module indeed.

.. moduleauthor:: gage
"""

from zato.server.service import Service
import sys
from contextlib import closing
from sql import cte
from bunch import *


class CorporaList(Service):
    class SimpleIO:
        output_required = ('corpora', 'cid')
        output_optional = ('error')

    @staticmethod
    def get_name():
        return 'cte-corpora-list'

    def handle(self):
        db_config_name = 'cte-db-app'
        corpora = []

        with closing(self.outgoing.sql.get(db_config_name).session()) as session:
            for c in session.query(cte.Corpus).all():
                b = Bunch()
                b.id = c.idCorpus
                b.nam = c.nameb.description = c.description
                corpora.append(b)

        self.response.payload.corpora = corpora
        self.response.payload.cid = self.cid
        self.logger.info('Response: {}'.format(self.response))
