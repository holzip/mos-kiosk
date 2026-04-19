# Source Generated with Decompyle++
# File: context.pyc (Python 3.12)

import os
import sys
import threading
from  import process
from  import reduction
__all__ = ()

class ProcessError(Exception):
    pass


class BufferTooShort(ProcessError):
    pass


class TimeoutError(ProcessError):
    pass


class AuthenticationError(ProcessError):
    pass


class BaseContext(object):
    ProcessError = ProcessError
    BufferTooShort = BufferTooShort
    TimeoutError = TimeoutError
    AuthenticationError = AuthenticationError
    current_process = staticmethod(process.current_process)
    parent_process = staticmethod(process.parent_process)
    active_children = staticmethod(process.active_children)
    
    def cpu_count(self):
        '''Returns the number of CPUs in the system'''
        num = os.cpu_count()
    # WARNING: Decompyle incomplete

    
    def Manager(self):
        '''Returns a manager associated with a running server process

        The managers methods such as `Lock()`, `Condition()` and `Queue()`
        can be used to create shared objects.
        '''
        SyncManager = SyncManager
        import managers
        m = SyncManager(ctx = self.get_context())
        m.start()
        return m

    
    def Pipe(self, duplex = (True,)):
        '''Returns two connection object connected by a pipe'''
        Pipe = Pipe
        import connection
        return Pipe(duplex)

    
    def Lock(self):
        '''Returns a non-recursive lock object'''
        Lock = Lock
        import synchronize
        return Lock(ctx = self.get_context())

    
    def RLock(self):
        '''Returns a recursive lock object'''
        RLock = RLock
        import synchronize
        return RLock(ctx = self.get_context())

    
    def Condition(self, lock = (None,)):
        '''Returns a condition object'''
        Condition = Condition
        import synchronize
        return Condition(lock, ctx = self.get_context())

    
    def Semaphore(self, value = (1,)):
        '''Returns a semaphore object'''
        Semaphore = Semaphore
        import synchronize
        return Semaphore(value, ctx = self.get_context())

    
    def BoundedSemaphore(self, value = (1,)):
        '''Returns a bounded semaphore object'''
        BoundedSemaphore = BoundedSemaphore
        import synchronize
        return BoundedSemaphore(value, ctx = self.get_context())

    
    def Event(self):
        '''Returns an event object'''
        Event = Event
        import synchronize
        return Event(ctx = self.get_context())

    
    def Barrier(self, parties, action, timeout = (None, None)):
        '''Returns a barrier object'''
        Barrier = Barrier
        import synchronize
        return Barrier(parties, action, timeout, ctx = self.get_context())

    
    def Queue(self, maxsize = (0,)):
        '''Returns a queue object'''
        Queue = Queue
        import queues
        return Queue(maxsize, ctx = self.get_context())

    
    def JoinableQueue(self, maxsize = (0,)):
        '''Returns a queue object'''
        JoinableQueue = JoinableQueue
        import queues
        return JoinableQueue(maxsize, ctx = self.get_context())

    
    def SimpleQueue(self):
        '''Returns a queue object'''
        SimpleQueue = SimpleQueue
        import queues
        return SimpleQueue(ctx = self.get_context())

    
    def Pool(self, processes, initializer, initargs, maxtasksperchild = (None, None, (), None)):
        '''Returns a process pool object'''
        Pool = Pool
        import pool
        return Pool(processes, initializer, initargs, maxtasksperchild, context = self.get_context())

    
    def RawValue(self, typecode_or_type, *args):
        '''Returns a shared object'''
        RawValue = RawValue
        import sharedctypes
    # WARNING: Decompyle incomplete

    
    def RawArray(self, typecode_or_type, size_or_initializer):
        '''Returns a shared array'''
        RawArray = RawArray
        import sharedctypes
        return RawArray(typecode_or_type, size_or_initializer)

    
    def Value(self = None, typecode_or_type = {
        'lock': True }, *, lock, *args):
        '''Returns a synchronized shared object'''
        Value = Value
        import sharedctypes
    # WARNING: Decompyle incomplete

    
    def Array(self, typecode_or_type = None, size_or_initializer = {
        'lock': True }, *, lock):
        '''Returns a synchronized shared array'''
        Array = Array
        import sharedctypes
        return Array(typecode_or_type, size_or_initializer, lock = lock, ctx = self.get_context())

    
    def freeze_support(self):
        '''Check whether this is a fake forked process in a frozen executable.
        If so then run code specified by commandline and exit.
        '''
        if sys.platform == 'win32':
            if getattr(sys, 'frozen', False):
                freeze_support = freeze_support
                import spawn
                freeze_support()
                return None
            return None

    
    def get_logger(self):
        '''Return package logger -- if it does not already exist then
        it is created.
        '''
        get_logger = get_logger
        import util
        return get_logger()

    
    def log_to_stderr(self, level = (None,)):
        '''Turn on logging and add a handler which prints to stderr'''
        log_to_stderr = log_to_stderr
        import util
        return log_to_stderr(level)

    
    def allow_connection_pickling(self):
        '''Install support for sending connections and sockets
        between processes
        '''
        connection = connection
        import 

    
    def set_executable(self, executable):
        """Sets the path to a python.exe or pythonw.exe binary used to run
        child processes instead of sys.executable when using the 'spawn'
        start method.  Useful for people embedding Python.
        """
        set_executable = set_executable
        import spawn
        set_executable(executable)

    
    def set_forkserver_preload(self, module_names):
        '''Set list of module names to try to load in forkserver process.
        This is really just a hint.
        '''
        set_forkserver_preload = set_forkserver_preload
        import forkserver
        set_forkserver_preload(module_names)

    
    def get_context(self, method = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_start_method(self, allow_none = (False,)):
        return self._name

    
    def set_start_method(self, method, force = (False,)):
        raise ValueError('cannot set start method of concrete context')

    reducer = (lambda self: globals().get('reduction'))()
    reducer = (lambda self, reduction: globals()['reduction'] = reduction)()
    
    def _check_available(self):
        pass



class Process(process.BaseProcess):
    _start_method = None
    _Popen = (lambda process_obj: _default_context.get_context().Process._Popen(process_obj))()
    _after_fork = (lambda : _default_context.get_context().Process._after_fork())()


class DefaultContext(BaseContext):
    pass
# WARNING: Decompyle incomplete


def _force_start_method(method):
    _default_context._actual_context = _concrete_contexts[method]

_tls = threading.local()

def get_spawning_popen():
    return getattr(_tls, 'spawning_popen', None)


def set_spawning_popen(popen):
    _tls.spawning_popen = popen


def assert_spawning(obj):
    pass
# WARNING: Decompyle incomplete

