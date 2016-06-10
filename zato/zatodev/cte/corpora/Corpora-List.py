"""
.. module:: corpora
   :synopsis: A useful module indeed.

.. moduleauthor:: gage
"""

from zato.server.service import Service


class CorporaList(Service):
    class SimpleIO:
        output_required = ('corpora', 'cid')

    @staticmethod
    def get_name():
        return 'cte-corpora-list'

    def handle(self):
        self.response.payload.corpora = ["name","blue"]
        self.response.payload.cid = self.cid
        self.logger.info('Response: {}'.format(self.response))
