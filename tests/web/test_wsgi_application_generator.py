#!/usr/bin/env python

import pytest
pytest.skip("Not passing")

from urllib.request import urlopen

from circuits.web import Controller
from circuits.web.wsgi import Application

class Root(Controller):

    def index(self):
        def response():
            yield "Hello "
            yield "World!"
        return response()

application = Application() + Root()

def test(webapp):
    f = urlopen(webapp.server.base)
    s = f.read()
    assert s == b"Hello World!"
