# Source Generated with Decompyle++
# File: connection.pyc (Python 3.12)

__all__ = [
    'Client',
    'Listener',
    'Pipe',
    'wait']
import errno
import io
import os
import sys
import socket
import struct
import time
import tempfile
import itertools
import _multiprocessing
from  import util
from  import AuthenticationError, BufferTooShort
from context import reduction
_ForkingPickler = reduction.ForkingPickler

try:
    import _winapi
    from _winapi import WAIT_OBJECT_0, WAIT_ABANDONED_0, WAIT_TIMEOUT, INFINITE
    BUFSIZE = 8192
    CONNECTION_TIMEOUT = 20
    _mmap_counter = itertools.count()
    default_family = 'AF_INET'
    families = [
        'AF_INET']
    if hasattr(socket, 'AF_UNIX'):
        default_family = 'AF_UNIX'
        families += [
            'AF_UNIX']
    if sys.platform == 'win32':
        default_family = 'AF_PIPE'
        families += [
            'AF_PIPE']
    
    def _init_timeout(timeout = (CONNECTION_TIMEOUT,)):
        return time.monotonic() + timeout

    
    def _check_timeout(t):
        return time.monotonic() > t

    
    def arbitrary_address(family):
        '''
    Return an arbitrary free address for the given family
    '''
        if family == 'AF_INET':
            return ('localhost', 0)
        if family == 'AF_UNIX':
            return tempfile.mktemp(prefix = 'listener-', dir = util.get_temp_dir())
        if None == 'AF_PIPE':
            return tempfile.mktemp(prefix = '\\\\.\\pipe\\pyc-%d-%d-' % (os.getpid(), next(_mmap_counter)), dir = '')
        raise None('unrecognized family')

    
    def _validate_family(family):
        '''
    Checks if the family is valid for the current environment.
    '''
        if sys.platform != 'win32' and family == 'AF_PIPE':
            raise ValueError('Family %s is not recognized.' % family)
        if sys.platform == 'win32':
            if family == 'AF_UNIX':
                if not hasattr(socket, family):
                    raise ValueError('Family %s is not recognized.' % family)
                return None
            return None

    
    def address_type(address):
        """
    Return the types of the address

    This can be 'AF_INET', 'AF_UNIX', or 'AF_PIPE'
    """
        if type(address) == tuple:
            return 'AF_INET'
        if type(address) is str and address.startswith('\\\\'):
            return 'AF_PIPE'
        if type(address) is str or util.is_abstract_socket_namespace(address):
            return 'AF_UNIX'
        raise ValueError('address type of %r unrecognized' % address)

    
    class _ConnectionBase:
        _handle = None
        
        def __init__(self, handle, readable, writable = (True, True)):
            handle = handle.__index__()
            if handle < 0:
                raise ValueError('invalid handle')
            if not readable and writable:
                raise ValueError('at least one of `readable` and `writable` must be True')
            self._handle = handle
            self._readable = readable
            self._writable = writable

        
        def __del__(self):
            pass
        # WARNING: Decompyle incomplete

        
        def _check_closed(self):
            pass
        # WARNING: Decompyle incomplete

        
        def _check_readable(self):
            if not self._readable:
                raise OSError('connection is write-only')

        
        def _check_writable(self):
            if not self._writable:
                raise OSError('connection is read-only')

        
        def _bad_message_length(self):
            if self._writable:
                self._readable = False
                raise OSError('bad message length')
            self.close()
            raise OSError('bad message length')

        closed = (lambda self: self._handle is None)()
        readable = (lambda self: self._readable)()
        writable = (lambda self: self._writable)()
        
        def fileno(self):
            '''File descriptor or handle of the connection'''
            self._check_closed()
            return self._handle

        
        def close(self):
            '''Close the connection'''
            pass
        # WARNING: Decompyle incomplete

        
        def send_bytes(self, buf, offset, size = (0, None)):
            '''Send the bytes data from a bytes-like object'''
            self._check_closed()
            self._check_writable()
            m = memoryview(buf)
            if m.itemsize > 1:
                m = m.cast('B')
            n = m.nbytes
            if offset < 0:
                raise ValueError('offset is negative')
            if n < offset:
                raise ValueError('buffer length < offset')
        # WARNING: Decompyle incomplete

        
        def send(self, obj):
            '''Send a (picklable) object'''
            self._check_closed()
            self._check_writable()
            self._send_bytes(_ForkingPickler.dumps(obj))

        
        def recv_bytes(self, maxlength = (None,)):
            '''
        Receive bytes data as a bytes object.
        '''
            self._check_closed()
            self._check_readable()
        # WARNING: Decompyle incomplete

        
        def recv_bytes_into(self, buf, offset = (0,)):
            '''
        Receive bytes data into a writeable bytes-like object.
        Return the number of bytes read.
        '''
            self._check_closed()
            self._check_readable()
            m = memoryview(buf)
            itemsize = m.itemsize
            bytesize = itemsize * len(m)
            if offset < 0:
                raise ValueError('negative offset')
            if offset > bytesize:
                raise ValueError('offset too large')
            result = self._recv_bytes()
            size = result.tell()
            if bytesize < offset + size:
                raise BufferTooShort(result.getvalue())
            result.seek(0)
            result.readinto(m[offset // itemsize:(offset + size) // itemsize])
            None(None, None)
            return 
            with None:
                if not None, size:
                    pass

        
        def recv(self):
            '''Receive a (picklable) object'''
            self._check_closed()
            self._check_readable()
            buf = self._recv_bytes()
            return _ForkingPickler.loads(buf.getbuffer())

        
        def poll(self, timeout = (0,)):
            '''Whether there is any input available to be read'''
            self._check_closed()
            self._check_readable()
            return self._poll(timeout)

        
        def __enter__(self):
            return self

        
        def __exit__(self, exc_type, exc_value, exc_tb):
            self.close()


    if _winapi:
        
        class PipeConnection(_ConnectionBase):
            '''
        Connection class based on a Windows named pipe.
        Overlapped I/O is used, so the handles must have been created
        with FILE_FLAG_OVERLAPPED.
        '''
            _got_empty_message = False
            _send_ov = None
            
            def _close(self, _CloseHandle = (_winapi.CloseHandle,)):
                ov = self._send_ov
            # WARNING: Decompyle incomplete

            
            def _send_bytes(self, buf):
                pass
            # WARNING: Decompyle incomplete

            
            def _recv_bytes(self, maxsize = (None,)):
                if self._got_empty_message:
                    self._got_empty_message = False
                    return io.BytesIO()
            # WARNING: Decompyle incomplete

            
            def _poll(self, timeout):
                if self._got_empty_message or _winapi.PeekNamedPipe(self._handle)[0] != 0:
                    return True
                return bool(wait([
                    self], timeout))

            
            def _get_more_data(self, ov, maxsize):
                buf = ov.getbuffer()
                f = io.BytesIO()
                f.write(buf)
                left = _winapi.PeekNamedPipe(self._handle)[1]
            # WARNING: Decompyle incomplete


    
    class Connection(_ConnectionBase):
        '''
    Connection class based on an arbitrary file descriptor (Unix only), or
    a socket handle (Windows).
    '''
        if _winapi:
            
            def _close(self, _close = (_multiprocessing.closesocket,)):
                _close(self._handle)

            _write = _multiprocessing.send
            _read = _multiprocessing.recv
        else:
            
            def _close(self, _close = (os.close,)):
                _close(self._handle)

            _write = os.write
            _read = os.read
        
        def _send(self, buf, write = (_write,)):
            remaining = len(buf)
            n = write(self._handle, buf)
            remaining -= n
            if remaining == 0:
                return None
            buf = buf[n:]
            continue

        
        def _recv(self, size, read = (_read,)):
            buf = io.BytesIO()
            handle = self._handle
            remaining = size
            if remaining > 0:
                chunk = read(handle, remaining)
                n = len(chunk)
                if n == 0:
                    if remaining == size:
                        raise EOFError
                    raise OSError('got end of file during message')
                buf.write(chunk)
                remaining -= n
                if remaining > 0:
                    continue
            return buf

        
        def _send_bytes(self, buf):
            n = len(buf)
            if n > 2147483647:
                pre_header = struct.pack('!i', -1)
                header = struct.pack('!Q', n)
                self._send(pre_header)
                self._send(header)
                self._send(buf)
                return None
            header = struct.pack('!i', n)
            if n > 16384:
                self._send(header)
                self._send(buf)
                return None
            self._send(header + buf)

        
        def _recv_bytes(self, maxsize = (None,)):
            buf = self._recv(4)
            (size,) = struct.unpack('!i', buf.getvalue())
            if size == -1:
                buf = self._recv(8)
                (size,) = struct.unpack('!Q', buf.getvalue())
        # WARNING: Decompyle incomplete

        
        def _poll(self, timeout):
            r = wait([
                self], timeout)
            return bool(r)


    
    class Listener(object):
        """
    Returns a listener object.

    This is a wrapper for a bound socket which is 'listening' for
    connections, or for a Windows named pipe.
    """
        
        def __init__(self, address, family, backlog, authkey = (None, None, 1, None)):
            if not family:
                family
                if address:
                    address
                if not address_type(address):
                    address_type(address)
            family = default_family
            if not address:
                address
            address = arbitrary_address(family)
            _validate_family(family)
            if family == 'AF_PIPE':
                self._listener = PipeListener(address, backlog)
            else:
                self._listener = SocketListener(address, family, backlog)
        # WARNING: Decompyle incomplete

        
        def accept(self):
            '''
        Accept a connection on the bound socket or named pipe of `self`.

        Returns a `Connection` object.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        def close(self):
            '''
        Close the bound socket or named pipe of `self`.
        '''
            listener = self._listener
        # WARNING: Decompyle incomplete

        address = (lambda self: self._listener._address)()
        last_accepted = (lambda self: self._listener._last_accepted)()
        
        def __enter__(self):
            return self

        
        def __exit__(self, exc_type, exc_value, exc_tb):
            self.close()


    
    def Client(address, family, authkey = (None, None)):
        '''
    Returns a connection to the address of a `Listener`
    '''
        if not family:
            family
        family = address_type(address)
        _validate_family(family)
        if family == 'AF_PIPE':
            c = PipeClient(address)
        else:
            c = SocketClient(address)
    # WARNING: Decompyle incomplete

    
    class SocketListener(object):
        '''
    Representation of a socket which is bound to an address and listening
    '''
        
        def __init__(self, address, family, backlog = (1,)):
            self._socket = socket.socket(getattr(socket, family))
            
            try:
                if os.name == 'posix':
                    self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self._socket.setblocking(True)
                self._socket.bind(address)
                self._socket.listen(backlog)
                self._address = self._socket.getsockname()
                self._family = family
                self._last_accepted = None
                if not family == 'AF_UNIX' and util.is_abstract_socket_namespace(address):
                    self._unlink = util.Finalize(self, os.unlink, args = (address,), exitpriority = 0)
                    return None
                self._unlink = None
                return None
            except OSError:
                self._socket.close()
                raise 


        
        def accept(self):
            (s, self._last_accepted) = self._socket.accept()
            s.setblocking(True)
            return Connection(s.detach())

        
        def close(self):
            pass
        # WARNING: Decompyle incomplete


    
    def SocketClient(address):
        '''
    Return a connection object connected to the socket given by `address`
    '''
        family = address_type(address)
        s = socket.socket(getattr(socket, family))
        s.setblocking(True)
        s.connect(address)
        None(None, None)
        return 
        with None:
            if not None, Connection(s.detach()):
                pass

    if sys.platform == 'win32':
        
        class PipeListener(object):
            '''
        Representation of a named pipe
        '''
            
            def __init__(self, address, backlog = (None,)):
                self._address = address
                self._handle_queue = [
                    self._new_handle(first = True)]
                self._last_accepted = None
                util.sub_debug('listener created with address=%r', self._address)
                self.close = util.Finalize(self, PipeListener._finalize_pipe_listener, args = (self._handle_queue, self._address), exitpriority = 0)

            
            def _new_handle(self, first = (False,)):
                flags = _winapi.PIPE_ACCESS_DUPLEX | _winapi.FILE_FLAG_OVERLAPPED
                if first:
                    flags |= _winapi.FILE_FLAG_FIRST_PIPE_INSTANCE
                return _winapi.CreateNamedPipe(self._address, flags, _winapi.PIPE_TYPE_MESSAGE | _winapi.PIPE_READMODE_MESSAGE | _winapi.PIPE_WAIT, _winapi.PIPE_UNLIMITED_INSTANCES, BUFSIZE, BUFSIZE, _winapi.NMPWAIT_WAIT_FOREVER, _winapi.NULL)

            
            def accept(self):
                self._handle_queue.append(self._new_handle())
                handle = self._handle_queue.pop(0)
            # WARNING: Decompyle incomplete

            _finalize_pipe_listener = (lambda queue, address: util.sub_debug('closing listener with address=%r', address)for handle in queue:
_winapi.CloseHandle(handle))()

        
        def PipeClient(address):
            '''
        Return a connection object connected to the pipe given by `address`
        '''
            t = _init_timeout()
            
            try:
                _winapi.WaitNamedPipe(address, 1000)
                h = _winapi.CreateFile(address, _winapi.GENERIC_READ | _winapi.GENERIC_WRITE, 0, _winapi.NULL, _winapi.OPEN_EXISTING, _winapi.FILE_FLAG_OVERLAPPED, _winapi.NULL)
                _winapi.SetNamedPipeHandleState(h, _winapi.PIPE_READMODE_MESSAGE, None, None)
                return PipeConnection(h)
            except OSError:
                e = None
                if e.winerror not in (_winapi.ERROR_SEM_TIMEOUT, _winapi.ERROR_PIPE_BUSY) or _check_timeout(t):
                    raise 
                e = None
                del e
            except:
                e = None
                del e

            continue

    MESSAGE_LENGTH = 40
    _CHALLENGE = b'#CHALLENGE#'
    _WELCOME = b'#WELCOME#'
    _FAILURE = b'#FAILURE#'
    _ALLOWED_DIGESTS = frozenset({
        b'md5',
        b'sha256',
        b'sha384',
        b'sha3_256',
        b'sha3_384'})
    _MAX_DIGEST_LEN = (lambda .0: pass# WARNING: Decompyle incomplete
)(_ALLOWED_DIGESTS())
    _MD5ONLY_MESSAGE_LENGTH = 20
    _MD5_DIGEST_LEN = 16
    _LEGACY_LENGTHS = (_MD5ONLY_MESSAGE_LENGTH, _MD5_DIGEST_LEN)
    
    def _get_digest_name_and_payload(message):
        '''Returns a digest name and the payload for a response hash.

    If a legacy protocol is detected based on the message length
    or contents the digest name returned will be empty to indicate
    legacy mode where MD5 and no digest prefix should be sent.
    '''
        if len(message) in _LEGACY_LENGTHS:
            return ('', message)
        if None.startswith(b'{'):
            curly = message.find(b'}', 1, _MAX_DIGEST_LEN + 2)
            if message.find(b'}', 1, _MAX_DIGEST_LEN + 2) > 0:
                digest = message[1:curly]
                if digest in _ALLOWED_DIGESTS:
                    payload = message[curly + 1:]
                    return (digest.decode('ascii'), payload)
                raise None(f'''unsupported message length, missing digest prefix, or unsupported digest: message={message!r}''')

    
    def _create_response(authkey, message):
        """Create a MAC based on authkey and message

    The MAC algorithm defaults to HMAC-MD5, unless MD5 is not available or
    the message has a '{digest_name}' prefix. For legacy HMAC-MD5, the response
    is the raw MAC, otherwise the response is prefixed with '{digest_name}',
    e.g. b'{sha256}abcdefg...'

    Note: The MAC protects the entire message including the digest_name prefix.
    """
        import hmac
        digest_name = _get_digest_name_and_payload(message)[0]
        if not digest_name:
            
            try:
                return hmac.new(authkey, message, 'md5').digest()
                response = hmac.new(authkey, message, digest_name).digest()
                return b'{%s}%s' % (digest_name.encode('ascii'), response)
            except ValueError:
                digest_name = 'sha256'
                continue


    
    def _verify_challenge(authkey, message, response):
        """Verify MAC challenge

    If our message did not include a digest_name prefix, the client is allowed
    to select a stronger digest_name from _ALLOWED_DIGESTS.

    In case our message is prefixed, a client cannot downgrade to a weaker
    algorithm, because the MAC is calculated over the entire message
    including the '{digest_name}' prefix.
    """
        import hmac
        (response_digest, response_mac) = _get_digest_name_and_payload(response)
        if not response_digest:
            response_digest
        response_digest = 'md5'
        
        try:
            expected = hmac.new(authkey, message, response_digest).digest()
            if len(expected) != len(response_mac):
                raise AuthenticationError(f'''expected {response_digest!r} of length {len(expected)} got {len(response_mac)}''')
            if not hmac.compare_digest(expected, response_mac):
                raise AuthenticationError('digest received was wrong')
            return None
        except ValueError:
            raise AuthenticationError(f'''response_digest={response_digest!r} unsupported''')


    
    def deliver_challenge(connection = None, authkey = None, digest_name = max):
        if not isinstance(authkey, bytes):
            raise ValueError('Authkey must be bytes, not {0!s}'.format(type(authkey)))
    # WARNING: Decompyle incomplete

    
    def answer_challenge(connection = None, authkey = None if sys.platform != 'win32' else None):
        if not isinstance(authkey, bytes):
            raise ValueError('Authkey must be bytes, not {0!s}'.format(type(authkey)))
        message = connection.recv_bytes(256)
        if not message.startswith(_CHALLENGE):
            raise AuthenticationError(f'''Protocol error, expected challenge: message={message!r}''')
        message = message[len(_CHALLENGE):]
        if len(message) < _MD5ONLY_MESSAGE_LENGTH:
            raise AuthenticationError(f'''challenge too short: {len(message)} bytes''')
        digest = _create_response(authkey, message)
        connection.send_bytes(digest)
        response = connection.recv_bytes(256)
        if response != _WELCOME:
            raise AuthenticationError('digest sent was rejected')

    
    class ConnectionWrapper(object):
        
        def __init__(self, conn, dumps, loads):
            self._conn = conn
            self._dumps = dumps
            self._loads = loads
            for attr in ('fileno', 'close', 'poll', 'recv_bytes', 'send_bytes'):
                obj = getattr(conn, attr)
                setattr(self, attr, obj)

        
        def send(self, obj):
            s = self._dumps(obj)
            self._conn.send_bytes(s)

        
        def recv(self):
            s = self._conn.recv_bytes()
            return self._loads(s)


    
    def _xml_dumps(obj):
        return xmlrpclib.dumps((obj,), None, None, None, 1).encode('utf-8')

    
    def _xml_loads(s):
        (obj,) = ()
        method = xmlrpclib.loads(s.decode('utf-8'))
        return obj

    
    class XmlListener(Listener):
        
        def accept(self):
            global xmlrpclib
            xmlrpclib = client
            import xmlrpc.client
            obj = Listener.accept(self)
            return ConnectionWrapper(obj, _xml_dumps, _xml_loads)


    
    def XmlClient(*args, **kwds):
        global xmlrpclib
        xmlrpclib = client
        import xmlrpc.client
    # WARNING: Decompyle incomplete

    if sys.platform == 'win32':
        
        def reduce_connection(conn):
            handle = conn.fileno()
            s = socket.fromfd(handle, socket.AF_INET, socket.SOCK_STREAM)
            resource_sharer = resource_sharer
            import 
            ds = resource_sharer.DupSocket(s)
            None(None, None)
            return 
            with None:
                if not None, (rebuild_connection, (ds, conn.readable, conn.writable)):
                    pass

        
        def rebuild_connection(ds, readable, writable):
            sock = ds.detach()
            return Connection(sock.detach(), readable, writable)

        reduction.register(Connection, reduce_connection)
        
        def reduce_pipe_connection(conn):
            access = _winapi.FILE_GENERIC_READ if conn.readable else 0 | _winapi.FILE_GENERIC_WRITE if conn.writable else 0
            dh = reduction.DupHandle(conn.fileno(), access)
            return (rebuild_pipe_connection, (dh, conn.readable, conn.writable))

        
        def rebuild_pipe_connection(dh, readable, writable):
            handle = dh.detach()
            return PipeConnection(handle, readable, writable)

        reduction.register(PipeConnection, reduce_pipe_connection)
        return None
    
    def reduce_connection(conn):
        df = reduction.DupFd(conn.fileno())
        return (rebuild_connection, (df, conn.readable, conn.writable))

    
    def rebuild_connection(df, readable, writable):
        fd = df.detach()
        return Connection(fd, readable, writable)

    reduction.register(Connection, reduce_connection)
    return None
except ImportError:
    if sys.platform == 'win32':
        raise 
    _winapi = None
    continue

