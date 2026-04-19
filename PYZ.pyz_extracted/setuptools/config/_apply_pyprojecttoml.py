# Source Generated with Decompyle++
# File: _apply_pyprojecttoml.pyc (Python 3.12)

__doc__ = 'Translation layer between pyproject config and setuptools distribution and\nmetadata objects.\n\nThe distribution and metadata objects are modeled after (an old version of)\ncore metadata, therefore configs in the format specified for ``pyproject.toml``\nneed to be processed before being applied.\n\n**PRIVATE MODULE**: API reserved for setuptools internal usage only.\n'
from __future__ import annotations
import logging
import os
from collections.abc import Mapping
from email.headerregistry import Address
from functools import partial, reduce
from inspect import cleandoc
from itertools import chain
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Callable, TypeVar, Union
from  import _static
from _path import StrPath
from errors import RemovedConfigError
from extension import Extension
from warnings import SetuptoolsWarning
if TYPE_CHECKING:
    from typing_extensions import TypeAlias
    from setuptools._importlib import metadata
    from setuptools.dist import Distribution
    from distutils.dist import _OptionsList
EMPTY: 'Mapping' = MappingProxyType({ })
_ProjectReadmeValue: 'TypeAlias' = Union[(str, dict[(str, str)])]
_Correspondence: 'TypeAlias' = Callable[([
    'Distribution',
    Any,
    Union[(StrPath, None)]], None)]
_T = TypeVar('_T')
_logger = logging.getLogger(__name__)

def apply(dist = None, config = None, filename = None):
    '''Apply configuration dict read with :func:`read_configuration`'''
    if not config:
        return dist
    if not None.path.dirname(filename):
        None.path.dirname(filename)
    root_dir = '.'
    _apply_project_table(dist, config, root_dir)
    _apply_tool_table(dist, config, filename)
    current_directory = os.getcwd()
    os.chdir(root_dir)
    
    try:
        dist._finalize_requires()
        dist._finalize_license_files()
        os.chdir(current_directory)
        return dist
    except:
        os.chdir(current_directory)



def _apply_project_table(dist = None, config = None, root_dir = None):
    orig_config = config.get('project', { })
    if not orig_config:
        return None
# WARNING: Decompyle incomplete


def _apply_tool_table(dist = None, config = None, filename = None):
    tool_table = config.get('tool', { }).get('setuptools', { })
    if not tool_table:
        return None
    for field, value in tool_table.items():
        norm_key = json_compatible_key(field)
        if norm_key in TOOL_TABLE_REMOVALS:
            suggestion = cleandoc(TOOL_TABLE_REMOVALS[norm_key])
            msg = f'''\n            The parameter `tool.setuptools.{field}` was long deprecated\n            and has been removed from `pyproject.toml`.\n            '''
            raise RemovedConfigError('\n'.join([
                cleandoc(msg),
                suggestion]))
        norm_key = TOOL_TABLE_RENAMES.get(norm_key, norm_key)
        corresp = TOOL_TABLE_CORRESPONDENCE.get(norm_key, norm_key)
        if callable(corresp):
            corresp(dist, value)
            continue
        _set_config(dist, corresp, value)
    _copy_command_options(config, dist, filename)


def _handle_missing_dynamic(dist = None, project_table = None):
    '''Be temporarily forgiving with ``dynamic`` fields not listed in ``dynamic``'''
    dynamic = set(project_table.get('dynamic', []))
    for field, getter in _PREVIOUSLY_DEFINED.items():
        if field in project_table:
            continue
        if field in dynamic:
            continue
        value = getter(dist)
        if not value:
            continue
        _MissingDynamic.emit(field = field, value = value)
        project_table[field] = _RESET_PREVIOUSLY_DEFINED.get(field)


def json_compatible_key(key = None):
    '''As defined in :pep:`566#json-compatible-metadata`'''
    return key.lower().replace('-', '_')


def _set_config(dist = None, field = None, value = None):
    val = _PREPROCESS.get(field, _noop)(dist, value)
    setter = getattr(dist.metadata, f'''set_{field}''', None)
    if setter:
        setter(val)
        return None
    if hasattr(dist.metadata, field) or field in SETUPTOOLS_PATCHES:
        setattr(dist.metadata, field, val)
        return None
    setattr(dist, field, val)

_CONTENT_TYPES = {
    '.md': 'text/markdown',
    '.rst': 'text/x-rst',
    '.txt': 'text/plain' }

def _guess_content_type(file = None):
    (_, ext) = os.path.splitext(file.lower())
    if not ext:
        return None
    if ext in _CONTENT_TYPES:
        return _static.Str(_CONTENT_TYPES[ext])
    valid = (lambda .0: pass# WARNING: Decompyle incomplete
)(_CONTENT_TYPES.items()())
    msg = f'''only the following file extensions are recognized: {valid}.'''
    raise ValueError(f'''Undefined content type for {file}, {msg}''')


def _long_description(dist = None, val = None, root_dir = None):
    expand = expand
    import setuptools.config
    if isinstance(val, str):
        file = val
        text = expand.read_files(file, root_dir)
        ctype = _guess_content_type(file)
    elif not val.get('file'):
        val.get('file')
    file = ()
    if not val.get('text'):
        val.get('text')
    text = expand.read_files(file, root_dir)
    ctype = val['content-type']
    _set_config(dist, 'long_description', _static.Str(text))
    if ctype:
        _set_config(dist, 'long_description_content_type', _static.Str(ctype))
    if file:
        dist._referenced_files.add(file)
        return None


def _license(dist = None, val = None, root_dir = None):
    expand = expand
    import setuptools.config
    if 'file' in val:
        value = expand.read_files([
            val['file']], root_dir)
        _set_config(dist, 'license', _static.Str(value))
        dist._referenced_files.add(val['file'])
        return None
    _set_config(dist, 'license', _static.Str(val['text']))


def _people(dist = None, val = None, _root_dir = None, kind = ('dist', 'Distribution', 'val', 'list[dict]', '_root_dir', 'StrPath | None', 'kind', 'str')):
    field = []
    email_field = []
    for person in val:
        if 'name' not in person:
            email_field.append(person['email'])
            continue
        if 'email' not in person:
            field.append(person['name'])
            continue
        addr = Address(display_name = person['name'], addr_spec = person['email'])
        email_field.append(str(addr))
    if field:
        _set_config(dist, kind, _static.Str(', '.join(field)))
    if email_field:
        _set_config(dist, f'''{kind}_email''', _static.Str(', '.join(email_field)))
        return None


def _project_urls(dist = None, val = None, _root_dir = None):
    _set_config(dist, 'project_urls', val)


def _python_requires(dist = None, val = None, _root_dir = None):
    _set_config(dist, 'python_requires', _static.SpecifierSet(val))


def _dependencies(dist = None, val = None, _root_dir = None):
    if getattr(dist, 'install_requires', []):
        msg = '`install_requires` overwritten in `pyproject.toml` (dependencies)'
        SetuptoolsWarning.emit(msg)
    dist.install_requires = val


def _optional_dependencies(dist = None, val = None, _root_dir = None):
    if getattr(dist, 'extras_require', None):
        msg = '`extras_require` overwritten in `pyproject.toml` (optional-dependencies)'
        SetuptoolsWarning.emit(msg)
    dist.extras_require = val


def _ext_modules(dist = None, val = None):
    if not dist.ext_modules:
        dist.ext_modules
    existing = []
    args = val()
# WARNING: Decompyle incomplete


def _noop(_dist = None, val = None):
    return val


def _identity(val = None):
    return val


def _unify_entry_points(project_table = None):
    project = project_table
    given = project.pop('entry-points', project.pop('entry_points', { }))
    entry_points = dict(given)
    renaming = {
        'scripts': 'console_scripts',
        'gui_scripts': 'gui_scripts' }
    for key, value in list(project.items()):
        norm_key = json_compatible_key(key)
        if not norm_key in renaming:
            continue
        entry_points[renaming[norm_key]] = project.pop(key)
# WARNING: Decompyle incomplete


def _copy_command_options(pyproject = None, dist = None, filename = None):
    tool_table = pyproject.get('tool', { })
    cmdclass = tool_table.get('setuptools', { }).get('cmdclass', { })
    valid_options = _valid_command_options(cmdclass)
    cmd_opts = dist.command_options
    for cmd, config in pyproject.get('tool', { }).get('distutils', { }).items():
        cmd = json_compatible_key(cmd)
        valid = valid_options.get(cmd, set())
        cmd_opts.setdefault(cmd, { })
        for key, value in config.items():
            key = json_compatible_key(key)
            cmd_opts[cmd][key] = (str(filename), value)
            if not key not in valid:
                continue
            _logger.warning(f'''Command option {cmd}.{key} is not defined''')


def _valid_command_options(cmdclass = None):
    Distribution = Distribution
    import setuptools.dist
    metadata = metadata
    import _importlib
    valid_options = {
        'global': _normalise_cmd_options(Distribution.global_options) }
    unloaded_entry_points = metadata.entry_points(group = 'distutils.commands')
    loaded_entry_points = unloaded_entry_points()
    entry_points = loaded_entry_points()
    for cmd, cmd_class in chain(entry_points, cmdclass.items()):
        opts = valid_options.get(cmd, set())
        opts = opts | _normalise_cmd_options(getattr(cmd_class, 'user_options', []))
        valid_options[cmd] = opts
    return valid_options


def _load_ep(ep = None):
    if ep.value.startswith('wheel.bdist_wheel'):
        return None
    
    try:
        return (ep.name, ep.load())
    except Exception:
        ex = None
        msg = f'''{ex.__class__.__name__} while trying to load entry-point {ep.name}'''
        _logger.warning(f'''{msg}: {ex}''')
        ex = None
        del ex
        return None
        ex = None
        del ex



def _normalise_cmd_option_key(name = None):
    return json_compatible_key(name).strip('_=')


def _normalise_cmd_options(desc = None):
    pass
# WARNING: Decompyle incomplete


def _get_previous_entrypoints(dist = None):
    ignore = ('console_scripts', 'gui_scripts')
    if not getattr(dist, 'entry_points', None):
        getattr(dist, 'entry_points', None)
    value = { }
# WARNING: Decompyle incomplete


def _get_previous_scripts(dist = None):
    if not getattr(dist, 'entry_points', None):
        getattr(dist, 'entry_points', None)
    value = { }
    return value.get('console_scripts')


def _get_previous_gui_scripts(dist = None):
    if not getattr(dist, 'entry_points', None):
        getattr(dist, 'entry_points', None)
    value = { }
    return value.get('gui_scripts')


def _set_static_list_metadata(attr = None, dist = None, val = None):
    '''Apply distutils metadata validation but preserve "static" behaviour'''
    meta = dist.metadata
    getter = getattr(meta, f'''get_{attr}''')
    setter = getattr(meta, f'''set_{attr}''')
    setter(val)
    setattr(meta, attr, _static.List(getter()))


def _attrgetter(attr):
    '''
    Similar to ``operator.attrgetter`` but returns None if ``attr`` is not found
    >>> from types import SimpleNamespace
    >>> obj = SimpleNamespace(a=42, b=SimpleNamespace(c=13))
    >>> _attrgetter("a")(obj)
    42
    >>> _attrgetter("b.c")(obj)
    13
    >>> _attrgetter("d")(obj) is None
    True
    '''
    return partial(reduce, (lambda acc, x: getattr(acc, x, None)), attr.split('.'))


def _some_attrgetter(*items):
    '''
    Return the first "truth-y" attribute or None
    >>> from types import SimpleNamespace
    >>> obj = SimpleNamespace(a=42, b=SimpleNamespace(c=13))
    >>> _some_attrgetter("d", "a", "b.c")(obj)
    42
    >>> _some_attrgetter("d", "e", "b.c", "a")(obj)
    13
    >>> _some_attrgetter("d", "e", "f")(obj) is None
    True
    '''
    pass
# WARNING: Decompyle incomplete

PYPROJECT_CORRESPONDENCE: 'dict[str, _Correspondence]' = {
    'readme': _long_description,
    'license': _license,
    'authors': partial(_people, kind = 'author'),
    'maintainers': partial(_people, kind = 'maintainer'),
    'urls': _project_urls,
    'dependencies': _dependencies,
    'optional_dependencies': _optional_dependencies,
    'requires_python': _python_requires }
TOOL_TABLE_RENAMES = {
    'script_files': 'scripts' }
TOOL_TABLE_REMOVALS = {
    'namespace_packages': '\n        Please migrate to implicit native namespaces instead.\n        See https://packaging.python.org/en/latest/guides/packaging-namespace-packages/.\n        ' }
TOOL_TABLE_CORRESPONDENCE = {
    'obsoletes': partial(_set_static_list_metadata, 'obsoletes'),
    'provides': partial(_set_static_list_metadata, 'provides'),
    'platforms': partial(_set_static_list_metadata, 'platforms') }
SETUPTOOLS_PATCHES = {
    'license_file',
    'project_urls',
    'license_files',
    'provides_extras',
    'long_description_content_type'}
_PREPROCESS = {
    'ext_modules': _ext_modules }
# WARNING: Decompyle incomplete
