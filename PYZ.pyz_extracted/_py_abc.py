# Source Generated with Decompyle++
# File: _py_abc.pyc (Python 3.12)

from _weakrefset import WeakSet

def get_cache_token():
    '''Returns the current ABC cache token.

    The token is an opaque object (supporting equality testing) identifying the
    current version of the ABC cache for virtual subclasses. The token changes
    with every call to ``register()`` on any ABC.
    '''
    return ABCMeta._abc_invalidation_counter


class ABCMeta(type):
    pass
# WARNING: Decompyle incomplete

