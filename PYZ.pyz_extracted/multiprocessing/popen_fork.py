# Source Generated with Decompyle++
# File: popen_fork.pyc (Python 3.12)

import os
import signal
from  import util
__all__ = [
    'Popen']

class Popen(object):
    method = 'fork'
    
    def __init__(self, process_obj):
        util._flush_std_streams()
        self.returncode = None
        self.finalizer = None
        self._launch(process_obj)

    
    def duplicate_for_child(self, fd):
        return fd

    
    def poll(self, flag = (os.WNOHANG,)):
        pass
    # WARNING: Decompyle incomplete

    
    def wait(self, timeout = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _send_signal(self, sig):
        pass
    # WARNING: Decompyle incomplete

    
    def terminate(self):
        self._send_signal(signal.SIGTERM)

    
    def kill(self):
        self._send_signal(signal.SIGKILL)

    
    def _launch(self, process_obj):
        code = 1
        (parent_r, child_w) = os.pipe()
        (child_r, parent_w) = os.pipe()
        self.pid = os.fork()
        if self.pid == 0:
            
            try:
                os.close(parent_r)
                os.close(parent_w)
                code = process_obj._bootstrap(parent_sentinel = child_r)
                os._exit(code)
                return None
                os.close(child_w)
                os.close(child_r)
                self.finalizer = util.Finalize(self, util.close_fds, (parent_r, parent_w))
                self.sentinel = parent_r
                return None
            except:
                os._exit(code)


    
    def close(self):
        pass
    # WARNING: Decompyle incomplete


