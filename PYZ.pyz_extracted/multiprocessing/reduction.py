# Source Generated with Decompyle++
# File: reduction.pyc (Python 3.12)

from abc import ABCMeta
import copyreg
import functools
import io
import os
import pickle
import socket
import sys
from  import context
__all__ = [
    'send_handle',
    'recv_handle',
    'ForkingPickler',
    'register',
    'dump']
if not sys.platform == 'win32':
    sys.platform == 'win32'
    if hasattr(socket, 'CMSG_LEN'):
        hasattr(socket, 'CMSG_LEN')
        if hasattr(socket, 'SCM_RIGHTS'):
            hasattr(socket, 'SCM_RIGHTS')
HAVE_SEND_HANDLE = hasattr(socket.socket, 'sendmsg')

class ForkingPickler(pickle.Pickler):
    pass
# WARNING: Decompyle incomplete

register = ForkingPickler.register

def dump(obj, file, protocol = (None,)):
    '''Replacement for pickle.dump() using ForkingPickler.'''
    ForkingPickler(file, protocol).dump(obj)


def _reduce_method(m):
    pass
# WARNING: Decompyle incomplete


class _C:
    
    def f(self):
        pass


register(type(_C().f), _reduce_method)

def _reduce_method_descriptor(m):
    return (getattr, (m.__objclass__, m.__name__))

register(type(list.append), _reduce_method_descriptor)
register(type(int.__add__), _reduce_method_descriptor)

def _reduce_partial(p):
    if not p.keywords:
        p.keywords
    return (_rebuild_partial, (p.func, p.args, { }))


def _rebuild_partial(func, args, keywords):
    pass
# WARNING: Decompyle incomplete

register(functools.partial, _reduce_partial)

def AbstractReducer():
    '''AbstractReducer'''
    __doc__ = 'Abstract base class for use in implementing a Reduction class\n    suitable for use in replacing the standard reduction mechanism\n    used in multiprocessing.'
    ForkingPickler = ForkingPickler
    register = register
    dump = dump
    send_handle = send_handle
    recv_handle = recv_handle
    if sys.platform == 'win32':
        steal_handle = steal_handle
        duplicate = duplicate
        DupHandle = DupHandle
    else:
        sendfds = sendfds
        recvfds = recvfds
        DupFd = DupFd
    _reduce_method = _reduce_method
    _reduce_method_descriptor = _reduce_method_descriptor
    _rebuild_partial = _rebuild_partial
    _reduce_socket = _reduce_socket
    _rebuild_socket = _rebuild_socket
    
    def __init__(self, *args):
        register(type(_C().f), _reduce_method)
        register(type(list.append), _reduce_method_descriptor)
        register(type(int.__add__), _reduce_method_descriptor)
        register(functools.partial, _reduce_partial)
        register(socket.socket, _reduce_socket)


AbstractReducer = <NODE:27>(AbstractReducer, 'AbstractReducer', metaclass = ABCMeta)
