# -*- coding: utf-8 -*-

"""
Copyright (C) Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Part of Zato - Open-Source ESB, SOA, REST, APIs and Cloud Integrations in Python
# https://zato.io

# stdlib
import os

ENVIRONMENT = '''# -*- coding: utf-8 -*-

"""
Copyright (C) Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Part of Zato - Open-Source ESB, SOA, REST, APIs and Cloud Integrations in Python
# https://zato.io

# stdlib
import os

# Zato
from zato.apitest.util import new_context

def before_feature(context, feature):
    environment_dir = os.path.dirname(os.path.realpath(__file__))
    context.zato = new_context(None, environment_dir)
'''

STEPS = '''# -*- coding: utf-8 -*-

"""
Copyright (C) Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Part of Zato - Open-Source ESB, SOA, REST, APIs and Cloud Integrations in Python
# https://zato.io

# Behave
from behave import given, then

# Zato
from zato.apitest import steps as default_steps
from zato.apitest.steps.json import set_pointer
from zato.apitest.util import obtain_values
'''

CONFIG_INI = """
[behave]
options=--format pretty --no-source --no-timings

[user]
sample=Hello

[vault]
[[default]]
address=http://localhost:8200
token=invalid
"""

DEMO_FEATURE = """
Feature: zato-apitest demonstration

Scenario: *** REST API Demo ***

    Given address "http://localhost:11223"
    Given URL path "/demo/json"
    Given query string "?demo=1"
    Given format "JSON"
    Given header "X-Custom-Header" "MyValue"
    Given request is "{}"
    Given path "/a" in request is "abc"
    Given path "/foo" in request is an integer "7"
    Given path "/bar" in request is a list "1,2,3,4,5"
    Given path "/baz" in request is a random string
    Given path "/hi5" in request is one of "a,b,c,d,e"

    When the URL is invoked

    Then path "/action/msg" is "How do you do?"
    And path "/action/code" is an integer "0"
    And path "/action/flow" is a list "Ack,Done"
    And status is "200"
    And header "Server" is not empty

    # You can also compare responses directly inline ..
    And JSON response is equal to "{"action":{"code":0, "msg":"How do you do?", "flow":["Ack", "Done"]}}"

    # .. or read them from disk.
    And response is equal to that from "demo.json"
"""

DEMO_JSON_REQ = """{"hello":"world"}"""
DEMO_JSON_RESP = """{"action":{"code":0, "msg":"How do you do?", "flow":["Ack", "Done"]}}"""

# No demo response for XML, we're not comparing them directly yet.
DEMO_XML_REQ = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      <howdy>Friend</howdy>
      <hello>Howdy</hello>
      <world>All good?</world>
      <and-beyond>Sweet</and-beyond>
   </soapenv:Body>
</soapenv:Envelope>"""

def handle(base_path):
    """ Sets up runtime directories and sample features.
    """
    # Top-level directory for tests
    features_dir = os.path.join(base_path, 'features')
    os.mkdir(features_dir)

    # Requests and responses
    request_json_dir = os.path.join(base_path, 'features', 'json', 'request')
    request_xml_dir = os.path.join(base_path, 'features', 'xml', 'request')

    response_json_dir = os.path.join(base_path, 'features', 'json', 'response')
    response_xml_dir = os.path.join(base_path, 'features', 'xml', 'response')

    os.makedirs(request_json_dir)
    os.makedirs(request_xml_dir)

    os.makedirs(response_json_dir)
    os.makedirs(response_xml_dir)

    # Demo feature
    open(os.path.join(features_dir, 'demo.feature'), 'w').write(DEMO_FEATURE)
    open(os.path.join(request_json_dir, 'demo.json'), 'w').write(DEMO_JSON_REQ)
    open(os.path.join(request_xml_dir, 'demo.xml'), 'w').write(DEMO_XML_REQ)
    open(os.path.join(response_json_dir, 'demo.json'), 'w').write(DEMO_JSON_RESP)

    # Add environment.py
    open(os.path.join(features_dir, 'environment.py'), 'w').write(ENVIRONMENT)

    # Add steps
    steps_dir = os.path.join(features_dir, 'steps')
    os.mkdir(steps_dir)
    open(os.path.join(steps_dir, 'steps.py'), 'w').write(STEPS)

    # User-provided CLI parameters, if any, passed to behave as they are.
    # Also, user-defined config stanzas.
    open(os.path.join(features_dir, 'config.ini'), 'w').write(CONFIG_INI)
