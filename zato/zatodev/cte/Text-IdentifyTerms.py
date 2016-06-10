"""
.. module:: terms
   :synopsis: A useful module indeed.


.. moduleauthor:: gage

"""

from zato.server.service import Service


class IdentifyTerms(Service):
    class SimpleIO:
        input_required = ('text',)
        output_required = ('terms', 'cid')

    @staticmethod
    def get_name():
        return 'text-identifyterms'

    def handle(self):
        self.logger.info('Request: {}'.format(self.request.payload))
        self.logger.info('Request type: {}'.format(type(self.request.payload)))

        out = self.outgoing.plain_http.get('ctakes')

        url_params = {}
        url_params['text'] = self.request.input.text

        response = out.conn.get(self.cid, url_params)

        self.response.payload.terms = response.text
        self.response.payload.cid = self.cid

        self.logger.info(response.text)

