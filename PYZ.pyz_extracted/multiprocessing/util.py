# Source Generated with Decompyle++
# File: util.pyc (Python 3.12)

import os
import itertools
import sys
import weakref
import atexit
import threading
from subprocess import _args_from_interpreter_flags
from  import process
__all__ = [
    'sub_debug',
    'debug',
    'info',
    'sub_warning',
    'get_logger',
    'log_to_stderr',
    'get_temp_dir',
    'register_after_fork',
    'is_exiting',
    'Finalize',
    'ForkAwareThreadLock',
    'ForkAwareLocal',
    'close_all_fds_except',
    'SUBDEBUG',
    'SUBWARNING']
NOTSET = 0
SUBDEBUG = 5
DEBUG = 10
INFO = 20
SUBWARNING = 25
LOGGER_NAME = 'multiprocessing'
DEFAULT_LOGGING_FORMAT = '[%(levelname)s/%(processName)s] %(message)s'
_logger = None
_log_to_stderr = False

def sub_debug(msg, *args):
    pass
# WARNING: Decompyle incomplete


def debug(msg, *args):
    pass
# WARNING: Decompyle incomplete


def info(msg, *args):
    pass
# WARNING: Decompyle incomplete


def sub_warning(msg, *args):
    pass
# WARNING: Decompyle incomplete


def get_logger():
    '''
    Returns logger used by multiprocessing
    '''
    global _logger
    import logging
    logging._acquireLock()
    
    try:
        if not _logger:
            _logger = logging.getLogger(LOGGER_NAME)
            _logger.propagate = 0
            if hasattr(atexit, 'unregister'):
                atexit.unregister(_exit_function)
                atexit.register(_exit_function)
            else:
                atexit._exithandlers.remove((_exit_function, (), { }))
                atexit._exithandlers.append((_exit_function, (), { }))
        logging._releaseLock()
        return _logger
    except:
        logging._releaseLock()



def log_to_stderr(level = (None,)):
    '''
    Turn on logging and add a handler which prints to stderr
    '''
    global _log_to_stderr
    import logging
    logger = get_logger()
    formatter = logging.Formatter(DEFAULT_LOGGING_FORMAT)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if level:
        logger.setLevel(level)
    _log_to_stderr = True
    return _logger


def _platform_supports_abstract_sockets():
    if sys.platform == 'linux':
        return True
    if hasattr(sys, 'getandroidapilevel'):
        return True
    return False


def is_abstract_socket_namespace(address):
    if not address:
        return False
    if isinstance(address, bytes):
        return address[0] == 0
    if None(address, str):
        return address[0] == '\x00'
    raise None(f'''address type of {address!r} unrecognized''')

abstract_sockets_supported = _platform_supports_abstract_sockets()

def _remove_temp_dir(rmtree, tempdir):
    
    def onerror(func, path, err_info):
        if not issubclass(err_info[0], FileNotFoundError):
            raise 

    rmtree(tempdir, onerror = onerror)
    current_process = process.current_process()
# WARNING: Decompyle incomplete


def get_temp_dir():
    tempdir = process.current_process()._config.get('tempdir')
# WARNING: Decompyle incomplete

_afterfork_registry = weakref.WeakValueDictionary()
_afterfork_counter = itertools.count()

def _run_after_forkers():
    items = list(_afterfork_registry.items())
    items.sort()
    for index, ident, func in items:
        obj = None
        func(obj)
    return None
    except Exception:
        e = None
        info('after forker raised exception %s', e)
        e = None
        del e
        continue
        e = None
        del e


def register_after_fork(obj, func):
    _afterfork_registry[(next(_afterfork_counter), id(obj), func)] = obj

_finalizer_registry = { }
_finalizer_counter = itertools.count()

class Finalize(object):
    '''
    Class which supports object finalization using weakrefs
    '''
    
    def __init__(self, obj, callback, args, kwargs, exitpriority = ((), None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, wr, _finalizer_registry, sub_debug, getpid = (None, _finalizer_registry, sub_debug, os.getpid)):
        '''
        Run the callback unless it has already been called or cancelled
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def cancel(self):
        '''
        Cancel finalization of the object
        '''
        
        try:
            del _finalizer_registry[self._key]
            self._weakref = None
            self._callback = None
            self._args = None
            self._kwargs = None
            self._key = None
            return None
        except KeyError:
            return None


    
    def still_active(self):
        '''
        Return whether this finalizer is still waiting to invoke callback
        '''
        return self._key in _finalizer_registry

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete



def _run_finalizers(minpriority = (None,)):
    '''
    Run all finalizers whose exit priority is not None and at least minpriority

    Finalizers with highest priority are called first; finalizers with
    the same priority will be called in reverse order of creation.
    '''
    pass
# WARNING: Decompyle incomplete


def is_exiting():
    '''
    Returns true if the process is shutting down
    '''
    if not _exiting:
        _exiting
    return _exiting is None

_exiting = False

def _exit_function(info, debug, _run_finalizers, active_children, current_process = (info, debug, _run_finalizers, process.active_children, process.current_process)):
    global _exiting
    pass
# WARNING: Decompyle incomplete

atexit.register(_exit_function)

class ForkAwareThreadLock(object):
    
    def __init__(self):
        self._lock = threading.Lock()
        self.acquire = self._lock.acquire
        self.release = self._lock.release
        register_after_fork(self, ForkAwareThreadLock._at_fork_reinit)

    
    def _at_fork_reinit(self):
        self._lock._at_fork_reinit()

    
    def __enter__(self):
        return self._lock.__enter__()

    
    def __exit__(self, *args):
        pass
    # WARNING: Decompyle incomplete



class ForkAwareLocal(threading.local):
    
    def __init__(self):
        register_after_fork(self, (lambda obj: obj.__dict__.clear()))

    
    def __reduce__(self):
        return (type(self), ())



try:
    MAXFD = os.sysconf('SC_OPEN_MAX')
    
    def close_all_fds_except(fds):
        fds = list(fds) + [
            -1,
            MAXFD]
        fds.sort()
    # WARNING: Decompyle incomplete

    
    def _close_stdin():
        pass
    # WARNING: Decompyle incomplete

    
    def _flush_std_streams():
        
        try:
            sys.stdout.flush()
            
            try:
                sys.stderr.flush()
                return None
                except (AttributeError, ValueError):
                    continue
            except (AttributeError, ValueError):
                return None



    
    def spawnv_passfds(path, args, passfds):
        import _posixsubprocess
        import subprocess
        passfds = tuple(sorted(map(int, passfds)))
        (errpipe_read, errpipe_write) = os.pipe()
        
        try:
            os.close(errpipe_read)
            os.close(errpipe_write)
            return _posixsubprocess.fork_exec(args, [
                path], True, passfds, None, None, -1, -1, -1, -1, -1, -1, errpipe_read, errpipe_write, False, False, -1, None, None, None, -1, None, subprocess._USE_VFORK)
        except:
            os.close(errpipe_read)
            os.close(errpipe_write)


    
    def close_fds(*fds):
        '''Close each file descriptor given as an argument'''
        for fd in fds:
            os.close(fd)

    
    def _cleanup_tests():
        '''Cleanup multiprocessing resources when multiprocessing tests
    completed.'''
        support = support
        import test
        process._cleanup()
        forkserver = forkserver
        import multiprocessing
        forkserver._forkserver._stop()
        resource_tracker = resource_tracker
        import multiprocessing
        resource_tracker._resource_tracker._stop()
        _run_finalizers()
        support.gc_collect()
        support.reap_children()

    return None
except Exception:
    MAXFD = 256
    continue

