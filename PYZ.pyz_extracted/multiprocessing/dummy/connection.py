# Source Generated with Decompyle++
# File: connection.pyc (Python 3.12)

__all__ = [
    'Client',
    'Listener',
    'Pipe']
from queue import Queue
families = [
    None]

class Listener(object):
    
    def __init__(self, address, family, backlog = (None, None, 1)):
        self._backlog_queue = Queue(backlog)

    
    def accept(self):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        self._backlog_queue = None

    address = (lambda self: self._backlog_queue)()
    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()



def Client(address):
    _out = Queue()
    _in = Queue()
    address.put((_out, _in))
    return Connection(_in, _out)


def Pipe(duplex = (True,)):
    b = Queue()
    a = Queue()
    return (Connection(a, b), Connection(b, a))


class Connection(object):
    
    def __init__(self, _in, _out):
        self._out = _out
        self._in = _in
        self.send = _out.put
        self.send_bytes = _out.put
        self.recv = _in.get
        self.recv_bytes = _in.get

    
    def poll(self, timeout = (0,)):
        if self._in.qsize() > 0:
            return True
        if timeout <= 0:
            return False
        self._in.not_empty
        self._in.not_empty.wait(timeout)
        None(None, None)
        return self._in.qsize() > 0
        with None:
            if not None:
                pass
        continue

    
    def close(self):
        pass

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()


