# Source Generated with Decompyle++
# File: coroutines.pyc (Python 3.12)

__all__ = ('iscoroutinefunction', 'iscoroutine')
import collections.abc as collections
import inspect
import os
import sys
import types

def _is_debug_mode():
    if not sys.flags.dev_mode:
        sys.flags.dev_mode
        if not (sys.flags.ignore_environment):
            not (sys.flags.ignore_environment)
    return bool(os.environ.get('PYTHONASYNCIODEBUG'))

_is_coroutine = object()

def iscoroutinefunction(func):
    '''Return True if func is a decorated coroutine function.'''
    if not inspect.iscoroutinefunction(func):
        inspect.iscoroutinefunction(func)
    return getattr(func, '_is_coroutine', None) is _is_coroutine

_COROUTINE_TYPES = (types.CoroutineType, collections.abc.Coroutine)
_iscoroutine_typecache = set()

def iscoroutine(obj):
    '''Return True if obj is a coroutine object.'''
    if type(obj) in _iscoroutine_typecache:
        return True
    if isinstance(obj, _COROUTINE_TYPES):
        if len(_iscoroutine_typecache) < 100:
            _iscoroutine_typecache.add(type(obj))
        return True
    return False


def _format_coroutine(coro):
    pass
# WARNING: Decompyle incomplete

