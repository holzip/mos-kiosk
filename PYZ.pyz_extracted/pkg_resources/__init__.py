# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

'''
Package resource API
--------------------

A resource is a logical file contained within a package, or a logical
subdirectory thereof.  The package resource API expects resource names
to have their path parts separated with ``/``, *not* whatever the local
path separator is.  Do not use os.path operations to manipulate resource
names being passed into the API.

The package resource API is designed to work with normal filesystem packages,
.egg files, and unpacked .egg files.  It can also work in a limited way with
.zip files and with custom PEP 302 loaders that support the ``get_data()``
method.

This module is deprecated. Users are directed to :mod:`importlib.resources`,
:mod:`importlib.metadata` and :pypi:`packaging` instead.
'''
from __future__ import annotations
import sys
if sys.version_info < (3, 9):
    raise RuntimeError('Python 3.9 or later is required')
import _imp
import collections
import email.parser as email
import errno
import functools
import importlib
import importlib.abc as importlib
import importlib.machinery as importlib
import inspect
import io
import ntpath
import operator
import os
import pkgutil
import platform
import plistlib
import posixpath
import re
import stat
import tempfile
import textwrap
import time
import types
import warnings
import zipfile
import zipimport
from collections.abc import Iterable, Iterator, Mapping, MutableSequence
from pkgutil import get_importer
from typing import TYPE_CHECKING, Any, BinaryIO, Callable, Literal, NamedTuple, NoReturn, Protocol, TypeVar, Union, overload
vendor_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'setuptools', '_vendor')
sys.path.extend((os.path.join(os.path.dirname(os.path.dirname(__file__)), 'setuptools', '_vendor') not in sys.path) * [
    vendor_path])
sys.modules.pop('backports', None)
from os import open as os_open, utime
from os.path import isdir, split

try:
    from os import mkdir, rename, unlink
    WRITE_SUPPORT = True
    import packaging.markers as packaging
    import packaging.requirements as packaging
    import packaging.specifiers as packaging
    import packaging.utils as packaging
    import packaging.version as packaging
    from jaraco.text import drop_comment, join_continuation, yield_lines
    from platformdirs import user_cache_dir as _user_cache_dir
    if TYPE_CHECKING:
        from _typeshed import BytesPath, StrOrBytesPath, StrPath
        from _typeshed.importlib import LoaderProtocol
        from typing_extensions import Self, TypeAlias
    warnings.warn('pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html', DeprecationWarning, stacklevel = 2)
    _T = TypeVar('_T')
    _DistributionT = TypeVar('_DistributionT', bound = 'Distribution')
    _NestedStr: 'TypeAlias' = Union[(str, Iterable[Union[(str, Iterable['_NestedStr'])]])]
    _StrictInstallerType: 'TypeAlias' = Callable[([
        'Requirement'], '_DistributionT')]
    _InstallerType: 'TypeAlias' = Callable[([
        'Requirement'], Union[('Distribution', None)])]
    _PkgReqType: 'TypeAlias' = Union[(str, 'Requirement')]
    _EPDistType: 'TypeAlias' = Union[('Distribution', _PkgReqType)]
    _MetadataType: 'TypeAlias' = Union[('IResourceProvider', None)]
    _ResolvedEntryPoint: 'TypeAlias' = Any
    _ResourceStream: 'TypeAlias' = Any
    _ModuleLike: 'TypeAlias' = Union[(object, types.ModuleType)]
    _ProviderFactoryType: 'TypeAlias' = Callable[([
        Any], 'IResourceProvider')]
    _DistFinderType: 'TypeAlias' = Callable[([
        _T,
        str,
        bool], Iterable['Distribution'])]
    _NSHandlerType: 'TypeAlias' = Callable[([
        _T,
        str,
        str,
        types.ModuleType], Union[(str, None)])]
    _AdapterT = TypeVar('_AdapterT', _DistFinderType[Any], _ProviderFactoryType, _NSHandlerType[Any])
    
    class _ZipLoaderModule(Protocol):
        __loader__: 'zipimport.zipimporter' = '_ZipLoaderModule'

    _PEP440_FALLBACK = re.compile('^v?(?P<safe>(?:[0-9]+!)?[0-9]+(?:\\.[0-9]+)*)', re.I)
    
    class PEP440Warning(RuntimeWarning):
        '''
    Used when there is an issue with a version or specifier not complying with
    PEP 440.
    '''
        pass

    parse_version = packaging.version.Version
    _state_vars: 'dict[str, str]' = { }
    
    def _declare_state(vartype = None, varname = None, initial_value = None):
        _state_vars[varname] = vartype
        return initial_value

    
    def __getstate__():
        state = { }
        g = globals()
        for k, v in _state_vars.items():
            state[k] = g['_sget_' + v](g[k])
        return state

    
    def __setstate__(state = None):
        g = globals()
        for k, v in state.items():
            g['_sset_' + _state_vars[k]](k, g[k], v)
        return state

    
    def _sget_dict(val):
        return val.copy()

    
    def _sset_dict(key = None, ob = None, state = None):
        ob.clear()
        ob.update(state)

    
    def _sget_object(val):
        return val.__getstate__()

    
    def _sset_object(key = None, ob = None, state = None):
        ob.__setstate__(state)

    
    _sget_none = lambda *args: pass
    
    _sset_none = lambda *args: pass
    
    def get_supported_platform():
        """Return this platform's maximum compatible version.

    distutils.util.get_platform() normally reports the minimum version
    of macOS that would be required to *use* extensions produced by
    distutils.  But what we want when checking compatibility is to know the
    version of macOS that we are *running*.  To allow usage of packages that
    explicitly require a newer version of macOS, we must also know the
    current version of the OS.

    If this condition occurs for any other platform with a version in its
    platform strings, this function should be extended accordingly.
    """
        plat = get_build_platform()
        m = macosVersionString.match(plat)
    # WARNING: Decompyle incomplete

    __all__ = [
        'require',
        'run_script',
        'get_provider',
        'get_distribution',
        'load_entry_point',
        'get_entry_map',
        'get_entry_info',
        'iter_entry_points',
        'resource_string',
        'resource_stream',
        'resource_filename',
        'resource_listdir',
        'resource_exists',
        'resource_isdir',
        'declare_namespace',
        'working_set',
        'add_activation_listener',
        'find_distributions',
        'set_extraction_path',
        'cleanup_resources',
        'get_default_cache',
        'Environment',
        'WorkingSet',
        'ResourceManager',
        'Distribution',
        'Requirement',
        'EntryPoint',
        'ResolutionError',
        'VersionConflict',
        'DistributionNotFound',
        'UnknownExtra',
        'ExtractionError',
        'PEP440Warning',
        'parse_requirements',
        'parse_version',
        'safe_name',
        'safe_version',
        'get_platform',
        'compatible_platforms',
        'yield_lines',
        'split_sections',
        'safe_extra',
        'to_filename',
        'invalid_marker',
        'evaluate_marker',
        'ensure_directory',
        'normalize_path',
        'EGG_DIST',
        'BINARY_DIST',
        'SOURCE_DIST',
        'CHECKOUT_DIST',
        'DEVELOP_DIST',
        'IMetadataProvider',
        'IResourceProvider',
        'FileMetadata',
        'PathMetadata',
        'EggMetadata',
        'EmptyProvider',
        'empty_provider',
        'NullProvider',
        'EggProvider',
        'DefaultProvider',
        'ZipProvider',
        'register_finder',
        'register_namespace_handler',
        'register_loader_type',
        'fixup_namespace_packages',
        'get_importer',
        'PkgResourcesDeprecationWarning',
        'run_main',
        'AvailableDistributions']
    
    class ResolutionError(Exception):
        '''Abstract base for dependency resolution errors'''
        
        def __repr__(self = None):
            return self.__class__.__name__ + repr(self.args)


    
    class VersionConflict(ResolutionError):
        '''
    An already-installed version conflicts with the requested version.

    Should be initialized with the installed Distribution and the requested
    Requirement.
    '''
        _template = '{self.dist} is installed but {self.req} is required'
        dist = (lambda self = None: self.args[0])()
        req = (lambda self = None: self.args[1])()
        
        def report(self):
            pass
        # WARNING: Decompyle incomplete

        
        def with_context(self = None, required_by = None):
            '''
        If required_by is non-empty, return a version of self that is a
        ContextualVersionConflict.
        '''
            if not required_by:
                return self
            args = None.args + (required_by,)
        # WARNING: Decompyle incomplete


    
    class ContextualVersionConflict(VersionConflict):
        '''
    A VersionConflict that accepts a third parameter, the set of the
    requirements that required the installed Distribution.
    '''
        _template = VersionConflict._template + ' by {self.required_by}'
        required_by = (lambda self = None: self.args[2])()

    
    class DistributionNotFound(ResolutionError):
        '''A requested distribution was not found'''
        _template = "The '{self.req}' distribution was not found and is required by {self.requirers_str}"
        req = (lambda self = None: self.args[0])()
        requirers = (lambda self = None: self.args[1])()
        requirers_str = (lambda self: if not self.requirers:
'the application'', '.join(self.requirers))()
        
        def report(self):
            pass
        # WARNING: Decompyle incomplete

        
        def __str__(self = None):
            return self.report()


    
    class UnknownExtra(ResolutionError):
        '''Distribution doesn\'t have an "extra feature" of the given name'''
        pass

    _provider_factories: 'dict[type[_ModuleLike], _ProviderFactoryType]' = { }
    PY_MAJOR = f'''{sys.version_info.major}.{sys.version_info.minor}'''
    EGG_DIST = 3
    BINARY_DIST = 2
    SOURCE_DIST = 1
    CHECKOUT_DIST = 0
    DEVELOP_DIST = -1
    
    def register_loader_type(loader_type = None, provider_factory = None):
        '''Register `provider_factory` to make providers for `loader_type`

    `loader_type` is the type or class of a PEP 302 ``module.__loader__``,
    and `provider_factory` is a function that, passed a *module* object,
    returns an ``IResourceProvider`` for that module.
    '''
        _provider_factories[loader_type] = provider_factory

    get_provider = (lambda moduleOrReq = None: pass)()
    get_provider = (lambda moduleOrReq = None: pass)()
    
    def get_provider(moduleOrReq = None):
        '''Return an IResourceProvider for the named module or requirement'''
        if isinstance(moduleOrReq, Requirement):
            if not working_set.find(moduleOrReq):
                working_set.find(moduleOrReq)
            return require(str(moduleOrReq))[0]
        
        try:
            module = sys.modules[moduleOrReq]
            loader = getattr(module, '__loader__', None)
            return _find_adapter(_provider_factories, loader)(module)
        except KeyError:
            __import__(moduleOrReq)
            module = sys.modules[moduleOrReq]
            continue


    _macos_vers = (lambda : version = platform.mac_ver()[0]# WARNING: Decompyle incomplete
)()
    
    def _macos_arch(machine):
        return {
            'PowerPC': 'ppc',
            'Power_Macintosh': 'ppc' }.get(machine, machine)

    
    def get_build_platform():
        """Return this platform's string for platform-specific distributions

    XXX Currently this is the same as ``distutils.util.get_platform()``, but it
    needs some hacks for Linux and macOS.
    """
        get_platform = get_platform
        import sysconfig
        plat = get_platform()
        if not sys.platform == 'darwin' and plat.startswith('macosx-'):
            
            try:
                version = _macos_vers()
                machine = _macos_arch(os.uname()[4].replace(' ', '_'))
                return f'''macosx-{version[0]}.{version[1]}-{machine}'''
                return plat
            except ValueError:
                return plat


    macosVersionString = re.compile('macosx-(\\d+)\\.(\\d+)-(.*)')
    darwinVersionString = re.compile('darwin-(\\d+)\\.(\\d+)\\.(\\d+)-(.*)')
    get_platform = get_build_platform
    
    def compatible_platforms(provided = None, required = None):
        '''Can code for the `provided` platform run on the `required` platform?

    Returns true if either platform is ``None``, or the platforms are equal.

    XXX Needs compatibility checks for Linux and other unixy OSes.
    '''
        pass
    # WARNING: Decompyle incomplete

    get_distribution = (lambda dist = None: pass)()
    get_distribution = (lambda dist = None: pass)()
    
    def get_distribution(dist = None):
        '''Return a current distribution object for a Requirement or string'''
        if isinstance(dist, str):
            dist = Requirement.parse(dist)
        if isinstance(dist, Requirement):
            dist = get_provider(dist)
        if not isinstance(dist, Distribution):
            raise TypeError('Expected str, Requirement, or Distribution', dist)
        return dist

    
    def load_entry_point(dist = None, group = None, name = None):
        '''Return `name` entry point of `group` for `dist` or raise ImportError'''
        return get_distribution(dist).load_entry_point(group, name)

    get_entry_map = (lambda dist = None, group = None: pass)()
    get_entry_map = (lambda dist = None, group = None: pass)()
    
    def get_entry_map(dist = None, group = None):
        '''Return the entry point map for `group`, or the full entry map'''
        return get_distribution(dist).get_entry_map(group)

    
    def get_entry_info(dist = None, group = None, name = None):
        '''Return the EntryPoint object for `group`+`name`, or ``None``'''
        return get_distribution(dist).get_entry_info(group, name)

    
    class IMetadataProvider(Protocol):
        
        def has_metadata(self = None, name = None):
            """Does the package's distribution contain the named metadata?"""
            pass

        
        def get_metadata(self = None, name = None):
            '''The named metadata resource as a string'''
            pass

        
        def get_metadata_lines(self = None, name = None):
            '''Yield named metadata resource as list of non-blank non-comment lines

        Leading and trailing whitespace is stripped from each line, and lines
        with ``#`` as the first non-blank character are omitted.'''
            pass

        
        def metadata_isdir(self = None, name = None):
            '''Is the named metadata a directory?  (like ``os.path.isdir()``)'''
            pass

        
        def metadata_listdir(self = None, name = None):
            '''List of metadata names in the directory (like ``os.listdir()``)'''
            pass

        
        def run_script(self = None, script_name = None, namespace = None):
            '''Execute the named script in the supplied namespace dictionary'''
            pass


    
    class IResourceProvider(Protocol, IMetadataProvider):
        '''An object that provides access to package resources'''
        
        def get_resource_filename(self = None, manager = None, resource_name = None):
            '''Return a true filesystem path for `resource_name`

        `manager` must be a ``ResourceManager``'''
            pass

        
        def get_resource_stream(self = None, manager = None, resource_name = None):
            '''Return a readable file-like object for `resource_name`

        `manager` must be a ``ResourceManager``'''
            pass

        
        def get_resource_string(self = None, manager = None, resource_name = None):
            '''Return the contents of `resource_name` as :obj:`bytes`

        `manager` must be a ``ResourceManager``'''
            pass

        
        def has_resource(self = None, resource_name = None):
            '''Does the package contain the named resource?'''
            pass

        
        def resource_isdir(self = None, resource_name = None):
            '''Is the named resource a directory?  (like ``os.path.isdir()``)'''
            pass

        
        def resource_listdir(self = None, resource_name = None):
            '''List of resource names in the directory (like ``os.listdir()``)'''
            pass


    
    class WorkingSet:
        '''A collection of active distributions on sys.path (or a similar list)'''
        
        def __init__(self = None, entries = None):
            '''Create working set from list of path entries (default=sys.path)'''
            self.entries = []
            self.entry_keys = { }
            self.by_key = { }
            self.normalized_to_canonical_keys = { }
            self.callbacks = []
        # WARNING: Decompyle incomplete

        _build_master = (lambda cls: ws = cls()try:
__requires__ = __requires__import __main__try:
ws.require(__requires__)wsexcept ImportError:
except VersionConflict:
)()
        _build_from_requirements = (lambda cls, req_spec: ws = cls([])reqs = parse_requirements(req_spec)dists = ws.resolve(reqs, Environment())for dist in dists:
ws.add(dist)for entry in sys.path:
if not entry not in ws.entries:
continuews.add_entry(entry)sys.path[:] = ws.entriesws)()
        
        def add_entry(self = None, entry = classmethod):
            '''Add a path item to ``.entries``, finding any distributions on it

        ``find_distributions(entry, True)`` is used to find distributions
        corresponding to the path entry, and they are added.  `entry` is
        always appended to ``.entries``, even if it is already present.
        (This is because ``sys.path`` can contain the same value more than
        once, and the ``.entries`` of the ``sys.path`` WorkingSet should always
        equal ``sys.path``.)
        '''
            self.entry_keys.setdefault(entry, [])
            self.entries.append(entry)
            for dist in find_distributions(entry, True):
                self.add(dist, entry, False)

        
        def __contains__(self = None, dist = None):
            '''True if `dist` is the active distribution for its project'''
            return self.by_key.get(dist.key) == dist

        
        def find(self = None, req = None):
            '''Find a distribution matching requirement `req`

        If there is an active distribution for the requested project, this
        returns it as long as it meets the version requirement specified by
        `req`.  But, if there is an active distribution for the project and it
        does *not* meet the `req` requirement, ``VersionConflict`` is raised.
        If there is no active distribution for the requested project, ``None``
        is returned.
        '''
            dist = None
            candidates = (req.key, self.normalized_to_canonical_keys.get(req.key), safe_name(req.key).replace('.', '-'))
            for candidate in filter(None, candidates):
                dist = self.by_key.get(candidate)
                if not dist:
                    continue
                req.key = candidate
                filter(None, candidates)
        # WARNING: Decompyle incomplete

        
        def iter_entry_points(self = None, group = None, name = None):
            '''Yield entry point objects from `group` matching `name`

        If `name` is None, yields all entry points in `group` from all
        distributions in the working set, otherwise only ones matching
        both `group` and `name` are yielded (in distribution order).
        '''
            pass
        # WARNING: Decompyle incomplete

        
        def run_script(self = None, requires = None, script_name = None):
            '''Locate distribution for `requires` and run `script_name` script'''
            ns = sys._getframe(1).f_globals
            name = ns['__name__']
            ns.clear()
            ns['__name__'] = name
            self.require(requires)[0].run_script(script_name, ns)

        
        def __iter__(self = None):
            """Yield distributions for non-duplicate projects in the working set

        The yield order is the order in which the items' path entries were
        added to the working set.
        """
            pass
        # WARNING: Decompyle incomplete

        
        def add(self = None, dist = None, entry = None, insert = (None, True, False), replace = ('dist', 'Distribution', 'entry', 'str | None', 'insert', 'bool', 'replace', 'bool', 'return', 'None')):
            """Add `dist` to working set, associated with `entry`

        If `entry` is unspecified, it defaults to the ``.location`` of `dist`.
        On exit from this routine, `entry` is added to the end of the working
        set's ``.entries`` (if it wasn't already present).

        `dist` is only added to the working set if it's for a project that
        doesn't already have a distribution in the set, unless `replace=True`.
        If it's added, any callbacks registered with the ``subscribe()`` method
        will be called.
        """
            if insert:
                dist.insert_on(self.entries, entry, replace = replace)
        # WARNING: Decompyle incomplete

        resolve = (lambda self, requirements = None, env = None, installer = overload, replace_conflicting = (False, None), extras = ('requirements', 'Iterable[Requirement]', 'env', 'Environment | None', 'installer', '_StrictInstallerType[_DistributionT]', 'replace_conflicting', 'bool', 'extras', 'tuple[str, ...] | None', 'return', 'list[_DistributionT]'): pass)()
        resolve = (lambda self = None, requirements = None, env = None, *, installer, replace_conflicting, extras: pass)()
        resolve = (lambda self, requirements = None, env = None, installer = overload, replace_conflicting = (None, None, False, None), extras = ('requirements', 'Iterable[Requirement]', 'env', 'Environment | None', 'installer', '_InstallerType | None', 'replace_conflicting', 'bool', 'extras', 'tuple[str, ...] | None', 'return', 'list[Distribution]'): pass)()
        
        def resolve(self, requirements = None, env = None, installer = None, replace_conflicting = (None, None, False, None), extras = ('requirements', 'Iterable[Requirement]', 'env', 'Environment | None', 'installer', '_InstallerType | None | _StrictInstallerType[_DistributionT]', 'replace_conflicting', 'bool', 'extras', 'tuple[str, ...] | None', 'return', 'list[Distribution] | list[_DistributionT]')):
            '''List all distributions needed to (recursively) meet `requirements`

        `requirements` must be a sequence of ``Requirement`` objects.  `env`,
        if supplied, should be an ``Environment`` instance.  If
        not supplied, it defaults to all distributions available within any
        entry or distribution in the working set.  `installer`, if supplied,
        will be invoked with each requirement that cannot be met by an
        already-installed distribution; it should return a ``Distribution`` or
        ``None``.

        Unless `replace_conflicting=True`, raises a VersionConflict exception
        if
        any requirements are found on the path that have the correct name but
        the wrong version.  Otherwise, if an `installer` is supplied it will be
        invoked to obtain the correct version of the requirement and activate
        it.

        `extras` is a list of the extras to be used with these requirements.
        This is important because extra requirements may look like `my_req;
        extra = "my_extra"`, which would otherwise be interpreted as a purely
        optional requirement.  Instead, we want to be able to assert that these
        requirements are truly required.
        '''
            requirements = list(requirements)[::-1]
            processed = set()
            best = { }
            to_activate = []
            req_extras = _ReqExtras()
            required_by = collections.defaultdict[(Requirement, set[str])](set)
            if requirements:
                req = requirements.pop(0)
                if req in processed:
                    continue
                if not req_extras.markers_pass(req, extras):
                    continue
                dist = self._resolve_dist(req, best, replace_conflicting, env, installer, required_by, to_activate)
                new_requirements = dist.requires(req.extras)[::-1]
                requirements.extend(new_requirements)
                for new_requirement in new_requirements:
                    required_by[new_requirement].add(req.project_name)
                    req_extras[new_requirement] = req.extras
                processed.add(req)
                if requirements:
                    continue
            return to_activate

        
        def _resolve_dist(self, req, best, replace_conflicting, env = None, installer = None, required_by = None, to_activate = ('return', 'Distribution')):
            dist = best.get(req.key)
        # WARNING: Decompyle incomplete

        find_plugins = (lambda self = None, plugin_env = None, full_env = overload, installer = (True,), fallback = ('plugin_env', 'Environment', 'full_env', 'Environment | None', 'installer', '_StrictInstallerType[_DistributionT]', 'fallback', 'bool', 'return', 'tuple[list[_DistributionT], dict[Distribution, Exception]]'): pass)()
        find_plugins = (lambda self = None, plugin_env = None, full_env = None, *, installer, fallback, 