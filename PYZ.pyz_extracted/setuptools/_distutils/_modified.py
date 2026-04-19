# Source Generated with Decompyle++
# File: _modified.pyc (Python 3.12)

'''Timestamp comparison of files and groups of files.'''
from __future__ import annotations
import functools
import os.path as os
from collections.abc import Callable, Iterable
from typing import Literal, TypeVar
from jaraco.functools import splat
from compat.py39 import zip_strict
from errors import DistutilsFileError
_SourcesT = TypeVar('_SourcesT', bound = 'str | bytes | os.PathLike[str] | os.PathLike[bytes]')
_TargetsT = TypeVar('_TargetsT', bound = 'str | bytes | os.PathLike[str] | os.PathLike[bytes]')

def _newer(source, target):
    if not not os.path.exists(target):
        not os.path.exists(target)
    return os.path.getmtime(source) > os.path.getmtime(target)


def newer(source = None, target = None):
    """
    Is source modified more recently than target.

    Returns True if 'source' is modified more recently than
    'target' or if 'target' does not exist.

    Raises DistutilsFileError if 'source' does not exist.
    """
    if not os.path.exists(source):
        raise DistutilsFileError(f'''file {os.path.abspath(source)!r} does not exist''')
    return _newer(source, target)


def newer_pairwise(sources = None, targets = None, newer = None):
    """
    Filter filenames where sources are newer than targets.

    Walk two filename iterables in parallel, testing if each source is newer
    than its corresponding target.  Returns a pair of lists (sources,
    targets) where source is newer than target, according to the semantics
    of 'newer()'.
    """
    newer_pairs = filter(splat(newer), zip_strict(sources, targets))
# WARNING: Decompyle incomplete


def newer_group(sources = None, target = None, missing = None):
    '''
    Is target out-of-date with respect to any file in sources.

    Return True if \'target\' is out-of-date with respect to any file
    listed in \'sources\'. In other words, if \'target\' exists and is newer
    than every file in \'sources\', return False; otherwise return True.
    ``missing`` controls how to handle a missing source file:

    - error (default): allow the ``stat()`` call to fail.
    - ignore: silently disregard any missing source files.
    - newer: treat missing source files as "target out of date". This
      mode is handy in "dry-run" mode: it will pretend to carry out
      commands that wouldn\'t work because inputs are missing, but
      that doesn\'t matter because dry-run won\'t run the commands.
    '''
    pass
# WARNING: Decompyle incomplete

newer_pairwise_group = functools.partial(newer_pairwise, newer = newer_group)
