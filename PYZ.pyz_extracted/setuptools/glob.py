# Source Generated with Decompyle++
# File: glob.pyc (Python 3.12)

'''
Filename globbing utility. Mostly a copy of `glob` from Python 3.5.

Changes include:
 * `yield from` and PEP3102 `*` removed.
 * Hidden files are not ignored.
'''
from __future__ import annotations
import fnmatch
import os
import re
from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING, AnyStr, overload
if TYPE_CHECKING:
    from _typeshed import BytesPath, StrOrBytesPath, StrPath
__all__ = [
    'glob',
    'iglob',
    'escape']

def glob(pathname = None, recursive = None):
    """Return a list of paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    return list(iglob(pathname, recursive = recursive))


def iglob(pathname = None, recursive = None):
    """Return an iterator which yields the paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    it = _iglob(pathname, recursive)
# WARNING: Decompyle incomplete


def _iglob(pathname = None, recursive = None):
    pass
# WARNING: Decompyle incomplete

glob1 = (lambda dirname = None, pattern = None: pass)()
glob1 = (lambda dirname = None, pattern = None: pass)()

def glob1(dirname = None, pattern = None):
    if not dirname:
        if isinstance(pattern, bytes):
            dirname = os.curdir.encode('ASCII')
        else:
            dirname = os.curdir
    
    try:
        names = os.listdir(dirname)
        return fnmatch.filter(names, pattern)
    except OSError:
        return 



def glob0(dirname, basename):
    if not basename:
        if os.path.isdir(dirname):
            return [
                basename]
        return None
    if None.path.lexists(os.path.join(dirname, basename)):
        return [
            basename]

glob2 = (lambda dirname = None, pattern = None: pass)()
glob2 = (lambda dirname = None, pattern = None: pass)()

def glob2(dirname = None, pattern = None):
    pass
# WARNING: Decompyle incomplete

_rlistdir = (lambda dirname = None: pass)()
_rlistdir = (lambda dirname = None: pass)()

def _rlistdir(dirname = None):
    pass
# WARNING: Decompyle incomplete

magic_check = re.compile('([*?[])')
magic_check_bytes = re.compile(b'([*?[])')

def has_magic(s = None):
    if isinstance(s, bytes):
        return magic_check_bytes.search(s) is not None
    return None.search(s) is not None


def _isrecursive(pattern = None):
    if isinstance(pattern, bytes):
        return pattern == b'**'
    return None == '**'


def escape(pathname):
    '''Escape all special characters.'''
    (drive, pathname) = os.path.splitdrive(pathname)
    if isinstance(pathname, bytes):
        pathname = magic_check_bytes.sub(b'[\\1]', pathname)
        return drive + pathname
    pathname = None.sub('[\\1]', pathname)
    return drive + pathname

