# Source Generated with Decompyle++
# File: forkserver.pyc (Python 3.12)

import errno
import os
import selectors
import signal
import socket
import struct
import sys
import threading
import warnings
from  import connection
from  import process
from context import reduction
from  import resource_tracker
from  import spawn
from  import util
__all__ = [
    'ensure_running',
    'get_inherited_fds',
    'connect_to_new_process',
    'set_forkserver_preload']
MAXFDS_TO_SEND = 256
SIGNED_STRUCT = struct.Struct('q')

class ForkServer(object):
    
    def __init__(self):
        self._forkserver_address = None
        self._forkserver_alive_fd = None
        self._forkserver_pid = None
        self._inherited_fds = None
        self._lock = threading.Lock()
        self._preload_modules = [
            '__main__']

    
    def _stop(self):
        self._lock
        self._stop_unlocked()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _stop_unlocked(self):
        pass
    # WARNING: Decompyle incomplete

    
    def set_forkserver_preload(self, modules_names):
        '''Set list of module names to try to load in forkserver process.'''
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(modules_names()):
            raise TypeError('module_names must be a list of strings')
        self._preload_modules = modules_names

    
    def get_inherited_fds(self):
        '''Return list of fds inherited from parent process.

        This returns None if the current process was not started by fork
        server.
        '''
        return self._inherited_fds

    
    def connect_to_new_process(self, fds):
        """Request forkserver to create a child process.

        Returns a pair of fds (status_r, data_w).  The calling process can read
        the child process's pid and (eventually) its returncode from status_r.
        The calling process should write to data_w the pickled preparation and
        process data.
        """
        self.ensure_running()
        if len(fds) + 4 >= MAXFDS_TO_SEND:
            raise ValueError('too many fds')
        client = socket.socket(socket.AF_UNIX)
        client.connect(self._forkserver_address)
        (parent_r, child_w) = os.pipe()
        (child_r, parent_w) = os.pipe()
        allfds = [
            child_r,
            child_w,
            self._forkserver_alive_fd,
            resource_tracker.getfd()]
        allfds += fds
        reduction.sendfds(client, allfds)
        os.close(child_r)
        os.close(child_w)
        None(None, None)
        return 
        None, (parent_r, parent_w)
        os.close(parent_r)
        os.close(parent_w)
        raise 
        os.close(child_r)
        os.close(child_w)
        with None:
            if not None:
                pass

    
    def ensure_running(self):
        '''Make sure that a fork server is running.

        This can be called from any process.  Note that usually a child
        process will just reuse the forkserver started by its parent, so
        ensure_running() will do nothing.
        '''
        self._lock
        resource_tracker.ensure_running()
    # WARNING: Decompyle incomplete



def main(listener_fd, alive_r, preload, main_path, sys_path = (None, None)):
    '''Run forkserver.'''
    pass
# WARNING: Decompyle incomplete


def _serve_one(child_r, fds, unused_fds, handlers):
    signal.set_wakeup_fd(-1)
    for sig, val in handlers.items():
        signal.signal(sig, val)
    for fd in unused_fds:
        os.close(fd)
# WARNING: Decompyle incomplete


def read_signed(fd):
    data = b''
    length = SIGNED_STRUCT.size
    if len(data) < length:
        s = os.read(fd, length - len(data))
        if not s:
            raise EOFError('unexpected EOF')
        data += s
        if len(data) < length:
            continue
    return SIGNED_STRUCT.unpack(data)[0]


def write_signed(fd, n):
    msg = SIGNED_STRUCT.pack(n)
    if msg:
        nbytes = os.write(fd, msg)
        if nbytes == 0:
            raise RuntimeError('should not get here')
        msg = msg[nbytes:]
        if msg:
            continue
        return None

_forkserver = ForkServer()
ensure_running = _forkserver.ensure_running
get_inherited_fds = _forkserver.get_inherited_fds
connect_to_new_process = _forkserver.connect_to_new_process
set_forkserver_preload = _forkserver.set_forkserver_preload
