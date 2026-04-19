# Source Generated with Decompyle++
# File: base_events.pyc (Python 3.12)

'''Base implementation of event loop.

The event loop can be broken up into a multiplexer (the part
responsible for notifying us of I/O events) and the event loop proper,
which wraps a multiplexer with functionality for scheduling callbacks,
immediately or at a given time in the future.

Whenever a public API takes a callback, subsequent positional
arguments will be passed to the callback if/when it is called.  This
avoids the proliferation of trivial lambdas implementing closures.
Keyword arguments for the callback are not supported; this is a
conscious design decision, leaving the door open for keyword arguments
to modify the meaning of the API call itself.
'''
import collections
import collections.abc as collections
import concurrent.futures as concurrent
import errno
import heapq
import itertools
import os
import socket
import stat
import subprocess
import threading
import time
import traceback
import sys
import warnings
import weakref

try:
    import ssl
    from  import constants
    from  import coroutines
    from  import events
    from  import exceptions
    from  import futures
    from  import protocols
    from  import sslproto
    from  import staggered
    from  import tasks
    from  import timeouts
    from  import transports
    from  import trsock
    from log import logger
    __all__ = ('BaseEventLoop', 'Server')
    _MIN_SCHEDULED_TIMER_HANDLES = 100
    _MIN_CANCELLED_TIMER_HANDLES_FRACTION = 0.5
    _HAS_IPv6 = hasattr(socket, 'AF_INET6')
    MAXIMUM_SELECT_TIMEOUT = 86400
    
    def _format_handle(handle):
        cb = handle._callback
        if isinstance(getattr(cb, '__self__', None), tasks.Task):
            return repr(cb.__self__)
        return None(handle)

    
    def _format_pipe(fd):
        if fd == subprocess.PIPE:
            return '<pipe>'
        if fd == subprocess.STDOUT:
            return '<stdout>'
        return repr(fd)

    
    def _set_reuseport(sock):
        if not hasattr(socket, 'SO_REUSEPORT'):
            raise ValueError('reuse_port not supported by socket module')
        
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            return None
        except OSError:
            raise ValueError('reuse_port not supported by socket module, SO_REUSEPORT defined but not implemented.')


    
    def _ipaddr_info(host, port, family, type, proto, flowinfo, scopeid = (0, 0)):
        if not hasattr(socket, 'inet_pton'):
            return None
    # WARNING: Decompyle incomplete

    
    def _interleave_addrinfos(addrinfos, first_address_family_count = (1,)):
        '''Interleave list of addrinfo tuples by family.'''
        addrinfos_by_family = collections.OrderedDict()
        for addr in addrinfos:
            family = addr[0]
            if family not in addrinfos_by_family:
                addrinfos_by_family[family] = []
            addrinfos_by_family[family].append(addr)
        addrinfos_lists = list(addrinfos_by_family.values())
        reordered = []
        if first_address_family_count > 1:
            reordered.extend(addrinfos_lists[0][:first_address_family_count - 1])
            del addrinfos_lists[0][:first_address_family_count - 1]
    # WARNING: Decompyle incomplete

    
    def _run_until_complete_cb(fut):
        if not fut.cancelled():
            exc = fut.exception()
            if isinstance(exc, (SystemExit, KeyboardInterrupt)):
                return None
        futures._get_loop(fut).stop()

    if hasattr(socket, 'TCP_NODELAY'):
        
        def _set_nodelay(sock):
            if sock.family in {
                socket.AF_INET,
                socket.AF_INET6}:
                if sock.type == socket.SOCK_STREAM:
                    if sock.proto == socket.IPPROTO_TCP:
                        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                        return None
                    return None
                return None

    else:
        
        def _set_nodelay(sock):
            pass

    
    def _check_ssl_socket(sock):
        pass
    # WARNING: Decompyle incomplete

    
    class _SendfileFallbackProtocol(protocols.Protocol):
        
        def __init__(self, transp):
            if not isinstance(transp, transports._FlowControlMixin):
                raise TypeError('transport should be _FlowControlMixin instance')
            self._transport = transp
            self._proto = transp.get_protocol()
            self._should_resume_reading = transp.is_reading()
            self._should_resume_writing = transp._protocol_paused
            transp.pause_reading()
            transp.set_protocol(self)
            if self._should_resume_writing:
                self._write_ready_fut = self._transport._loop.create_future()
                return None
            self._write_ready_fut = None

        
        async def drain(self):
            pass
        # WARNING: Decompyle incomplete

        
        def connection_made(self, transport):
            raise RuntimeError('Invalid state: connection should have been established already.')

        
        def connection_lost(self, exc):
            pass
        # WARNING: Decompyle incomplete

        
        def pause_writing(self):
            pass
        # WARNING: Decompyle incomplete

        
        def resume_writing(self):
            pass
        # WARNING: Decompyle incomplete

        
        def data_received(self, data):
            raise RuntimeError('Invalid state: reading should be paused')

        
        def eof_received(self):
            raise RuntimeError('Invalid state: reading should be paused')

        
        async def restore(self):
            pass
        # WARNING: Decompyle incomplete


    
    class Server(events.AbstractServer):
        
        def __init__(self, loop, sockets, protocol_factory, ssl_context, backlog, ssl_handshake_timeout, ssl_shutdown_timeout = (None,)):
            self._loop = loop
            self._sockets = sockets
            self._active_count = 0
            self._waiters = []
            self._protocol_factory = protocol_factory
            self._backlog = backlog
            self._ssl_context = ssl_context
            self._ssl_handshake_timeout = ssl_handshake_timeout
            self._ssl_shutdown_timeout = ssl_shutdown_timeout
            self._serving = False
            self._serving_forever_fut = None

        
        def __repr__(self):
            return f'''<{self.__class__.__name__} sockets={self.sockets!r}>'''

        
        def _attach(self):
            pass
        # WARNING: Decompyle incomplete

        
        def _detach(self):
            pass
        # WARNING: Decompyle incomplete

        
        def _wakeup(self):
            waiters = self._waiters
            self._waiters = None
            for waiter in waiters:
                if waiter.done():
                    continue
                waiter.set_result(None)

        
        def _start_serving(self):
            if self._serving:
                return None
            self._serving = True
            for sock in self._sockets:
                sock.listen(self._backlog)
                self._loop._start_serving(self._protocol_factory, sock, self._ssl_context, self, self._backlog, self._ssl_handshake_timeout, self._ssl_shutdown_timeout)

        
        def get_loop(self):
            return self._loop

        
        def is_serving(self):
            return self._serving

        sockets = (lambda self: pass# WARNING: Decompyle incomplete
)()
        
        def close(self):
            sockets = self._sockets
        # WARNING: Decompyle incomplete

        
        async def start_serving(self):
            pass
        # WARNING: Decompyle incomplete

        
        async def serve_forever(self):
            pass
        # WARNING: Decompyle incomplete

        
        async def wait_closed(self):
            '''Wait until server is closed and all connections are dropped.

        - If the server is not closed, wait.
        - If it is closed, but there are still active connections, wait.

        Anyone waiting here will be unblocked once both conditions
        (server is closed and all connections have been dropped)
        have become true, in either order.

        Historical note: In 3.11 and before, this was broken, returning
        immediately if the server was already closed, even if there
        were still active connections. An attempted fix in 3.12.0 was
        still broken, returning immediately if the server was still
        open and there were no active connections. Hopefully in 3.12.1
        we have it right.
        '''
            pass
        # WARNING: Decompyle incomplete


    
    class BaseEventLoop(events.AbstractEventLoop):
        
        def __init__(self):
            self._timer_cancelled_count = 0
            self._closed = False
            self._stopping = False
            self._ready = collections.deque()
            self._scheduled = []
            self._default_executor = None
            self._internal_fds = 0
            self._thread_id = None
            self._clock_resolution = time.get_clock_info('monotonic').resolution
            self._exception_handler = None
            self.set_debug(coroutines._is_debug_mode())
            self.slow_callback_duration = 0.1
            self._current_handle = None
            self._task_factory = None
            self._coroutine_origin_tracking_enabled = False
            self._coroutine_origin_tracking_saved_depth = None
            self._asyncgens = weakref.WeakSet()
            self._asyncgens_shutdown_called = False
            self._executor_shutdown_called = False

        
        def __repr__(self):
            return f'''<{self.__class__.__name__} running={self.is_running()} closed={self.is_closed()} debug={self.get_debug()}>'''

        
        def create_future(self):
            '''Create a Future object attached to the loop.'''
            return futures.Future(loop = self)

        
        def create_task(self = None, coro = {
            'name': None,
            'context': None }, *, name, context):
            '''Schedule a coroutine object.

        Return a task object.
        '''
            self._check_closed()
        # WARNING: Decompyle incomplete

        
        def set_task_factory(self, factory):
            """Set a task factory that will be used by loop.create_task().

        If factory is None the default task factory will be set.

        If factory is a callable, it should have a signature matching
        '(loop, coro)', where 'loop' will be a reference to the active
        event loop, 'coro' will be a coroutine object.  The callable
        must return a Future.
        """
            pass
        # WARNING: Decompyle incomplete

        
        def get_task_factory(self):
            '''Return a task factory, or None if the default one is in use.'''
            return self._task_factory

        
        def _make_socket_transport(self, sock = None, protocol = (None,), waiter = {
            'extra': None,
            'server': None }, *, extra, server):
            '''Create socket transport.'''
            raise NotImplementedError

        
        def _make_ssl_transport(self, rawsock, protocol = None, sslcontext = (None,), waiter = {
            'server_side': False,
            'server_hostname': None,
            'extra': None,
            'server': None,
            'ssl_handshake_timeout': None,
            'ssl_shutdown_timeout': None,
            'call_connection_made': True }, *, server_side, server_hostname, extra, server, ssl_handshake_timeout, ssl_shutdown_timeout, call_connection_made):
            '''Create SSL transport.'''
            raise NotImplementedError

        
        def _make_datagram_transport(self, sock, protocol, address, waiter, extra = (None, None, None)):
            '''Create datagram transport.'''
            raise NotImplementedError

        
        def _make_read_pipe_transport(self, pipe, protocol, waiter, extra = (None, None)):
            '''Create read pipe transport.'''
            raise NotImplementedError

        
        def _make_write_pipe_transport(self, pipe, protocol, waiter, extra = (None, None)):
            '''Create write pipe transport.'''
            raise NotImplementedError

        
        async def _make_subprocess_transport(self, protocol, args, shell, stdin, stdout, stderr, bufsize, extra = (None,), **kwargs):
            '''Create subprocess transport.'''
            pass
        # WARNING: Decompyle incomplete

        
        def _write_to_self(self):
            '''Write a byte to self-pipe, to wake up the event loop.

        This may be called from a different thread.

        The subclass is responsible for implementing the self-pipe.
        '''
            raise NotImplementedError

        
        def _process_events(self, event_list):
            '''Process selector events.'''
            raise NotImplementedError

        
        def _check_closed(self):
            if self._closed:
                raise RuntimeError('Event loop is closed')

        
        def _check_default_executor(self):
            if self._executor_shutdown_called:
                raise RuntimeError('Executor shutdown has been called')

        
        def _asyncgen_finalizer_hook(self, agen):
            self._asyncgens.discard(agen)
            if not self.is_closed():
                self.call_soon_threadsafe(self.create_task, agen.aclose())
                return None

        
        def _asyncgen_firstiter_hook(self, agen):
            if self._asyncgens_shutdown_called:
                warnings.warn(f'''asynchronous generator {agen!r} was scheduled after loop.shutdown_asyncgens() call''', ResourceWarning, source = self)
            self._asyncgens.add(agen)

        
        async def shutdown_asyncgens(self):
            '''Shutdown all active asynchronous generators.'''
            pass
        # WARNING: Decompyle incomplete

        
        async def shutdown_default_executor(self, timeout = (None,)):
            '''Schedule the shutdown of the default executor.

        The timeout parameter specifies the amount of time the executor will
        be given to finish joining. The default value is None, which means
        that the executor will be given an unlimited amount of time.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        def _do_shutdown(self, future):
            
            try:
                self._default_executor.shutdown(wait = True)
                if not self.is_closed():
                    self.call_soon_threadsafe(futures._set_result_unless_cancelled, future, None)
                    return None
                return None
            except Exception:
                ex = None
                if not self.is_closed():
                    if not future.cancelled():
                        self.call_soon_threadsafe(future.set_exception, ex)
                        ex = None
                        del ex
                        return None
                    ex = None
                    del ex
                    return None
                ex = None
                del ex
                return None
                ex = None
                del ex


        
        def _check_running(self):
            if self.is_running():
                raise RuntimeError('This event loop is already running')
        # WARNING: Decompyle incomplete

        
        def run_forever(self):
            '''Run until stop() is called.'''
            self._check_closed()
            self._check_running()
            self._set_coroutine_origin_tracking(self._debug)
            old_agen_hooks = sys.get_asyncgen_hooks()
        # WARNING: Decompyle incomplete

        
        def run_until_complete(self, future):
            """Run until the Future is done.

        If the argument is a coroutine, it is wrapped in a Task.

        WARNING: It would be disastrous to call run_until_complete()
        with the same coroutine twice -- it would wrap it in two
        different Tasks and that can't be good.

        Return the Future's result, or raise its exception.
        """
            self._check_closed()
            self._check_running()
            new_task = not futures.isfuture(future)
            future = tasks.ensure_future(future, loop = self)
            if new_task:
                future._log_destroy_pending = False
            future.add_done_callback(_run_until_complete_cb)
            
            try:
                self.run_forever()
                future.remove_done_callback(_run_until_complete_cb)
                if not future.done():
                    raise RuntimeError('Event loop stopped before Future completed.')
                return future.result()
            except:
                if not new_task and future.done() and future.cancelled():
                    future.exception()
                raise 
                
                try:
                    pass
                except:
                    future.remove_done_callback(_run_until_complete_cb)



        
        def stop(self):
            '''Stop running the event loop.

        Every callback already scheduled will still run.  This simply informs
        run_forever to stop looping after a complete iteration.
        '''
            self._stopping = True

        
        def close(self):
            '''Close the event loop.

        This clears the queues and shuts down the executor,
        but does not wait for the executor to finish.

        The event loop must not be running.
        '''
            if self.is_running():
                raise RuntimeError('Cannot close a running event loop')
            if self._closed:
                return None
            if self._debug:
                logger.debug('Close %r', self)
            self._closed = True
            self._ready.clear()
            self._scheduled.clear()
            self._executor_shutdown_called = True
            executor = self._default_executor
        # WARNING: Decompyle incomplete

        
        def is_closed(self):
            '''Returns True if the event loop was closed.'''
            return self._closed

        
        def __del__(self, _warn = (warnings.warn,)):
            if not self.is_closed():
                _warn(f'''unclosed event loop {self!r}''', ResourceWarning, source = self)
                if not self.is_running():
                    self.close()
                    return None
                return None

        
        def is_running(self):
            '''Returns True if the event loop is running.'''
            return self._thread_id is not None

        
        def time(self):
            """Return the time according to the event loop's clock.

        This is a float expressed in seconds since an epoch, but the
        epoch, precision, accuracy and drift are unspecified and may
        differ per event loop.
        """
            return time.monotonic()

        
        def call_later(self, delay = None, callback = {
            'context': None }, *, context, *args):
            '''Arrange for a callback to be called at a given time.

        Return a Handle: an opaque object with a cancel() method that
        can be used to cancel the call.

        The delay can be an int or float, expressed in seconds.  It is
        always relative to the current time.

        Each callback will be called exactly once.  If two callbacks
        are scheduled for exactly the same time, it is undefined which
        will be called first.

        Any positional arguments after the callback will be passed to
        the callback when it is called.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        def call_at(self, when = None, callback = {
            'context': None }, *, context, *args):
            """Like call_later(), but uses an absolute time.

        Absolute time corresponds to the event loop's time() method.
        """
            pass
        # WARNING: Decompyle incomplete

        
        def call_soon(self = None, callback = {
            'context': None }, *, context, *args):
            '''Arrange for a callback to be called as soon as possible.

        This operates as a FIFO queue: callbacks are called in the
        order in which they are registered.  Each callback will be
        called exactly once.

        Any positional arguments after the callback will be passed to
        the callback when it is called.
        '''
            self._check_closed()
            if self._debug:
                self._check_thread()
                self._check_callback(callback, 'call_soon')
            handle = self._call_soon(callback, args, context)
            if handle._source_traceback:
                del handle._source_traceback[-1]
            return handle

        
        def _check_callback(self, callback, method):
            if coroutines.iscoroutine(callback) or coroutines.iscoroutinefunction(callback):
                raise TypeError(f'''coroutines cannot be used with {method}()''')
            if not callable(callback):
                raise TypeError(f'''a callable object was expected by {method}(), got {callback!r}''')

        
        def _call_soon(self, callback, args, context):
            handle = events.Handle(callback, args, self, context)
            if handle._source_traceback:
                del handle._source_traceback[-1]
            self._ready.append(handle)
            return handle

        
        def _check_thread(self):
            '''Check that the current thread is the thread running the event loop.

        Non-thread-safe methods of this class make this assumption and will
        likely behave incorrectly when the assumption is violated.

        Should only be called when (self._debug == True).  The caller is
        responsible for checking this condition for performance reasons.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        def call_soon_threadsafe(self = None, callback = {
            'context': None }, *, context, *args):
            '''Like call_soon(), but thread-safe.'''
            self._check_closed()
            if self._debug:
                self._check_callback(callback, 'call_soon_threadsafe')
            handle = self._call_soon(callback, args, context)
            if handle._source_traceback:
                del handle._source_traceback[-1]
            self._write_to_self()
            return handle

        
        def run_in_executor(self, executor, func, *args):
            self._check_closed()
            if self._debug:
                self._check_callback(func, 'run_in_executor')
        # WARNING: Decompyle incomplete

        
        def set_default_executor(self, executor):
            if not isinstance(executor, concurrent.futures.ThreadPoolExecutor):
                raise TypeError('executor must be ThreadPoolExecutor instance')
            self._default_executor = executor

        
        def _getaddrinfo_debug(self, host, port, family, type, proto, flags):
            msg = [
                f'''{host}:{port!r}''']
            if family:
                msg.append(f'''family={family!r}''')
            if type:
                msg.append(f'''type={type!r}''')
            if proto:
                msg.append(f'''proto={proto!r}''')
            if flags:
                msg.append(f'''flags={flags!r}''')
            msg = ', '.join(msg)
            logger.debug('Get address info %s', msg)
            t0 = self.time()
            addrinfo = socket.getaddrinfo(host, port, family, type, proto, flags)
            dt = self.time() - t0
            msg = f'''Getting address info {msg} took {dt * 1000:.3f}ms: {addrinfo!r}'''
            if dt >= self.slow_callback_duration:
                logger.info(msg)
                return addrinfo
            None.debug(msg)
            return addrinfo

        
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

        
        async def sock_sendfile(self, sock, file = None, offset = (0, None), count = {
            'fallback': True }, *, fallback):
            pass
        # WARNING: Decompyle incomplete

        
        async def _sock_sendfile_native(self, sock, file, offset, count):
            pass
        # WARNING: Decompyle incomplete

        
        async def _sock_sendfile_fallback(self, sock, file, offset, count):
            pass
        # WARNING: Decompyle incomplete

        
        def _check_sendfile_params(self, sock, file, offset, count):
            if 'b' not in getattr(file, 'mode', 'b'):
                raise ValueError('file should be opened in binary mode')
            if not sock.type == socket.SOCK_STREAM:
                raise ValueError('only SOCK_STREAM type sockets are supported')
        # WARNING: Decompyle incomplete

        
        async def _connect_sock(self, exceptions, addr_info, local_addr_infos = (None,)):
            '''Create, bind and connect one socket.'''
            pass
        # WARNING: Decompyle incomplete

        
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
            'interleave': None,
            'all_errors': False }, *, ssl, family, proto, flags, sock, local_addr, server_hostname, ssl_handshake_timeout, ssl_shutdown_timeout, happy_eyeballs_delay, interleave, all_errors):
            '''Connect to a TCP server.

        Create a streaming transport connection to a given internet host and
        port: socket family AF_INET or socket.AF_INET6 depending on host (or
        family if specified), socket type SOCK_STREAM. protocol_factory must be
        a callable returning a protocol instance.

        This method is a coroutine which will try to establish the connection
        in the background.  When successful, the coroutine returns a
        (transport, protocol) pair.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        async def _create_connection_transport(self, sock, protocol_factory, ssl, server_hostname, server_side, ssl_handshake_timeout, ssl_shutdown_timeout = (False, None, None)):
            pass
        # WARNING: Decompyle incomplete

        
        async def sendfile(self, transport, file = None, offset = (0, None), count = {
            'fallback': True }, *, fallback):
            '''Send a file to transport.

        Return the total number of bytes which were sent.

        The method uses high-performance os.sendfile if available.

        file must be a regular file object opened in binary mode.

        offset tells from where to start reading the file. If specified,
        count is the total number of bytes to transmit as opposed to
        sending the file until EOF is reached. File position is updated on
        return or also in case of error in which case file.tell()
        can be used to figure out the number of bytes
        which were sent.

        fallback set to True makes asyncio to manually read and send
        the file when the platform does not support the sendfile syscall
        (e.g. Windows or SSL socket on Unix).

        Raise SendfileNotAvailableError if the system does not support
        sendfile syscall and fallback is False.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        async def _sendfile_native(self, transp, file, offset, count):
            pass
        # WARNING: Decompyle incomplete

        
        async def _sendfile_fallback(self, transp, file, offset, count):
            pass
        # WARNING: Decompyle incomplete

        
        async def start_tls(self, transport, protocol = None, sslcontext = {
            'server_side': False,
            'server_hostname': None,
            'ssl_handshake_timeout': None,
            'ssl_shutdown_timeout': None }, *, server_side, server_hostname, ssl_handshake_timeout, ssl_shutdown_timeout):
            '''Upgrade transport to TLS.

        Return a new transport that *protocol* should start using
        immediately.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        async def create_datagram_endpoint(self, protocol_factory = None, local_addr = (None, None), remote_addr = {
            'family': 0,
            'proto': 0,
            'flags': 0,
            'reuse_port': None,
            'allow_broadcast': None,
            'sock': None }, *, family, proto, flags, reuse_port, allow_broadcast, sock):
            '''Create datagram connection.'''
            pass
        # WARNING: Decompyle incomplete

        
        async def _ensure_resolved(self = None, address = {
            'family': 0,
            'type': socket.SOCK_STREAM,
            'proto': 0,
            'flags': 0 }, *, family, type, proto, flags, loop):
            pass
        # WARNING: Decompyle incomplete

        
        async def _create_server_getaddrinfo(self, host, port, family, flags):
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
            '''Create a TCP server.

        The host parameter can be a string, in that case the TCP server is
        bound to host and port.

        The host parameter can also be a sequence of strings and in that case
        the TCP server is bound to all hosts of the sequence. If a host
        appears multiple times (possibly indirectly e.g. when hostnames
        resolve to the same IP address), the server is only bound once to that
        host.

        Return a Server object which can be used to stop the service.

        This method is a coroutine.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        async def connect_accepted_socket(self, protocol_factory = None, sock = {
            'ssl': None,
            'ssl_handshake_timeout': None,
            'ssl_shutdown_timeout': None }, *, ssl, ssl_handshake_timeout, ssl_shutdown_timeout):
            pass
        # WARNING: Decompyle incomplete

        
        async def connect_read_pipe(self, protocol_factory, pipe):
            pass
        # WARNING: Decompyle incomplete

        
        async def connect_write_pipe(self, protocol_factory, pipe):
            pass
        # WARNING: Decompyle incomplete

        
        def _log_subprocess(self, msg, stdin, stdout, stderr):
            info = [
                msg]
        # WARNING: Decompyle incomplete

        
        async def subprocess_shell(self, protocol_factory = None, cmd = {
            'stdin': subprocess.PIPE,
            'stdout': subprocess.PIPE,
            'stderr': subprocess.PIPE,
            'universal_newlines': False,
            'shell': True,
            'bufsize': 0,
            'encoding': None,
            'errors': None,
            'text': None }, *, stdin, stdout, stderr, universal_newlines, shell, bufsize, encoding, errors, text, **kwargs):
            pass
        # WARNING: Decompyle incomplete

        
        async def subprocess_exec(self, protocol_factory = None, program = {
            'stdin': subprocess.PIPE,
            'stdout': subprocess.PIPE,
            'stderr': subprocess.PIPE,
            'universal_newlines': False,
            'shell': False,
            'bufsize': 0,
            'encoding': None,
            'errors': None,
            'text': None }, *, stdin, stdout, stderr, universal_newlines, shell, bufsize, encoding, errors, text, *args, **kwargs):
            pass
        # WARNING: Decompyle incomplete

        
        def get_exception_handler(self):
            '''Return an exception handler, or None if the default one is in use.
        '''
            return self._exception_handler

        
        def set_exception_handler(self, handler):
            """Set handler as the new event loop exception handler.

        If handler is None, the default exception handler will
        be set.

        If handler is a callable object, it should have a
        signature matching '(loop, context)', where 'loop'
        will be a reference to the active event loop, 'context'
        will be a dict object (see `call_exception_handler()`
        documentation for details about context).
        """
            pass
        # WARNING: Decompyle incomplete

        
        def default_exception_handler(self, context):
            '''Default exception handler.

        This is called when an exception occurs and no exception
        handler is set, and can be called by a custom exception
        handler that wants to defer to the default behavior.

        This default handler logs the error message and other
        context-dependent information.  In debug mode, a truncated
        stack trace is also appended showing where the given object
        (e.g. a handle or future or task) was created, if any.

        The context parameter has the same meaning as in
        `call_exception_handler()`.
        '''
            message = context.get('message')
            if not message:
                message = 'Unhandled exception in event loop'
            exception = context.get('exception')
        # WARNING: Decompyle incomplete

        
        def call_exception_handler(self, context):
            """Call the current event loop's exception handler.

        The context argument is a dict containing the following keys:

        - 'message': Error message;
        - 'exception' (optional): Exception object;
        - 'future' (optional): Future instance;
        - 'task' (optional): Task instance;
        - 'handle' (optional): Handle instance;
        - 'protocol' (optional): Protocol instance;
        - 'transport' (optional): Transport instance;
        - 'socket' (optional): Socket instance;
        - 'asyncgen' (optional): Asynchronous generator that caused
                                 the exception.

        New keys maybe introduced in the future.

        Note: do not overload this method in an event loop subclass.
        For custom exception handling, use the
        `set_exception_handler()` method.
        """
            pass
        # WARNING: Decompyle incomplete

        
        def _add_callback(self, handle):
            '''Add a Handle to _ready.'''
            if not handle._cancelled:
                self._ready.append(handle)
                return None

        
        def _add_callback_signalsafe(self, handle):
            '''Like _add_callback() but called from a signal handler.'''
            self._add_callback(handle)
            self._write_to_self()

        
        def _timer_handle_cancelled(self, handle):
            '''Notification that a TimerHandle has been cancelled.'''
            if handle._scheduled:
                return None

        
        def _run_once(self):
            """Run one full iteration of the event loop.

        This calls all currently ready callbacks, polls for I/O,
        schedules the resulting callbacks, and finally schedules
        'call_later' callbacks.
        """
            sched_count = len(self._scheduled)
            if sched_count > _MIN_SCHEDULED_TIMER_HANDLES and self._timer_cancelled_count / sched_count > _MIN_CANCELLED_TIMER_HANDLES_FRACTION:
                new_scheduled = []
                for handle in self._scheduled:
                    if handle._cancelled:
                        handle._scheduled = False
                        continue
                    new_scheduled.append(handle)
                heapq.heapify(new_scheduled)
                self._scheduled = new_scheduled
                self._timer_cancelled_count = 0
            elif self._scheduled and self._scheduled[0]._cancelled:
                heapq.heappop(self._scheduled) = self, self._timer_cancelled_count -= 1, ._timer_cancelled_count
                handle._scheduled = False
                if self._scheduled and self._scheduled[0]._cancelled:
                    continue
            timeout = None
            if self._ready or self._stopping:
                timeout = 0
            elif self._scheduled:
                when = self._scheduled[0]._when
                timeout = min(max(0, when - self.time()), MAXIMUM_SELECT_TIMEOUT)
            event_list = self._selector.select(timeout)
            self._process_events(event_list)
            event_list = None
            end_time = self.time() + self._clock_resolution
            if self._scheduled:
                handle = self._scheduled[0]
                if handle._when >= end_time:
                    pass
                else:
                    handle = heapq.heappop(self._scheduled)
                    handle._scheduled = False
                    self._ready.append(handle)
                    if self._scheduled:
                        continue
            ntodo = len(self._ready)
            for i in range(ntodo):
                handle = self._ready.popleft()
                if handle._cancelled:
                    continue
                if self._debug:
                    self._current_handle = handle
                    t0 = self.time()
                    handle._run()
                    dt = self.time() - t0
                    if dt >= self.slow_callback_duration:
                        logger.warning('Executing %s took %.3f seconds', _format_handle(handle), dt)
                    self._current_handle = None
                    continue
                handle._run()
            handle = None
            return None
            self._current_handle = None

        
        def _set_coroutine_origin_tracking(self, enabled):
            if bool(enabled) == bool(self._coroutine_origin_tracking_enabled):
                return None
            if enabled:
                self._coroutine_origin_tracking_saved_depth = sys.get_coroutine_origin_tracking_depth()
                sys.set_coroutine_origin_tracking_depth(constants.DEBUG_STACK_DEPTH)
                self._coroutine_origin_tracking_enabled = enabled
                return None
            sys.set_coroutine_origin_tracking_depth(self._coroutine_origin_tracking_saved_depth)
            self._coroutine_origin_tracking_enabled = enabled

        
        def get_debug(self):
            return self._debug

        
        def set_debug(self, enabled):
            self._debug = enabled
            if self.is_running():
                self.call_soon_threadsafe(self._set_coroutine_origin_tracking, enabled)
                return None


    return None
except ImportError:
    ssl = None
    continue

