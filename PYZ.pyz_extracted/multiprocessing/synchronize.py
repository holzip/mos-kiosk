# Source Generated with Decompyle++
# File: synchronize.pyc (Python 3.12)

__all__ = [
    'Lock',
    'RLock',
    'Semaphore',
    'BoundedSemaphore',
    'Condition',
    'Event']
import threading
import sys
import tempfile
import _multiprocessing
import time
from  import context
from  import process
from  import util

try:
    from _multiprocessing import SemLock, sem_unlink
    (RECURSIVE_MUTEX, SEMAPHORE) = list(range(2))
    SEM_VALUE_MAX = _multiprocessing.SemLock.SEM_VALUE_MAX
    
    class SemLock(object):
        _rand = tempfile._RandomNameSequence()
        
        def __init__(self, kind, value, maxvalue, *, ctx):
            pass
        # WARNING: Decompyle incomplete

        _cleanup = (lambda name: unregister = unregisterimport resource_trackersem_unlink(name)unregister(name, 'semaphore'))()
        
        def _make_methods(self):
            self.acquire = self._semlock.acquire
            self.release = self._semlock.release

        
        def __enter__(self):
            return self._semlock.__enter__()

        
        def __exit__(self, *args):
            pass
        # WARNING: Decompyle incomplete

        
        def __getstate__(self):
            context.assert_spawning(self)
            sl = self._semlock
            if sys.platform == 'win32':
                h = context.get_spawning_popen().duplicate_for_child(sl.handle)
            elif self._is_fork_ctx:
                raise RuntimeError('A SemLock created in a fork context is being shared with a process in a spawn context. This is not supported. Please use the same context to create multiprocessing objects and Process.')
            h = sl.handle
            return (h, sl.kind, sl.maxvalue, sl.name)

        
        def __setstate__(self, state):
            pass
        # WARNING: Decompyle incomplete

        _make_name = (lambda : f'''{process.current_process()._config['semprefix']!s}-{next(SemLock._rand)!s}''')()

    
    class Semaphore(SemLock):
        
        def __init__(self, value = (1,), *, ctx):
            SemLock.__init__(self, SEMAPHORE, value, SEM_VALUE_MAX, ctx = ctx)

        
        def get_value(self):
            return self._semlock._get_value()

        
        def __repr__(self):
            
            try:
                value = self._semlock._get_value()
                return f'''<{self.__class__.__name__!s}(value={value!s})>'''
            except Exception:
                value = 'unknown'
                continue



    
    class BoundedSemaphore(Semaphore):
        
        def __init__(self, value = (1,), *, ctx):
            SemLock.__init__(self, SEMAPHORE, value, value, ctx = ctx)

        
        def __repr__(self):
            
            try:
                value = self._semlock._get_value()
                return f'''<{self.__class__.__name__!s}(value={value!s}, maxvalue={self._semlock.maxvalue!s})>'''
            except Exception:
                value = 'unknown'
                continue



    
    class Lock(SemLock):
        
        def __init__(self, *, ctx):
            SemLock.__init__(self, SEMAPHORE, 1, 1, ctx = ctx)

        
        def __repr__(self):
            
            try:
                if self._semlock._is_mine():
                    name = process.current_process().name
                    if threading.current_thread().name != 'MainThread':
                        name += '|' + threading.current_thread().name
                    elif not self._semlock._is_zero():
                        name = 'None'
                    elif self._semlock._count() > 0:
                        name = 'SomeOtherThread'
                    else:
                        name = 'SomeOtherProcess'
                return f'''<{self.__class__.__name__!s}(owner={name!s})>'''
            except Exception:
                name = 'unknown'
                continue



    
    class RLock(SemLock):
        
        def __init__(self, *, ctx):
            SemLock.__init__(self, RECURSIVE_MUTEX, 1, 1, ctx = ctx)

        
        def __repr__(self):
            
            try:
                if self._semlock._is_mine():
                    name = process.current_process().name
                    if threading.current_thread().name != 'MainThread':
                        name += '|' + threading.current_thread().name
                    count = self._semlock._count()
                elif not self._semlock._is_zero():
                    (name, count) = ('None', 0)
                elif self._semlock._count() > 0:
                    (name, count) = ('SomeOtherThread', 'nonzero')
                else:
                    (name, count) = ('SomeOtherProcess', 'nonzero')
                return f'''<{self.__class__.__name__!s}({name!s}, {count!s})>'''
            except Exception:
                (name, count) = ('unknown', 'unknown')
                continue



    
    class Condition(object):
        
        def __init__(self, lock = (None,), *, ctx):
            if not lock:
                lock
            self._lock = ctx.RLock()
            self._sleeping_count = ctx.Semaphore(0)
            self._woken_count = ctx.Semaphore(0)
            self._wait_semaphore = ctx.Semaphore(0)
            self._make_methods()

        
        def __getstate__(self):
            context.assert_spawning(self)
            return (self._lock, self._sleeping_count, self._woken_count, self._wait_semaphore)

        
        def __setstate__(self, state):
            (self._lock, self._sleeping_count, self._woken_count, self._wait_semaphore) = state
            self._make_methods()

        
        def __enter__(self):
            return self._lock.__enter__()

        
        def __exit__(self, *args):
            pass
        # WARNING: Decompyle incomplete

        
        def _make_methods(self):
            self.acquire = self._lock.acquire
            self.release = self._lock.release

        
        def __repr__(self):
            
            try:
                num_waiters = self._sleeping_count._semlock._get_value() - self._woken_count._semlock._get_value()
                return f'''<{self.__class__.__name__!s}({self._lock!s}, {num_waiters!s})>'''
            except Exception:
                num_waiters = 'unknown'
                continue


        
        def wait(self, timeout = (None,)):
            pass
        # WARNING: Decompyle incomplete

        
        def notify(self, n = (1,)):
            pass
        # WARNING: Decompyle incomplete

        
        def notify_all(self):
            self.notify(n = sys.maxsize)

        
        def wait_for(self, predicate, timeout = (None,)):
            result = predicate()
            if result:
                return result
        # WARNING: Decompyle incomplete


    
    class Event(object):
        
        def __init__(self, *, ctx):
            self._cond = ctx.Condition(ctx.Lock())
            self._flag = ctx.Semaphore(0)

        
        def is_set(self):
            self._cond
            if self._flag.acquire(False):
                self._flag.release()
                None(None, None)
                return True
            None(None, None)
            return False
            with None:
                if not None:
                    pass

        
        def set(self):
            self._cond
            self._flag.acquire(False)
            self._flag.release()
            self._cond.notify_all()
            None(None, None)
            return None
            with None:
                if not None:
                    pass

        
        def clear(self):
            self._cond
            self._flag.acquire(False)
            None(None, None)
            return None
            with None:
                if not None:
                    pass

        
        def wait(self, timeout = (None,)):
            self._cond
            if self._flag.acquire(False):
                self._flag.release()
            else:
                self._cond.wait(timeout)
            if self._flag.acquire(False):
                self._flag.release()
                None(None, None)
                return True
            None(None, None)
            return False
            with None:
                if not None:
                    pass

        
        def __repr__(self):
            set_status = 'set' if self.is_set() else 'unset'
            return f'''<{type(self).__qualname__} at {id(self):#x} {set_status}>'''


    
    class Barrier(threading.Barrier):
        
        def __init__(self, parties, action, timeout = (None, None), *, ctx):
            import struct
            BufferWrapper = BufferWrapper
            import heap
            wrapper = BufferWrapper(struct.calcsize('i') * 2)
            cond = ctx.Condition()
            self.__setstate__((parties, action, timeout, cond, wrapper))
            self._state = 0
            self._count = 0

        
        def __setstate__(self, state):
            (self._parties, self._action, self._timeout, self._cond, self._wrapper) = state
            self._array = self._wrapper.create_memoryview().cast('i')

        
        def __getstate__(self):
            return (self._parties, self._action, self._timeout, self._cond, self._wrapper)

        _state = (lambda self: self._array[0])()
        _state = (lambda self, value: self._array[0] = value)()
        _count = (lambda self: self._array[1])()
        _count = (lambda self, value: self._array[1] = value)()

    return None
except ImportError:
    raise ImportError('This platform lacks a functioning sem_open implementation, therefore, the required synchronization primitives needed will not function, see issue 3770.')

