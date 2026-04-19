# Source Generated with Decompyle++
# File: popen_spawn_posix.pyc (Python 3.12)

import io
import os
from context import reduction, set_spawning_popen
from  import popen_fork
from  import spawn
from  import util
__all__ = [
    'Popen']

class _DupFd(object):
    
    def __init__(self, fd):
        self.fd = fd

    
    def detach(self):
        return self.fd



class Popen(popen_fork.Popen):
    pass
# WARNING: Decompyle incomplete

