# Source Generated with Decompyle++
# File: unix_events.pyc (Python 3.12)

'''Selector event loop for Unix with signal handling.'''
import errno
import io
import itertools
import os
import selectors
import signal
import socket
import stat
import subprocess
import sys
import threading
import warnings
from  import base_events
from  import base_subprocess
from  import constants
from  import coroutines
from  import events
from  import exceptions
from  import futures
from  import selector_events
from  import tasks
from  import transports
from log import logger
__all__ = ('SelectorEventLoop', 'AbstractChildWatcher', 'SafeChildWatcher', 'FastChildWatcher', 'PidfdChildWatcher', 'MultiLoopChildWatcher', 'ThreadedChildWatcher', 'DefaultEventLoopPolicy')
if sys.platform == 'win32':
    raise ImportError('Signals are not really supported on Windows')

def _sighandler_noop(signum, frame):
    '''Dummy signal handler.'''
    pass


def waitstatus_to_exitcode(status):
    
    try:
        return os.waitstatus_to_exitcode(status)
    except ValueError:
        return 



class _UnixSelectorEventLoop(selector_events.BaseSelectorEventLoop):
    pass
# WARNING: Decompyle incomplete


class _UnixReadPipeTransport(transports.ReadTransport):
    pass
# WARNING: Decompyle incomplete


class _UnixWritePipeTransport(transports.WriteTransport, transports._FlowControlMixin):
    pass
# WARNING: Decompyle incomplete


class _UnixSubprocessTransport(base_subprocess.BaseSubprocessTransport):
    
    def _start(self, args, shell, stdin, stdout, stderr, bufsize, **kwargs):
        stdin_w = None
        if stdin == subprocess.PIPE and sys.platform.startswith('aix'):
            (stdin, stdin_w) = socket.socketpair()
    # WARNING: Decompyle incomplete



class AbstractChildWatcher:
    '''Abstract base class for monitoring child processes.

    Objects derived from this class monitor a collection of subprocesses and
    report their termination or interruption by a signal.

    New callbacks are registered with .add_child_handler(). Starting a new
    process must be done within a \'with\' block to allow the watcher to suspend
    its activity until the new process if fully registered (this is needed to
    prevent a race condition in some implementations).

    Example:
        with watcher:
            proc = subprocess.Popen("sleep 1")
            watcher.add_child_handler(proc.pid, callback)

    Notes:
        Implementations of this class must be thread-safe.

        Since child watcher objects may catch the SIGCHLD signal and call
        waitpid(-1), there should be only one active object per process.
    '''
    
    def __init_subclass__(cls = None):
        if cls.__module__ != __name__:
            warnings._deprecated('AbstractChildWatcher', '{name!r} is deprecated as of Python 3.12 and will be removed in Python {remove}.', remove = (3, 14))
            return None

    
    def add_child_handler(self, pid, callback, *args):
        """Register a new child handler.

        Arrange for callback(pid, returncode, *args) to be called when
        process 'pid' terminates. Specifying another callback for the same
        process replaces the previous handler.

        Note: callback() must be thread-safe.
        """
        raise NotImplementedError()

    
    def remove_child_handler(self, pid):
        """Removes the handler for process 'pid'.

        The function returns True if the handler was successfully removed,
        False if there was nothing to remove."""
        raise NotImplementedError()

    
    def attach_loop(self, loop):
        '''Attach the watcher to an event loop.

        If the watcher was previously attached to an event loop, then it is
        first detached before attaching to the new loop.

        Note: loop may be None.
        '''
        raise NotImplementedError()

    
    def close(self):
        '''Close the watcher.

        This must be called to make sure that any underlying resource is freed.
        '''
        raise NotImplementedError()

    
    def is_active(self):
        '''Return ``True`` if the watcher is active and is used by the event loop.

        Return True if the watcher is installed and ready to handle process exit
        notifications.

        '''
        raise NotImplementedError()

    
    def __enter__(self):
        """Enter the watcher's context and allow starting new processes

        This function must return self"""
        raise NotImplementedError()

    
    def __exit__(self, a, b, c):
        """Exit the watcher's context"""
        raise NotImplementedError()



class PidfdChildWatcher(AbstractChildWatcher):
    '''Child watcher implementation using Linux\'s pid file descriptors.

    This child watcher polls process file descriptors (pidfds) to await child
    process termination. In some respects, PidfdChildWatcher is a "Goldilocks"
    child watcher implementation. It doesn\'t require signals or threads, doesn\'t
    interfere with any processes launched outside the event loop, and scales
    linearly with the number of subprocesses launched by the event loop. The
    main disadvantage is that pidfds are specific to Linux, and only work on
    recent (5.3+) kernels.
    '''
    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    
    def is_active(self):
        return True

    
    def close(self):
        pass

    
    def attach_loop(self, loop):
        pass

    
    def add_child_handler(self, pid, callback, *args):
        loop = events.get_running_loop()
        pidfd = os.pidfd_open(pid)
        loop._add_reader(pidfd, self._do_wait, pid, pidfd, callback, args)

    
    def _do_wait(self, pid, pidfd, callback, args):
        loop = events.get_running_loop()
        loop._remove_reader(pidfd)
    # WARNING: Decompyle incomplete

    
    def remove_child_handler(self, pid):
        return True



class BaseChildWatcher(AbstractChildWatcher):
    
    def __init__(self):
        self._loop = None
        self._callbacks = { }

    
    def close(self):
        self.attach_loop(None)

    
    def is_active(self):
        if self._loop is not None:
            self._loop is not None
        return self._loop.is_running()

    
    def _do_waitpid(self, expected_pid):
        raise NotImplementedError()

    
    def _do_waitpid_all(self):
        raise NotImplementedError()

    
    def attach_loop(self, loop):
        pass
    # WARNING: Decompyle incomplete

    
    def _sig_chld(self):
        
        try:
            self._do_waitpid_all()
            return None
        except (SystemExit, KeyboardInterrupt):
            raise 
            except BaseException:
                exc = None
                self._loop.call_exception_handler({
                    'message': 'Unknown exception in SIGCHLD handler',
                    'exception': exc })
                exc = None
                del exc
                return None
                exc = None
                del exc




class SafeChildWatcher(BaseChildWatcher):
    pass
# WARNING: Decompyle incomplete


class FastChildWatcher(BaseChildWatcher):
    pass
# WARNING: Decompyle incomplete


class MultiLoopChildWatcher(AbstractChildWatcher):
    """A watcher that doesn't require running loop in the main thread.

    This implementation registers a SIGCHLD signal handler on
    instantiation (which may conflict with other code that
    install own handler for this signal).

    The solution is safe but it has a significant overhead when
    handling a big number of processes (*O(n)* each time a
    SIGCHLD is received).
    """
    
    def __init__(self):
        self._callbacks = { }
        self._saved_sighandler = None
        warnings._deprecated('MultiLoopChildWatcher', '{name!r} is deprecated as of Python 3.12 and will be removed in Python {remove}.', remove = (3, 14))

    
    def is_active(self):
        return self._saved_sighandler is not None

    
    def close(self):
        self._callbacks.clear()
    # WARNING: Decompyle incomplete

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    
    def add_child_handler(self, pid, callback, *args):
        loop = events.get_running_loop()
        self._callbacks[pid] = (loop, callback, args)
        self._do_waitpid(pid)

    
    def remove_child_handler(self, pid):
        
        try:
            del self._callbacks[pid]
            return True
        except KeyError:
            return False


    
    def attach_loop(self, loop):
        pass
    # WARNING: Decompyle incomplete

    
    def _do_waitpid_all(self):
        for pid in list(self._callbacks):
            self._do_waitpid(pid)

    
    def _do_waitpid(self, expected_pid):
        pass
    # WARNING: Decompyle incomplete

    
    def _sig_chld(self, signum, frame):
        
        try:
            self._do_waitpid_all()
            return None
        except (SystemExit, KeyboardInterrupt):
            raise 
            except BaseException:
                logger.warning('Unknown exception in SIGCHLD handler', exc_info = True)
                return None




class ThreadedChildWatcher(AbstractChildWatcher):
    """Threaded child watcher implementation.

    The watcher uses a thread per process
    for waiting for the process finish.

    It doesn't require subscription on POSIX signal
    but a thread creation is not free.

    The watcher has O(1) complexity, its performance doesn't depend
    on amount of spawn processes.
    """
    
    def __init__(self):
        self._pid_counter = itertools.count(0)
        self._threads = { }

    
    def is_active(self):
        return True

    
    def close(self):
        pass

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    
    def __del__(self, _warn = (warnings.warn,)):
        pass
    # WARNING: Decompyle incomplete

    
    def add_child_handler(self, pid, callback, *args):
        loop = events.get_running_loop()
        thread = threading.Thread(target = self._do_waitpid, name = f'''asyncio-waitpid-{next(self._pid_counter)}''', args = (loop, pid, callback, args), daemon = True)
        self._threads[pid] = thread
        thread.start()

    
    def remove_child_handler(self, pid):
        return True

    
    def attach_loop(self, loop):
        pass

    
    def _do_waitpid(self, loop, expected_pid, callback, args):
        pass
    # WARNING: Decompyle incomplete



def can_use_pidfd():
    if not hasattr(os, 'pidfd_open'):
        return False
    
    try:
        pid = os.getpid()
        os.close(os.pidfd_open(pid, 0))
        return True
    except OSError:
        return False



class _UnixDefaultEventLoopPolicy(events.BaseDefaultEventLoopPolicy):
    pass
# WARNING: Decompyle incomplete

SelectorEventLoop = _UnixSelectorEventLoop
DefaultEventLoopPolicy = _UnixDefaultEventLoopPolicy
