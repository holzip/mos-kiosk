# Source Generated with Decompyle++
# File: context.pyc (Python 3.12)

from __future__ import annotations
import contextlib
import functools
import operator
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request as urllib
import warnings
from typing import Iterator
if sys.version_info < (3, 12):
    from backports import tarfile
else:
    import tarfile
pushd = (lambda dir = None: pass# WARNING: Decompyle incomplete
)()
tarball = (lambda url = None, target_dir = None: pass# WARNING: Decompyle incomplete
)()

def strip_first_component(member = None, path = None):
    (_, member.name) = member.name.split('/', 1)
    return member


def _compose(*cmgrs):
    '''
    Compose any number of dependent context managers into a single one.

    The last, innermost context manager may take arbitrary arguments, but
    each successive context manager should accept the result from the
    previous as a single parameter.

    Like :func:`jaraco.functools.compose`, behavior works from right to
    left, so the context manager should be indicated from outermost to
    innermost.

    Example, to create a context manager to change to a temporary
    directory:

    >>> temp_dir_as_cwd = _compose(pushd, temp_dir)
    >>> with temp_dir_as_cwd() as dir:
    ...     assert os.path.samefile(os.getcwd(), dir)
    '''
    
    def compose_two(inner, outer):
        pass
    # WARNING: Decompyle incomplete

    return functools.reduce(compose_two, reversed(cmgrs))

tarball_cwd = _compose(pushd, tarball)
tarball_context = (lambda : pass# WARNING: Decompyle incomplete
)()

def infer_compression(url):
    """
    Given a URL or filename, infer the compression code for tar.

    >>> infer_compression('http://foo/bar.tar.gz')
    'z'
    >>> infer_compression('http://foo/bar.tgz')
    'z'
    >>> infer_compression('file.bz')
    'j'
    >>> infer_compression('file.xz')
    'J'
    """
    warnings.warn('infer_compression is deprecated with no replacement', DeprecationWarning, stacklevel = 2)
    compression_indicator = url[-2:]
    mapping = dict(gz = 'z', bz = 'j', xz = 'J')
    return mapping.get(compression_indicator, 'z')

temp_dir = (lambda remover = (shutil.rmtree,): pass# WARNING: Decompyle incomplete
)()
repo_context = (lambda url, branch, quiet, dest_ctx = (None, True, temp_dir): pass# WARNING: Decompyle incomplete
)()

def null():
    '''
    A null context suitable to stand in for a meaningful context.

    >>> with null() as value:
    ...     assert value is None

    This context is most useful when dealing with two or more code
    branches but only some need a context. Wrap the others in a null
    context to provide symmetry across all options.
    '''
    warnings.warn('null is deprecated. Use contextlib.nullcontext', DeprecationWarning, stacklevel = 2)
    return contextlib.nullcontext()


class ExceptionTrap:
    '''
    A context manager that will catch certain exceptions and provide an
    indication they occurred.

    >>> with ExceptionTrap() as trap:
    ...     raise Exception()
    >>> bool(trap)
    True

    >>> with ExceptionTrap() as trap:
    ...     pass
    >>> bool(trap)
    False

    >>> with ExceptionTrap(ValueError) as trap:
    ...     raise ValueError("1 + 1 is not 3")
    >>> bool(trap)
    True
    >>> trap.value
    ValueError(\'1 + 1 is not 3\')
    >>> trap.tb
    <traceback object at ...>

    >>> with ExceptionTrap(ValueError) as trap:
    ...     raise Exception()
    Traceback (most recent call last):
    ...
    Exception

    >>> bool(trap)
    False
    '''
    exc_info = (None, None, None)
    
    def __init__(self, exceptions = ((Exception,),)):
        self.exceptions = exceptions

    
    def __enter__(self):
        return self

    type = (lambda self: self.exc_info[0])()
    value = (lambda self: self.exc_info[1])()
    tb = (lambda self: self.exc_info[2])()
    
    def __exit__(self, *exc_info):
        type = exc_info[0]
        if type:
            type
        matches = issubclass(type, self.exceptions)
        if matches:
            self.exc_info = exc_info
        return matches

    
    def __bool__(self):
        return bool(self.type)

    
    def raises(self = property, func = {
        '_test': bool }, *, _test):
        """
        Wrap func and replace the result with the truth
        value of the trap (True if an exception occurred).

        First, give the decorator an alias to support Python 3.8
        Syntax.

        >>> raises = ExceptionTrap(ValueError).raises

        Now decorate a function that always fails.

        >>> @raises
        ... def fail():
        ...     raise ValueError('failed')
        >>> fail()
        True
        """
        pass
    # WARNING: Decompyle incomplete

    
    def passes(self, func):
        """
        Wrap func and replace the result with the truth
        value of the trap (True if no exception).

        First, give the decorator an alias to support Python 3.8
        Syntax.

        >>> passes = ExceptionTrap(ValueError).passes

        Now decorate a function that always fails.

        >>> @passes
        ... def fail():
        ...     raise ValueError('failed')

        >>> fail()
        False
        """
        return self.raises(func, _test = operator.not_)



class suppress(contextlib.ContextDecorator, contextlib.suppress):
    """
    A version of contextlib.suppress with decorator support.

    >>> @suppress(KeyError)
    ... def key_error():
    ...     {}['']
    >>> key_error()
    """
    pass


class on_interrupt(contextlib.ContextDecorator):
    """
    Replace a KeyboardInterrupt with SystemExit(1)

    >>> def do_interrupt():
    ...     raise KeyboardInterrupt()
    >>> on_interrupt('error')(do_interrupt)()
    Traceback (most recent call last):
    ...
    SystemExit: 1
    >>> on_interrupt('error', code=255)(do_interrupt)()
    Traceback (most recent call last):
    ...
    SystemExit: 255
    >>> on_interrupt('suppress')(do_interrupt)()
    >>> with __import__('pytest').raises(KeyboardInterrupt):
    ...     on_interrupt('ignore')(do_interrupt)()
    """
    
    def __init__(self, action, code = ('error', 1)):
        self.action = action
        self.code = code

    
    def __enter__(self):
        return self

    
    def __exit__(self, exctype, excinst, exctb):
        if exctype is not KeyboardInterrupt or self.action == 'ignore':
            return None
        if self.action == 'error':
            raise SystemExit(self.code), excinst
        return self.action == 'suppress'


