# -*- coding: utf-8 -*-

"""
Copyright (C) 2018, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Originally part of Zato - open-source ESB, SOA, REST, APIs and cloud integrations in Python
# https://zato.io

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from unittest import TestCase

# Bunch
from bunch import Bunch

# Zato
from zato.apitest import util
from zato.apitest.steps import xml

class GivenTestCase(TestCase):

    def setUp(self):
        self.ctx = Bunch()
        self.ctx.zato = util.new_context(None, util.rand_string(), {})

    def test_given_soap_action(self):
        value = util.rand_string()
        xml.given_soap_action(self.ctx, value)
        self.assertEquals(self.ctx.zato.request.headers['SOAPAction'], value)
