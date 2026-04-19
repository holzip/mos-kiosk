# Source Generated with Decompyle++
# File: windows_events.pyc (Python 3.12)

'''Selector and proactor event loops for Windows.'''
import sys
if sys.platform != 'win32':
    raise ImportError('win32 only')
import _overlapped
import _winapi
import errno
from functools import partial
import math
import msvcrt
import socket
import struct
import time
import weakref
from  import events
from  import base_subprocess
from  import futures
from  import exceptions
from  import proactor_events
from  import selector_events
from  import tasks
from  import windows_utils
from log import logger
__all__ = ('SelectorEventLoop', 'ProactorEventLoop', 'IocpProactor', 'DefaultEventLoopPolicy', 'WindowsSelectorEventLoopPolicy', 'WindowsProactorEventLoopPolicy')
NULL = _winapi.NULL
INFINITE = _winapi.INFINITE
ERROR_CONNECTION_REFUSED = 1225
ERROR_CONNECTION_ABORTED = 1236
CONNECT_PIPE_INIT_DELAY = 0.001
CONNECT_PIPE_MAX_DELAY = 0.1

class _OverlappedFuture(futures.Future):
    pass
# WARNING: Decompyle incomplete


class _BaseWaitHandleFuture(futures.Future):
    pass
# WARNING: Decompyle incomplete


class _WaitCancelFuture(_BaseWaitHandleFuture):
    pass
# WARNING: Decompyle incomplete


class _WaitHandleFuture(_BaseWaitHandleFuture):
    pass
# WARNING: Decompyle incomplete


class PipeServer(object):
    '''Class representing a pipe server.

    This is much like a bound, listening socket.
    '''
    
    def __init__(self, address):
        self._address = address
        self._free_instances = weakref.WeakSet()
        self._pipe = None
        self._accept_pipe_future = None
        self._pipe = self._server_pipe_handle(True)

    
    def _get_unconnected_pipe(self):
        tmp, self._pipe = self._pipe, self._server_pipe_handle(False)
        return tmp

    
    def _server_pipe_handle(self, first):
        if self.closed():
            return None
        flags = _winapi.PIPE_ACCESS_DUPLEX | _winapi.FILE_FLAG_OVERLAPPED
        if first:
            flags |= _winapi.FILE_FLAG_FIRST_PIPE_INSTANCE
        h = _winapi.CreateNamedPipe(self._address, flags, _winapi.PIPE_TYPE_MESSAGE | _winapi.PIPE_READMODE_MESSAGE | _winapi.PIPE_WAIT, _winapi.PIPE_UNLIMITED_INSTANCES, windows_utils.BUFSIZE, windows_utils.BUFSIZE, _winapi.NMPWAIT_WAIT_FOREVER, _winapi.NULL)
        pipe = windows_utils.PipeHandle(h)
        self._free_instances.add(pipe)
        return pipe

    
    def closed(self):
        return self._address is None

    
    def close(self):
        pass
    # WARNING: Decompyle incomplete

    __del__ = close


class _WindowsSelectorEventLoop(selector_events.BaseSelectorEventLoop):
    '''Windows version of selector event loop.'''
    pass


class ProactorEventLoop(proactor_events.BaseProactorEventLoop):
    pass
# WARNING: Decompyle incomplete


class IocpProactor:
    '''Proactor implementation using IOCP.'''
    
    def __init__(self, concurrency = (INFINITE,)):
        self._loop = None
        self._results = []
        self._iocp = _overlapped.CreateIoCompletionPort(_overlapped.INVALID_HANDLE_VALUE, NULL, 0, concurrency)
        self._cache = { }
        self._registered = weakref.WeakSet()
        self._unregistered = []
        self._stopped_serving = weakref.WeakSet()

    
    def _check_closed(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        info = [
            'overlapped#=%s' % len(self._cache),
            'result#=%s' % len(self._results)]
    # WARNING: Decompyle incomplete

    
    def set_loop(self, loop):
        self._loop = loop

    
    def select(self, timeout = (None,)):
        if not self._results:
            self._poll(timeout)
        tmp = self._results
        self._results = []
        
        try:
            tmp = None
            return tmp
        except:
            tmp = None


    
    def _result(self, value):
        fut = self._loop.create_future()
        fut.set_result(value)
        return fut

    finish_socket_func = (lambda trans, key, ov: pass# WARNING: Decompyle incomplete
)()
    _finish_recvfrom = (lambda cls, trans, key, ov, *, empty_result, exc = None, 