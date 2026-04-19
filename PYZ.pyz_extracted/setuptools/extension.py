# Source Generated with Decompyle++
# File: extension.pyc (Python 3.12)

from __future__ import annotations
import functools
import re
from typing import TYPE_CHECKING
from setuptools._path import StrPath
from monkey import get_unpatched
import distutils.core as distutils
import distutils.errors as distutils
import distutils.extension as distutils

def _have_cython():
    '''
    Return True if Cython can be imported.
    '''
    cython_impl = 'Cython.Distutils.build_ext'
    
    try:
        __import__(cython_impl, fromlist = [
            'build_ext']).build_ext
        return True
    except Exception:
        return False


have_pyrex = _have_cython
if TYPE_CHECKING:
    from distutils.core import Extension as _Extension
else:
    _Extension = get_unpatched(distutils.core.Extension)

class Extension(_Extension):
    pass
# WARNING: Decompyle incomplete


class Library(Extension):
    '''Just like a regular Extension, but built as a library instead'''
    pass

