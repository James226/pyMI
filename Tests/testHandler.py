import unittest

import Tkinter

class MockObject(object):
    def __init__(self, *p, **kw):
        self.__internaldict__ = { }
        self.__receivedcalls__ = { }
        if p is not () and 'name' in kw:
            p[0].children[kw['name']] = self

    def __getattr__(self, name):
        if name not in self.__dict__:
            self.__dict__[name] = MockObject()
        return self.__dict__[name]

    def __setattr__(self, name, val):
        self.__dict__[name] = val

    def __call__(self, *p, **kw):
        self.__receivedcalls__[p] = kw

    def __add__(self, other):
        return self

    def __iter__(self):
        class iterator(object):
            def __init__(self, obj):
                self.obj = obj
                self.index = 0

            def __iter__(self):
                return self

            def next(self):
                if self.index < len(self.obj.__internaldict__) - 1:
                    self.index += 1
                    return self.obj[self.index - 1]
                else:
                    raise StopIteration

        return iterator(self)

    def __getitem__(self, key):
        if key not in self.__internaldict__:
            self.__internaldict__[key] = MockObject()
        return self.__internaldict__[key]

    def __setitem__(self, key, value):
        self.__internaldict__[key] = value

    def mainloop(self):
        pass

Tkinter.__dict__['Tk'] = MockObject
Tkinter.__dict__['Label'] = MockObject
Tkinter.__dict__['Button'] = MockObject

import Handlers
import UI.GUI as ui




class testHandler(unittest.TestCase):
    def test_ShouldListenToSubmitHandlerWhenSubmitCalled(self):
        interface = ui.index.Index()
        self.assertEqual(1, len(interface.root.title.__receivedcalls__))
        self.assertEqual(2, len(interface.root.children.__internaldict__))
        interface.Render()