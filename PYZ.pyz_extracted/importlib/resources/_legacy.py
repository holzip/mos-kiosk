# Source Generated with Decompyle++
# File: _legacy.pyc (Python 3.12)

import functools
import os
import pathlib
import types
import warnings
from typing import Union, Iterable, ContextManager, BinaryIO, TextIO, Any
from  import _common
Package = Union[(types.ModuleType, str)]
Resource = str

def normalize_path(path = None):
    '''Normalize a path by ensuring it is a string.

    If the resulting string contains path separators, an exception is raised.
    '''
    str_path = str(path)
    (parent, file_name) = os.path.split(str_path)
    if parent:
        raise ValueError(f'''{path!r} must be only a file name''')
    return file_name


def open_binary(package = None, resource = None):
    '''Return a file-like object opened for binary reading of the resource.'''
    return (_common.files(package) / normalize_path(resource)).open('rb')


def read_binary(package = None, resource = None):
    '''Return the binary contents of the resource.'''
    return (_common.files(package) / normalize_path(resource)).read_bytes()


def open_text(package = None, resource = None, encoding = None, errors = ('utf-8', 'strict')):
    '''Return a file-like object opened for text reading of the resource.'''
    return (_common.files(package) / normalize_path(resource)).open('r', encoding = encoding, errors = errors)


def read_text(package = None, resource = None, encoding = None, errors = ('utf-8', 'strict')):
    '''Return the decoded string of the resource.

    The decoding-related arguments have the same semantics as those of
    bytes.decode().
    '''
    fp = open_text(package, resource, encoding, errors)
    None(None, None)
    return 
    with None:
        if not None, fp.read():
            pass


def contents(package = None):
    '''Return an iterable of entries in `package`.

    Note that not all entries are resources.  Specifically, directories are
    not considered resources.  Use `is_resource()` on each entry returned here
    to check if it is a resource or not.
    '''
    pass
# WARNING: Decompyle incomplete


def is_resource(package = None, name = None):
    '''True if `name` is a resource inside `package`.

    Directories are *not* resources.
    '''
    pass
# WARNING: Decompyle incomplete


def path(package = None, resource = None):
    '''A context manager providing a file path object to the resource.

    If the resource does not already exist on its own on the file system,
    a temporary file will be created. If the file was created, the file
    will be deleted upon exiting the context manager (no exception is
    raised if the file was deleted prior to the context manager
    exiting).
    '''
    return _common.as_file(_common.files(package) / normalize_path(resource))

