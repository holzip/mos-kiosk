# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

from __future__ import annotations
from events import QAsyncioEventLoopPolicy, QAsyncioEventLoop, QAsyncioHandle, QAsyncioTimerHandle
from futures import QAsyncioFuture
from tasks import QAsyncioTask
from typing import Coroutine, Any
import asyncio
__all__ = [
    'QAsyncioEventLoopPolicy',
    'QAsyncioEventLoop',
    'QAsyncioHandle',
    'QAsyncioTimerHandle',
    'QAsyncioFuture',
    'QAsyncioTask']

def run(coro = None, keep_running = None, quit_qapp = None, *, handle_sigint, debug):
    '''
    Run the QtAsyncio event loop.

    If there is no instance of a QCoreApplication, QGuiApplication or
    QApplication yet, a new instance of QCoreApplication is created.

    :param coro:            The coroutine to run. Optional if keep_running is
                            True.
    :param keep_running:    If True, QtAsyncio (the asyncio event loop) will
                            continue running after the coroutine finished, or
                            run "forever" if no coroutine was provided.
                            If False, QtAsyncio will stop after the
                            coroutine finished. A coroutine must be provided if
                            this argument is set to False.
    :param quit_qapp:       If True, the QCoreApplication will quit when
                            QtAsyncio (the asyncio event loop) stops.
                            If False, the QCoreApplication will remain active
                            after QtAsyncio stops, and can continue to be used.
    :param handle_sigint:   If True, the SIGINT signal will be handled by the
                            event loop, causing it to stop.
    :param debug:           If True, the event loop will run in debug mode.
                            If False, the event loop will run in normal mode.
                            If None, the default behavior is used.
    '''
    default_policy = asyncio.get_event_loop_policy()
    asyncio.set_event_loop_policy(QAsyncioEventLoopPolicy(quit_qapp = quit_qapp, handle_sigint = handle_sigint))
    ret = None
    exc = None
    if keep_running:
        if coro:
            asyncio.ensure_future(coro)
        asyncio.get_event_loop().run_forever()
    elif coro:
        ret = asyncio.run(coro, debug = debug)
    else:
        exc = RuntimeError('QtAsyncio was set not to keep running after the coroutine finished, but no coroutine was provided.')
    asyncio.set_event_loop_policy(default_policy)
    if ret:
        return ret
    if None:
        raise exc

