# Source Generated with Decompyle++
# File: resource_tracker.pyc (Python 3.12)

import os
import signal
import sys
import threading
import warnings
from  import spawn
from  import util
__all__ = [
    'ensure_running',
    'register',
    'unregister']
_HAVE_SIGMASK = hasattr(signal, 'pthread_sigmask')
_IGNORED_SIGNALS = (signal.SIGINT, signal.SIGTERM)
_CLEANUP_FUNCS = {
    'noop': (lambda : pass) }
if os.name == 'posix':
    import _multiprocessing
    import _posixshmem
    if hasattr(_multiprocessing, 'sem_unlink'):
        _CLEANUP_FUNCS.update({
            'semaphore': _multiprocessing.sem_unlink })
    _CLEANUP_FUNCS.update({
        'shared_memory': _posixshmem.shm_unlink })

class ReentrantCallError(RuntimeError):
    pass


class ResourceTracker(object):
    
    def __init__(self):
        self._lock = threading.RLock()
        self._fd = None
        self._pid = None

    
    def _reentrant_call_error(self):
        raise ReentrantCallError('Reentrant call into the multiprocessing resource tracker')

    
    def __del__(self):
        self._stop(use_blocking_lock = False)

    
    def _stop(self, use_blocking_lock = (True,)):
        if use_blocking_lock:
            self._lock
            self._stop_locked()
            None(None, None)
            return None
        acquired = self._lock.acquire(blocking = False)
        
        try:
            self._stop_locked()
            if acquired:
                self._lock.release()
                return None
            return None
            with None:
                if not None:
                    pass
            return None
        except:
            if acquired:
                self._lock.release()


    
    def _stop_locked(self, close, waitpid, waitstatus_to_exitcode = (os.close, os.waitpid, os.waitstatus_to_exitcode)):
        if self._lock._recursion_count() > 1:
            return self._reentrant_call_error()
    # WARNING: Decompyle incomplete

    
    def getfd(self):
        self.ensure_running()
        return self._fd

    
    def ensure_running(self):
        '''Make sure that resource tracker process is running.

        This can be run from any process.  Usually a child process will use
        the resource created by its parent.'''
        self._lock
        if self._lock._recursion_count() > 1:
            None(None, None)
            return 
    # WARNING: Decompyle incomplete

    
    def _check_alive(self):
        '''Check that the pipe has not been closed by sending a probe.'''
        
        try:
            os.write(self._fd, b'PROBE:0:noop\n')
            return True
        except OSError:
            return False


    
    def register(self, name, rtype):
        '''Register name of resource with resource tracker.'''
        self._send('REGISTER', name, rtype)

    
    def unregister(self, name, rtype):
        '''Unregister name of resource with resource tracker.'''
        self._send('UNREGISTER', name, rtype)

    
    def _send(self, cmd, name, rtype):
        pass
    # WARNING: Decompyle incomplete


_resource_tracker = ResourceTracker()
ensure_running = _resource_tracker.ensure_running
register = _resource_tracker.register
unregister = _resource_tracker.unregister
getfd = _resource_tracker.getfd

def main(fd):
    '''Run resource tracker.'''
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    if _HAVE_SIGMASK:
        signal.pthread_sigmask(signal.SIG_UNBLOCK, _IGNORED_SIGNALS)
    for f in (sys.stdin, sys.stdout):
        f.close()
# WARNING: Decompyle incomplete

