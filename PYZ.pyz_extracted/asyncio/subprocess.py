# Source Generated with Decompyle++
# File: subprocess.pyc (Python 3.12)

__all__ = ('create_subprocess_exec', 'create_subprocess_shell')
import subprocess
from  import events
from  import protocols
from  import streams
from  import tasks
from log import logger
PIPE = subprocess.PIPE
STDOUT = subprocess.STDOUT
DEVNULL = subprocess.DEVNULL

class SubprocessStreamProtocol(protocols.SubprocessProtocol, streams.FlowControlMixin):
    pass
# WARNING: Decompyle incomplete


class Process:
    
    def __init__(self, transport, protocol, loop):
        self._transport = transport
        self._protocol = protocol
        self._loop = loop
        self.stdin = protocol.stdin
        self.stdout = protocol.stdout
        self.stderr = protocol.stderr
        self.pid = transport.get_pid()

    
    def __repr__(self):
        return f'''<{self.__class__.__name__} {self.pid}>'''

    returncode = (lambda self: self._transport.get_returncode())()
    
    async def wait(self):
        '''Wait until the process exit and return the process return code.'''
        pass
    # WARNING: Decompyle incomplete

    
    def send_signal(self, signal):
        self._transport.send_signal(signal)

    
    def terminate(self):
        self._transport.terminate()

    
    def kill(self):
        self._transport.kill()

    
    async def _feed_stdin(self, input):
        pass
    # WARNING: Decompyle incomplete

    
    async def _noop(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def _read_stream(self, fd):
        pass
    # WARNING: Decompyle incomplete

    
    async def communicate(self, input = (None,)):
        pass
    # WARNING: Decompyle incomplete



async def create_subprocess_shell(cmd, stdin, stdout, stderr, limit = (None, None, None, streams._DEFAULT_LIMIT), **kwds):
    pass
# WARNING: Decompyle incomplete


async def create_subprocess_exec(program = None, *, stdin, stdout, stderr, limit, *args, **kwds):
    pass
# WARNING: Decompyle incomplete

