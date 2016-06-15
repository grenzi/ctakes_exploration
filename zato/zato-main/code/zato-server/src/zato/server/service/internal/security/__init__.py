# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from contextlib import closing

# Zato
from zato.common import SEC_DEF_TYPE
from zato.common.odb import query
from zato.server.service import Boolean, Integer, List
from zato.server.service.internal import AdminService, AdminSIO

class GetList(AdminService):
    """ Returns a list of all security definitions available.
    """
    class SimpleIO(AdminSIO):
        request_elem = 'zato_security_get_list_request'
        response_elem = 'zato_security_get_list_response'
        input_required = ('cluster_id',)
        input_optional = (List('sec_type'), Boolean('needs_internal', default=True))
        output_required = ('id', 'name', 'is_active', 'sec_type')
        output_optional = ('username', 'realm', 'password_type',
            Boolean('reject_empty_nonce_creat'), Boolean('reject_stale_tokens'), Integer('reject_expiry_limit'),
            Integer('nonce_freshness_time'), 'proto_version', 'sig_method', Integer('max_nonce_log'))
        output_repeated = True

    def handle(self):

        has_needs_internal = self.request.input.get('needs_internal') != ''

        if has_needs_internal:
            needs_internal = True if self.request.input.get('needs_internal') is True else False
        else:
            needs_internal = True

        with closing(self.odb.session()) as session:
            pairs = ((SEC_DEF_TYPE.APIKEY, query.apikey_security_list),
                     (SEC_DEF_TYPE.AWS, query.aws_security_list),
                     (SEC_DEF_TYPE.BASIC_AUTH, query.basic_auth_list),
                     (SEC_DEF_TYPE.NTLM, query.ntlm_list),
                     (SEC_DEF_TYPE.OAUTH, query.oauth_list),
                     (SEC_DEF_TYPE.OPENSTACK, query.openstack_security_list),
                     (SEC_DEF_TYPE.TECH_ACCOUNT, query.tech_acc_list),
                     (SEC_DEF_TYPE.WSS, query.wss_list),
                     (SEC_DEF_TYPE.TLS_CHANNEL_SEC, query.tls_channel_sec_list),
                     (SEC_DEF_TYPE.TLS_KEY_CERT, query.tls_key_cert_list),
                     (SEC_DEF_TYPE.XPATH_SEC, query.xpath_sec_list),
                     )

            for def_type, func in pairs:

                filter_by = self.request.input.get('sec_type', [])
                if filter_by and def_type not in filter_by:
                    continue

                for definition in func(session, self.request.input.cluster_id, False):

                    if definition.name.startswith('zato') or definition.name in('admin.invoke', 'pubapi'):
                        if not needs_internal:
                            continue

                    self.response.payload.append(definition)
