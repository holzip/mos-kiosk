# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

'''
A Path-like interface for zipfiles.

This codebase is shared between zipfile.Path in the stdlib
and zipp in PyPI. See
https://github.com/python/importlib_metadata/wiki/Development-Methodology
for more detail.
'''
import io
import posixpath
import zipfile
import itertools
import contextlib
import pathlib
import re
from glob import translate
__all__ = [
    'Path']

def _parents(path):
    """
    Given a path with elements separated by
    posixpath.sep, generate all parents of that path.

    >>> list(_parents('b/d'))
    ['b']
    >>> list(_parents('/b/d/'))
    ['/b']
    >>> list(_parents('b/d/f/'))
    ['b/d', 'b']
    >>> list(_parents('b'))
    []
    >>> list(_parents(''))
    []
    """
    return itertools.islice(_ancestry(path), 1, None)


def _ancestry(path):
    """
    Given a path with elements separated by
    posixpath.sep, generate all elements of that path.

    >>> list(_ancestry('b/d'))
    ['b/d', 'b']
    >>> list(_ancestry('/b/d/'))
    ['/b/d', '/b']
    >>> list(_ancestry('b/d/f/'))
    ['b/d/f', 'b/d', 'b']
    >>> list(_ancestry('b'))
    ['b']
    >>> list(_ancestry(''))
    []

    Multiple separators are treated like a single.

    >>> list(_ancestry('//b//d///f//'))
    ['//b//d///f', '//b//d', '//b']
    """
    pass
# WARNING: Decompyle incomplete

_dedupe = dict.fromkeys

def _difference(minuend, subtrahend):
    '''
    Return items in minuend not in subtrahend, retaining order
    with O(1) lookup.
    '''
    return itertools.filterfalse(set(subtrahend).__contains__, minuend)


class InitializedState:
    pass
# WARNING: Decompyle incomplete


class CompleteDirs(zipfile.ZipFile, InitializedState):
    pass
# WARNING: Decompyle incomplete


class FastLookup(CompleteDirs):
    pass
# WARNING: Decompyle incomplete


def _extract_text_encoding(encoding = (None,), *args, **kwargs):
    return (io.text_encoding(encoding, 3), args, kwargs)


class Path:
    """
    A :class:`importlib.resources.abc.Traversable` interface for zip files.

    Implements many of the features users enjoy from
    :class:`pathlib.Path`.

    Consider a zip file with this structure::

        .
        ├── a.txt
        └── b
            ├── c.txt
            └── d
                └── e.txt

    >>> data = io.BytesIO()
    >>> zf = ZipFile(data, 'w')
    >>> zf.writestr('a.txt', 'content of a')
    >>> zf.writestr('b/c.txt', 'content of c')
    >>> zf.writestr('b/d/e.txt', 'content of e')
    >>> zf.filename = 'mem/abcde.zip'

    Path accepts the zipfile object itself or a filename

    >>> root = Path(zf)

    From there, several path operations are available.

    Directory iteration (including the zip file itself):

    >>> a, b = root.iterdir()
    >>> a
    Path('mem/abcde.zip', 'a.txt')
    >>> b
    Path('mem/abcde.zip', 'b/')

    name property:

    >>> b.name
    'b'

    join with divide operator:

    >>> c = b / 'c.txt'
    >>> c
    Path('mem/abcde.zip', 'b/c.txt')
    >>> c.name
    'c.txt'

    Read text:

    >>> c.read_text(encoding='utf-8')
    'content of c'

    existence:

    >>> c.exists()
    True
    >>> (b / 'missing.txt').exists()
    False

    Coercion to string:

    >>> import os
    >>> str(c).replace(os.sep, posixpath.sep)
    'mem/abcde.zip/b/c.txt'

    At the root, ``name``, ``filename``, and ``parent``
    resolve to the zipfile. Note these attributes are not
    valid and will raise a ``ValueError`` if the zipfile
    has no filename.

    >>> root.name
    'abcde.zip'
    >>> str(root.filename).replace(os.sep, posixpath.sep)
    'mem/abcde.zip'
    >>> str(root.parent)
    'mem'
    """
    __repr = '{self.__class__.__name__}({self.root.filename!r}, {self.at!r})'
    
    def __init__(self, root, at = ('',)):
        '''
        Construct a Path from a ZipFile or filename.

        Note: When the source is an existing ZipFile object,
        its type (__class__) will be mutated to a
        specialized type. If the caller wishes to retain the
        original type, the caller should either create a
        separate ZipFile object or pass a filename.
        '''
        self.root = FastLookup.make(root)
        self.at = at

    
    def __eq__(self, other):
        """
        >>> Path(zipfile.ZipFile(io.BytesIO(), 'w')) == 'foo'
        False
        """
        if self.__class__ is not other.__class__:
            return NotImplemented
        return (None.root, self.at) == (other.root, other.at)

    
    def __hash__(self):
        return hash((self.root, self.at))

    
    def open(self = None, mode = ('r',), *, pwd, *args, **kwargs):
        '''
        Open this entry as text or binary following the semantics
        of ``pathlib.Path.open()`` by passing arguments through
        to io.TextIOWrapper().
        '''
        if self.is_dir():
            raise IsADirectoryError(self)
        zip_mode = mode[0]
        if not zip_mode == 'r' and self.exists():
            raise FileNotFoundError(self)
        stream = self.root.open(self.at, zip_mode, pwd = pwd)
        if 'b' in mode:
            if args or kwargs:
                raise ValueError('encoding args invalid for binary operation')
            return stream
    # WARNING: Decompyle incomplete

    
    def _base(self):
        if not self.at:
            self.at
        return pathlib.PurePosixPath(self.root.filename)

    name = (lambda self: self._base().name)()
    suffix = (lambda self: self._base().suffix)()
    suffixes = (lambda self: self._base().suffixes)()
    stem = (lambda self: self._base().stem)()
    filename = (lambda self: pathlib.Path(self.root.filename).joinpath(self.at))()
    
    def read_text(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def read_bytes(self):
        strm = self.open('rb')
        None(None, None)
        return 
        with None:
            if not None, strm.read():
                pass

    
    def _is_child(self, path):
        return posixpath.dirname(path.at.rstrip('/')) == self.at.rstrip('/')

    
    def _next(self, at):
        return self.__class__(self.root, at)

    
    def is_dir(self):
        if not not (self.at):
            not (self.at)
        return self.at.endswith('/')

    
    def is_file(self):
        if self.exists():
            self.exists()
        return not self.is_dir()

    
    def exists(self):
        return self.at in self.root._name_set()

    
    def iterdir(self):
        if not self.is_dir():
            raise ValueError("Can't listdir a file")
        subs = map(self._next, self.root.namelist())
        return filter(self._is_child, subs)

    
    def match(self, path_pattern):
        return pathlib.PurePosixPath(self.at).match(path_pattern)

    
    def is_symlink(self):
        '''
        Return whether this path is a symlink. Always false (python/cpython#82102).
        '''
        return False

    
    def glob(self, pattern):
        if not pattern:
            raise ValueError(f'''Unacceptable pattern: {pattern!r}''')
        prefix = re.escape(self.at)
        matches = re.compile(prefix + translate(pattern)).fullmatch
        return map(self._next, filter(matches, self.root.namelist()))

    
    def rglob(self, pattern):
        return self.glob(f'''**/{pattern}''')

    
    def relative_to(self, other, *extra):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return posixpath.join(self.root.filename, self.at)

    
    def __repr__(self):
        return self.__repr.format(self = self)

    
    def joinpath(self, *other):
        pass
    # WARNING: Decompyle incomplete

    __truediv__ = joinpath
    parent = (lambda self: if not self.at:
self.filename.parentparent_at = None.dirname(self.at.rstrip('/'))if parent_at:
parent_at += '/'self._next(parent_at))()

