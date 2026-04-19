# Source Generated with Decompyle++
# File: trsock.pyc (Python 3.12)

import socket

class TransportSocket:
    '''A socket-like wrapper for exposing real transport sockets.

    These objects can be safely returned by APIs like
    `transport.get_extra_info(\'socket\')`.  All potentially disruptive
    operations (like "socket.close()") are banned.
    '''
    __slots__ = ('_sock',)
    
    def __init__(self = None, sock = None):
        self._sock = sock

    family = (lambda self: self._sock.family)()
    type = (lambda self: self._sock.type)()
    proto = (lambda self: self._sock.proto)()
    
    def __repr__(self):
        s = f'''<asyncio.TransportSocket fd={self.fileno()}, family={self.family!s}, type={self.type!s}, proto={self.proto}'''
        if self.fileno() != -1:
            
            try:
                laddr = self.getsockname()
                if laddr:
                    s = f'''{s}, laddr={laddr}'''
                
                try:
                    raddr = self.getpeername()
                    if raddr:
                        s = f'''{s}, raddr={raddr}'''
                    return f'''{s}>'''
                    except socket.error:
                        continue
                except socket.error:
                    continue



    
    def __getstate__(self):
        raise TypeError('Cannot serialize asyncio.TransportSocket object')

    
    def fileno(self):
        return self._sock.fileno()

    
    def dup(self):
        return self._sock.dup()

    
    def get_inheritable(self):
        return self._sock.get_inheritable()

    
    def shutdown(self, how):
        self._sock.shutdown(how)

    
    def getsockopt(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def setsockopt(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def getpeername(self):
        return self._sock.getpeername()

    
    def getsockname(self):
        return self._sock.getsockname()

    
    def getsockbyname(self):
        return self._sock.getsockbyname()

    
    def settimeout(self, value):
        if value == 0:
            return None
        raise ValueError('settimeout(): only 0 timeout is allowed on transport sockets')

    
    def gettimeout(self):
        return 0

    
    def setblocking(self, flag):
        if not flag:
            return None
        raise ValueError('setblocking(): transport sockets cannot be blocking')


