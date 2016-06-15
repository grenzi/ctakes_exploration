# -*- coding: utf-8 -*-

"""
Copyright (C) 2013 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import os
from tempfile import NamedTemporaryFile
from unittest import TestCase
from uuid import uuid4

# Bunch
from bunch import Bunch

# Mock
from mock import Mock

# Zato
from zato.common import util
from zato.common.test import rand_int
from zato.server.pickup import BasePickupEventProcessor

class BasePickupEventProcessorTest(TestCase):
    def test_delete_after_pick_up(self):

        package_id = rand_int()
        support_values = (True, False)

        for delete_after_pick_up in support_values:
            def dummy(*ignored, **ignored_kwargs):
                return package_id

            server = Bunch()
            server.parallel_server = Bunch()
            server.parallel_server.id = rand_int()
            server.parallel_server.hot_deploy_config = Bunch()
            server.parallel_server.hot_deploy_config.delete_after_pick_up = delete_after_pick_up
            server.parallel_server.odb = Bunch()

            server.parallel_server.notify_new_package = dummy
            server.parallel_server.odb.hot_deploy = dummy

            file_name = '{}.py'.format(uuid4().hex)

            processor = BasePickupEventProcessor(uuid4().hex, server)

            _os_remove = Mock()
            util._os_remove = _os_remove

            with NamedTemporaryFile(prefix='zato-test-', suffix=file_name) as tf:
                tf.flush()

                ret = processor.hot_deploy(os.path.abspath(tf.name), tf.name)
                self.assertEquals(ret, package_id)

                if delete_after_pick_up:
                    _os_remove.assert_called_with(tf.name)
                else:
                    self.assertFalse(_os_remove.called)
