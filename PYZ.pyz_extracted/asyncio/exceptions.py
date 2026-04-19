# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.12)

'''asyncio exceptions.'''
__all__ = ('BrokenBarrierError', 'CancelledError', 'InvalidStateError', 'TimeoutError', 'IncompleteReadError', 'LimitOverrunError', 'SendfileNotAvailableError')

class CancelledError(BaseException):
    '''The Future or Task was cancelled.'''
    pass

TimeoutError = TimeoutError

class InvalidStateError(Exception):
    '''The operation is not allowed in this state.'''
    pass


class SendfileNotAvailableError(RuntimeError):
    '''Sendfile syscall is not available.

    Raised if OS does not support sendfile syscall for given socket or
    file type.
    '''
    pass


class IncompleteReadError(EOFError):
    pass
# WARNING: Decompyle incomplete


class LimitOverrunError(Exception):
    pass
# WARNING: Decompyle incomplete


class BrokenBarrierError(RuntimeError):
    '''Barrier is broken by barrier.abort() call.'''
    pass

