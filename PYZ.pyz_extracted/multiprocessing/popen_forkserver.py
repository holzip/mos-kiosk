# Source Generated with Decompyle++
# File: popen_forkserver.pyc (Python 3.12)

import io
import os
from context import reduction, set_spawning_popen
if not reduction.HAVE_SEND_HANDLE:
    raise ImportError('No support for sending fds between processes')
from  import forkserver
from  import popen_fork
from  import spawn
from  import util
__all__ = [
    'Popen']

class _DupFd(object):
    
    def __init__(self, ind):
        self.ind = ind

    
    def detach(self):
        return forkserver.get_inherited_fds()[self.ind]



class Popen(popen_fork.Popen):
    pass
# WARNING: Decompyle incomplete

