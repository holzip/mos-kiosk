# Source Generated with Decompyle++
# File: futures.pyc (Python 3.12)

'''A Future class similar to the one in PEP 3148.'''
__all__ = ('Future', 'wrap_future', 'isfuture')
import concurrent.futures as concurrent
import contextvars
import logging
import sys
from types import GenericAlias
from  import base_futures
from  import events
from  import exceptions
from  import format_helpers
isfuture = base_futures.isfuture
_PENDING = base_futures._PENDING
_CANCELLED = base_futures._CANCELLED
_FINISHED = base_futures._FINISHED
STACK_DEBUG = logging.DEBUG - 1

class Future:
    """This class is *almost* compatible with concurrent.futures.Future.

    Differences:

    - This class is not thread-safe.

    - result() and exception() do not take a timeout argument and
      raise an exception when the future isn't done yet.

    - Callbacks registered with add_done_callback() are always called
      via the event loop's call_soon().

    - This class is not compatible with the wait() and as_completed()
      methods in the concurrent.futures package.

    (In Python 3.4 or later we may be able to unify the implementations.)
    """
    _state = _PENDING
    _result = None
    _exception = None
    _loop = None
    _source_traceback = None
    _cancel_message = None
    _cancelled_exc = None
    _asyncio_future_blocking = False
    __log_traceback = False
    
    def __init__(self = None, *, loop):
        """Initialize the future.

        The optional event_loop argument allows explicitly setting the event
        loop object used by the future. If it's not provided, the future uses
        the default event loop.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return base_futures._future_repr(self)

    
    def __del__(self):
        if not self.__log_traceback:
            return None
        exc = self._exception
        context = {
            'message': f'''{self.__class__.__name__} exception was never retrieved''',
            'exception': exc,
            'future': self }
        if self._source_traceback:
            context['source_traceback'] = self._source_traceback
        self._loop.call_exception_handler(context)

    __class_getitem__ = classmethod(GenericAlias)
    _log_traceback = (lambda self: self.__log_traceback)()
    _log_traceback = (lambda self, val: if val:
raise ValueError('_log_traceback can only be set to False')self.__log_traceback = False)()
    
    def get_loop(self):
        '''Return the event loop the Future is bound to.'''
        loop = self._loop
    # WARNING: Decompyle incomplete

    
    def _make_cancelled_error(self):
        '''Create the CancelledError to raise if the Future is cancelled.

        This should only be called once when handling a cancellation since
        it erases the saved context exception value.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def cancel(self, msg = (None,)):
        """Cancel the future and schedule callbacks.

        If the future is already done or cancelled, return False.  Otherwise,
        change the future's state to cancelled, schedule the callbacks and
        return True.
        """
        self.__log_traceback = False
        if self._state != _PENDING:
            return False
        self._state = _CANCELLED
        self._cancel_message = msg
        self.__schedule_callbacks()
        return True

    
    def __schedule_callbacks(self):
        '''Internal: Ask the event loop to call all callbacks.

        The callbacks are scheduled to be called as soon as possible. Also
        clears the callback list.
        '''
        callbacks = self._callbacks[:]
        if not callbacks:
            return None
        self._callbacks[:] = []
        for callback, ctx in callbacks:
            self._loop.call_soon(callback, self, context = ctx)

    
    def cancelled(self):
        '''Return True if the future was cancelled.'''
        return self._state == _CANCELLED

    
    def done(self):
        '''Return True if the future is done.

        Done means either that a result / exception are available, or that the
        future was cancelled.
        '''
        return self._state != _PENDING

    
    def result(self):
        """Return the result this future represents.

        If the future has been cancelled, raises CancelledError.  If the
        future's result isn't yet available, raises InvalidStateError.  If
        the future is done and has an exception set, this exception is raised.
        """
        if self._state == _CANCELLED:
            raise self._make_cancelled_error()
        if self._state != _FINISHED:
            raise exceptions.InvalidStateError('Result is not ready.')
        self.__log_traceback = False
    # WARNING: Decompyle incomplete

    
    def exception(self):
        """Return the exception that was set on this future.

        The exception (or None if no exception was set) is returned only if
        the future is done.  If the future has been cancelled, raises
        CancelledError.  If the future isn't done yet, raises
        InvalidStateError.
        """
        if self._state == _CANCELLED:
            raise self._make_cancelled_error()
        if self._state != _FINISHED:
            raise exceptions.InvalidStateError('Exception is not set.')
        self.__log_traceback = False
        return self._exception

    
    def add_done_callback(self = _log_traceback.setter, fn = {
        'context': None }, *, context):
        '''Add a callback to be run when the future becomes done.

        The callback is called with a single argument - the future object. If
        the future is already done when this is called, the callback is
        scheduled with call_soon.
        '''
        if self._state != _PENDING:
            self._loop.call_soon(fn, self, context = context)
            return None
    # WARNING: Decompyle incomplete

    
    def remove_done_callback(self, fn):
        '''Remove all instances of a callback from the "call when done" list.

        Returns the number of callbacks removed.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_result(self, result):
        '''Mark the future done and set its result.

        If the future is already done when this method is called, raises
        InvalidStateError.
        '''
        if self._state != _PENDING:
            raise exceptions.InvalidStateError(f'''{self._state}: {self!r}''')
        self._result = result
        self._state = _FINISHED
        self.__schedule_callbacks()

    
    def set_exception(self, exception):
        '''Mark the future done and set an exception.

        If the future is already done when this method is called, raises
        InvalidStateError.
        '''
        if self._state != _PENDING:
            raise exceptions.InvalidStateError(f'''{self._state}: {self!r}''')
        if isinstance(exception, type):
            exception = exception()
        if isinstance(exception, StopIteration):
            new_exc = RuntimeError('StopIteration interacts badly with generators and cannot be raised into a Future')
            new_exc.__cause__ = exception
            new_exc.__context__ = exception
            exception = new_exc
        self._exception = exception
        self._exception_tb = exception.__traceback__
        self._state = _FINISHED
        self.__schedule_callbacks()
        self.__log_traceback = True

    
    def __await__(self):
        pass
    # WARNING: Decompyle incomplete

    __iter__ = __await__

_PyFuture = Future

def _get_loop(fut):
    
    try:
        get_loop = fut.get_loop
        return get_loop()
    except AttributeError:
        return fut._loop



def _set_result_unless_cancelled(fut, result):
    '''Helper setting the result only if the future was not cancelled.'''
    if fut.cancelled():
        return None
    fut.set_result(result)


def _convert_future_exc(exc):
    exc_class = type(exc)
# WARNING: Decompyle incomplete


def _set_concurrent_future_state(concurrent, source):
    '''Copy state from a future to a concurrent.futures.Future.'''
    pass
# WARNING: Decompyle incomplete


def _copy_future_state(source, dest):
    '''Internal helper to copy state from another Future.

    The other Future may be a concurrent.futures.Future.
    '''
    pass
# WARNING: Decompyle incomplete


def _chain_future(source, destination):
    '''Chain two futures so that when one completes, so does the other.

    The result (or exception) of source will be copied to destination.
    If destination is cancelled, source gets cancelled too.
    Compatible with both asyncio.Future and concurrent.futures.Future.
    '''
    pass
# WARNING: Decompyle incomplete


def wrap_future(future = None, *, loop):
    '''Wrap concurrent.futures.Future object.'''
    if isfuture(future):
        return future
# WARNING: Decompyle incomplete


try:
    import _asyncio
    Future = _asyncio.Future
    _CFuture = _asyncio.Future
    return None
except ImportError:
    return None

