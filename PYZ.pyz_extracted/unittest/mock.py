# Source Generated with Decompyle++
# File: mock.pyc (Python 3.12)

__all__ = ('Mock', 'MagicMock', 'patch', 'sentinel', 'DEFAULT', 'ANY', 'call', 'create_autospec', 'AsyncMock', 'FILTER_DIR', 'NonCallableMock', 'NonCallableMagicMock', 'mock_open', 'PropertyMock', 'seal')
import asyncio
import contextlib
import io
import inspect
import pprint
import sys
import builtins
import pkgutil
from asyncio import iscoroutinefunction
from types import CodeType, ModuleType, MethodType
from unittest.util import safe_repr
from functools import wraps, partial
from threading import RLock

class InvalidSpecError(Exception):
    '''Indicates that an invalid value was used as a mock spec.'''
    pass

# WARNING: Decompyle incomplete
