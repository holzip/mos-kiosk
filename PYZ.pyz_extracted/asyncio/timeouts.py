# Source Generated with Decompyle++
# File: timeouts.pyc (Python 3.12)

import enum
from types import TracebackType
from typing import final, Optional, Type
from  import events
from  import exceptions
from  import tasks
__all__ = ('Timeout', 'timeout', 'timeout_at')

class _State(enum.Enum):
    CREATED = 'created'
    ENTERED = 'active'
    EXPIRING = 'expiring'
    EXPIRED = 'expired'
    EXITED = 'finished'

Timeout = <NODE:12>()

def timeout(delay = None):
    '''Timeout async context manager.

    Useful in cases when you want to apply timeout logic around block
    of code or in cases when asyncio.wait_for is not suitable. For example:

    >>> async with asyncio.timeout(10):  # 10 seconds timeout
    ...     await long_running_task()


    delay - value in seconds or None to disable timeout logic

    long_running_task() is interrupted by raising asyncio.CancelledError,
    the top-most affected timeout() context manager converts CancelledError
    into TimeoutError.
    '''
    loop = events.get_running_loop()
# WARNING: Decompyle incomplete


def timeout_at(when = None):
    '''Schedule the timeout at absolute time.

    Like timeout() but argument gives absolute time in the same clock system
    as loop.time().

    Please note: it is not POSIX time but a time with
    undefined starting base, e.g. the time of the system power on.

    >>> async with asyncio.timeout_at(loop.time() + 10):
    ...     await long_running_task()


    when - a deadline when timeout occurs or None to disable timeout logic

    long_running_task() is interrupted by raising asyncio.CancelledError,
    the top-most affected timeout() context manager converts CancelledError
    into TimeoutError.
    '''
    return Timeout(when)

