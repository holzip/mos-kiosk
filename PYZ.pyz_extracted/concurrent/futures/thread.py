# Source Generated with Decompyle++
# File: thread.pyc (Python 3.12)

'''Implements ThreadPoolExecutor.'''
__author__ = 'Brian Quinlan (brian@sweetapp.com)'
from concurrent.futures import _base
import itertools
import queue
import threading
import types
import weakref
import os
_threads_queues = weakref.WeakKeyDictionary()
_shutdown = False
_global_shutdown_lock = threading.Lock()

def _python_exit():
    global _shutdown
    _global_shutdown_lock
    _shutdown = True
    None(None, None)
    items = list(_threads_queues.items())
    for t, q in items:
        q.put(None)
    for t, q in items:
        t.join()
    return None
    with None:
        if not None:
            pass
    continue

threading._register_atexit(_python_exit)
if hasattr(os, 'register_at_fork'):
    os.register_at_fork(before = _global_shutdown_lock.acquire, after_in_child = _global_shutdown_lock._at_fork_reinit, after_in_parent = _global_shutdown_lock.release)
    os.register_at_fork(after_in_child = _threads_queues.clear)

class _WorkItem:
    
    def __init__(self, future, fn, args, kwargs):
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    
    def run(self):
        if not self.future.set_running_or_notify_cancel():
            return None
    # WARNING: Decompyle incomplete

    __class_getitem__ = classmethod(types.GenericAlias)


def _worker(executor_reference, work_queue, initializer, initargs):
    pass
# WARNING: Decompyle incomplete


class BrokenThreadPool(_base.BrokenExecutor):
    '''
    Raised when a worker thread in a ThreadPoolExecutor failed initializing.
    '''
    pass


class ThreadPoolExecutor(_base.Executor):
    _counter = itertools.count().__next__
    
    def __init__(self, max_workers, thread_name_prefix, initializer, initargs = (None, '', None, ())):
        '''Initializes a new ThreadPoolExecutor instance.

        Args:
            max_workers: The maximum number of threads that can be used to
                execute the given calls.
            thread_name_prefix: An optional name prefix to give our threads.
            initializer: A callable used to initialize worker threads.
            initargs: A tuple of arguments to pass to the initializer.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def submit(self, fn, *args, **kwargs):
        self._shutdown_lock
        _global_shutdown_lock
        if self._broken:
            raise BrokenThreadPool(self._broken)
        if self._shutdown:
            raise RuntimeError('cannot schedule new futures after shutdown')
        if _shutdown:
            raise RuntimeError('cannot schedule new futures after interpreter shutdown')
        f = _base.Future()
        w = _WorkItem(f, fn, args, kwargs)
        self._work_queue.put(w)
        self._adjust_thread_count()
        None(None, None)
        None(None, None)
        return 
        with None:
            if not None, f, :
                pass
        None(None, None)

    submit.__doc__ = _base.Executor.submit.__doc__
    
    def _adjust_thread_count(self):
        if self._idle_semaphore.acquire(timeout = 0):
            return None
        
        def weakref_cb(_, q = (self._work_queue,)):
            q.put(None)

        num_threads = len(self._threads)
        if num_threads < self._max_workers:
            if not self._thread_name_prefix:
                self._thread_name_prefix
            thread_name = '%s_%d' % (self, num_threads)
            t = threading.Thread(name = thread_name, target = _worker, args = (weakref.ref(self, weakref_cb), self._work_queue, self._initializer, self._initargs))
            t.start()
            self._threads.add(t)
            _threads_queues[t] = self._work_queue
            return None

    
    def _initializer_failed(self):
        self._shutdown_lock
        self._broken = 'A thread initializer failed, the thread pool is not usable anymore'
        work_item = self._work_queue.get_nowait()
    # WARNING: Decompyle incomplete

    
    def shutdown(self = None, wait = (True,), *, cancel_futures):
        self._shutdown_lock
        self._shutdown = True
    # WARNING: Decompyle incomplete

    shutdown.__doc__ = _base.Executor.shutdown.__doc__

