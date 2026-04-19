# Source Generated with Decompyle++
# File: _shutil.pyc (Python 3.12)

"""Convenience layer on top of stdlib's shutil and os"""
import os
import stat
from typing import Callable, TypeVar
from compat import py311
from distutils import log

try:
    from os import chmod
    _T = TypeVar('_T')
    
    def attempt_chmod_verbose(path, mode):
        log.debug('changing mode of %s to %o', path, mode)
        
        try:
            chmod(path, mode)
            return None
        except OSError:
            e = None
            log.debug('chmod failed: %s', e)
            e = None
            del e
            return None
            e = None
            del e


    
    def _auto_chmod(func = None, arg = None, exc = None):
        '''shutils onexc callback to automatically call chmod for certain functions.'''
        if func in (os.unlink, os.remove) and os.name == 'nt':
            attempt_chmod_verbose(arg, stat.S_IWRITE)
            return func(arg)
        raise None

    
    def rmtree(path, ignore_errors, onexc = (False, _auto_chmod)):
        '''
    Similar to ``shutil.rmtree`` but automatically executes ``chmod``
    for well know Windows failure scenarios.
    '''
        return py311.shutil_rmtree(path, ignore_errors, onexc)

    
    def rmdir(path, **opts):
        pass
    # WARNING: Decompyle incomplete

    return None
except ImportError:
    
    def chmod(*args, **kwargs):
        pass

    continue

