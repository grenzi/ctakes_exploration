# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from contextlib import closing
from time import time
from uuid import uuid4

# Zato
from zato.common.broker_message import OUTGOING
from zato.common.odb.model import OutgoingOdoo
from zato.common.odb.query import out_odoo_list
from zato.common.util import ping_odoo
from zato.server.service.internal import AdminService, AdminSIO, ChangePasswordBase
from zato.server.service.meta import CreateEditMeta, DeleteMeta, GetListMeta

elem = 'email_imap'
model = OutgoingOdoo
label = 'an Odoo connection'
broker_message = OUTGOING
broker_message_prefix = 'ODOO_'
list_func = out_odoo_list
skip_input_params = ['password']

def instance_hook(service, input, instance, attrs):
    if 'create' in service.get_name().lower():
        instance.password = uuid4().hex

def broker_message_hook(service, input, instance, attrs, service_type):
    if service_type == 'create_edit':
        input.password = instance.password

class GetList(AdminService):
    __metaclass__ = GetListMeta

class Create(AdminService):
    __metaclass__ = CreateEditMeta

class Edit(AdminService):
    __metaclass__ = CreateEditMeta

class Delete(AdminService):
    __metaclass__ = DeleteMeta

class ChangePassword(ChangePasswordBase):
    """ Changes the password of an Odoo connection
    """
    password_required = False

    class SimpleIO(ChangePasswordBase.SimpleIO):
        request_elem = 'zato_outgoing_odoo_change_password_request'
        response_elem = 'zato_outgoing_odoo_change_password_response'

    def handle(self):
        def _auth(instance, password):
            instance.password = password

        return self._handle(OutgoingOdoo, _auth, OUTGOING.ODOO_CHANGE_PASSWORD.value,
            publish_instance_attrs=['host', 'protocol', 'port', 'database', 'user', 'password', 'pool_size'])

class Ping(AdminService):

    class SimpleIO(AdminSIO):
        request_elem = 'zato_outgoing_odoo_ping_request'
        response_elem = 'zato_outgoing_odoo_ping_response'
        input_required = ('id',)
        output_required = ('info',)

    def handle(self):

        with closing(self.odb.session()) as session:
            item = session.query(OutgoingOdoo).filter_by(id=self.request.input.id).one()

        with self.outgoing.odoo[item.name].conn.client() as client:

            start_time = time()
            ping_odoo(client)
            response_time = time() - start_time

            self.response.payload.info = 'Ping OK, took:`{0:03.4f} s`'.format(response_time)
