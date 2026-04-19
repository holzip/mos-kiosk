# Source Generated with Decompyle++
# File: process.pyc (Python 3.12)

'''Implements ProcessPoolExecutor.

The following diagram and text describe the data-flow through the system:

|======================= In-process =====================|== Out-of-process ==|

+----------+     +----------+       +--------+     +-----------+    +---------+
|          |  => | Work Ids |       |        |     | Call Q    |    | Process |
|          |     +----------+       |        |     +-----------+    |  Pool   |
|          |     | ...      |       |        |     | ...       |    +---------+
|          |     | 6        |    => |        |  => | 5, call() | => |         |
|          |     | 7        |       |        |     | ...       |    |         |
| Process  |     | ...      |       | Local  |     +-----------+    | Process |
|  Pool    |     +----------+       | Worker |                      |  #1..n  |
| Executor |                        | Thread |                      |         |
|          |     +----------- +     |        |     +-----------+    |         |
|          | <=> | Work Items | <=> |        | <=  | Result Q  | <= |         |
|          |     +------------+     |        |     +-----------+    |         |
|          |     | 6: call()  |     |        |     | ...       |    |         |
|          |     |    future  |     |        |     | 4, result |    |         |
|          |     | ...        |     |        |     | 3, except |    |         |
+----------+     +------------+     +--------+     +-----------+    +---------+

Executor.submit() called:
- creates a uniquely numbered _WorkItem and adds it to the "Work Items" dict
- adds the id of the _WorkItem to the "Work Ids" queue

Local worker thread:
- reads work ids from the "Work Ids" queue and looks up the corresponding
  WorkItem from the "Work Items" dict: if the work item has been cancelled then
  it is simply removed from the dict, otherwise it is repackaged as a
  _CallItem and put in the "Call Q". New _CallItems are put in the "Call Q"
  until "Call Q" is full. NOTE: the size of the "Call Q" is kept small because
  calls placed in the "Call Q" can no longer be cancelled with Future.cancel().
- reads _ResultItems from "Result Q", updates the future stored in the
  "Work Items" dict and deletes the dict entry

Process #1..n:
- reads _CallItems from "Call Q", executes the calls, and puts the resulting
  _ResultItems in "Result Q"
'''
__author__ = 'Brian Quinlan (brian@sweetapp.com)'
import os
from concurrent.futures import _base
import queue
import multiprocessing as mp
import multiprocessing.connection as multiprocessing
from multiprocessing.queues import Queue
import threading
import weakref
from functools import partial
import itertools
import sys
from traceback import format_exception
_threads_wakeups = weakref.WeakKeyDictionary()
_global_shutdown = False

class _ThreadWakeup:
    
    def __init__(self):
        self._closed = False
        self._lock = threading.Lock()
        (self._reader, self._writer) = mp.Pipe(duplex = False)

    
    def close(self):
        self._lock
        if not self._closed:
            self._closed = True
            self._writer.close()
            self._reader.close()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def wakeup(self):
        self._lock
        if not self._closed:
            self._writer.send_bytes(b'')
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def clear(self):
        if self._closed:
            raise RuntimeError('operation on closed _ThreadWakeup')
        if self._reader.poll():
            self._reader.recv_bytes()
            if self._reader.poll():
                continue
            return None



def _python_exit():
    global _global_shutdown
    _global_shutdown = True
    items = list(_threads_wakeups.items())
    for _, thread_wakeup in items:
        thread_wakeup.wakeup()
    for t, _ in items:
        t.join()

threading._register_atexit(_python_exit)
EXTRA_QUEUED_CALLS = 1
_MAX_WINDOWS_WORKERS = 61

class _RemoteTraceback(Exception):
    
    def __init__(self, tb):
        self.tb = tb

    
    def __str__(self):
        return self.tb



class _ExceptionWithTraceback:
    
    def __init__(self, exc, tb):
        tb = ''.join(format_exception(type(exc), exc, tb))
        self.exc = exc
        self.exc.__traceback__ = None
        self.tb = '\n"""\n%s"""' % tb

    
    def __reduce__(self):
        return (_rebuild_exc, (self.exc, self.tb))



def _rebuild_exc(exc, tb):
    exc.__cause__ = _RemoteTraceback(tb)
    return exc


class _WorkItem(object):
    
    def __init__(self, future, fn, args, kwargs):
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs



class _ResultItem(object):
    
    def __init__(self, work_id, exception, result, exit_pid = (None, None, None)):
        self.work_id = work_id
        self.exception = exception
        self.result = result
        self.exit_pid = exit_pid



class _CallItem(object):
    
    def __init__(self, work_id, fn, args, kwargs):
        self.work_id = work_id
        self.fn = fn
        self.args = args
        self.kwargs = kwargs



class _SafeQueue(Queue):
    pass
# WARNING: Decompyle incomplete


def _get_chunks(*, chunksize, *iterables):
    ''' Iterates over zip()ed iterables in chunks. '''
    pass
# WARNING: Decompyle incomplete


def _process_chunk(fn, chunk):
    ''' Processes a chunk of an iterable passed to map.

    Runs the function passed to map() on a chunk of the
    iterable passed to map.

    This function is run in a separate process.

    '''
    pass
# WARNING: Decompyle incomplete


def _sendback_result(result_queue, work_id, result, exception, exit_pid = (None, None, None)):
    '''Safely send back the given result or exception'''
    
    try:
        result_queue.put(_ResultItem(work_id, result = result, exception = exception, exit_pid = exit_pid))
        return None
    except BaseException:
        e = None
        exc = _ExceptionWithTraceback(e, e.__traceback__)
        result_queue.put(_ResultItem(work_id, exception = exc, exit_pid = exit_pid))
        e = None
        del e
        return None
        e = None
        del e



def _process_worker(call_queue, result_queue, initializer, initargs, max_tasks = (None,)):
    '''Evaluates calls from call_queue and places the results in result_queue.

    This worker is run in a separate process.

    Args:
        call_queue: A ctx.Queue of _CallItems that will be read and
            evaluated by the worker.
        result_queue: A ctx.Queue of _ResultItems that will written
            to by the worker.
        initializer: A callable initializer, or None
        initargs: A tuple of args for the initializer
    '''
    pass
# WARNING: Decompyle incomplete


class _ExecutorManagerThread(threading.Thread):
    pass
# WARNING: Decompyle incomplete

_system_limits_checked = False
_system_limited = None

def _check_system_limits():
    global _system_limits_checked, _system_limited, _system_limited
    if _system_limits_checked and _system_limited:
        raise NotImplementedError(_system_limited)
    _system_limits_checked = True
    
    try:
        import multiprocessing.synchronize as multiprocessing
        
        try:
            nsems_max = os.sysconf('SC_SEM_NSEMS_MAX')
            if nsems_max == -1:
                return None
            if nsems_max >= 256:
                return None
            _system_limited = 'system provides too few semaphores (%d available, 256 necessary)' % nsems_max
            raise NotImplementedError(_system_limited)
            except ImportError:
                _system_limited = 'This Python build lacks multiprocessing.synchronize, usually due to named semaphores being unavailable on this platform.'
                raise NotImplementedError(_system_limited)
        except (AttributeError, ValueError):
            return None




def _chain_from_iterable_of_lists(iterable):
    '''
    Specialized implementation of itertools.chain.from_iterable.
    Each item in *iterable* should be a list.  This function is
    careful not to keep references to yielded objects.
    '''
    pass
# WARNING: Decompyle incomplete


class BrokenProcessPool(_base.BrokenExecutor):
    '''
    Raised when a process in a ProcessPoolExecutor terminated abruptly
    while a future was in the running state.
    '''
    pass


class ProcessPoolExecutor(_base.Executor):
    pass
# WARNING: Decompyle incomplete

