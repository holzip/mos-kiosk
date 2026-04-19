# Source Generated with Decompyle++
# File: _path.pyc (Python 3.12)

from __future__ import annotations
import contextlib
import os
import sys
from typing import TYPE_CHECKING, TypeVar, Union
from more_itertools import unique_everseen
if TYPE_CHECKING:
    from typing_extensions import TypeAlias
StrPath: 'TypeAlias' = Union[(str, os.PathLike[str])]
StrPathT = TypeVar('StrPathT', bound = Union[(str, os.PathLike[str])])

def ensure_directory(path):
    '''Ensure that the parent directory of `path` exists'''
    dirname = os.path.dirname(path)
    os.makedirs(dirname, exist_ok = True)


def same_path(p1 = None, p2 = None):
    '''Differs from os.path.samefile because it does not require paths to exist.
    Purely string based (no comparison between i-nodes).
    >>> same_path("a/b", "./a/b")
    True
    >>> same_path("a/b", "a/./b")
    True
    >>> same_path("a/b", "././a/b")
    True
    >>> same_path("a/b", "./a/b/c/..")
    True
    >>> same_path("a/b", "../a/b/c")
    False
    >>> same_path("a", "a/b")
    False
    '''
    return normpath(p1) == normpath(p2)


def normpath(filename = None):
    '''Normalize a file/dir name for comparison purposes.'''
    file = os.path.abspath(filename) if sys.platform == 'cygwin' else filename
    return os.path.normcase(os.path.realpath(os.path.normpath(file)))

paths_on_pythonpath = (lambda paths: pass# WARNING: Decompyle incomplete
)()
