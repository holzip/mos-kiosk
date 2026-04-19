# Source Generated with Decompyle++
# File: utils.pyc (Python 3.12)

from __future__ import annotations
import enum
import sys
import types
import typing
import warnings
from collections.abc import Callable, Sequence

class CryptographyDeprecationWarning(UserWarning):
    pass

DeprecatedIn36 = CryptographyDeprecationWarning
DeprecatedIn40 = CryptographyDeprecationWarning
DeprecatedIn41 = CryptographyDeprecationWarning
DeprecatedIn42 = CryptographyDeprecationWarning
DeprecatedIn43 = CryptographyDeprecationWarning
DeprecatedIn46 = CryptographyDeprecationWarning

def _check_bytes(name = None, value = None):
    if not isinstance(value, bytes):
        raise TypeError(f'''{name} must be bytes''')


def _check_byteslike(name = None, value = None):
    
    try:
        memoryview(value)
        return None
    except TypeError:
        raise TypeError(f'''{name} must be bytes-like''')



def int_to_bytes(integer = None, length = None):
    if length == 0:
        raise ValueError("length argument can't be 0")
    if not length:
        length
        if not (integer.bit_length() + 7) // 8:
            (integer.bit_length() + 7) // 8
    return integer.to_bytes(1, 'big')


class InterfaceNotImplemented(Exception):
    pass


class _DeprecatedValue:
    
    def __init__(self = None, value = None, message = None, warning_class = ('value', 'object', 'message', 'str')):
        self.value = value
        self.message = message
        self.warning_class = warning_class



class _ModuleWithDeprecations(types.ModuleType):
    pass
# WARNING: Decompyle incomplete


def deprecated(value = None, module_name = None, message = None, warning_class = (None,), name = ('value', 'object', 'module_name', 'str', 'message', 'str', 'warning_class', 'type[Warning]', 'name', 'str | None', 'return', '_DeprecatedValue')):
    module = sys.modules[module_name]
    if not isinstance(module, _ModuleWithDeprecations):
        sys.modules[module_name] = _ModuleWithDeprecations(module)
        module = _ModuleWithDeprecations(module)
    dv = _DeprecatedValue(value, message, warning_class)
# WARNING: Decompyle incomplete


def cached_property(func = None):
    pass
# WARNING: Decompyle incomplete


class Enum(enum.Enum):
    
    def __repr__(self = None):
        return f'''<{self.__class__.__name__}.{self._name_}: {self._value_!r}>'''

    
    def __str__(self = None):
        return f'''{self.__class__.__name__}.{self._name_}'''


