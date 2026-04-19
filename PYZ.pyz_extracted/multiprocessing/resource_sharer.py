# Source Generated with Decompyle++
# File: resource_sharer.pyc (Python 3.12)

import os
import signal
import socket
import sys
import threading
from  import process
from context import reduction
from  import util
__all__ = [
    'stop']

class _ResourceSharer(object):
    '''Manager for resources using background thread.'''
    
    def __init__(self):
        self._key = 0
        self._cache = { }
        self._lock = threading.Lock()
        self._listener = None
        self._address = None
        self._thread = None
        util.register_after_fork(self, _ResourceSharer._afterfork)

    
    def register(self, send, close):
        '''Register resource, returning an identifier.'''
        self._lock
    # WARNING: Decompyle incomplete

    get_connection = (lambda ident: Client = Clientimport connection(address, key) = identc = Client(address, authkey = process.current_process().authkey)c.send((key, os.getpid()))c)()
    
    def stop(self, timeout = (None,)):
        '''Stop the background thread and clear registered resources.'''
        Client = Client
        import connection
        self._lock
    # WARNING: Decompyle incomplete

    
    def _afterfork(self):
        for send, close in self._cache.items():
            close()
        self._cache.clear()
        self._lock._at_fork_reinit()
    # WARNING: Decompyle incomplete

    
    def _start(self):
        Listener = Listener
        import connection
    # WARNING: Decompyle incomplete

    
    def _serve(self):
        if hasattr(signal, 'pthread_sigmask'):
            signal.pthread_sigmask(signal.SIG_BLOCK, signal.valid_signals())
    # WARNING: Decompyle incomplete


_resource_sharer = _ResourceSharer()
stop = _resource_sharer.stop
