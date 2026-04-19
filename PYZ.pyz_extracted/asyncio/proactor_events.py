# Source Generated with Decompyle++
# File: proactor_events.pyc (Python 3.12)

'''Event loop using a proactor and related classes.

A proactor is a "notify-on-completion" multiplexer.  Currently a
proactor is only implemented on Windows with IOCP.
'''
__all__ = ('BaseProactorEventLoop',)
import io
import os
import socket
import warnings
import signal
import threading
import collections
from  import base_events
from  import constants
from  import futures
from  import exceptions
from  import protocols
from  import sslproto
from  import transports
from  import trsock
from log import logger

def _set_socket_extra(transport, sock):
    transport._extra['socket'] = trsock.TransportSocket(sock)
    
    try:
        transport._extra['sockname'] = sock.getsockname()
        if 'peername' not in transport._extra:
            
            try:
                transport._extra['peername'] = sock.getpeername()
                return None
                return None
                except socket.error:
                    if transport._loop.get_debug():
                        logger.warning('getsockname() failed on %r', sock, exc_info = True)
                    continue
            except socket.error:
                transport._extra['peername'] = None
                return None




class _ProactorBasePipeTransport(transports.BaseTransport, transports._FlowControlMixin):
    pass
# WARNING: Decompyle incomplete


class _ProactorReadPipeTransport(transports.ReadTransport, _ProactorBasePipeTransport):
    pass
# WARNING: Decompyle incomplete


class _ProactorBaseWritePipeTransport(transports.WriteTransport, _ProactorBasePipeTransport):
    pass
# WARNING: Decompyle incomplete


class _ProactorWritePipeTransport(_ProactorBaseWritePipeTransport):
    pass
# WARNING: Decompyle incomplete


class _ProactorDatagramTransport(transports.DatagramTransport, _ProactorBasePipeTransport):
    pass
# WARNING: Decompyle incomplete


class _ProactorDuplexPipeTransport(transports.Transport, _ProactorBaseWritePipeTransport, _ProactorReadPipeTransport):
    '''Transport for duplex pipes.'''
    
    def can_write_eof(self):
        return False

    
    def write_eof(self):
        raise NotImplementedError



class _ProactorSocketTransport(transports.Transport, _ProactorBaseWritePipeTransport, _ProactorReadPipeTransport):
    pass
# WARNING: Decompyle incomplete


class BaseProactorEventLoop(base_events.BaseEventLoop):
    pass
# WARNING: Decompyle incomplete

