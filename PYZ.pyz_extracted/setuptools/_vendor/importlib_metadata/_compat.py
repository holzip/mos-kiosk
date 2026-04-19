# Source Generated with Decompyle++
# File: _compat.pyc (Python 3.12)

import sys
import platform
__all__ = [
    'install',
    'NullFinder']

def install(cls):
    '''
    Class decorator for installation on sys.meta_path.

    Adds the backport DistributionFinder to sys.meta_path and
    attempts to disable the finder functionality of the stdlib
    DistributionFinder.
    '''
    sys.meta_path.append(cls())
    disable_stdlib_finder()
    return cls


def disable_stdlib_finder():
    '''
    Give the backport primacy for discovering path-based distributions
    by monkey-patching the stdlib O_O.

    See #91 for more background for rationale on this sketchy
    behavior.
    '''
    
    def matches(finder):
        if getattr(finder, '__module__', None) == '_frozen_importlib_external':
            getattr(finder, '__module__', None) == '_frozen_importlib_external'
        return hasattr(finder, 'find_distributions')

    for finder in filter(matches, sys.meta_path):
        del finder.find_distributions


class NullFinder:
    '''
    A "Finder" (aka "MetaPathFinder") that never finds any modules,
    but may find distributions.
    '''
    find_spec = (lambda : pass)()


def pypy_partial(val):
    '''
    Adjust for variable stacklevel on partial under PyPy.

    Workaround for #327.
    '''
    is_pypy = platform.python_implementation() == 'PyPy'
    return val + is_pypy

