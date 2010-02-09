#!/usr/bin/env python

from urllib2 import urlopen
from urllib import urlencode

from circuits.web import Server, Controller, Sessions

class Root(Controller):

    def index(self):
        return "Hello World!"

    def test_args(self, *args, **kwargs):
        return "%s\n%s" % (repr(args), repr(kwargs))

    def test_redirect(self):
        return self.redirect("/")

def test(app):
    f = urlopen(app.base)
    assert f.read() == "Hello World!"

def test_args(app):
    args = ("1", "2", "3")
    kwargs = {"1": "one", "2": "two", "3": "three"}
    url = "%s/test_args/%s" % (app.base, "/".join(args))
    data = urlencode(kwargs)

    f = urlopen(url, data)
    data = f.read().split("\n")
    assert data[0] == repr(args)
    assert data[1] == repr(kwargs)

def test_redirect(app):
    f = urlopen("%s/test_redirect" % app.base)
    assert f.read() == "Hello World!"
