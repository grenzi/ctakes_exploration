# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Zato
from zato.common.broker_message import DEFINITION
from zato.common.odb.model import CassandraConn
from zato.common.odb.query import cassandra_conn_list
from zato.server.service.internal import AdminService, ChangePasswordBase
from zato.server.service.meta import CreateEditMeta, DeleteMeta, GetListMeta

elem = 'definition_cassandra'
model = CassandraConn
label = 'a Cassandra connection'
broker_message = DEFINITION
broker_message_prefix = 'CASSANDRA_'
list_func = cassandra_conn_list

class GetList(AdminService):
    __metaclass__ = GetListMeta

class Create(AdminService):
    __metaclass__ = CreateEditMeta

class Edit(AdminService):
    __metaclass__ = CreateEditMeta

class Delete(AdminService):
    __metaclass__ = DeleteMeta

class ChangePassword(ChangePasswordBase):
    """ Changes the password of a Cassandra connection definition.
    """
    password_required = False

    class SimpleIO(ChangePasswordBase.SimpleIO):
        request_elem = 'zato_definition_cassandra_change_password_request'
        response_elem = 'zato_definition_cassandra_change_password_response'

    def handle(self):
        def _auth(instance, password):
            instance.password = password

        return self._handle(CassandraConn, _auth, DEFINITION.CASSANDRA_CHANGE_PASSWORD.value)
