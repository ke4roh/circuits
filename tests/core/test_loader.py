#!/usr/bin/env python

from os.path import dirname

import pytest

from circuits import Event, Loader, Manager


class Test(Event):
    """Test Event"""


def test():
    from circuits import Debugger
    m = Manager() + Debugger()
    loader = Loader(paths=[dirname(__file__)]).register(m)

    m.start()

    loader.load("app")

    x = m.push(Test())

    assert pytest.wait_for(x, "result")

    s = x.value
    assert s == "Hello World!"

    m.stop()
