# Source Generated with Decompyle++
# File: pool.pyc (Python 3.12)

__all__ = [
    'Pool',
    'ThreadPool']
import collections
import itertools
import os
import queue
import threading
import time
import traceback
import types
import warnings
from  import util
from  import get_context, TimeoutError
from connection import wait
INIT = 'INIT'
RUN = 'RUN'
CLOSE = 'CLOSE'
TERMINATE = 'TERMINATE'
job_counter = itertools.count()

def mapstar(args):
    pass
# WARNING: Decompyle incomplete


def starmapstar(args):
    return list(itertools.starmap(args[0], args[1]))


class RemoteTraceback(Exception):
    
    def __init__(self, tb):
        self.tb = tb

    
    def __str__(self):
        return self.tb



class ExceptionWithTraceback:
    
    def __init__(self, exc, tb):
        tb = traceback.format_exception(type(exc), exc, tb)
        tb = ''.join(tb)
        self.exc = exc
        self.tb = '\n"""\n%s"""' % tb

    
    def __reduce__(self):
        return (rebuild_exc, (self.exc, self.tb))



def rebuild_exc(exc, tb):
    exc.__cause__ = RemoteTraceback(tb)
    return exc


class MaybeEncodingError(Exception):
    pass
# WARNING: Decompyle incomplete


def worker(inqueue, outqueue, initializer, initargs, maxtasks, wrap_exception = (None, (), None, False)):
    pass
# WARNING: Decompyle incomplete


def _helper_reraises_exception(ex):
    '''Pickle-able helper function for use by _guarded_task_generation.'''
    raise ex


class _PoolCache(dict):
    pass
# WARNING: Decompyle incomplete


class Pool(object):
    '''
    Class which supports an async version of applying functions to arguments.
    '''
    _wrap_exception = True
    Process = (lambda ctx: pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self, processes, initializer, initargs, maxtasksperchild, context = (None, None, (), None, None)):
        self._pool = []
        self._state = INIT
        if not context:
            context
        self._ctx = get_context()
        self._setup_queues()
        self._taskqueue = queue.SimpleQueue()
        self._change_notifier = self._ctx.SimpleQueue()
        self._cache = _PoolCache(notifier = self._change_notifier)
        self._maxtasksperchild = maxtasksperchild
        self._initializer = initializer
        self._initargs = initargs
    # WARNING: Decompyle incomplete

    
    def __del__(self, _warn, RUN = (warnings.warn, RUN)):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        cls = self.__class__
        return f'''<{cls.__module__}.{cls.__qualname__} state={self._state} pool_size={len(self._pool)}>'''

    
    def _get_sentinels(self):
