# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from copy import deepcopy
from datetime import datetime
from traceback import format_exc
from uuid import uuid4

# SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Zato
from zato.cli import common_odb_opts, get_tech_account_opts, ZatoCommand
from zato.common import SIMPLE_IO
from zato.common.odb.model import Cluster, HTTPBasicAuth, HTTPSOAP, RBACPermission, RBACRole, Service, WSSDefinition
from zato.common.util import get_http_json_channel, get_http_soap_channel

zato_services = {

    # Channels - AMQP
    'zato.channel.amqp.create':'zato.server.service.internal.channel.amqp.Create',
    'zato.channel.amqp.delete':'zato.server.service.internal.channel.amqp.Delete',
    'zato.channel.amqp.edit':'zato.server.service.internal.channel.amqp.Edit',
    'zato.channel.amqp.get-list':'zato.server.service.internal.channel.amqp.GetList',

    # Channels - JMS WebSphere MQ
    'zato.channel.jms-wmq.create':'zato.server.service.internal.channel.jms_wmq.Create',
    'zato.channel.jms-wmq.delete':'zato.server.service.internal.channel.jms_wmq.Delete',
    'zato.channel.jms-wmq.edit':'zato.server.service.internal.channel.jms_wmq.Edit',
    'zato.channel.jms-wmq.get-list':'zato.server.service.internal.channel.jms_wmq.GetList',

    # Channels - ZeroMQ
    'zato.channel.zmq.create':'zato.server.service.internal.channel.zmq.Create',
    'zato.channel.zmq.delete':'zato.server.service.internal.channel.zmq.Delete',
    'zato.channel.zmq.edit':'zato.server.service.internal.channel.zmq.Edit',
    'zato.channel.zmq.get-list':'zato.server.service.internal.channel.zmq.GetList',

    # Cloud - AWS - S3
    'zato.cloud.aws.s3.create':'zato.server.service.internal.cloud.aws.s3.Create',
    'zato.cloud.aws.s3.delete':'zato.server.service.internal.cloud.aws.s3.Delete',
    'zato.cloud.aws.s3.edit':'zato.server.service.internal.cloud.aws.s3.Edit',
    'zato.cloud.aws.s3.get-list':'zato.server.service.internal.cloud.aws.s3.GetList',

    # Cloud - OpenStack - Swift
    'zato.cloud.openstack.swift.create':'zato.server.service.internal.cloud.openstack.swift.Create',
    'zato.cloud.openstack.swift.delete':'zato.server.service.internal.cloud.openstack.swift.Delete',
    'zato.cloud.openstack.swift.edit':'zato.server.service.internal.cloud.openstack.swift.Edit',
    'zato.cloud.openstack.swift.get-list':'zato.server.service.internal.cloud.openstack.swift.GetList',

    # Definitions - AMQP
    'zato.definition.amqp.change-password':'zato.server.service.internal.definition.amqp.ChangePassword',
    'zato.definition.amqp.create':'zato.server.service.internal.definition.amqp.Create',
    'zato.definition.amqp.delete':'zato.server.service.internal.definition.amqp.Delete',
    'zato.definition.amqp.edit':'zato.server.service.internal.definition.amqp.Edit',
    'zato.definition.amqp.get-by-id':'zato.server.service.internal.definition.amqp.GetByID',
    'zato.definition.amqp.get-list':'zato.server.service.internal.definition.amqp.GetList',

    # Definitions - Cassandra
    'zato.definition.cassandra.create':'zato.server.service.internal.definition.cassandra.Create',
    'zato.definition.cassandra.delete':'zato.server.service.internal.definition.cassandra.Delete',
    'zato.definition.cassandra.edit':'zato.server.service.internal.definition.cassandra.Edit',
    'zato.definition.cassandra.get-by-id':'zato.server.service.internal.definition.cassandra.GetByID',
    'zato.definition.cassandra.get-list':'zato.server.service.internal.definition.cassandra.GetList',

    # Definitions - JMS WebSphere MQ
    'zato.definition.jms-wmq.create':'zato.server.service.internal.definition.jms_wmq.Create',
    'zato.definition.jms-wmq.delete':'zato.server.service.internal.definition.jms_wmq.Delete',
    'zato.definition.jms-wmq.edit':'zato.server.service.internal.definition.jms_wmq.Edit',
    'zato.definition.jms-wmq.get-by-id':'zato.server.service.internal.definition.jms_wmq.GetByID',
    'zato.definition.jms-wmq.get-list':'zato.server.service.internal.definition.jms_wmq.GetList',

    # E-mail - IMAP
    'zato.email.imap.change-password': 'zato.server.service.internal.email.imap.ChangePassword',
    'zato.email.imap.create': 'zato.server.service.internal.email.imap.Create',
    'zato.email.imap.delete': 'zato.server.service.internal.email.imap.Delete',
    'zato.email.imap.edit': 'zato.server.service.internal.email.imap.Edit',
    'zato.email.imap.get-list': 'zato.server.service.internal.email.imap.GetList',
    'zato.email.imap.ping': 'zato.server.service.internal.email.imap.Ping',

    # E-mail - SMTP
    'zato.email.smtp.change-password': 'zato.server.service.internal.email.smtp.ChangePassword',
    'zato.email.smtp.create': 'zato.server.service.internal.email.smtp.Create',
    'zato.email.smtp.delete': 'zato.server.service.internal.email.smtp.Delete',
    'zato.email.smtp.edit': 'zato.server.service.internal.email.smtp.Edit',
    'zato.email.smtp.get-list': 'zato.server.service.internal.email.smtp.GetList',
    'zato.email.smtp.ping': 'zato.server.service.internal.email.smtp.Ping',

    # Helpers
    'zato.helpers.echo': 'zato.server.service.internal.helpers.Echo',
    'zato.helpers.input-logger': 'zato.server.service.internal.helpers.InputLogger',
    'zato.helpers.sio-input-logger': 'zato.server.service.internal.helpers.SIOInputLogger',

    # Hot-deploy
    'zato.hot_deploy.create': 'zato.server.service.internal.hot_deploy.Create',

    # HTTP/SOAP
    'zato.http-soap.create':'zato.server.service.internal.http_soap.Create',
    'zato.http-soap.delete':'zato.server.service.internal.http_soap.Delete',
    'zato.http-soap.edit':'zato.server.service.internal.http_soap.Edit',
    'zato.http-soap.get-list':'zato.server.service.internal.http_soap.GetList',
    'zato.http-soap.ping':'zato.server.service.internal.http_soap.Ping',

    # Clusters - Connections map
    'zato.info.get-info':'zato.server.service.internal.info.GetInfo',
    'zato.info.get-server-info':'zato.server.service.internal.info.GetServerInfo',

    # Key/value DB
    'zato.kvdb.data-dict.dictionary.create':'zato.server.service.internal.kvdb.data_dict.dictionary.Create',
    'zato.kvdb.data-dict.dictionary.delete':'zato.server.service.internal.kvdb.data_dict.dictionary.Delete',
    'zato.kvdb.data-dict.dictionary.edit':'zato.server.service.internal.kvdb.data_dict.dictionary.Edit',
    'zato.kvdb.data-dict.dictionary.get-key-list':'zato.server.service.internal.kvdb.data_dict.dictionary.GetKeyList',
    'zato.kvdb.data-dict.dictionary.get-last-id':'zato.server.service.internal.kvdb.data_dict.dictionary.GetLastID',
    'zato.kvdb.data-dict.dictionary.get-list':'zato.server.service.internal.kvdb.data_dict.dictionary.GetList',
    'zato.kvdb.data-dict.dictionary.get-system-list':'zato.server.service.internal.kvdb.data_dict.dictionary.GetSystemList',
    'zato.kvdb.data-dict.dictionary.get-value-list':'zato.server.service.internal.kvdb.data_dict.dictionary.GetValueList',
    'zato.kvdb.data-dict.impexp.import':'zato.server.service.internal.kvdb.data_dict.impexp.Import',
    'zato.kvdb.data-dict.translation.create':'zato.server.service.internal.kvdb.data_dict.translation.Create',
    'zato.kvdb.data-dict.translation.delete':'zato.server.service.internal.kvdb.data_dict.translation.Delete',
    'zato.kvdb.data-dict.translation.edit':'zato.server.service.internal.kvdb.data_dict.translation.Edit',
    'zato.kvdb.data-dict.translation.get-last-id':'zato.server.service.internal.kvdb.data_dict.translation.GetLastID',
    'zato.kvdb.data-dict.translation.get-list':'zato.server.service.internal.kvdb.data_dict.translation.GetList',
    'zato.kvdb.data-dict.translation.translate':'zato.server.service.internal.kvdb.data_dict.translation.Translate',
    'zato.kvdb.remote-command.execute':'zato.server.service.internal.kvdb.ExecuteCommand',

    # Messages - Namespaces
    'zato.server.message.namespace.create': 'zato.server.service.internal.message.namespace.Create',
    'zato.server.message.namespace.edit': 'zato.server.service.internal.message.namespace.Edit',
    'zato.server.message.namespace.delete': 'zato.server.service.internal.message.namespace.Delete',
    'zato.server.message.namespace.get-list': 'zato.server.service.internal.message.namespace.GetList',

    # Messages - JSON Pointers
    'zato.server.message.json_pointer.create': 'zato.server.service.internal.message.json_pointer.Create',
    'zato.server.message.json_pointer.edit': 'zato.server.service.internal.message.json_pointer.Edit',
    'zato.server.message.json_pointer.delete': 'zato.server.service.internal.message.json_pointer.Delete',
    'zato.server.message.json_pointer.get-list': 'zato.server.service.internal.message.json_pointer.GetList',

    # Messages - XPath
    'zato.server.message.xpath.create': 'zato.server.service.internal.message.xpath.Create',
    'zato.server.message.xpath.edit': 'zato.server.service.internal.message.xpath.Edit',
    'zato.server.message.xpath.delete': 'zato.server.service.internal.message.xpath.Delete',
    'zato.server.message.xpath.get-list': 'zato.server.service.internal.message.xpath.GetList',

    # Notifications - Cloud - OpenStack - Swift
    'zato.notif.cloud.openstack.swift.create': 'zato.server.service.internal.notif.cloud.openstack.swift.Create',
    'zato.notif.cloud.openstack.swift.edit': 'zato.server.service.internal.notif.cloud.openstack.swift.Edit',
    'zato.notif.cloud.openstack.swift.delete': 'zato.server.service.internal.notif.cloud.openstack.swift.Delete',
    'zato.notif.cloud.openstack.swift.get-list': 'zato.server.service.internal.notif.cloud.openstack.swift.GetList',

    # Notifications - SQL
    'zato.notif.cloud.sql.create': 'zato.server.service.internal.notif.cloud.sql.Create',
    'zato.notif.cloud.sql.edit': 'zato.server.service.internal.notif.cloud.sql.Edit',
    'zato.notif.cloud.sql.delete': 'zato.server.service.internal.notif.cloud.sql.Delete',
    'zato.notif.cloud.sql.get-list': 'zato.server.service.internal.notif.cloud.sql.GetList',

    # Outgoing connections - AMQP
    'zato.outgoing.amqp.create':'zato.server.service.internal.outgoing.amqp.Create',
    'zato.outgoing.amqp.delete':'zato.server.service.internal.outgoing.amqp.Delete',
    'zato.outgoing.amqp.edit':'zato.server.service.internal.outgoing.amqp.Edit',
    'zato.outgoing.amqp.get-list':'zato.server.service.internal.outgoing.amqp.GetList',

    # Outgoing connections - FTP
    'zato.outgoing.ftp.change-password':'zato.server.service.internal.outgoing.ftp.ChangePassword',
    'zato.outgoing.ftp.create':'zato.server.service.internal.outgoing.ftp.Create',
    'zato.outgoing.ftp.delete':'zato.server.service.internal.outgoing.ftp.Delete',
    'zato.outgoing.ftp.edit':'zato.server.service.internal.outgoing.ftp.Edit',
    'zato.outgoing.ftp.get-list':'zato.server.service.internal.outgoing.ftp.GetList',

    # Outgoing connections - JMS WebSphere MQ
    'zato.outgoing.jms-wmq.create':'zato.server.service.internal.outgoing.jms_wmq.Create',
    'zato.outgoing.jms-wmq.delete':'zato.server.service.internal.outgoing.jms_wmq.Delete',
    'zato.outgoing.jms-wmq.edit':'zato.server.service.internal.outgoing.jms_wmq.Edit',
    'zato.outgoing.jms-wmq.get-list':'zato.server.service.internal.outgoing.jms_wmq.GetList',

    # Outgoing connections - Odoo
    'zato.outgoing.odoo.change-password':'zato.server.service.internal.outgoing.odoo.ChangePassword',
    'zato.outgoing.odoo.create':'zato.server.service.internal.outgoing.odoo.Create',
    'zato.outgoing.odoo.delete':'zato.server.service.internal.outgoing.odoo.Delete',
    'zato.outgoing.odoo.edit':'zato.server.service.internal.outgoing.odoo.Edit',
    'zato.outgoing.odoo.get-list':'zato.server.service.internal.outgoing.odoo.GetList',
    'zato.outgoing.odoo.ping':'zato.server.service.internal.outgoing.odoo.Ping',

    # Outgoing connections - SQL
    'zato.outgoing.sql.change-password':'zato.server.service.internal.outgoing.sql.ChangePassword',
    'zato.outgoing.sql.create':'zato.server.service.internal.outgoing.sql.Create',
    'zato.outgoing.sql.delete':'zato.server.service.internal.outgoing.sql.Delete',
    'zato.outgoing.sql.edit':'zato.server.service.internal.outgoing.sql.Edit',
    'zato.outgoing.sql.get-list':'zato.server.service.internal.outgoing.sql.GetList',
    'zato.outgoing.sql.ping':'zato.server.service.internal.outgoing.sql.Ping',

    # Outgoing connections - ZeroMQ
    'zato.outgoing.zmq.create':'zato.server.service.internal.outgoing.zmq.Create',
    'zato.outgoing.zmq.delete':'zato.server.service.internal.outgoing.zmq.Delete',
    'zato.outgoing.zmq.edit':'zato.server.service.internal.outgoing.zmq.Edit',
    'zato.outgoing.zmq.get-list':'zato.server.service.internal.outgoing.zmq.GetList',

    # Publish/subscribe - init
    'zato.pubsub.delete-expired':'zato.server.service.internal.pubsub.DeleteExpired',
    'zato.pubsub.invoke-callbacks':'zato.server.service.internal.pubsub.InvokeCallbacks',
    'zato.pubsub.move-to-target-queues':'zato.server.service.internal.pubsub.MoveToTargetQueues',
    'zato.pubsub.rest-handler':'zato.server.service.internal.pubsub.RESTHandler',

    # Publish/subscribe - consumer
    'zato.pubsub.consumers.create':'zato.server.service.internal.pubsub.consumers.Create',
    'zato.pubsub.consumers.delete':'zato.server.service.internal.pubsub.consumers.Delete',
    'zato.pubsub.consumers.edit':'zato.server.service.internal.pubsub.consumers.Edit',
    'zato.pubsub.consumers.get-info':'zato.server.service.internal.pubsub.consumers.GetInfo',
    'zato.pubsub.consumers.get-list':'zato.server.service.internal.pubsub.consumers.GetList',

    # Publish/subscribe - messages
    'zato.pubsub.message.create.delete':'zato.server.service.internal.pubsub.message.Delete',
    'zato.pubsub.message.create.get':'zato.server.service.internal.pubsub.message.Get',
    'zato.pubsub.message.create.get-list':'zato.server.service.internal.pubsub.message.GetList',

    # Publish/subscribe - producers
    'zato.pubsub.producers.create':'zato.server.service.internal.pubsub.producers.Create',
    'zato.pubsub.producers.delete':'zato.server.service.internal.pubsub.producers.Delete',
    'zato.pubsub.producers.edit':'zato.server.service.internal.pubsub.producers.Edit',
    'zato.pubsub.producers.get-info':'zato.server.service.internal.pubsub.producers.GetInfo',
    'zato.pubsub.producers.get-list':'zato.server.service.internal.pubsub.producers.GetList',

    # Query - Cassandra
    'zato.query.cassandra.create':'zato.server.service.internal.query.cassandra.Create',
    'zato.query.cassandra.delete':'zato.server.service.internal.query.cassandra.Delete',
    'zato.query.cassandra.edit':'zato.server.service.internal.query.cassandra.Edit',
    'zato.query.cassandra.get-list':'zato.server.service.internal.query.cassandra.GetList',

    # Publish/subscribe - topics
    'zato.pubsub.topics.create':'zato.server.service.internal.pubsub.topics.Create',
    'zato.pubsub.topics.delete':'zato.server.service.internal.pubsub.topics.Delete',
    'zato.pubsub.topics.edit':'zato.server.service.internal.pubsub.topics.Edit',
    'zato.pubsub.topics.get-info':'zato.server.service.internal.pubsub.topics.GetInfo',
    'zato.pubsub.topics.get-list':'zato.server.service.internal.pubsub.topics.GetList',
    'zato.pubsub.topics.publish':'zato.server.service.internal.pubsub.topics.Publish',

    # Search - ElasticSearch
    'zato.search.es.create':'zato.server.service.internal.search.es.Create',
    'zato.search.es.delete':'zato.server.service.internal.search.es.Delete',
    'zato.search.es.edit':'zato.server.service.internal.search.es.Edit',
    'zato.search.es.get-list':'zato.server.service.internal.search.es.GetList',

    # Search - Solr
    'zato.search.solr.create':'zato.server.service.internal.search.solr.Create',
    'zato.search.solr.delete':'zato.server.service.internal.search.solr.Delete',
    'zato.search.solr.edit':'zato.server.service.internal.search.solr.Edit',
    'zato.search.solr.get-list':'zato.server.service.internal.search.solr.GetList',

    # Ping services are added in Create.add_ping_services

    # Scheduler
    'zato.scheduler.job.create':'zato.server.service.internal.scheduler.Create',
    'zato.scheduler.job.delete':'zato.server.service.internal.scheduler.Delete',
    'zato.scheduler.job.edit':'zato.server.service.internal.scheduler.Edit',
    'zato.scheduler.job.execute':'zato.server.service.internal.scheduler.Execute',
    'zato.scheduler.job.get-by-name':'zato.server.service.internal.scheduler.GetByName',
    'zato.scheduler.job.get-list':'zato.server.service.internal.scheduler.GetList',

    # Security
    'zato.security.get-list':'zato.server.service.internal.security.GetList',

    # Security - API keys
    'zato.security.apikey.change-password':'zato.server.service.internal.security.apikey.ChangePassword',
    'zato.security.apikey.create':'zato.server.service.internal.security.apikey.Create',
    'zato.security.apikey.delete':'zato.server.service.internal.security.apikey.Delete',
    'zato.security.apikey.edit':'zato.server.service.internal.security.apikey.Edit',
    'zato.security.apikey.get-list':'zato.server.service.internal.security.apikey.GetList',

    # Security - AWS
    'zato.security.aws.change-password':'zato.server.service.internal.security.aws.ChangePassword',
    'zato.security.aws.create':'zato.server.service.internal.security.aws.Create',
    'zato.security.aws.delete':'zato.server.service.internal.security.aws.Delete',
    'zato.security.aws.edit':'zato.server.service.internal.security.aws.Edit',
    'zato.security.aws.get-list':'zato.server.service.internal.security.aws.GetList',

    # Security - HTTP Basic Auth
    'zato.security.basic-auth.change-password':'zato.server.service.internal.security.basic_auth.ChangePassword',
    'zato.security.basic-auth.create':'zato.server.service.internal.security.basic_auth.Create',
    'zato.security.basic-auth.delete':'zato.server.service.internal.security.basic_auth.Delete',
    'zato.security.basic-auth.edit':'zato.server.service.internal.security.basic_auth.Edit',
    'zato.security.basic-auth.get-list':'zato.server.service.internal.security.basic_auth.GetList',

    # Security - NTLM
    'zato.security.tls.ca_cert.change-password':'zato.server.service.internal.security.tls.ca_cert.ChangePassword',
    'zato.security.tls.ca_cert.create':'zato.server.service.internal.security.tls.ca_cert.Create',
    'zato.security.tls.ca_cert.delete':'zato.server.service.internal.security.tls.ca_cert.Delete',
    'zato.security.tls.ca_cert.edit':'zato.server.service.internal.security.tls.ca_cert.Edit',
    'zato.security.tls.ca_cert.get-list':'zato.server.service.internal.security.tls.ca_cert.GetList',

    # Security - OAuth
    'zato.security.oauth.change-password':'zato.server.service.internal.security.oauth.ChangePassword',
    'zato.security.oauth.create':'zato.server.service.internal.security.oauth.Create',
    'zato.security.oauth.delete':'zato.server.service.internal.security.oauth.Delete',
    'zato.security.oauth.edit':'zato.server.service.internal.security.oauth.Edit',
    'zato.security.oauth.get-list':'zato.server.service.internal.security.oauth.GetList',

    # Security - OpenStack
    'zato.security.openstack.change-password':'zato.server.service.internal.security.openstack.ChangePassword',
    'zato.security.openstack.create':'zato.server.service.internal.security.openstack.Create',
    'zato.security.openstack.delete':'zato.server.service.internal.security.openstack.Delete',
    'zato.security.openstack.edit':'zato.server.service.zato_servicesinternal.security.openstack.Edit',
    'zato.security.openstack.get-list':'zato.server.service.internal.security.openstack.GetList',

    # Security - RBAC - Roles
    'zato.security.rbac.role.create':'zato.server.service.internal.security.rbac.role.Create',
    'zato.security.rbac.role.delete':'zato.server.service.internal.security.rbac.role.Delete',
    'zato.security.rbac.role.edit':'zato.server.service.internal.security.rbac.role.Edit',
    'zato.security.rbac.role.get-list':'zato.server.service.internal.security.rbac.role.get-list',

    # Security - RBAC - Client roles
    'zato.security.rbac.client-role.create':'zato.server.service.internal.security.rbac.client_role.Create',
    'zato.security.rbac.client-role.delete':'zato.server.service.internal.security.rbac.client_role.Delete',
    'zato.security.rbac.client-role.get-list':'zato.server.service.internal.security.rbac.client_role.get-list',

    # Security - RBAC - Permissions
    'zato.security.rbac.permission.create':'zato.server.service.internal.security.rbac.permission.Create',
    'zato.security.rbac.permission.delete':'zato.server.service.internal.security.rbac.permission.Delete',
    'zato.security.rbac.permission.edit':'zato.server.service.internal.security.rbac.permission.Edit',
    'zato.security.rbac.permission.get-list':'zato.server.service.internal.security.rbac.permission.get-list',

    # Security - RBAC - Permissions for roles
    'zato.security.rbac.role-permission.create':'zato.server.service.internal.security.rbac.role_permission.Create',
    'zato.security.rbac.role-permission.delete':'zato.server.service.internal.security.rbac.role_permission.Delete',
    'zato.security.rbac.role-permission.get-list':'zato.server.service.internal.security.rbac.role_permission.get-list',

    # Security - Technical accounts
    'zato.security.tech-account.change-password':'zato.server.service.internal.security.tech_account.ChangePassword',
    'zato.security.tech-account.create':'zato.server.service.internal.security.tech_account.Create',
    'zato.security.tech-account.delete':'zato.server.service.internal.security.tech_account.Delete',
    'zato.security.tech-account.edit':'zato.server.service.internal.security.tech_account.Edit',
    'zato.security.tech-account.get-by-id':'zato.server.service.internal.security.tech_account.GetByID',
    'zato.security.tech-account.get-list':'zato.server.service.internal.security.tech_account.GetList',

    # Security - TLS - CA certs
    'zato.security.tls.ca_cert.create':'zato.server.service.internal.security.tls.ca_cert.Create',
    'zato.security.tls.ca_cert.delete':'zato.server.service.internal.security.tls.ca_cert.Delete',
    'zato.security.tls.ca_cert.edit':'zato.server.service.internal.security.tls.ca_cert.Edit',
    'zato.security.tls.ca_cert.get-list':'zato.server.service.internal.security.tls.ca_cert.GetList',

    # Security - TLS - Key/cert pairs
    'zato.security.tls.key_cert.create':'zato.server.service.internal.security.tls.key_cert.Create',
    'zato.security.tls.key_cert.delete':'zato.server.service.internal.security.tls.key_cert.Delete',
    'zato.security.tls.key_cert.edit':'zato.server.service.internal.security.tls.key_cert.Edit',
    'zato.security.tls.key_cert.get-list':'zato.server.service.internal.security.tls.key_cert.GetList',

    # Security - WS-Security
    'zato.security.wss.change-password':'zato.server.service.internal.security.wss.ChangePassword',
    'zato.security.wss.create':'zato.server.service.internal.security.wss.Create',
    'zato.security.wss.delete':'zato.server.service.internal.security.wss.Delete',
    'zato.security.wss.edit':'zato.server.service.internal.security.wss.Edit',
    'zato.security.wss.get-list':'zato.server.service.internal.security.wss.GetList',

    # Security - XPath
    'zato.security.xpath.change-password':'zato.server.service.internal.security.xpath.ChangePassword',
    'zato.security.xpath.create':'zato.server.service.internal.security.xpath.Create',
    'zato.security.xpath.delete':'zato.server.service.internal.security.xpath.Delete',
    'zato.security.xpath.edit':'zato.server.service.internal.security.xpath.Edit',
    'zato.security.xpath.get-list':'zato.server.service.internal.security.xpath.GetList',

    # Servers
    'zato.server.delete':'zato.server.service.internal.server.Delete',
    'zato.server.edit':'zato.server.service.internal.server.Edit',
    'zato.server.get-by-id':'zato.server.service.internal.server.GetByID',

    # Services
    'zato.service.configure-request-response':'zato.server.service.internal.service.ConfigureRequestResponse',
    'zato.service.delete':'zato.server.service.internal.service.Delete',
    'zato.service.edit':'zato.server.service.internal.service.Edit',
    'zato.service.get-by-name':'zato.server.service.internal.service.GetByName',
    'zato.service.get-channel-list':'zato.server.service.interna.sol.service.GetChannelList',
    'zato.service.get-deployment-info-list':'zato.server.service.internal.service.GetDeploymentInfoList',
    'zato.service.get-list':'zato.server.service.internal.service.GetList',
    'zato.service.get-request-response':'zato.server.service.internal.service.GetRequestResponse',
    'zato.service.get-source-info':'zato.server.service.internal.service.GetSourceInfo',
    'zato.service.get-wsdl':'zato.server.service.internal.service.GetWSDL',
    'zato.service.has-wsdl':'zato.server.service.internal.service.HasWSDL',
    'zato.service.invoke':'zato.server.service.internal.service.Invoke',
    'zato.service.set-wsdl':'zato.server.service.internal.service.SetWSDL',
    'zato.service.slow-response.get':'zato.server.service.internal.service.GetSlowResponse',
    'zato.service.slow-response.get-list':'zato.server.service.internal.service.GetSlowResponseList',
    'zato.service.upload-package':'zato.server.service.internal.service.UploadPackage',

    # Statistics
    'zato.stats.delete':'zato.server.service.internal.stats.Delete',
    'zato.stats.get-by-service':'zato.server.service.internal.stats.GetByService',
    'zato.stats.summary.get-summary-by-day':'zato.server.service.internal.stats.summary.GetSummaryByDay',
    'zato.stats.summary.get-summary-by-month':'zato.server.service.internal.stats.summary.GetSummaryByMonth',
    'zato.stats.summary.get-summary-by-range':'zato.server.service.internal.stats.summary.GetSummaryByRange',
    'zato.stats.summary.get-summary-by-week':'zato.server.service.internal.stats.summary.GetSummaryByWeek',
    'zato.stats.summary.get-summary-by-year':'zato.server.service.internal.stats.summary.GetSummaryByYear',
    'zato.stats.trends.get-trends':'zato.server.service.internal.stats.trends.GetTrends',
}

class Create(ZatoCommand):
    """ Creates a new Zato cluster in the ODB
    """
    opts = deepcopy(common_odb_opts)

    opts.append({'name':'lb_host', 'help':"Load-balancer host"})
    opts.append({'name':'lb_port', 'help':'Load-balancer port'})
    opts.append({'name':'lb_agent_port', 'help':'Load-balancer agent host'})
    opts.append({'name':'broker_host', 'help':"Redis host"})
    opts.append({'name':'broker_port', 'help':'Redis port'})
    opts.append({'name':'cluster_name', 'help':'Name of the cluster to create'})

    opts += get_tech_account_opts('for web admin instances to use')

    def execute(self, args, show_output=True):

        engine = self._get_engine(args)
        session = self._get_session(engine)

        cluster = Cluster()
        cluster.name = args.cluster_name
        cluster.description = 'Created by {} on {} (UTC)'.format(self._get_user_host(), datetime.utcnow().isoformat())

        for name in(
              'odb_type', 'odb_host', 'odb_port', 'odb_user', 'odb_db_name',
              'broker_host', 'broker_port', 'lb_host', 'lb_port', 'lb_agent_port'):
            setattr(cluster, name, getattr(args, name))
        session.add(cluster)

        # TODO: getattrs below should be squared away - one of the attrs should win
        #       and the other one should be get ridden of.
        admin_invoke_sec = HTTPBasicAuth(
            None, 'admin.invoke', True, 'admin.invoke', 'Zato admin invoke', getattr(
                args, 'admin_invoke_password', None) or getattr(args, 'tech_account_password'), cluster)
        session.add(admin_invoke_sec)

        pubapi_sec = HTTPBasicAuth(None, 'pubapi', True, 'pubapi', 'Zato public API', uuid4().hex, cluster)
        session.add(pubapi_sec)

        self.add_soap_services(session, cluster, admin_invoke_sec, pubapi_sec)
        self.add_ping_services(session, cluster)
        self.add_default_pubsub_accounts(session, cluster)
        self.add_default_rbac_permissions(session, cluster)
        self.add_default_rbac_roles(session, cluster)

        try:
            session.commit()
        except IntegrityError, e:
            msg = 'Cluster name [{}] already exists'.format(cluster.name)
            if self.verbose:
                msg += '. Caught an exception:[{}]'.format(format_exc(e).decode('utf-8'))
                self.logger.error(msg)
            self.logger.error(msg)
            session.rollback()

            return self.SYS_ERROR.CLUSTER_NAME_ALREADY_EXISTS

        if show_output:
            if self.verbose:
                msg = 'Successfully created a new cluster [{}]'.format(args.cluster_name)
                self.logger.debug(msg)
            else:
                self.logger.info('OK')

    def add_soap_services(self, session, cluster, admin_invoke_sec, pubapi_sec):
        """ Adds these Zato internal services that can be accessed through SOAP requests.
        """

        #
        # HTTPSOAP + services
        #

        for name, impl_name in zato_services.iteritems():

            service = Service(None, name, True, impl_name, True, cluster)
            session.add(service)

            # Add the HTTP channel for WSDLs
            if name == 'zato.service.get-wsdl':
                http_soap = HTTPSOAP(
                    None, '{}.soap'.format(name), True, True, 'channel', 'plain_http',
                    None, '/zato/wsdl', None, '', None, None, service=service, cluster=cluster)
                session.add(http_soap)

            elif name == 'zato.service.invoke':
                self.add_admin_invoke(session, cluster, service, admin_invoke_sec)

            elif name == 'zato.pubsub.rest-handler':
                self.add_pubsub_rest_handler(session, cluster, service)

            session.add(get_http_soap_channel(name, service, cluster, pubapi_sec))
            session.add(get_http_json_channel(name, service, cluster, pubapi_sec))

    def add_ping_services(self, session, cluster):
        """ Adds a ping service and channels, with and without security checks.
        """
        passwords = {
            'ping.plain_http.basic_auth': None,
            'ping.soap.basic_auth': None,
            'ping.soap.wss.clear_text': None,
        }

        for password in passwords:
            passwords[password] = uuid4().hex

        ping_impl_name = 'zato.server.service.internal.Ping'
        ping_service_name = 'zato.ping'
        ping_service = Service(None, ping_service_name, True, ping_impl_name, True, cluster)
        session.add(ping_service)

        #
        # .. no security ..
        #
        # TODO
        # Change it to /zato/json/ping
        # and add an actual /zato/ping with no data format specified.
        ping_no_sec_channel = HTTPSOAP(
            None, 'zato.ping', True, True, 'channel',
            'plain_http', None, '/zato/ping', None, '', None, SIMPLE_IO.FORMAT.JSON, service=ping_service, cluster=cluster)
        session.add(ping_no_sec_channel)

        #
        # All the possible options
        #
        # Plain HTTP / Basic auth
        # SOAP / Basic auth
        # SOAP / WSS / Clear text
        #

        transports = ['plain_http', 'soap']
        wss_types = ['clear_text']

        for transport in transports:

            if transport == 'plain_http':
                data_format = SIMPLE_IO.FORMAT.JSON
            else:
                data_format = SIMPLE_IO.FORMAT.XML

            base_name = 'ping.{0}.basic_auth'.format(transport)
            zato_name = 'zato.{0}'.format(base_name)
            url = '/zato/{0}'.format(base_name)
            soap_action, soap_version = (zato_name, '1.1') if transport == 'soap' else ('', None)
            password = passwords[base_name]

            sec = HTTPBasicAuth(None, zato_name, True, zato_name, 'Zato ping', password, cluster)
            session.add(sec)

            channel = HTTPSOAP(
                None, zato_name, True, True, 'channel', transport, None, url, None, soap_action,
                soap_version, data_format, service=ping_service, security=sec, cluster=cluster)
            session.add(channel)

            if transport == 'soap':
                for wss_type in wss_types:
                    base_name = 'ping.{0}.wss.{1}'.format(transport, wss_type)
                    zato_name = 'zato.{0}'.format(base_name)
                    url = '/zato/{0}'.format(base_name)
                    password = passwords[base_name]

                    sec = WSSDefinition(None, zato_name, True, zato_name, password, wss_type, False, True, 3600, 3600, cluster)
                    session.add(sec)

                    channel = HTTPSOAP(
                        None, zato_name, True, True, 'channel', transport, None, url, None, soap_action,
                        soap_version, data_format, service=ping_service, security=sec, cluster=cluster)
                    session.add(channel)

    def add_admin_invoke(self, session, cluster, service, admin_invoke_sec):
        """ Adds an admin channel for invoking services from web admin and CLI.
        """
        channel = HTTPSOAP(
            None, 'admin.invoke.json', True, True, 'channel', 'plain_http',
            None, '/zato/admin/invoke', None, '', None, SIMPLE_IO.FORMAT.JSON, service=service, cluster=cluster,
            security=admin_invoke_sec)
        session.add(channel)

    def add_default_pubsub_accounts(self, session, cluster):
        """ Adds default accounts used by pub/sub internally.
        """
        for suffix in('consumer', 'producer'):
            name = 'zato.pubsub.default-{}'.format(suffix)
            item = HTTPBasicAuth(None, name, True, name, 'Zato pub/sub', uuid4().hex, cluster)
            session.add(item)

    def add_default_rbac_permissions(self, session, cluster):
        """ Adds default CRUD permissions used by RBAC.
        """
        for name in('Create', 'Read', 'Update', 'Delete'):
            item = RBACPermission()
            item.name = name
            item.cluster = cluster
            session.add(item)

    def add_default_rbac_roles(self, session, cluster):
        """ Adds default roles used by RBAC.
        """
        item = RBACRole()
        item.id = 0
        item.name = 'Root'
        item.parent_id = None
        item.cluster = cluster
        session.add(item)

    def add_pubsub_rest_handler(self, session, cluster, service):
        channel = HTTPSOAP(None, 'zato.pubsub.rest', True, True, 'channel', 'plain_http',
            None, '/zato/pubsub/{item_type}/{item}/', None, '', None, None, merge_url_params_req=True, service=service, cluster=cluster)
        session.add(channel)
