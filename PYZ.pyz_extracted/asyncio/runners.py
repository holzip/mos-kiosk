# Source Generated with Decompyle++
# File: runners.pyc (Python 3.12)

__all__ = ('Runner', 'run')
import contextvars
import enum
import functools
import threading
import signal
from  import coroutines
from  import events
from  import exceptions
from  import tasks
from  import constants

class _State(enum.Enum):
    CREATED = 'created'
    INITIALIZED = 'initialized'
    CLOSED = 'closed'


class Runner:
    """A context manager that controls event loop life cycle.

    The context manager always creates a new event loop,
    allows to run async functions inside it,
    and properly finalizes the loop at the context manager exit.

    If debug is True, the event loop will be run in debug mode.
    If loop_factory is passed, it is used for new event loop creation.

    asyncio.run(main(), debug=True)

    is a shortcut for

    with asyncio.Runner(debug=True) as runner:
        runner.run(main())

    The run() method can be called multiple times within the runner's context.

    This can be useful for interactive console (e.g. IPython),
    unittest runners, console tools, -- everywhere when async code
    is called from existing sync framework and where the preferred single
    asyncio.run() call doesn't work.

    """
    
    def __init__(self = None, *, debug, loop_factory):
        self._state = _State.CREATED
        self._debug = debug
        self._loop_factory = loop_factory
        self._loop = None
        self._context = None
        self._interrupt_count = 0
        self._set_event_loop = False

    
    def __enter__(self):
        self._lazy_init()
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    
    def close(self):
        '''Shutdown and close event loop.'''
        if self._state is not _State.INITIALIZED:
            return None
    # WARNING: Decompyle incomplete

    
    def get_loop(self):
        '''Return embedded event loop.'''
        self._lazy_init()
        return self._loop

    
    def run(self = None, coro = {
        'context': None }, *, context):
        '''Run a coroutine inside the embedded event loop.'''
        if not coroutines.iscoroutine(coro):
            raise ValueError('a coroutine was expected, got {!r}'.format(coro))
    # WARNING: Decompyle incomplete

    
    def _lazy_init(self):
        if self._state is _State.CLOSED:
            raise RuntimeError('Runner is closed')
        if self._state is _State.INITIALIZED:
            return None
    # WARNING: Decompyle incomplete

    
    def _on_sigint(self, signum, frame, main_task):
        if not self._interrupt_count == 1 and main_task.done():
            main_task.cancel()
            self._loop.call_soon_threadsafe((lambda : pass))
            return None
        raise KeyboardInterrupt()



def run(main = None, *, debug, loop_factory):
    """Execute the coroutine and return the result.

    This function runs the passed coroutine, taking care of
    managing the asyncio event loop, finalizing asynchronous
    generators and closing the default executor.

    This function cannot be called when another asyncio event loop is
    running in the same thread.

    If debug is True, the event loop will be run in debug mode.
    If loop_factory is passed, it is used for new event loop creation.

    This function always creates a new event loop and closes it at the end.
    It should be used as a main entry point for asyncio programs, and should
    ideally only be called once.

    The executor is given a timeout duration of 5 minutes to shutdown.
    If the executor hasn't finished within that duration, a warning is
    emitted and the executor is closed.

    Example:

        async def main():
            await asyncio.sleep(1)
            print('hello')

        asyncio.run(main())
    """
    pass
# WARNING: Decompyle incomplete


def _cancel_all_tasks(loop):
    to_cancel = tasks.all_tasks(loop)
    if not to_cancel:
        return None
    for task in to_cancel:
        task.cancel()
# WARNING: Decompyle incomplete

