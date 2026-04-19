# Source Generated with Decompyle++
# File: _common.pyc (Python 3.12)

import os
import pathlib
import tempfile
import functools
import contextlib
import types
import importlib
import inspect
import warnings
import itertools
from typing import Union, Optional, cast
from abc import ResourceReader, Traversable
from _adapters import wrap_spec
Package = Union[(types.ModuleType, str)]
Anchor = Package

def package_to_anchor(func):
    """
    Replace 'package' parameter as 'anchor' and warn about the change.

    Other errors should fall through.

    >>> files('a', 'b')
    Traceback (most recent call last):
    TypeError: files() takes from 0 to 1 positional arguments but 2 were given
    """
    pass
# WARNING: Decompyle incomplete

files = (lambda anchor = None: from_package(resolve(anchor)))()

def get_resource_reader(package = None):
    """
    Return the package's loader if it's a ResourceReader.
    """
    spec = package.__spec__
    reader = getattr(spec.loader, 'get_resource_reader', None)
# WARNING: Decompyle incomplete

resolve = (lambda cand = None: cast(types.ModuleType, cand))()
_ = (lambda cand = None: importlib.import_module(cand))()
_ = (lambda cand = None: resolve(_infer_caller().f_globals['__name__']))()

def _infer_caller():
    '''
    Walk the stack and find the frame of the first caller not in this module.
    '''
    pass
# WARNING: Decompyle incomplete


def from_package(package = None):
    '''
    Return a Traversable object for the given package.

    '''
    spec = wrap_spec(package)
    reader = spec.loader.get_resource_reader(spec.name)
    return reader.files()

_tempfile = (lambda reader = contextlib.contextmanager, suffix = ('',), *, _os_remove, fd = None: pass# WARNING: Decompyle incomplete
)()

def _temp_file(path):
    return _tempfile(path.read_bytes, suffix = path.name)


def _is_present_dir(path = None):
    """
    Some Traversables implement ``is_dir()`` to raise an
    exception (i.e. ``FileNotFoundError``) when the
    directory doesn't exist. This function wraps that call
    to always return a boolean and only return True
    if there's a dir and it exists.
    """
    contextlib.suppress(FileNotFoundError)
    None(None, None)
    return 
    with None:
        if not None, path.is_dir():
            pass
    return False

as_file = (lambda path: if _is_present_dir(path):
_temp_dir(path)None(path))()
_ = (lambda path: pass# WARNING: Decompyle incomplete
)()()
_temp_path = (lambda dir = as_file.register(pathlib.Path): pass# WARNING: Decompyle incomplete
)()
_temp_dir = (lambda path: pass# WARNING: Decompyle incomplete
)()

def _write_contents(target, source):
    child = target.joinpath(source.name)
    if source.is_dir():
        child.mkdir()
        for item in source.iterdir():
            _write_contents(child, item)
        return child
    None.write_bytes(source.read_bytes())
    return child

