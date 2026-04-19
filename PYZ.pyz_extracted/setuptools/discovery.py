# Source Generated with Decompyle++
# File: discovery.pyc (Python 3.12)

'''Automatic discovery of Python modules and packages (for inclusion in the
distribution) and other config values.

For the purposes of this module, the following nomenclature is used:

- "src-layout": a directory representing a Python project that contains a "src"
  folder. Everything under the "src" folder is meant to be included in the
  distribution when packaging the project. Example::

    .
    ├── tox.ini
    ├── pyproject.toml
    └── src/
        └── mypkg/
            ├── __init__.py
            ├── mymodule.py
            └── my_data_file.txt

- "flat-layout": a Python project that does not use "src-layout" but instead
  have a directory under the project root for each package::

    .
    ├── tox.ini
    ├── pyproject.toml
    └── mypkg/
        ├── __init__.py
        ├── mymodule.py
        └── my_data_file.txt

- "single-module": a project that contains a single Python script direct under
  the project root (no directory used)::

    .
    ├── tox.ini
    ├── pyproject.toml
    └── mymodule.py

'''
from __future__ import annotations
import itertools
import os
from collections.abc import Iterable, Iterator, Mapping
from fnmatch import fnmatchcase
from glob import glob
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar
import _distutils_hack.override as _distutils_hack
from _path import StrPath
from distutils import log
from distutils.util import convert_path
if TYPE_CHECKING:
    from setuptools import Distribution
chain_iter = itertools.chain.from_iterable

def _valid_name(path = None):
    return os.path.basename(path).isidentifier()


class _Filter:
    '''
    Given a list of patterns, create a callable that will be true only if
    the input matches at least one of the patterns.
    '''
    
    def __init__(self = None, *patterns):
        self._patterns = dict.fromkeys(patterns)

    
    def __call__(self = None, item = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, item = None):
        return item in self._patterns



class _Finder:
    '''Base class that exposes functionality for module/package finders'''
    ALWAYS_EXCLUDE: 'ClassVar[tuple[str, ...]]' = ()
    DEFAULT_EXCLUDE: 'ClassVar[tuple[str, ...]]' = ()
    find = (lambda cls = None, where = None, exclude = classmethod, include = ('.', (), ('*',)): 