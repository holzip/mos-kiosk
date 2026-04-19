# Source Generated with Decompyle++
# File: pyprojecttoml.pyc (Python 3.12)

'''
Load setuptools configuration from ``pyproject.toml`` files.

**PRIVATE MODULE**: API reserved for setuptools internal usage only.

To read project metadata, consider using
``build.util.project_wheel_metadata`` (https://pypi.org/project/build/).
For simple scenarios, you can also try parsing the file directly
with the help of ``tomllib`` or ``tomli``.
'''
from __future__ import annotations
import logging
import os
from collections.abc import Mapping
from contextlib import contextmanager
from functools import partial
from types import TracebackType
from typing import TYPE_CHECKING, Any, Callable
from _path import StrPath
from errors import FileError, InvalidConfigError
from warnings import SetuptoolsWarning
from  import expand as _expand
from _apply_pyprojecttoml import _PREVIOUSLY_DEFINED, _MissingDynamic, apply as _apply
if TYPE_CHECKING:
    from typing_extensions import Self
    from setuptools.dist import Distribution
_logger = logging.getLogger(__name__)

def load_file(filepath = None):
    tomllib = tomllib
    import compat.py310
    file = open(filepath, 'rb')
    None(None, None)
    return 
    with None:
        if not None, tomllib.load(file):
            pass


def validate(config = None, filepath = None):
    validator = _validate_pyproject
    import 
    trove_classifier = validator.FORMAT_FUNCTIONS.get('trove-classifier')
    if hasattr(trove_classifier, '_disable_download'):
        trove_classifier._disable_download()
    
    try:
        return validator.validate(config)
    except validator.ValidationError:
        ex = None
        summary = f'''configuration error: {ex.summary}'''
        if ex.name.strip('`') != 'project':
            _logger.debug(summary)
            _logger.debug(ex.details)
        error = f'''invalid pyproject.toml config: {ex.name}.'''
        raise ValueError(f'''{error}\n{summary}'''), None
        ex = None
        del ex



def apply_configuration(dist = None, filepath = None, ignore_option_errors = None):
    '''Apply the configuration from a ``pyproject.toml`` file into an existing
    distribution object.
    '''
    config = read_configuration(filepath, True, ignore_option_errors, dist)
    return _apply(dist, config, filepath)


def read_configuration(filepath = None, expand = None, ignore_option_errors = None, dist = (True, False, None)):
    '''Read given configuration file and returns options from it as a dict.

    :param str|unicode filepath: Path to configuration file in the ``pyproject.toml``
        format.

    :param bool expand: Whether to expand directives and other computed values
        (i.e. post-process the given configuration)

    :param bool ignore_option_errors: Whether to silently ignore
        options, values of which could not be resolved (e.g. due to exceptions
        in directives such as file:, attr:, etc.).
        If False exceptions are propagated as expected.

    :param Distribution|None: Distribution object to which the configuration refers.
        If not given a dummy object will be created and discarded after the
        configuration is read. This is used for auto-discovery of packages and in the
        case a dynamic configuration (e.g. ``attr`` or ``cmdclass``) is expanded.
        When ``expand=False`` this object is simply ignored.

    :rtype: dict
    '''
    filepath = os.path.abspath(filepath)
    if not os.path.isfile(filepath):
        raise FileError(f'''Configuration file {filepath!r} does not exist.''')
    if not load_file(filepath):
        load_file(filepath)
    asdict = { }
    project_table = asdict.get('project', { })
    tool_table = asdict.get('tool', { })
    setuptools_table = tool_table.get('setuptools', { })
    if not (asdict or project_table) and setuptools_table:
        return { }
    if None in asdict.get('tools', { }):
        _ToolsTypoInMetadata.emit()
    if 'distutils' in tool_table:
        _ExperimentalConfiguration.emit(subject = '[tool.distutils]')
# WARNING: Decompyle incomplete


def expand_configuration(config = None, root_dir = None, ignore_option_errors = None, dist = (None, False, None)):
    '''Given a configuration with unresolved fields (e.g. dynamic, cmdclass, ...)
    find their final values.

    :param dict config: Dict containing the configuration for the distribution
    :param str root_dir: Top-level directory for the distribution/project
        (the same directory where ``pyproject.toml`` is place)
    :param bool ignore_option_errors: see :func:`read_configuration`
    :param Distribution|None: Distribution object to which the configuration refers.
        If not given a dummy object will be created and discarded after the
        configuration is read. Used in the case a dynamic configuration
        (e.g. ``attr`` or ``cmdclass``).

    :rtype: dict
    '''
    return _ConfigExpander(config, root_dir, ignore_option_errors, dist).expand()


class _ConfigExpander:
    
    def __init__(self = None, config = None, root_dir = None, ignore_option_errors = (None, False, None), dist = ('config', 'dict', 'root_dir', 'StrPath | None', 'ignore_option_errors', 'bool', 'dist', 'Distribution | None', 'return', 'None')):
        self.config = config
        if not root_dir:
            root_dir
        self.root_dir = os.getcwd()
        self.project_cfg = config.get('project', { })
        self.dynamic = self.project_cfg.get('dynamic', [])
        self.setuptools_cfg = config.get('tool', { }).get('setuptools', { })
        self.dynamic_cfg = self.setuptools_cfg.get('dynamic', { })
        self.ignore_option_errors = ignore_option_errors
        self._dist = dist
        self._referenced_files = set[str]()

    
    def _ensure_dist(self = None):
        Distribution = Distribution
        import setuptools.dist
        attrs = {
            'src_root': self.root_dir,
            'name': self.project_cfg.get('name', None) }
        if not self._dist:
            self._dist
        return Distribution(attrs)

    
    def _process_field(self = None, container = None, field = None, fn = ('container', 'dict', 'field', 'str', 'fn', 'Callable')):
        if field in container:
            _ignore_errors(self.ignore_option_errors)
            container[field] = fn(container[field])
            None(None, None)
            return None
        return None
        with None:
            if not None:
                pass

    
    def _canonic_package_data(self, field = ('package-data',)):
        package_data = self.setuptools_cfg.get(field, { })
        return _expand.canonic_package_data(package_data)

    
    def expand(self):
        self._expand_packages()
        self._canonic_package_data()
        self._canonic_package_data('exclude-package-data')
        dist = self._ensure_dist()
        ctx = _EnsurePackagesDiscovered(dist, self.project_cfg, self.setuptools_cfg)
        ensure_discovered = ctx
        package_dir = ensure_discovered.package_dir
        self._expand_data_files()
        self._expand_cmdclass(package_dir)
        self._expand_all_dynamic(dist, package_dir)
        None(None, None)
        dist._referenced_files.update(self._referenced_files)
        return self.config
        with None:
            if not None:
                pass
        continue

    
    def _expand_packages(self):
        packages = self.setuptools_cfg.get('packages')
    # WARNING: Decompyle incomplete

    
    def _expand_data_files(self):
        data_files = partial(_expand.canonic_data_files, root_dir = self.root_dir)
        self._process_field(self.setuptools_cfg, 'data-files', data_files)

    
    def _expand_cmdclass(self = None, package_dir = None):
        root_dir = self.root_dir
        cmdclass = partial(_expand.cmdclass, package_dir = package_dir, root_dir = root_dir)
        self._process_field(self.setuptools_cfg, 'cmdclass', cmdclass)

    
    def _expand_all_dynamic(self = None, dist = None, package_dir = None):
        special = ('version', 'readme', 'entry-points', 'scripts', 'gui-scripts', 'classifiers', 'dependencies', 'optional-dependencies')
    # WARNING: Decompyle incomplete

    
    def _ensure_previously_set(self = None, dist = None, field = None):
        previous = _PREVIOUSLY_DEFINED[field](dist)
    # WARNING: Decompyle incomplete

    
    def _expand_directive(self = None, specifier = None, directive = None, package_dir = ('specifier', 'str', 'package_dir', 'Mapping[str, str]')):
        always_iterable = always_iterable
        import more_itertools
        _ignore_errors(self.ignore_option_errors)
        root_dir = self.root_dir
        if 'file' in directive:
            self._referenced_files.update(always_iterable(directive['file']))
            None(None, None)
            return 
        if None in directive:
            None(None, None)
            return 
        raise None(f'''invalid `{specifier}`: {directive!r}''')
        with None:
            if not None:
                pass

    
    def _obtain(self = None, dist = None, field = None, package_dir = ('dist', 'Distribution', 'field', 'str', 'package_dir', 'Mapping[str, str]')):
        if field in self.dynamic_cfg:
            return self._expand_directive(f'''tool.setuptools.dynamic.{field}''', self.dynamic_cfg[field], package_dir)
        None._ensure_previously_set(dist, field)

    
    def _obtain_version(self = None, dist = None, package_dir = None):
        if 'version' in self.dynamic and 'version' in self.dynamic_cfg:
            return _expand.version(self._obtain(dist, 'version', package_dir))

    
    def _obtain_readme(self = None, dist = None):
        if 'readme' not in self.dynamic:
            return None
        dynamic_cfg = self.dynamic_cfg
        if 'readme' in dynamic_cfg:
            return {
                'text': self._obtain(dist, 'readme', { }),
                'content-type': dynamic_cfg['readme'].get('content-type', 'text/x-rst') }
        None._ensure_previously_set(dist, 'readme')

    
    def _obtain_entry_points(self = None, dist = None, package_dir = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _obtain_classifiers(self = None, dist = None):
        if 'classifiers' in self.dynamic:
            value = self._obtain(dist, 'classifiers', { })
            if value:
                return value.splitlines()

    
    def _obtain_dependencies(self = None, dist = None):
        if 'dependencies' in self.dynamic:
            value = self._obtain(dist, 'dependencies', { })
            if value:
                return _parse_requirements_list(value)

    
    def _obtain_optional_dependencies(self = None, dist = None):
        if 'optional-dependencies' not in self.dynamic:
            return None
    # WARNING: Decompyle incomplete



def _parse_requirements_list(value):
    pass
# WARNING: Decompyle incomplete

_ignore_errors = (lambda ignore_option_errors = None: pass# WARNING: Decompyle incomplete
)()

class _EnsurePackagesDiscovered(_expand.EnsurePackagesDiscovered):
    pass
# WARNING: Decompyle incomplete


class _ExperimentalConfiguration(SetuptoolsWarning):
    _SUMMARY = '`{subject}` in `pyproject.toml` is still *experimental* and likely to change in future releases.'


class _ToolsTypoInMetadata(SetuptoolsWarning):
    _SUMMARY = 'Ignoring [tools.setuptools] in pyproject.toml, did you mean [tool.setuptools]?'

