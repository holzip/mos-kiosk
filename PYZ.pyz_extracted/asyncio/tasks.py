# Source Generated with Decompyle++
# File: tasks.pyc (Python 3.12)

'''Support for tasks, coroutines and the scheduler.'''
__all__ = ('Task', 'create_task', 'FIRST_COMPLETED', 'FIRST_EXCEPTION', 'ALL_COMPLETED', 'wait', 'wait_for', 'as_completed', 'sleep', 'gather', 'shield', 'ensure_future', 'run_coroutine_threadsafe', 'current_task', 'all_tasks', 'create_eager_task_factory', 'eager_task_factory', '_register_task', '_unregister_task', '_enter_task', '_leave_task')
import concurrent.futures as concurrent
import contextvars
import functools
import inspect
import itertools
import types
import warnings
import weakref
from types import GenericAlias
from  import base_tasks
from  import coroutines
from  import events
from  import exceptions
from  import futures
from  import timeouts
_task_name_counter = itertools.count(1).__next__

def current_task(loop = (None,)):
    '''Return a currently executed task.'''
    pass
# WARNING: Decompyle incomplete


def all_tasks(loop = (None,)):
    '''Return a set of all tasks for the loop.'''
    pass
# WARNING: Decompyle incomplete


def _set_task_name(task, name):
    pass
# WARNING: Decompyle incomplete


class Task(futures._PyFuture):
    pass
# WARNING: Decompyle incomplete

_PyTask = Task

try:
    import _asyncio
    Task = _asyncio.Task
    _CTask = _asyncio.Task
    
    def create_task(coro = None, *, name, context):
        '''Schedule the execution of a coroutine object in a spawn task.

    Return a Task object.
    '''
        loop = events.get_running_loop()
    # WARNING: Decompyle incomplete

    FIRST_COMPLETED = concurrent.futures.FIRST_COMPLETED
    FIRST_EXCEPTION = concurrent.futures.FIRST_EXCEPTION
    ALL_COMPLETED = concurrent.futures.ALL_COMPLETED
    
    async def wait(fs = None, *, timeout, return_when):
        """Wait for the Futures or Tasks given by fs to complete.

    The fs iterable must not be empty.

    Coroutines will be wrapped in Tasks.

    Returns two sets of Future: (done, pending).

    Usage:

        done, pending = await asyncio.wait(fs)

    Note: This does not raise TimeoutError! Futures that aren't done
    when the timeout occurs are returned in the second set.
    """
        pass
    # WARNING: Decompyle incomplete

    
    def _release_waiter(waiter, *args):
        if not waiter.done():
            waiter.set_result(None)
            return None

    
    async def wait_for(fut, timeout):
        '''Wait for the single Future or coroutine to complete, with timeout.

    Coroutine will be wrapped in Task.

    Returns result of the Future or coroutine.  When a timeout occurs,
    it cancels the task and raises TimeoutError.  To avoid the task
    cancellation, wrap it in shield().

    If the wait is cancelled, the task is also cancelled.

    If the task suppresses the cancellation and returns a value instead,
    that value is returned.

    This function is a coroutine.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _wait(fs, timeout, return_when, loop):
        '''Internal helper for wait().

    The fs argument must be a collection of Futures.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _cancel_and_wait(fut):
        '''Cancel the *fut* future or task and wait until it completes.'''
        pass
    # WARNING: Decompyle incomplete

    
    def as_completed(fs = None, *, timeout):
        """Return an iterator whose values are coroutines.

    When waiting for the yielded coroutines you'll get the results (or
    exceptions!) of the original Futures (or coroutines), in the order
    in which and as soon as they complete.

    This differs from PEP 3148; the proper way to use this is:

        for f in as_completed(fs):
            result = await f  # The 'await' may raise.
            # Use result.

    If a timeout is specified, the 'await' will raise
    TimeoutError when the timeout occurs before all Futures are done.

    Note: The futures 'f' are not necessarily members of fs.
    """
        pass
    # WARNING: Decompyle incomplete

    __sleep0 = (lambda : pass# WARNING: Decompyle incomplete
)()
    
    async def sleep(delay, result = (None,)):
        '''Coroutine that completes after a given time (in seconds).'''
        pass
    # WARNING: Decompyle incomplete

    
    def ensure_future(coro_or_future = types.coroutine, *, loop):
        '''Wrap a coroutine or an awaitable in a future.

    If the argument is a Future, it is returned directly.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    class _GatheringFuture(futures.Future):
        pass
    # WARNING: Decompyle incomplete

    
    def gather(*, return_exceptions, *coros_or_futures):
        """Return a future aggregating results from the given coroutines/futures.

    Coroutines will be wrapped in a future and scheduled in the event
    loop. They will not necessarily be scheduled in the same order as
    passed in.

    All futures must share the same event loop.  If all the tasks are
    done successfully, the returned future's result is the list of
    results (in the order of the original sequence, not necessarily
    the order of results arrival).  If *return_exceptions* is True,
    exceptions in the tasks are treated the same as successful
    results, and gathered in the result list; otherwise, the first
    raised exception will be immediately propagated to the returned
    future.

    Cancellation: if the outer Future is cancelled, all children (that
    have not completed yet) are also cancelled.  If any child is
    cancelled, this is treated as if it raised CancelledError --
    the outer Future is *not* cancelled in this case.  (This is to
    prevent the cancellation of one child to cause other children to
    be cancelled.)

    If *return_exceptions* is False, cancelling gather() after it
    has been marked done won't cancel any submitted awaitables.
    For instance, gather can be marked done after propagating an
    exception to the caller, therefore, calling ``gather.cancel()``
    after catching an exception (raised by one of the awaitables) from
    gather won't cancel any other awaitables.
    """
        pass
    # WARNING: Decompyle incomplete

    
    def shield(arg):
        """Wait for a future, shielding it from cancellation.

    The statement

        task = asyncio.create_task(something())
        res = await shield(task)

    is exactly equivalent to the statement

        res = await something()

    *except* that if the coroutine containing it is cancelled, the
    task running in something() is not cancelled.  From the POV of
    something(), the cancellation did not happen.  But its caller is
    still cancelled, so the yield-from expression still raises
    CancelledError.  Note: If something() is cancelled by other means
    this will still cancel shield().

    If you want to completely ignore cancellation (not recommended)
    you can combine shield() with a try/except clause, as follows:

        task = asyncio.create_task(something())
        try:
            res = await shield(task)
        except CancelledError:
            res = None

    Save a reference to tasks passed to this function, to avoid
    a task disappearing mid-execution. The event loop only keeps
    weak references to tasks. A task that isn't referenced elsewhere
    may get garbage collected at any time, even before it's done.
    """
        pass
    # WARNING: Decompyle incomplete

    
    def run_coroutine_threadsafe(coro, loop):
        '''Submit a coroutine object to a given event loop.

    Return a concurrent.futures.Future to access the result.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def create_eager_task_factory(custom_task_constructor):
        """Create a function suitable for use as a task factory on an event-loop.

        Example usage:

            loop.set_task_factory(
                asyncio.create_eager_task_factory(my_task_constructor))

        Now, tasks created will be started immediately (rather than being first
        scheduled to an event loop). The constructor argument can be any callable
        that returns a Task-compatible object and has a signature compatible
        with `Task.__init__`; it must have the `eager_start` keyword argument.

        Most applications will use `Task` for `custom_task_constructor` and in
        this case there's no need to call `create_eager_task_factory()`
        directly. Instead the  global `eager_task_factory` instance can be
        used. E.g. `loop.set_task_factory(asyncio.eager_task_factory)`.
        """
        pass
    # WARNING: Decompyle incomplete

    eager_task_factory = create_eager_task_factory(Task)
    _scheduled_tasks = weakref.WeakSet()
    _eager_tasks = set()
    _current_tasks = { }
    
    def _register_task(task):
        '''Register an asyncio Task scheduled to run on an event loop.'''
        _scheduled_tasks.add(task)

    
    def _register_eager_task(task):
        '''Register an asyncio Task about to be eagerly executed.'''
        _eager_tasks.add(task)

    
    def _enter_task(loop, task):
        current_task = _current_tasks.get(loop)
    # WARNING: Decompyle incomplete

    
    def _leave_task(loop, task):
        current_task = _current_tasks.get(loop)
        if current_task is not task:
            raise RuntimeError(f'''Leaving task {task!r} does not match the current task {current_task!r}.''')
        del _current_tasks[loop]

    
    def _swap_current_task(loop, task):
        prev_task = _current_tasks.get(loop)
    # WARNING: Decompyle incomplete

    
    def _unregister_task(task):
        '''Unregister a completed, scheduled Task.'''
        _scheduled_tasks.discard(task)

    
    def _unregister_eager_task(task):
        '''Unregister a task which finished its first eager step.'''
        _eager_tasks.discard(task)

    _py_current_task = current_task
    _py_register_task = _register_task
    _py_register_eager_task = _register_eager_task
    _py_unregister_task = _unregister_task
    _py_unregister_eager_task = _unregister_eager_task
    _py_enter_task = _enter_task
    _py_leave_task = _leave_task
    _py_swap_current_task = _swap_current_task
    
    try:
        from _asyncio import _register_task, _register_eager_task, _unregister_task, _unregister_eager_task, _enter_task, _leave_task, _swap_current_task, _scheduled_tasks, _eager_tasks, _current_tasks, current_task
        _c_current_task = current_task
        _c_register_task = _register_task
        _c_register_eager_task = _register_eager_task
        _c_unregister_task = _unregister_task
        _c_unregister_eager_task = _unregister_eager_task
        _c_enter_task = _enter_task
        _c_leave_task = _leave_task
        _c_swap_current_task = _swap_current_task
        return None
        except ImportError:
            continue
    except ImportError:
        return None


