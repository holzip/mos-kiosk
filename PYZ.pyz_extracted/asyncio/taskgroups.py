# Source Generated with Decompyle++
# File: taskgroups.pyc (Python 3.12)

__all__ = ('TaskGroup',)
from  import events
from  import exceptions
from  import tasks

class TaskGroup:
    '''Asynchronous context manager for managing groups of tasks.

    Example use:

        async with asyncio.TaskGroup() as group:
            task1 = group.create_task(some_coroutine(...))
            task2 = group.create_task(other_coroutine(...))
        print("Both tasks have completed now.")

    All tasks are awaited when the context manager exits.

    Any exceptions other than `asyncio.CancelledError` raised within
    a task will cancel all remaining tasks and wait for them to exit.
    The exceptions are then combined and raised as an `ExceptionGroup`.
    '''
    
    def __init__(self):
        self._entered = False
        self._exiting = False
        self._aborting = False
        self._loop = None
        self._parent_task = None
        self._parent_cancel_requested = False
        self._tasks = set()
        self._errors = []
        self._base_error = None
        self._on_completed_fut = None

    
    def __repr__(self):
        info = [
            '']
        if self._tasks:
            info.append(f'''tasks={len(self._tasks)}''')
        if self._errors:
            info.append(f'''errors={len(self._errors)}''')
        if self._aborting:
            info.append('cancelling')
        elif self._entered:
            info.append('entered')
        info_str = ' '.join(info)
        return f'''<TaskGroup{info_str}>'''

    
    async def __aenter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self, et, exc, tb):
        pass
    # WARNING: Decompyle incomplete

    
    async def _aexit(self, et, exc):
        pass
    # WARNING: Decompyle incomplete

    
    def create_task(self = None, coro = {
        'name': None,
        'context': None }, *, name, context):
        '''Create a new task in this group and return it.

        Similar to `asyncio.create_task`.
        '''
        if not self._entered:
            raise RuntimeError(f'''TaskGroup {self!r} has not been entered''')
        if not self._exiting and self._tasks:
            raise RuntimeError(f'''TaskGroup {self!r} is finished''')
        if self._aborting:
            raise RuntimeError(f'''TaskGroup {self!r} is shutting down''')
    # WARNING: Decompyle incomplete

    
    def _is_base_error(self = None, exc = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _abort(self):
        self._aborting = True
        for t in self._tasks:
            if t.done():
                continue
            t.cancel()

    
    def _on_task_done(self, task):
        self._tasks.discard(task)
    # WARNING: Decompyle incomplete


