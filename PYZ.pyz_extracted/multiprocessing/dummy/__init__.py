# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

__all__ = [
    'Process',
    'current_process',
    'active_children',
    'freeze_support',
    'Lock',
    'RLock',
    'Semaphore',
    'BoundedSemaphore',
    'Condition',
    'Event',
    'Barrier',
    'Queue',
    'Manager',
    'Pipe',
    'Pool',
    'JoinableQueue']
import threading
import sys
import weakref
import array
from connection import Pipe
from threading import Lock, RLock, Semaphore, BoundedSemaphore
from threading import Event, Condition, Barrier
from queue import Queue

class DummyProcess(threading.Thread):
    
    def __init__(self, group, target, name, args, kwargs = (None, None, None, (), { })):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._pid = None
        self._children = weakref.WeakKeyDictionary()
        self._start_called = False
        self._parent = current_process()

    
    def start(self):
        if self._parent is not current_process():
            raise RuntimeError('Parent is {0!r} but current_process is {1!r}'.format(self._parent, current_process()))
        self._start_called = True
        if hasattr(self._parent, '_children'):
            self._parent._children[self] = None
        threading.Thread.start(self)

    exitcode = (lambda self: if not self._start_called and self.is_alive():
0)()

Process = DummyProcess
current_process = threading.current_thread
current_process()._children = weakref.WeakKeyDictionary()

def active_children():
    children = current_process()._children
    for p in list(children):
        if p.is_alive():
            continue
        children.pop(p, None)
    return list(children)


def freeze_support():
    pass


class Namespace(object):
    
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    
    def __repr__(self):
        items = list(self.__dict__.items())
        temp = []
        for name, value in items:
            if name.startswith('_'):
                continue
            temp.append(f'''{name!s}={value!r}''')
        temp.sort()
        return f'''{self.__class__.__name__!s}({', '.join(temp)!s})'''


dict = dict
list = list

def Array(typecode, sequence, lock = (True,)):
    return array.array(typecode, sequence)


class Value(object):
    
    def __init__(self, typecode, value, lock = (True,)):
        self._typecode = typecode
        self._value = value

    value = (lambda self: self._value)()
    value = (lambda self, value: self._value = value)()
    
    def __repr__(self):
        return f'''<{type(self).__name__!s}({self._typecode!r}, {self._value!r})>'''



def Manager():
    return sys.modules[__name__]


def shutdown():
    pass


def Pool(processes, initializer, initargs = (None, None, ())):
    ThreadPool = ThreadPool
    import pool
    return ThreadPool(processes, initializer, initargs)

JoinableQueue = Queue
