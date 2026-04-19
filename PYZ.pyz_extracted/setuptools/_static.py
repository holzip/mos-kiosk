# Source Generated with Decompyle++
# File: _static.pyc (Python 3.12)

from functools import wraps
from typing import TypeVar
import packaging.specifiers as packaging
from warnings import SetuptoolsDeprecationWarning

class Static:
    """
    Wrapper for built-in object types that are allow setuptools to identify
    static core metadata (in opposition to ``Dynamic``, as defined :pep:`643`).

    The trick is to mark values with :class:`Static` when they come from
    ``pyproject.toml`` or ``setup.cfg``, so if any plugin overwrite the value
    with a built-in, setuptools will be able to recognise the change.

    We inherit from built-in classes, so that we don't need to change the existing
    code base to deal with the new types.
    We also should strive for immutability objects to avoid changes after the
    initial parsing.
    """
    _mutated_: bool = False


def _prevent_modification(target = None, method = None, copying = None):
    '''
    Because setuptools is very flexible we cannot fully prevent
    plugins and user customizations from modifying static values that were
    parsed from config files.
    But we can attempt to block "in-place" mutations and identify when they
    were done.
    '''
    pass
# WARNING: Decompyle incomplete


class Str(Static, str):
    pass


class Tuple(Static, tuple):
    pass


class List(Static, list):
    '''
    :meta private:
    >>> x = List([1, 2, 3])
    >>> is_static(x)
    True
    >>> x += [0]  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    SetuptoolsDeprecationWarning: Direct modification ...
    >>> is_static(x)  # no longer static after modification
    False
    >>> y = list(x)
    >>> y.clear()
    >>> y
    []
    >>> y == x
    False
    >>> is_static(List(y))
    True
    '''
    pass

for _method in ('__delitem__', '__iadd__', '__setitem__', 'append', 'clear', 'extend', 'insert', 'remove', 'reverse', 'pop'):
    _prevent_modification(List, _method, '`list(value)`')

class Dict(Static, dict):
    """
    :meta private:
    >>> x = Dict({'a': 1, 'b': 2})
    >>> is_static(x)
    True
    >>> x['c'] = 0  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    SetuptoolsDeprecationWarning: Direct modification ...
    >>> x._mutated_
    True
    >>> is_static(x)  # no longer static after modification
    False
    >>> y = dict(x)
    >>> y.popitem()
    ('b', 2)
    >>> y == x
    False
    >>> is_static(Dict(y))
    True
    """
    pass

for _method in ('__delitem__', '__ior__', '__setitem__', 'clear', 'pop', 'popitem', 'setdefault', 'update'):
    _prevent_modification(Dict, _method, '`dict(value)`')

class SpecifierSet(Static, packaging.specifiers.SpecifierSet):
    '''Not exactly a built-in type but useful for ``requires-python``'''
    pass

T = TypeVar('T')

def noop(value = None):
    '''
    >>> noop(42)
    42
    '''
    return value

_CONVERSIONS = {
    dict: Dict,
    list: List,
    tuple: Tuple,
    str: Str }

def attempt_conversion(value = None):
    '''
    >>> is_static(attempt_conversion("hello"))
    True
    >>> is_static(object())
    False
    '''
    return _CONVERSIONS.get(type(value), noop)(value)


def is_static(value = None):
    """
    >>> is_static(a := Dict({'a': 1}))
    True
    >>> is_static(dict(a))
    False
    >>> is_static(b := List([1, 2, 3]))
    True
    >>> is_static(list(b))
    False
    """
    if isinstance(value, Static):
        isinstance(value, Static)
    return not (value._mutated_)

EMPTY_LIST = List()
EMPTY_DICT = Dict()
