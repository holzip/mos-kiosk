# Source Generated with Decompyle++
# File: windows_utils.pyc (Python 3.12)

'''Various Windows specific bits and pieces.'''
import sys
if sys.platform != 'win32':
    raise ImportError('win32 only')
import _winapi
import itertools
import msvcrt
import os
import subprocess
import tempfile
import warnings
__all__ = ('pipe', 'Popen', 'PIPE', 'PipeHandle')
BUFSIZE = 8192
PIPE = subprocess.PIPE
STDOUT = subprocess.STDOUT
_mmap_counter = itertools.count()

def pipe(*, duplex, overlapped, bufsize):
    '''Like os.pipe() but with overlapped support and using handles not fds.'''
    address = tempfile.mktemp(prefix = '\\\\.\\pipe\\python-pipe-{:d}-{:d}-'.format(os.getpid(), next(_mmap_counter)))
    if duplex:
        openmode = _winapi.PIPE_ACCESS_DUPLEX
        access = _winapi.GENERIC_READ | _winapi.GENERIC_WRITE
        ibsize = bufsize
        obsize = bufsize
    else:
        openmode = _winapi.PIPE_ACCESS_INBOUND
        access = _winapi.GENERIC_WRITE
        ibsize = bufsize
        obsize = 0
    openmode |= _winapi.FILE_FLAG_FIRST_PIPE_INSTANCE
    if overlapped[0]:
        openmode |= _winapi.FILE_FLAG_OVERLAPPED
    if overlapped[1]:
        flags_and_attribs = _winapi.FILE_FLAG_OVERLAPPED
    else:
        flags_and_attribs = 0
    h1 = None
    h2 = None
# WARNING: Decompyle incomplete


class PipeHandle:
    '''Wrapper for an overlapped pipe handle which is vaguely file-object like.

    The IOCP event loop can use these instead of socket objects.
    '''
    
    def __init__(self, handle):
        self._handle = handle

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    handle = (lambda self: self._handle)()
    
    def fileno(self):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = property, *, CloseHandle):
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self, _warn = (warnings.warn,)):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self):
        return self

    
    def __exit__(self, t, v, tb):
        self.close()



class Popen(subprocess.Popen):
    pass
# WARNING: Decompyle incomplete

