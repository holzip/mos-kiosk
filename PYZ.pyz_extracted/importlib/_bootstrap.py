# Source Generated with Decompyle++
# File: _bootstrap.pyc (Python 3.12)

'''Core implementation of import.

This module is NOT meant to be directly imported! It has been designed such
that it can be bootstrapped into Python as the implementation of import. As
such it requires the injection of specific modules and attributes in order to
work. One should use importlib as the public-facing version of this module.

'''

def _object_name(obj):
    
    try:
        return obj.__qualname__
    except AttributeError:
        return 


_thread = None
_warnings = None
_weakref = None
_bootstrap_external = None

def _wrap(new, old):
    '''Simple substitute for functools.update_wrapper.'''
    for replace in ('__module__', '__name__', '__qualname__', '__doc__'):
        if not hasattr(old, replace):
            continue
        setattr(new, replace, getattr(old, replace))
    new.__dict__.update(old.__dict__)


def _new_module(name):
    return type(sys)(name)


class _List(list):
    pass


class _WeakValueDictionary:
    
    def __init__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self):
        self._pending_removals = []
        self._iterating = set()
        self.data = { }

    
    def _commit_removals(self):
        pop = self._pending_removals.pop
        d = self.data
        
        try:
            key = pop()
            _weakref._remove_dead_weakref(d, key)
            continue
        except IndexError:
            return None


    
    def get(self, key, default = (None,)):
        if self._pending_removals:
            self._commit_removals()
    # WARNING: Decompyle incomplete

    
    def setdefault(self, key, default = (None,)):
        pass
    # WARNING: Decompyle incomplete


_module_locks = { }
_blocking_on = None

class _BlockingOnManager:
    '''A context manager responsible to updating ``_blocking_on``.'''
    
    def __init__(self, thread_id, lock):
        self.thread_id = thread_id
        self.lock = lock

    
    def __enter__(self):
        '''Mark the running thread as waiting for self.lock. via _blocking_on.'''
        self.blocked_on = _blocking_on.setdefault(self.thread_id, _List())
        self.blocked_on.append(self.lock)

    
    def __exit__(self, *args, **kwargs):
        """Remove self.lock from this thread's _blocking_on list."""
        self.blocked_on.remove(self.lock)



class _DeadlockError(RuntimeError):
    pass


def _has_deadlocked(target_id, *, seen_ids, candidate_ids, blocking_on):
    """Check if 'target_id' is holding the same lock as another thread(s).

    The search within 'blocking_on' starts with the threads listed in
    'candidate_ids'.  'seen_ids' contains any threads that are considered
    already traversed in the search.

    Keyword arguments:
    target_id     -- The thread id to try to reach.
    seen_ids      -- A set of threads that have already been visited.
    candidate_ids -- The thread ids from which to begin.
    blocking_on   -- A dict representing the thread/blocking-on graph.  This may
                     be the same object as the global '_blocking_on' but it is
                     a parameter to reduce the impact that global mutable
                     state has on the result of this function.
    """
    if target_id in candidate_ids:
        return True
# WARNING: Decompyle incomplete


class _ModuleLock:
    '''A recursive lock implementation which is able to detect deadlocks
    (e.g. thread 1 trying to take locks A then B, and thread 2 trying to
    take locks B then A).
    '''
    
    def __init__(self, name):
        self.lock = _thread.RLock()
        self.wakeup = _thread.allocate_lock()
        self.name = name
        self.owner = None
        self.count = []
        self.waiters = []

    
    def has_deadlock(self):
        return _has_deadlocked(target_id = _thread.get_ident(), seen_ids = set(), candidate_ids = [
            self.owner], blocking_on = _blocking_on)

    
    def acquire(self):
        '''
        Acquire the module lock.  If a potential deadlock is detected,
        a _DeadlockError is raised.
        Otherwise, the lock is always acquired and True is returned.
        '''
        tid = _thread.get_ident()
        _BlockingOnManager(tid, self)
        self.lock
        if self.count == [] or self.owner == tid:
            self.owner = tid
            self.count.append(True)
            None(None, None)
            None(None, None)
            return True
        if self.has_deadlock():
            raise _DeadlockError(f'''deadlock detected by {self!r}''')
        if self.wakeup.acquire(False):
            self.waiters.append(None)
        None(None, None)
        self.wakeup.acquire()
        self.wakeup.release()
        continue
        with None:
            if not None:
                pass
        continue
        with None:
            if not None:
                pass

    
    def release(self):
        tid = _thread.get_ident()
        self.lock
        if self.owner != tid:
            raise RuntimeError('cannot release un-acquired lock')
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''_ModuleLock({self.name!r}) at {id(self)}'''



class _DummyModuleLock:
    '''A simple _ModuleLock equivalent for Python builds without
    multi-threading support.'''
    
    def __init__(self, name):
        self.name = name
        self.count = 0

    
    def acquire(self):
        return True

    
    def release(self):
        if self.count == 0:
            raise RuntimeError('cannot release un-acquired lock')

    
    def __repr__(self):
        return f'''_DummyModuleLock({self.name!r}) at {id(self)}'''



class _ModuleLockManager:
    
    def __init__(self, name):
        self._name = name
        self._lock = None

    
    def __enter__(self):
        self._lock = _get_module_lock(self._name)
        self._lock.acquire()

    
    def __exit__(self, *args, **kwargs):
        self._lock.release()



def _get_module_lock(name):
    '''Get or create the module lock for a given module name.

    Acquire/release internally the global import lock to protect
    _module_locks.'''
    _imp.acquire_lock()
# WARNING: Decompyle incomplete


def _lock_unlock_module(name):
    '''Acquires then releases the module lock for a given module name.

    This is used to ensure a module is completely initialized, in the
    event it is being imported by another thread.
    '''
    lock = _get_module_lock(name)
    
    try:
        lock.acquire()
        lock.release()
        return None
    except _DeadlockError:
        return None



def _call_with_frames_removed(f, *args, **kwds):
    '''remove_importlib_frames in import.c will always remove sequences
    of importlib frames that end with a call to this function

    Use it instead of a normal call in places where including the importlib
    frames introduces unwanted noise into the traceback (e.g. when executing
    module code)
    '''
    pass
# WARNING: Decompyle incomplete


def _verbose_message(message = None, *, verbosity, *args):
    '''Print the message to stderr if -v/PYTHONVERBOSE is turned on.'''
    pass
# WARNING: Decompyle incomplete


def _requires_builtin(fxn):
    '''Decorator to verify the named module is built-in.'''
    pass
# WARNING: Decompyle incomplete


def _requires_frozen(fxn):
    '''Decorator to verify the named module is frozen.'''
    pass
# WARNING: Decompyle incomplete


def _load_module_shim(self, fullname):
    '''Load the specified module into sys.modules and return it.

    This method is deprecated.  Use loader.exec_module() instead.

    '''
    msg = 'the load_module() method is deprecated and slated for removal in Python 3.15; use exec_module() instead'
    _warnings.warn(msg, DeprecationWarning)
    spec = spec_from_loader(fullname, self)
    if fullname in sys.modules:
        module = sys.modules[fullname]
        _exec(spec, module)
        return sys.modules[fullname]
    return None(spec)


def _module_repr(module):
    '''The implementation of ModuleType.__repr__().'''
    loader = getattr(module, '__loader__', None)
    spec = getattr(module, '__spec__', None)
    if getattr(module, '__spec__', None):
        return _module_repr_from_spec(spec)
# WARNING: Decompyle incomplete


class ModuleSpec:
    '''The specification for a module, used for loading.

    A module\'s spec is the source for information about the module.  For
    data associated with the module, including source, use the spec\'s
    loader.

    `name` is the absolute name of the module.  `loader` is the loader
    to use when loading the module.  `parent` is the name of the
    package the module is in.  The parent is derived from the name.

    `is_package` determines if the module is considered a package or
    not.  On modules this is reflected by the `__path__` attribute.

    `origin` is the specific location used by the loader from which to
    load the module, if that information is available.  When filename is
    set, origin will match.

    `has_location` indicates that a spec\'s "origin" reflects a location.
    When this is True, `__file__` attribute of the module is set.

    `cached` is the location of the cached bytecode file, if any.  It
    corresponds to the `__cached__` attribute.

    `submodule_search_locations` is the sequence of path entries to
    search when importing submodules.  If set, is_package should be
    True--and False otherwise.

    Packages are simply modules that (may) have submodules.  If a spec
    has a non-None value in `submodule_search_locations`, the import
    system will consider modules loaded from the spec as packages.

    Only finders (see importlib.abc.MetaPathFinder and
    importlib.abc.PathEntryFinder) should modify ModuleSpec instances.

    '''
    
    def __init__(self, name = None, loader = {
        'origin': None,
        'loader_state': None,
        'is_package': None }, *, origin, loader_state, is_package):
        self.name = name
        self.loader = loader
        self.origin = origin
        self.loader_state = loader_state
        self.submodule_search_locations = [] if is_package else None
        self._uninitialized_submodules = []
        self._set_fileattr = False
        self._cached = None

    
    def __repr__(self):
        args = [
            f'''name={self.name!r}''',
            f'''loader={self.loader!r}''']
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
        smsl = self.submodule_search_locations
        
        try:
            if self.name == other.name:
                self.name == other.name
                if self.loader == other.loader:
                    self.loader == other.loader
                    if self.origin == other.origin:
                        self.origin == other.origin
                        if smsl == other.submodule_search_locations:
                            smsl == other.submodule_search_locations
                            if self.cached == other.cached:
                                self.cached == other.cached
            return self.has_location == other.has_location
        except AttributeError:
            return 


    cached = (lambda self: pass# WARNING: Decompyle incomplete
)()
    cached = (lambda self, cached: self._cached = cached)()
    parent = (lambda self: pass# WARNING: Decompyle incomplete
)()
    has_location = (lambda self: self._set_fileattr)()
    has_location = (lambda self, value: self._set_fileattr = bool(value))()


def spec_from_loader(name = None, loader = {
    'origin': None,
    'is_package': None }, *, origin, is_package):
    '''Return a module spec based on various loader methods.'''
    pass
# WARNING: Decompyle incomplete


def _spec_from_module(module, loader, origin = (None, None)):
    pass
# WARNING: Decompyle incomplete


def _init_module_attrs(spec = None, module = {
    'override': False }, *, override):
    pass
# WARNING: Decompyle incomplete


def module_from_spec(spec):
    '''Create a module based on the provided spec.'''
    module = None
    if hasattr(spec.loader, 'create_module'):
        module = spec.loader.create_module(spec)
    elif hasattr(spec.loader, 'exec_module'):
        raise ImportError('loaders that define exec_module() must also define create_module()')
# WARNING: Decompyle incomplete


def _module_repr_from_spec(spec):
    '''Return the repr to use for the module.'''
    pass
# WARNING: Decompyle incomplete


def _exec(spec, module):
    """Execute the spec's specified module in an existing module's namespace."""
    name = spec.name
    _ModuleLockManager(name)
    if sys.modules.get(name) is not module:
        msg = f'''module {name!r} not in sys.modules'''
        raise ImportError(msg, name = name)
# WARNING: Decompyle incomplete


def _load_backward_compatible(spec):
    pass
# WARNING: Decompyle incomplete


def _load_unlocked(spec):
    pass
# WARNING: Decompyle incomplete


def _load(spec):
    """Return a new module object, loaded by the spec's loader.

    The module is not added to its parent.

    If a module is already in sys.modules, that existing module gets
    clobbered.

    """
    _ModuleLockManager(spec.name)
    None(None, None)
    return 
    with None:
        if not None, _load_unlocked(spec):
            pass


class BuiltinImporter:
    '''Meta path import for built-in modules.

    All methods are either class or static methods to avoid the need to
    instantiate the class.

    '''
    _ORIGIN = 'built-in'
    find_spec = (lambda cls, fullname, path, target = (None, None): if _imp.is_builtin(fullname):
spec_from_loader(fullname, cls, origin = cls._ORIGIN))()
    create_module = (lambda spec: if spec.name not in sys.builtin_module_names:
raise ImportError(f'''{spec.name!r} is not a built-in module''', name = spec.name)_call_with_frames_removed(_imp.create_builtin, spec))()
    exec_module = (lambda module: _call_with_frames_removed(_imp.exec_builtin, module))()
    get_code = (lambda cls, fullname: pass)()()
    get_source = (lambda cls, fullname: pass)()()
    is_package = (lambda cls, fullname: False)()()
    load_module = classmethod(_load_module_shim)


class FrozenImporter:
    '''Meta path import for frozen modules.

    All methods are either class or static methods to avoid the need to
    instantiate the class.

    '''
    _ORIGIN = 'frozen'
    _fix_up_module = (lambda cls, module: spec = module.__spec__state = spec.loader_state# WARNING: Decompyle incomplete
)()
    _resolve_filename = (lambda cls, fullname, alias, ispkg = (None, False): if not fullname or getattr(sys, '_stdlib_dir', None):
(None, None)try:
sep = cls._SEPif fullname != alias:
if fullname.startswith('<'):
fullname = fullname[1:]if not ispkg:
fullname = f'''{fullname}.__init__'''else:
ispkg = Falserelfile = fullname.replace('.', sep)if ispkg:
pkgdir = f'''{sys._stdlib_dir}{sep}{relfile}'''filename = f'''{pkgdir}{sep}__init__.py'''(filename, pkgdir)pkgdir = Nonefilename = f'''{sys._stdlib_dir}{sep}{relfile}.py'''(filename, pkgdir)except AttributeError:
sep = '\\' if sys.platform == 'win32' else '/'cls._SEP = '\\' if sys.platform == 'win32' else '/'continue)()
    find_spec = (lambda cls, fullname, path, target = (None, None): info = _call_with_frames_removed(_imp.find_frozen, fullname)# WARNING: Decompyle incomplete
)()
    create_module = (lambda spec: module = _new_module(spec.name)try:
filename = spec.loader_state.filenameif filename:
module.__file__ = filenamemoduleexcept AttributeError:
module)()
    exec_module = (lambda module: spec = module.__spec__name = spec.namecode = _call_with_frames_removed(_imp.get_frozen_object, name)exec(code, module.__dict__))()
    load_module = (lambda cls, fullname: module = _load_module_shim(cls, fullname)info = _imp.find_frozen(fullname)# WARNING: Decompyle incomplete
)()
    get_code = (lambda cls, fullname: _imp.get_frozen_object(fullname))()()
    get_source = (lambda cls, fullname: pass)()()
    is_package = (lambda cls, fullname: _imp.is_frozen_package(fullname))()()


class _ImportLockContext:
    '''Context manager for the import lock.'''
    
    def __enter__(self):
        '''Acquire the import lock.'''
        _imp.acquire_lock()

    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''Release the import lock regardless of any raised exceptions.'''
        _imp.release_lock()



def _resolve_name(name, package, level):
    '''Resolve a relative module name to an absolute one.'''
    bits = package.rsplit('.', level - 1)
    if len(bits) < level:
        raise ImportError('attempted relative import beyond top-level package')
    base = bits[0]
    if name:
        return f'''{base}.{name}'''


def _find_spec(name, path, target = (None,)):
    """Find a module's spec."""
    meta_path = sys.meta_path
# WARNING: Decompyle incomplete


def _sanity_check(name, package, level):
    '''Verify arguments are "sane".'''
    if not isinstance(name, str):
        raise TypeError(f'''module name must be str, not {type(name)}''')
    if level < 0:
        raise ValueError('level must be >= 0')
    if level > 0:
        if not isinstance(package, str):
            raise TypeError('__package__ not set to a string')
        if not package:
            raise ImportError('attempted relative import with no known parent package')
    if not name:
        if level == 0:
            raise ValueError('Empty module name')
        return None

_ERR_MSG_PREFIX = 'No module named '
_ERR_MSG = _ERR_MSG_PREFIX + '{!r}'

def _find_and_load_unlocked(name, import_):
    path = None
    parent = name.rpartition('.')[0]
    parent_spec = None
# WARNING: Decompyle incomplete

_NEEDS_LOADING = object()

def _find_and_load(name, import_):
    '''Find and load the module.'''
    module = sys.modules.get(name, _NEEDS_LOADING)
    if module is _NEEDS_LOADING or getattr(getattr(module, '__spec__', None), '_initializing', False):
        _ModuleLockManager(name)
        module = sys.modules.get(name, _NEEDS_LOADING)
        if module is _NEEDS_LOADING:
            None(None, None)
            return 
        None(None, None)
        _lock_unlock_module(name)
# WARNING: Decompyle incomplete


def _gcd_import(name, package, level = (None, 0)):
    '''Import and return the module based on its name, the package the call is
    being made from, and the level adjustment.

    This function represents the greatest common denominator of functionality
    between import_module and __import__. This includes setting __package__ if
    the loader did not.

    '''
    _sanity_check(name, package, level)
    if level > 0:
        name = _resolve_name(name, package, level)
    return _find_and_load(name, _gcd_import)


def _handle_fromlist(module, fromlist = None, import_ = {
    'recursive': False }, *, recursive):
    """Figure out what __import__ should return.

    The import_ parameter is a callable which takes the name of module to
    import. It is required to decouple the function from assuming importlib's
    import implementation is desired.

    """
    for x in fromlist:
        if not isinstance(x, str):
            raise TypeError(f'''Item in {where} must be str, not {type(x).__name__}''')
        if x == '*':
            if recursive:
                continue
            if not hasattr(module, '__all__'):
                continue
            _handle_fromlist(module, module.__all__, import_, recursive = True)
            continue
        if hasattr(module, x):
            continue
        from_name = f'''{module.__name__}.{x}'''
        _call_with_frames_removed(import_, from_name)
    return module
# WARNING: Decompyle incomplete


def _calc___package__(globals):
    '''Calculate what __package__ should be.

    __package__ is not guaranteed to be defined or could be set to None
    to represent that its proper value is unknown.

    '''
    package = globals.get('__package__')
    spec = globals.get('__spec__')
# WARNING: Decompyle incomplete


def __import__(name, globals, locals, fromlist, level = (None, None, (), 0)):
    """Import a module.

    The 'globals' argument is used to infer where the import is occurring from
    to handle relative imports. The 'locals' argument is ignored. The
    'fromlist' argument specifies what should exist as attributes on the module
    being imported (e.g. ``from module import <fromlist>``).  The 'level'
    argument represents the package location to import from in a relative
    import (e.g. ``from ..pkg import mod`` would have a 'level' of 2).

    """
    if level == 0:
        module = _gcd_import(name)
# WARNING: Decompyle incomplete


def _builtin_from_name(name):
    spec = BuiltinImporter.find_spec(name)
# WARNING: Decompyle incomplete


def _setup(sys_module, _imp_module):
    '''Setup importlib by importing needed built-in modules and injecting them
    into the global namespace.

    As sys is needed for sys.modules access and _imp is needed to load built-in
    modules, those two modules must be explicitly passed in.

    '''
    global _imp, sys, _blocking_on
    _imp = _imp_module
    sys = sys_module
    module_type = type(sys)
    for name, module in sys.modules.items():
        if not isinstance(module, module_type):
            continue
        if name in sys.builtin_module_names:
            loader = BuiltinImporter
        elif _imp.is_frozen(name):
            loader = FrozenImporter
        
        spec = _spec_from_module(module, loader)
        _init_module_attrs(spec, module)
        if not loader is FrozenImporter:
            continue
        loader._fix_up_module(module)
    self_module = sys.modules[__name__]
    for builtin_name in ('_thread', '_warnings', '_weakref'):
        setattr(self_module, builtin_name, builtin_module)
    _blocking_on = _WeakValueDictionary()


def _install(sys_module, _imp_module):
    '''Install importers for builtin and frozen modules'''
    _setup(sys_module, _imp_module)
    sys.meta_path.append(BuiltinImporter)
    sys.meta_path.append(FrozenImporter)


def _install_external_importers():
    '''Install importers that require external filesystem access'''
    global _bootstrap_external
    import _frozen_importlib_external
    _bootstrap_external = _frozen_importlib_external
    _frozen_importlib_external._install(sys.modules[__name__])

