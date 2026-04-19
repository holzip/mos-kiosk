# Source Generated with Decompyle++
# File: futures.pyc (Python 3.12)

from __future__ import annotations
from  import events
from typing import Any, Callable
import asyncio
import contextvars
import enum

class QAsyncioFuture:
    ''' https://docs.python.org/3/library/asyncio-future.html '''
    _asyncio_future_blocking = False
    
    class FutureState(enum.Enum):
        PENDING = enum.auto()
        CANCELLED = enum.auto()
        DONE_WITH_RESULT = enum.auto()
        DONE_WITH_EXCEPTION = enum.auto()

    
    def __init__(self = None, *, loop, context):
        self
    # WARNING: Decompyle incomplete

    
    def __await__(self):
        pass
    # WARNING: Decompyle incomplete

    __iter__ = __await__
    
    def _schedule_callbacks(self = None, context = None):
        ''' A future can optionally have callbacks that are called when the future is done. '''
        for cb in self._callbacks:
            self._loop.call_soon(cb, self, context = context if context else self._context)

    
    def result(self = None):
        if self._state == QAsyncioFuture.FutureState.DONE_WITH_RESULT:
            return self._result
        if None._state == QAsyncioFuture.FutureState.DONE_WITH_EXCEPTION and self._exception:
            raise self._exception
        if self._state == QAsyncioFuture.FutureState.CANCELLED:
            if self._cancel_message:
                raise asyncio.CancelledError(self._cancel_message)
            raise asyncio.CancelledError
        raise asyncio.InvalidStateError

    
    def set_result(self = None, result = None):
        self._result = result
        self._state = QAsyncioFuture.FutureState.DONE_WITH_RESULT
        self._schedule_callbacks()

    
    def set_exception(self = None, exception = None):
        self._exception = exception
        self._state = QAsyncioFuture.FutureState.DONE_WITH_EXCEPTION
        self._schedule_callbacks()

    
    def done(self = None):
        return self._state != QAsyncioFuture.FutureState.PENDING

    
    def cancelled(self = None):
        return self._state == QAsyncioFuture.FutureState.CANCELLED

    
    def add_done_callback(self = None, cb = None, *, context):
        if self.done():
            if context:
                self._loop.call_soon(cb, self, context = context)
                return None
            None(None, None, context = self._context)
            return None
        self._callbacks.append(cb)

    
    def remove_done_callback(self = None, cb = None):
        original_len = len(self._callbacks)
    # WARNING: Decompyle incomplete

    
    def cancel(self = None, msg = None):
        if self.done():
            return False
        self._state = QAsyncioFuture.FutureState.CANCELLED
        self._cancel_message = msg
        self._schedule_callbacks()
        return True

    
    def exception(self = None):
        if self._state == QAsyncioFuture.FutureState.CANCELLED:
            raise asyncio.CancelledError
        if self.done():
            return self._exception
        raise None.InvalidStateError

    
    def get_loop(self = None):
        return self._loop


