# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import logging
from zato.server.service import Service

class SampleService(Service):

    def handle(self):
        self.response.payload = 'Greetings!'
        #
        #  msg = {
        #     'action': SERVICE.PUBLISH.value,
        #     'service': 'zato.helpers.input-logger',
        #     'payload': 'My payload',
        #     'cid': new_cid()
        # }
        # self.broker_client.invoke_async(msg)

    def finalize_handle(self):
        self.log_output('What was the output?', logging.DEBUG,
            ['wsgi_environ', 'name', 'impl_name'])