import unittest

import Tkinter
from Tests.MockObject import MockObject

Tkinter.__dict__['Tk'] = MockObject
Tkinter.__dict__['Label'] = MockObject
Tkinter.__dict__['Button'] = MockObject

import Handlers
import UI.GUI
import UI.Web
import inspect

class testHandler(object):
    def test_SetTextWithTestValueShouldSetTestValue(self):
        self.interface.SetText("TestValue")
        self.result_SetTextWithTestValueShouldSetTestValue()

    def result_SetTextWithTestValueShouldSetTestValue(self):
        self.throw_NotImplementedError()

    def throw_NotImplementedError(self):
        unittest.TestCase.fail(self, "'%s.%s' does not implement result for '%s'" % (type(self.interface).__module__, type(self.interface).__name__, inspect.stack()[2][3][5:]))


class testGUIHandler(unittest.TestCase, testHandler):
    def setUp(self):
        self.interface = UI.GUI.index.Index()

    def test_ShouldListenToSubmitHandlerWhenSubmitCalled(self):
        self.assertEqual(1, len(self.interface.root.title.__receivedcalls__))
        self.assertTrue(self.interface.root.title.__ReceivedCall__("Multi-Interface Tool"))
        self.assertEqual(2, len(self.interface.root.children))
        self.interface.Render()

    def result_SetTextWithTestValueShouldSetTestValue(self):
        self.interface.label.config(text="TestValue")

class testWebHandler(unittest.TestCase, testHandler):
    def setUp(self):
        self.interface = UI.Web.index.Index((), {})

    def result_SetTextWithTestValueShouldSetTestValue(self):
        self.assertEqual("TestValue", self.interface.value)