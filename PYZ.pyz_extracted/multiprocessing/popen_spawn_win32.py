# Source Generated with Decompyle++
# File: popen_spawn_win32.pyc (Python 3.12)

import os
import msvcrt
import signal
import sys
import _winapi
from context import reduction, get_spawning_popen, set_spawning_popen
from  import spawn
from  import util
__all__ = [
    'Popen']
TERMINATE = 65536
if sys.platform == 'win32':
    sys.platform == 'win32'
WINEXE = getattr(sys, 'frozen', False)
WINSERVICE = sys.executable.lower().endswith('pythonservice.exe')

def _path_eq(p1, p2):
    if not p1 == p2:
        p1 == p2
    return os.path.normcase(p1) == os.path.normcase(p2)

WINENV = not _path_eq(sys.executable, sys._base_executable)

def _close_handles(*handles):
    for handle in handles:
        _winapi.CloseHandle(handle)


class Popen(object):
    '''
    Start a subprocess to run the code of a process object
    '''
    method = 'spawn'
    
    def __init__(self, process_obj):
        prep_data = spawn.get_preparation_data(process_obj._name)
        (rhandle, whandle) = _winapi.CreatePipe(None, 0)
        wfd = msvcrt.open_osfhandle(whandle, 0)
        cmd = spawn.get_command_line(parent_pid = os.getpid(), pipe_handle = rhandle)
        python_exe = spawn.get_executable()
        if WINENV and _path_eq(python_exe, sys.executable):
            cmd[0] = sys._base_executable
            python_exe = sys._base_executable
            env = os.environ.copy()
            env['__PYVENV_LAUNCHER__'] = sys.executable
        else:
            env = None
        cmd = (lambda .0: pass# WARNING: Decompyle incomplete
)(cmd())
        to_child = open(wfd, 'wb', closefd = True)
        (hp, ht, pid, tid) = _winapi.CreateProcess(python_exe, cmd, None, None, False, 0, env, None, None)
        _winapi.CloseHandle(ht)
        self.pid = pid
        self.returncode = None
        self._handle = hp
        self.sentinel = int(hp)
        self.finalizer = util.Finalize(self, _close_handles, (self.sentinel, int(rhandle)))
        set_spawning_popen(self)
        reduction.dump(prep_data, to_child)
        reduction.dump(process_obj, to_child)
        set_spawning_popen(None)
        None(None, None)
        return None
        ' '.join
        _winapi.CloseHandle(rhandle)
        raise 
        set_spawning_popen(None)
        with None:
            if not None:
                pass

    
    def duplicate_for_child(self, handle):
        pass
    # WARNING: Decompyle incomplete

    
    def wait(self, timeout = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def poll(self):
        return self.wait(timeout = 0)

    
    def terminate(self):
        pass
    # WARNING: Decompyle incomplete

    kill = terminate
    
    def close(self):
        self.finalizer()


