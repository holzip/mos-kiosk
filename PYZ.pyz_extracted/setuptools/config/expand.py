# Source Generated with Decompyle++
# File: expand.pyc (Python 3.12)

'''Utility functions to expand configuration directives or special values
(such glob patterns).

We can split the process of interpreting configuration files into 2 steps:

1. The parsing the file contents from strings to value objects
   that can be understand by Python (for example a string with a comma
   separated list of keywords into an actual Python list of strings).

2. The expansion (or post-processing) of these values according to the
   semantics ``setuptools`` assign to them (for example a configuration field
   with the ``file:`` directive should be expanded from a list of file paths to
   a single string with the contents of those files concatenated)

This module focus on the second step, and therefore allow sharing the expansion
functions among several configuration file formats.

**PRIVATE MODULE**: API reserved for setuptools internal usage only.
'''
from __future__ import annotations
import ast
import importlib
import os
import pathlib
import sys
from collections.abc import Iterable, Iterator, Mapping
from configparser import ConfigParser
from glob import iglob
from importlib.machinery import ModuleSpec, all_suffixes
from itertools import chain
from pathlib import Path
from types import ModuleType, TracebackType
from typing import TYPE_CHECKING, Any, Callable, TypeVar
from  import _static
from _path import StrPath, same_path as _same_path
from discovery import find_package_path
from warnings import SetuptoolsWarning
from distutils.errors import DistutilsOptionError
if TYPE_CHECKING:
    from typing_extensions import Self
    from setuptools.dist import Distribution
_K = TypeVar('_K')
_V_co = TypeVar('_V_co', covariant = True)

class StaticModule:
    '''Proxy to a module object that avoids executing arbitrary code.'''
    
    def __init__(self = None, name = None, spec = None):
        module = ast.parse(pathlib.Path(spec.origin).read_bytes())
        vars(self).update(locals())
        del self.self

    
    def _find_assignments(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, attr = None):
        '''Attempt to load an attribute "statically", via :func:`ast.literal_eval`.'''
        pass
    # WARNING: Decompyle incomplete



def glob_relative(patterns = None, root_dir = None):
    '''Expand the list of glob patterns, but preserving relative paths.

    :param list[str] patterns: List of glob patterns
    :param str root_dir: Path to which globs should be relative
                         (current directory by default)
    :rtype: list
    '''
    pass
# WARNING: Decompyle incomplete


def read_files(filepaths = None, root_dir = None):
    """Return the content of the files concatenated using ``
`` as str

    This function is sandboxed and won't reach anything outside ``root_dir``

    (By default ``root_dir`` is the current directory).
    """
    pass
# WARNING: Decompyle incomplete


def _filter_existing_files(filepaths = None):
    pass
# WARNING: Decompyle incomplete


def _read_file(filepath = None):
    f = open(filepath, encoding = 'utf-8')
    None(None, None)
    return 
    with None:
        if not None, f.read():
            pass


def _assert_local(filepath = None, root_dir = None):
    if Path(os.path.abspath(root_dir)) not in Path(os.path.abspath(filepath)).parents:
        msg = f'''Cannot access {filepath!r} (or anything outside {root_dir!r})'''
        raise DistutilsOptionError(msg)
    return True


def read_attr(attr_desc = None, package_dir = None, root_dir = None):
    '''Reads the value of an attribute from a module.

    This function will try to read the attributed statically first
    (via :func:`ast.literal_eval`), and only evaluate the module if it fails.

    Examples:
        read_attr("package.attr")
        read_attr("package.module.attr")

    :param str attr_desc: Dot-separated string describing how to reach the
        attribute (see examples above)
    :param dict[str, str] package_dir: Mapping of package names to their
        location in disk (represented by paths relative to ``root_dir``).
    :param str root_dir: Path to directory containing all the packages in
        ``package_dir`` (current directory by default).
    :rtype: str
    '''
    if not root_dir:
        root_dir
    root_dir = os.getcwd()
    attrs_path = attr_desc.strip().split('.')
    attr_name = attrs_path.pop()
    module_name = '.'.join(attrs_path)
    if not module_name:
        module_name
    module_name = '__init__'
    path = _find_module(module_name, package_dir, root_dir)
    spec = _find_spec(module_name, path)
    
    try:
        value = getattr(StaticModule(module_name, spec), attr_name)
        return _static.attempt_conversion(value)
    except Exception:
        module = _load_spec(spec, module_name)
        return 



def _find_spec(module_name = None, module_path = None):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if not spec:
        spec
    spec = importlib.util.find_spec(module_name)
# WARNING: Decompyle incomplete


def _load_spec(spec = None, module_name = None):
    name = getattr(spec, '__name__', module_name)
    if name in sys.modules:
        return sys.modules[name]
    module = None.util.module_from_spec(spec)
    sys.modules[name] = module
# WARNING: Decompyle incomplete


def _find_module(module_name = None, package_dir = None, root_dir = None):
    '''Find the path to the module named ``module_name``,
    considering the ``package_dir`` in the build configuration and ``root_dir``.

    >>> tmp = getfixture(\'tmpdir\')
    >>> _ = tmp.ensure("a/b/c.py")
    >>> _ = tmp.ensure("a/b/d/__init__.py")
    >>> r = lambda x: x.replace(str(tmp), "tmp").replace(os.sep, "/")
    >>> r(_find_module("a.b.c", None, tmp))
    \'tmp/a/b/c.py\'
    >>> r(_find_module("f.g.h", {"": "1", "f": "2", "f.g": "3", "f.g.h": "a/b/d"}, tmp))
    \'tmp/a/b/d/__init__.py\'
    '''
    pass
# WARNING: Decompyle incomplete


def resolve_class(qualified_class_name = None, package_dir = None, root_dir = None):
    '''Given a qualified class name, return the associated class object'''
    if not root_dir:
        root_dir
    root_dir = os.getcwd()
    idx = qualified_class_name.rfind('.')
    class_name = qualified_class_name[idx + 1:]
    pkg_name = qualified_class_name[:idx]
    path = _find_module(pkg_name, package_dir, root_dir)
    module = _load_spec(_find_spec(pkg_name, path), pkg_name)
    return getattr(module, class_name)


def cmdclass(values = None, package_dir = None, root_dir = None):
    '''Given a dictionary mapping command names to strings for qualified class
    names, apply :func:`resolve_class` to the dict values.
    '''
    pass
# WARNING: Decompyle incomplete


def find_packages(*, namespaces, fill_package_dir, root_dir, **kwargs):
    '''Works similarly to :func:`setuptools.find_packages`, but with all
    arguments given as keyword arguments. Moreover, ``where`` can be given
    as a list (the results will be simply concatenated).

    When the additional keyword argument ``namespaces`` is ``True``, it will
    behave like :func:`setuptools.find_namespace_packages`` (i.e. include
    implicit namespaces as per :pep:`420`).

    The ``where`` argument will be considered relative to ``root_dir`` (or the current
    working directory when ``root_dir`` is not given).

    If the ``fill_package_dir`` argument is passed, this function will consider it as a
    similar data structure to the ``package_dir`` configuration parameter add fill-in
    any missing package location.

    :rtype: list
    '''
    pass
# WARNING: Decompyle incomplete


def _nest_path(parent = None, path = None):
    path = parent if path in frozenset({'', '.'}) else os.path.join(parent, path)
    return os.path.normpath(path)


def version(value = None):
    '''When getting the version directly from an attribute,
    it should be normalised to string.
    '''
    _value = value() if callable(value) else value
    if isinstance(_value, str):
        return _value
    if None(_value, '__iter__'):
        return '.'.join(map(str, _value))
    return f'''{None}'''


def canonic_package_data(package_data = None):
    if '*' in package_data:
        package_data[''] = package_data.pop('*')
    return package_data


def canonic_data_files(data_files = None, root_dir = None):
    '''For compatibility with ``setup.py``, ``data_files`` should be a list
    of pairs instead of a dict.

    This function also expands glob patterns.
    '''
    if isinstance(data_files, list):
        return data_files
# WARNING: Decompyle incomplete


def entry_points(text = None, text_source = None):
    '''Given the contents of entry-points file,
    process it into a 2-level dictionary (``dict[str, dict[str, str]]``).
    The first level keys are entry-point groups, the second level keys are
    entry-point names, and the second level values are references to objects
    (that correspond to the entry-point value).
    '''
    parser = ConfigParser(default_section = None, delimiters = ('=',))
    parser.optionxform = str
    parser.read_string(text, text_source)
# WARNING: Decompyle incomplete


class EnsurePackagesDiscovered:
    '''Some expand functions require all the packages to already be discovered before
    they run, e.g. :func:`read_attr`, :func:`resolve_class`, :func:`cmdclass`.

    Therefore in some cases we will need to run autodiscovery during the evaluation of
    the configuration. However, it is better to postpone calling package discovery as
    much as possible, because some parameters can influence it (e.g. ``package_dir``),
    and those might not have been processed yet.
    '''
    
    def __init__(self = None, distribution = None):
        self._dist = distribution
        self._called = False

    
    def __call__(self):
        '''Trigger the automatic package discovery, if it is still necessary.'''
        if not self._called:
            self._called = True
            self._dist.set_defaults(name = False)
            return None

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None')):
        if self._called:
            self._dist.set_defaults.analyse_name()
            return None

    
    def _get_package_dir(self = None):
        self()
        pkg_dir = self._dist.package_dir
    # WARNING: Decompyle incomplete

    package_dir = (lambda self = None: LazyMappingProxy(self._get_package_dir))()


def LazyMappingProxy():
    '''LazyMappingProxy'''
    __doc__ = 'Mapping proxy that delays resolving the target object, until really needed.\n\n    >>> def obtain_mapping():\n    ...     print("Running expensive function!")\n    ...     return {"key": "value", "other key": "other value"}\n    >>> mapping = LazyMappingProxy(obtain_mapping)\n    >>> mapping["key"]\n    Running expensive function!\n    \'value\'\n    >>> mapping["other key"]\n    \'other value\'\n    '
    
    def __init__(self = None, obtain_mapping_value = None):
        self._obtain = obtain_mapping_value
        self._value = None

    
    def _target(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self = None, key = None):
        return self._target()[key]

    
    def __len__(self = None):
        return len(self._target())

    
    def __iter__(self = None):
        return iter(self._target())


LazyMappingProxy = <NODE:27>(LazyMappingProxy, 'LazyMappingProxy', Mapping[(_K, _V_co)])
