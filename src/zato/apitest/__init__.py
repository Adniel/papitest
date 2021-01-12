# -*- coding: utf-8 -*-

"""
Copyright (C) Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Part of Zato - Open-Source ESB, SOA, REST, APIs and Cloud Integrations in Python
# https://zato.io

# stdlib
from uuid import uuid4

# setuptools
from pkg_resources import get_distribution

version = get_distribution('zato-apitest').version

INVALID = 'invalid-{}'.format(uuid4().hex)
NO_VALUE = 'no-value-{}'.format(uuid4().hex)

class AUTH:
    BASIC_AUTH = 'basic-auth'

class CHANNEL_TYPE:
    HTTP = 'http'
    WEB_SOCKETS = 'web-sockets'
