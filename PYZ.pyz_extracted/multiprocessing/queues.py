# Source Generated with Decompyle++
# File: queues.pyc (Python 3.12)

__all__ = [
    'Queue',
    'SimpleQueue',
    'JoinableQueue']
import sys
import os
import threading
import collections
import time
import types
import weakref
import errno
from queue import Empty, Full
import _multiprocessing
from  import connection
from  import context
_ForkingPickler = context.reduction.ForkingPickler
from util import debug, info, Finalize, register_after_fork, is_exiting

class Queue(object):
    
    def __init__(self, maxsize = (0,), *, ctx):
        if maxsize <= 0:
            maxsize = SEM_VALUE_MAX
            import synchronize
        self._maxsize = maxsize
        (self._reader, self._writer) = connection.Pipe(duplex = False)
        self._rlock = ctx.Lock()
        self._opid = os.getpid()
        if sys.platform == 'win32':
            self._wlock = None
        else:
            self._wlock = ctx.Lock()
        self._sem = ctx.BoundedSemaphore(maxsize)
        self._ignore_epipe = False
        self._reset()
        if sys.platform != 'win32':
            register_after_fork(self, Queue._after_fork)
            return None

    
    def __getstate__(self):
        context.assert_spawning(self)
        return (self._ignore_epipe, self._maxsize, self._reader, self._writer, self._rlock, self._wlock, self._sem, self._opid)

    
    def __setstate__(self, state):
        (self._ignore_epipe, self._maxsize, self._reader, self._writer, self._rlock, self._wlock, self._sem, self._opid) = state
        self._reset()

    
    def _after_fork(self):
        debug('Queue._after_fork()')
        self._reset(after_fork = True)

    
    def _reset(self, after_fork = (False,)):
        if after_fork:
            self._notempty._at_fork_reinit()
        else:
            self._notempty = threading.Condition(threading.Lock())
        self._buffer = collections.deque()
        self._thread = None
        self._jointhread = None
        self._joincancelled = False
        self._closed = False
        self._close = None
        self._send_bytes = self._writer.send_bytes
        self._recv_bytes = self._reader.recv_bytes
        self._poll = self._reader.poll

    
    def put(self, obj, block, timeout = (True, None)):
        if self._closed:
            raise ValueError(f'''Queue {self!r} is closed''')
        if not self._sem.acquire(block, timeout):
            raise Full
        self._notempty
    # WARNING: Decompyle incomplete

    
    def get(self, block, timeout = (True, None)):
        if self._closed:
            raise ValueError(f'''Queue {self!r} is closed''')
    # WARNING: Decompyle incomplete

    
    def qsize(self):
        return self._maxsize - self._sem._semlock._get_value()

    
    def empty(self):
        return not self._poll()

    
    def full(self):
        return self._sem._semlock._is_zero()

    
    def get_nowait(self):
        return self.get(False)

    
    def put_nowait(self, obj):
        return self.put(obj, False)

    
    def close(self):
        self._closed = True
        close = self._close
        if close:
            self._close = None
            close()
            return None

    
    def join_thread(self):
        debug('Queue.join_thread()')
    # WARNING: Decompyle incomplete

    
    def cancel_join_thread(self):
        debug('Queue.cancel_join_thread()')
        self._joincancelled = True
        
        try:
            self._jointhread.cancel()
            return None
        except AttributeError:
            return None


    
    def _terminate_broken(self):
        self._reader.close()
        if sys.platform == 'win32':
            self._writer.close()
        self.close()
        self.join_thread()

    
    def _start_thread(self):
        debug('Queue._start_thread()')
        self._buffer.clear()
        self._thread = threading.Thread(target = Queue._feed, args = (self._buffer, self._notempty, self._send_bytes, self._wlock, self._reader.close, self._writer.close, self._ignore_epipe, self._on_queue_feeder_error, self._sem), name = 'QueueFeederThread', daemon = True)
        
        try:
            debug('doing self._thread.start()')
            self._thread.start()
            debug('... done self._thread.start()')
            if not self._joincancelled:
                self._jointhread = Finalize(self._thread, Queue._finalize_join, [
                    weakref.ref(self._thread)], exitpriority = -5)
            self._close = Finalize(self, Queue._finalize_close, [
                self._buffer,
                self._notempty], exitpriority = 10)
            return None
        except:
            self._thread = None
            raise 


    _finalize_join = (lambda twr: debug('joining queue thread')thread = twr()# WARNING: Decompyle incomplete
)()
    _finalize_close = (lambda buffer, notempty: debug('telling queue thread to quit')notemptybuffer.append(_sentinel)notempty.notify()None(None, None)Nonewith None:
if not None:
pass)()
    _feed = (lambda buffer, notempty, send_bytes, writelock, reader_close, writer_close, ignore_epipe, onerror, queue_sem: debug('starting thread to feed data to pipe')nacquire = notempty.acquirenrelease = notempty.releasenwait = notempty.waitbpopleft = buffer.popleftsentinel = _sentinelif sys.platform != 'win32':
wacquire = writelock.acquirewrelease = writelock.releaseelse:
wacquire = None# WARNING: Decompyle incomplete
)()
    _on_queue_feeder_error = (lambda e, obj: import tracebacktraceback.print_exc())()
    __class_getitem__ = classmethod(types.GenericAlias)

_sentinel = object()

class JoinableQueue(Queue):
    
    def __init__(self, maxsize = (0,), *, ctx):
        Queue.__init__(self, maxsize, ctx = ctx)
        self._unfinished_tasks = ctx.Semaphore(0)
        self._cond = ctx.Condition()

    
    def __getstate__(self):
        return Queue.__getstate__(self) + (self._cond, self._unfinished_tasks)

    
    def __setstate__(self, state):
        Queue.__setstate__(self, state[:-2])
        (self._cond, self._unfinished_tasks) = state[-2:]

    
    def put(self, obj, block, timeout = (True, None)):
        if self._closed:
            raise ValueError(f'''Queue {self!r} is closed''')
        if not self._sem.acquire(block, timeout):
            raise Full
        self._notempty
        self._cond
    # WARNING: Decompyle incomplete

    
    def task_done(self):
        self._cond
        if not self._unfinished_tasks.acquire(False):
            raise ValueError('task_done() called too many times')
        if self._unfinished_tasks._semlock._is_zero():
            self._cond.notify_all()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def join(self):
        self._cond
        if not self._unfinished_tasks._semlock._is_zero():
            self._cond.wait()
        None(None, None)
        return None
        with None:
            if not None:
                pass



class SimpleQueue(object):
    
    def __init__(self, *, ctx):
        (self._reader, self._writer) = connection.Pipe(duplex = False)
        self._rlock = ctx.Lock()
        self._poll = self._reader.poll
        if sys.platform == 'win32':
            self._wlock = None
            return None
        self._wlock = ctx.Lock()

    
    def close(self):
        self._reader.close()
        self._writer.close()

    
    def empty(self):
        return not self._poll()

    
    def __getstate__(self):
        context.assert_spawning(self)
        return (self._reader, self._writer, self._rlock, self._wlock)

    
    def __setstate__(self, state):
        (self._reader, self._writer, self._rlock, self._wlock) = state
        self._poll = self._reader.poll

    
    def get(self):
        self._rlock
        res = self._reader.recv_bytes()
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def put(self, obj):
        obj = _ForkingPickler.dumps(obj)
    # WARNING: Decompyle incomplete

    __class_getitem__ = classmethod(types.GenericAlias)

