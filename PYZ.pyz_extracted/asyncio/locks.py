# Source Generated with Decompyle++
# File: locks.pyc (Python 3.12)

'''Synchronization primitives.'''
__all__ = ('Lock', 'Event', 'Condition', 'Semaphore', 'BoundedSemaphore', 'Barrier')
import collections
import enum
from  import exceptions
from  import mixins

class _ContextManagerMixin:
    
    async def __aenter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self, exc_type, exc, tb):
        pass
    # WARNING: Decompyle incomplete



class Lock(mixins._LoopBoundMixin, _ContextManagerMixin):
    pass
# WARNING: Decompyle incomplete


class Event(mixins._LoopBoundMixin):
    pass
# WARNING: Decompyle incomplete


class Condition(mixins._LoopBoundMixin, _ContextManagerMixin):
    pass
# WARNING: Decompyle incomplete


class Semaphore(mixins._LoopBoundMixin, _ContextManagerMixin):
    pass
# WARNING: Decompyle incomplete


class BoundedSemaphore(Semaphore):
    pass
# WARNING: Decompyle incomplete


class _BarrierState(enum.Enum):
    FILLING = 'filling'
    DRAINING = 'draining'
    RESETTING = 'resetting'
    BROKEN = 'broken'


class Barrier(mixins._LoopBoundMixin):
    pass
# WARNING: Decompyle incomplete

