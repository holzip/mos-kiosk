# Source Generated with Decompyle++
# File: events.pyc (Python 3.12)

from __future__ import annotations
from PySide6.QtCore import QCoreApplication, QDateTime, QDeadlineTimer, QEventLoop, QObject, QTimer, QThread, Slot
from  import futures
from  import tasks
from typing import Any, Callable
import asyncio
import collections.abc as collections
import concurrent.futures as concurrent
import contextvars
import enum
import os
import signal
import socket
import subprocess
import warnings
__all__ = [
    'QAsyncioEventLoopPolicy',
    'QAsyncioEventLoop',
    'QAsyncioHandle',
    'QAsyncioTimerHandle']

class QAsyncioExecutorWrapper(QObject):
    pass
# WARNING: Decompyle incomplete


class QAsyncioEventLoopPolicy(asyncio.AbstractEventLoopPolicy):
    pass
# WARNING: Decompyle incomplete


class QAsyncioEventLoop(QObject, asyncio.BaseEventLoop):
    '''
    Implements the asyncio API:
    https://docs.python.org/3/library/asyncio-eventloop.html
    '''
    
    class ShutDownThread(QThread):
        pass
    # WARNING: Decompyle incomplete

    
    def __init__(self = None, application = None, quit_qapp = None):
        asyncio.BaseEventLoop.__init__(self)
        QObject.__init__(self)
        self._application = application
        self._quit_qapp = quit_qapp
        self._thread = QThread.currentThread()
        self._closed = False
        self._quit_from_inside = False
        self._quit_from_outside = False
        self._asyncgens = set()
        self._default_executor = concurrent.futures.ThreadPoolExecutor()
        self._exception_handler = self.default_exception_handler
        self._task_factory = None
        self._future_to_complete = None
        self._debug = bool(os.getenv('PYTHONASYNCIODEBUG', False))
        self._application.aboutToQuit.connect(self._about_to_quit_cb)

    
    def _run_until_complete_cb(self = None, future = None):
        '''
        A callback that stops the loop when the future is done, used when
        running the loop with run_until_complete().
        '''
        if future.cancelled() and isinstance(future.exception(), (SystemExit, KeyboardInterrupt)):
            return None
        future.get_loop().stop()

    
    def run_until_complete(self = None, future = None):
        if self.is_closed():
            raise RuntimeError('Event loop is closed')
        if self.is_running():
            raise RuntimeError('Event loop is already running')
        arg_was_coro = not asyncio.futures.isfuture(future)
        future = asyncio.tasks.ensure_future(future, loop = self)
        future.add_done_callback(self._run_until_complete_cb)
        self._future_to_complete = future
        
        try:
            self.run_forever()
            future.remove_done_callback(self._run_until_complete_cb)
            if not future.done():
                raise RuntimeError('Event loop stopped before Future completed')
            return future.result()
        except Exception:
            e = None
            if not arg_was_coro and future.done() and future.cancelled():
                future.exception()
            raise e
            e = None
            del e
            
            try:
                pass
            except:
                future.remove_done_callback(self._run_until_complete_cb)



    
    def run_forever(self = None):
        if self.is_closed():
            raise RuntimeError('Event loop is closed')
        if self.is_running():
            raise RuntimeError('Event loop is already running')
        asyncio.events._set_running_loop(self)
        self._application.exec()
        asyncio.events._set_running_loop(None)

    
    def _about_to_quit_cb(self):
        ''' A callback for the aboutToQuit signal of the QCoreApplication. '''
        if not self._quit_from_inside:
            self._quit_from_outside = True
            self.close()
            return None

    
    def stop(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_running(self = None):
        return self._thread.loopLevel() > 0

    
    def is_closed(self = None):
        return self._closed

    
    def close(self = None):
        if not self.is_running() and self._quit_from_outside:
            raise RuntimeError('Cannot close a running event loop')
        if self.is_closed():
            return None
    # WARNING: Decompyle incomplete

    
    async def shutdown_asyncgens(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def shutdown_default_executor(self = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _call_soon_impl(self = None, callback = None, *, context, is_threadsafe, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def call_soon(self = None, callback = None, *, context, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def call_soon_threadsafe(self = None, callback = None, *, context, *args):
        if self.is_closed():
            raise RuntimeError('Event loop is closed')
    # WARNING: Decompyle incomplete

    
    def _call_later_impl(self = None, delay = None, callback = None, *, context, is_threadsafe, *args):
        if not isinstance(delay, (int, float)):
            raise TypeError('delay must be an int or float')
    # WARNING: Decompyle incomplete

    
    def call_later(self = None, delay = None, callback = None, *, context, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def _call_at_impl(self = None, when = None, callback = None, *, context, is_threadsafe, *args):
        ''' All call_at() and call_later() methods map to this method. '''
        if not isinstance(when, (int, float)):
            raise TypeError('when must be an int or float')
        return QAsyncioTimerHandle(when, callback, args, self, context, is_threadsafe = is_threadsafe)

    
    def call_at(self = None, when = None, callback = None, *, context, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def time(self = None):
        return QDateTime.currentMSecsSinceEpoch() / 1000

    
    def create_future(self = None):
        return futures.QAsyncioFuture(loop = self)

    
    def create_task(self = None, coro = None, *, name, context):
        pass
    # WARNING: Decompyle incomplete

    
    def set_task_factory(self = None, factory = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_task_factory(self = None):
        return self._task_factory

    
    async def create_connection(self, protocol_factory = None, host = (None, None), port = {
        'ssl': None,
        'family': 0,
        'proto': 0,
        'flags': 0,
        'sock': None,
        'local_addr': None,
        'server_hostname': None,
        'ssl_handshake_timeout': None,
        'ssl_shutdown_timeout': None,
        'happy_eyeballs_delay': None,
        'interleave': None }, *, ssl, family, proto, flags, sock, local_addr, server_hostname, ssl_handshake_timeout, ssl_shutdown_timeout, happy_eyeballs_delay, interleave):
        pass
    # WARNING: Decompyle incomplete

    
    async def create_datagram_endpoint(self, protocol_factory = None, local_addr = (None, None), remote_addr = {
        'family': 0,
        'proto': 0,
        'flags': 0,
        'reuse_address': None,
        'reuse_port': None,
        'allow_broadcast': None,
        'sock': None }, *, family, proto, flags, reuse_address, reuse_port, allow_broadcast, sock):
        pass
    # WARNING: Decompyle incomplete

    
    async def create_unix_connection(self = None, protocol_factory = (None,), path = {
        'ssl': None,
        'sock': None,
        'server_hostname': None,
        'ssl_handshake_timeout': None,
        'ssl_shutdown_timeout': None }, *, ssl, sock, server_hostname, ssl_handshake_timeout, ssl_shutdown_timeout):
        pass
    # WARNING: Decompyle incomplete

    
    async def create_server(self, protocol_factory = None, host = (None, None), port = {
        'family': socket.AF_UNSPEC,
        'flags': socket.AI_PASSIVE,
        'sock': None,
        'backlog': 100,
        'ssl': None,
        'reuse_address': None,
        'reuse_port': None,
        'ssl_handshake_timeout': None,
        'ssl_shutdown_timeout': None,
        'start_serving': True }, *, family, flags, sock, backlog, ssl, reuse_address, reuse_port, ssl_handshake_timeout, ssl_shutdown_timeout, start_serving):
        pass
    # WARNING: Decompyle incomplete

    
    async def create_unix_server(self = None, protocol_factory = (None,), path = {
        'sock': None,
        'backlog': 100,
        'ssl': None,
        'ssl_handshake_timeout': None,
        'ssl_shutdown_timeout': None,
        'start_serving': True }, *, sock, backlog, ssl, ssl_handshake_timeout, ssl_shutdown_timeout, start_serving):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_accepted_socket(self, protocol_factory = None, sock = {
        'ssl': None,
        'ssl_handshake_timeout': None,
        'ssl_shutdown_timeout': None }, *, ssl, ssl_handshake_timeout, ssl_shutdown_timeout):
        pass
    # WARNING: Decompyle incomplete

    
    async def sendfile(self, transport, file = None, offset = (0, None), count = {
        'fallback': True }, *, fallback):
        pass
    # WARNING: Decompyle incomplete

    
    async def start_tls(self, transport, protocol = None, sslcontext = {
        'server_side': False,
        'server_hostname': None,
        'ssl_handshake_timeout': None,
        'ssl_shutdown_timeout': None }, *, server_side, server_hostname, ssl_handshake_timeout, ssl_shutdown_timeout):
        pass
    # WARNING: Decompyle incomplete

    
    def add_reader(self, fd, callback, *args):
        raise NotImplementedError('QAsyncioEventLoop.add_reader() is not implemented yet')

    
    def remove_reader(self, fd):
        raise NotImplementedError('QAsyncioEventLoop.remove_reader() is not implemented yet')

    
    def add_writer(self, fd, callback, *args):
        raise NotImplementedError('QAsyncioEventLoop.add_writer() is not implemented yet')

    
    def remove_writer(self, fd):
        raise NotImplementedError('QAsyncioEventLoop.remove_writer() is not implemented yet')

    
    async def sock_recv(self, sock, nbytes):
        pass
    # WARNING: Decompyle incomplete

    
    async def sock_recv_into(self, sock, buf):
        pass
    # WARNING: Decompyle incomplete

    
    async def sock_recvfrom(self, sock, bufsize):
        pass
    # WARNING: Decompyle incomplete

    
    async def sock_recvfrom_into(self, sock, buf, nbytes = (0,)):
        pass
    # WARNING: Decompyle incomplete

    
    async def sock_sendall(self, sock, data):
        pass
    # WARNING: Decompyle incomplete

    
    async def sock_sendto(self, sock, data, address):
        pass
    # WARNING: Decompyle incomplete

    
    async def sock_connect(self, sock, address):
        pass
    # WARNING: Decompyle incomplete

    
    async def sock_accept(self, sock):
        pass
    # WARNING: Decompyle incomplete

    
    async def sock_sendfile(self, sock, file = None, offset = (0, None), count = {
        'fallback': None }, *, fallback):
        pass
    # WARNING: Decompyle incomplete

    
    async def getaddrinfo(self, host = None, port = {
        'family': 0,
        'type': 0,
        'proto': 0,
        'flags': 0 }, *, family, type, proto, flags):
        pass
    # WARNING: Decompyle incomplete

    
    async def getnameinfo(self, sockaddr, flags = (0,)):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_read_pipe(self, protocol_factory, pipe):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_write_pipe(self, protocol_factory, pipe):
        pass
    # WARNING: Decompyle incomplete

    
    def add_signal_handler(self, sig, callback, *args):
        raise NotImplementedError('QAsyncioEventLoop.add_signal_handler() is not implemented yet')

    
    def remove_signal_handler(self, sig):
        raise NotImplementedError('QAsyncioEventLoop.remove_signal_handler() is not implemented yet')

    
    def run_in_executor(self = None, executor = None, func = None, *args):
        if self.is_closed():
            raise RuntimeError('Event loop is closed')
    # WARNING: Decompyle incomplete

    
    def set_default_executor(self = None, executor = None):
        if not isinstance(executor, concurrent.futures.ThreadPoolExecutor):
            raise TypeError('The executor must be a ThreadPoolExecutor')
        self._default_executor = executor

    
    def set_exception_handler(self = None, handler = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_exception_handler(self = None):
        return self._exception_handler

    
    def default_exception_handler(self = None, context = None):
        if context['message']:
            print(f'''{context['message']} from task {context['task']._name},read the following traceback:''')
            print(context['traceback'])
            return None

    
    def call_exception_handler(self = None, context = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_debug(self = None):
        return self._debug

    
    def set_debug(self = None, enabled = None):
        self._debug = enabled

    
    async def subprocess_exec(self = None, protocol_factory = {
        'stdin': subprocess.PIPE,
        'stdout': subprocess.PIPE,
        'stderr': subprocess.PIPE }, *, stdin, stdout, stderr, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    async def subprocess_shell(self, protocol_factory = None, cmd = {
        'stdin': subprocess.PIPE,
        'stdout': subprocess.PIPE,
        'stderr': subprocess.PIPE }, *, stdin, stdout, stderr, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class QAsyncioHandle:
    '''
    The handle enqueues a callback to be executed by the event loop, and allows
    for this callback to be cancelled before it is executed. This callback will
    typically execute the step function for a task. This makes the handle one
    of the main components of asyncio.
    '''
    
    class HandleState(enum.Enum):
        PENDING = enum.auto()
        CANCELLED = enum.auto()
        DONE = enum.auto()

    
    def __init__(self, callback = None, args = None, loop = None, context = (False,), is_threadsafe = ('callback', 'Callable', 'args', 'tuple', 'loop', 'QAsyncioEventLoop', 'context', 'contextvars.Context | None', 'is_threadsafe', 'bool | None', 'return', 'None')):
        self._callback = callback
        self._args = args
        self._loop = loop
        self._context = context
        self._is_threadsafe = is_threadsafe
        self._timeout = 0
        self._state = QAsyncioHandle.HandleState.PENDING
        self._start()

    
    def _start(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _schedule_event(self = None, timeout = None, func = None):
        if not self._loop.is_closed():
            if not self._loop._quit_from_outside:
                if self._is_threadsafe:
                    QTimer.singleShot(timeout, self._loop, func)
                    return None
                QTimer.singleShot(timeout, func)
                return None
            return None

    _cb = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def cancel(self = None):
        if self._state == QAsyncioHandle.HandleState.PENDING:
            self._state = QAsyncioHandle.HandleState.CANCELLED
            return None

    
    def cancelled(self = None):
        return self._state == QAsyncioHandle.HandleState.CANCELLED



class QAsyncioTimerHandle(asyncio.TimerHandle, QAsyncioHandle):
    
    def __init__(self, when, callback = None, args = None, loop = None, context = (False,), is_threadsafe = ('when', 'float', 'callback', 'Callable', 'args', 'tuple', 'loop', 'QAsyncioEventLoop', 'context', 'contextvars.Context | None', 'is_threadsafe', 'bool | None', 'return', 'None')):
        QAsyncioHandle.__init__(self, callback, args, loop, context, is_threadsafe)
        self._when = when
        time = self._loop.time()
        self._timeout = round(max(self._when - time, 0) * 1000)
        QAsyncioHandle._start(self)

    
    def _start(self = None):
        '''
        Overridden so that timer.start() is only called once at the end of the
        constructor for both QtHandle and QtTimerHandle.
        '''
        pass

    
    def when(self = None):
        return self._when


