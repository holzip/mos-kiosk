# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

from __future__ import annotations
from collections.abc import Iterable
from typing import TypeVar
_IterableT = TypeVar('_IterableT', bound = 'Iterable[str]')

def consolidate_linker_args(args = None):
    '''
    Ensure the return value is a string for backward compatibility.

    Retain until at least 2025-04-31. See pypa/distutils#246
    '''
    if not (lambda .0: pass# WARNING: Decompyle incomplete
)(args()):
        return args
    return ','.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(args())

