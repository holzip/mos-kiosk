# Source Generated with Decompyle++
# File: setupcfg.pyc (Python 3.12)

'''
Load setuptools configuration from ``setup.cfg`` files.

**API will be made private in the future**

To read project metadata, consider using
``build.util.project_wheel_metadata`` (https://pypi.org/project/build/).
For simple scenarios, you can also try parsing the file directly
with the help of ``configparser``.
'''
from __future__ import annotations
import contextlib
import functools
import os
from collections import defaultdict
from collections.abc import Iterable, Iterator
from functools import partial, wraps
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Generic, TypeVar, cast
from packaging.markers import default_environment as marker_env
from packaging.requirements import InvalidRequirement, Requirement
from packaging.version import InvalidVersion, Version
from  import _static
from _path import StrPath
from errors import FileError, OptionError
from warnings import SetuptoolsDeprecationWarning
from  import expand
if TYPE_CHECKING:
    from typing_extensions import TypeAlias
    from setuptools.dist import Distribution
    from distutils.dist import DistributionMetadata
SingleCommandOptions: 'TypeAlias' = dict[(str, tuple[(str, Any)])]
AllCommandOptions: 'TypeAlias' = dict[(str, SingleCommandOptions)]
Target = TypeVar('Target', 'Distribution', 'DistributionMetadata')

def read_configuration(filepath = None, find_others = None, ignore_option_errors = None):
    '''Read given configuration file and returns options from it as a dict.

    :param str|unicode filepath: Path to configuration file
        to get options from.

    :param bool find_others: Whether to search for other configuration files
        which could be on in various places.

    :param bool ignore_option_errors: Whether to silently ignore
        options, values of which could not be resolved (e.g. due to exceptions
        in directives such as file:, attr:, etc.).
        If False exceptions are propagated as expected.

    :rtype: dict
    '''
    Distribution = Distribution
    import setuptools.dist
    dist = Distribution()
    filenames = dist.find_config_files() if find_others else []
    handlers = _apply(dist, filepath, filenames, ignore_option_errors)
    return configuration_to_dict(handlers)


def apply_configuration(dist = None, filepath = None):
    '''Apply the configuration from a ``setup.cfg`` file into an existing
    distribution object.
    '''
    _apply(dist, filepath)
    dist._finalize_requires()
    return dist


def _apply(dist = None, filepath = None, other_files = None, ignore_option_errors = ((), False)):
    '''Read configuration from ``filepath`` and applies to the ``dist`` object.'''
    _Distribution = _Distribution
    import setuptools.dist
    filepath = os.path.abspath(filepath)
    if not os.path.isfile(filepath):
        raise FileError(f'''Configuration file {filepath} does not exist.''')
    current_directory = os.getcwd()
    os.chdir(os.path.dirname(filepath))
    filenames = None[filepath]
    
    try:
        _Distribution.parse_config_files(dist, filenames = cast(list[str], filenames))
        handlers = parse_configuration(dist, dist.command_options, ignore_option_errors = ignore_option_errors)
        dist._finalize_license_files()
        os.chdir(current_directory)
        return handlers
    except:
        os.chdir(current_directory)



def _get_option(target_obj = None, key = None):
    '''
    Given a target object and option key, get that option from
    the target object, either through a get_{key} method or
    from an attribute directly.
    '''
    getter_name = f'''get_{key}'''
    by_attribute = functools.partial(getattr, target_obj, key)
    getter = getattr(target_obj, getter_name, by_attribute)
    return getter()


def configuration_to_dict(handlers = None):
    '''Returns configuration data gathered by given handlers as a dict.

    :param Iterable[ConfigHandler] handlers: Handlers list,
        usually from parse_configuration()

    :rtype: dict
    '''
    config_dict = defaultdict(dict)
    for handler in handlers:
        for option in handler.set_options:
            value = _get_option(handler.target_obj, option)
            config_dict[handler.section_prefix][option] = value
    return config_dict


def parse_configuration(distribution = None, command_options = None, ignore_option_errors = None):
    '''Performs additional parsing of configuration options
    for a distribution.

    Returns a list of used option handlers.

    :param Distribution distribution:
    :param dict command_options:
    :param bool ignore_option_errors: Whether to silently ignore
        options, values of which could not be resolved (e.g. due to exceptions
        in directives such as file:, attr:, etc.).
        If False exceptions are propagated as expected.
    :rtype: list
    '''
    ensure_discovered = expand.EnsurePackagesDiscovered(distribution)
    options = ConfigOptionsHandler(distribution, command_options, ignore_option_errors, ensure_discovered)
    options.parse()
    if not distribution.package_dir:
        distribution.package_dir = options.package_dir
    meta = ConfigMetadataHandler(distribution.metadata, command_options, ignore_option_errors, ensure_discovered, distribution.package_dir, distribution.src_root)
    meta.parse()
    distribution._referenced_files.update(options._referenced_files, meta._referenced_files)
    None(None, None)
    return (meta, options)
    with None:
        if not None:
            pass
# WARNING: Decompyle incomplete


def _warn_accidental_env_marker_misconfig(label = None, orig_value = None, parsed = None):
    '''Because users sometimes misinterpret this configuration:

    [options.extras_require]
    foo = bar;python_version<"4"

    It looks like one requirement with an environment marker
    but because there is no newline, it\'s parsed as two requirements
    with a semicolon as separator.

    Therefore, if:
        * input string does not contain a newline AND
        * parsed result contains two requirements AND
        * parsing of the two parts from the result ("<first>;<second>")
        leads in a valid Requirement with a valid marker
    a UserWarning is shown to inform the user about the possible problem.
    '''
    pass
# WARNING: Decompyle incomplete


def ConfigHandler():
    '''ConfigHandler'''
    section_prefix: 'str' = 'Handles metadata supplied in configuration files.'
    aliases: 'ClassVar[dict[str, str]]' = { }
    
    def __init__(self, target_obj = None, options = None, ignore_option_errors = None, ensure_discovered = ('target_obj', 'Target', 'options', 'AllCommandOptions', 'ensure_discovered', 'expand.EnsurePackagesDiscovered', 'return', 'None')):
        self.ignore_option_errors = ignore_option_errors
        self.target_obj = target_obj
        self.sections = dict(self._section_options(options))
        self.set_options = []
        self.ensure_discovered = ensure_discovered
        self._referenced_files = set[str]()

    _section_options = (lambda cls = None, options = None: pass# WARNING: Decompyle incomplete
)()
    parsers = (lambda self: raise NotImplementedError(f'''{self.__class__.__name__} must provide .parsers property'''))()
    
    def __setitem__(self = None, option_name = None, value = property):
        target_obj = self.target_obj
        option_name = self.aliases.get(option_name, option_name)
        
        try:
            current_value = getattr(target_obj, option_name)
            if current_value:
                return None
            
            try:
                parsed = self.parsers.get(option_name, (lambda x: x))(value)
                simple_setter = functools.partial(target_obj.__setattr__, option_name)
                setter = getattr(target_obj, f'''set_{option_name}''', simple_setter)
                setter(parsed)
                self.set_options.append(option_name)
                return None
                except AttributeError:
                    e = None
                    raise KeyError(option_name), e
                    e = None
                    del e
            except (Exception,) * self.ignore_option_errors:
                return None



    _parse_list = (lambda cls, value, separator = (',',): if isinstance(value, list):
valueif None in value:
value = value.splitlines()else:
value = value.split(separator)# WARNING: Decompyle incomplete
)()
    _parse_dict = (lambda cls, value: separator = '='result = { }for line in cls._parse_list(value):
(key, sep, val) = line.partition(separator)if sep != separator:
raise OptionError(f'''Unable to parse option value to dict: {value}''')result[key.strip()] = val.strip()result)()
    _parse_bool = (lambda cls, value: value = value.lower()value in ('1', 'true', 'yes'))()
    _exclude_files_parser = (lambda cls, key: pass# WARNING: Decompyle incomplete
)()
    
    def _parse_file(self = classmethod, value = classmethod, root_dir = classmethod):
        """Represents value as a string, allowing including text
        from nearest files using `file:` directive.

        Directive is sandboxed and won't reach anything outside
        directory with setup.py.

        Examples:
            file: README.rst, CHANGELOG.md, src/file.txt

        :param str value:
        :rtype: str
        """
        include_directive = 'file:'
        if not isinstance(value, str):
            return value
        if not None.startswith(include_directive):
            return _static.Str(value)
        spec = None[len(include_directive):]
    # WARNING: Decompyle incomplete

    
    def _parse_attr(self = None, value = None, package_dir = classmethod, root_dir = ('root_dir', 'StrPath')):
        '''Represents value as a module attribute.

        Examples:
            attr: package.attr
            attr: package.module.attr

        :param str value:
        :rtype: str
        '''
        attr_directive = 'attr:'
        if not value.startswith(attr_directive):
            return _static.Str(value)
        attr_desc = None.replace(attr_directive, '')
        package_dir.update(self.ensure_discovered.package_dir)
        return expand.read_attr(attr_desc, package_dir, root_dir)

    _get_parser_compound = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    _parse_section_to_dict_with_key = (lambda cls, section_options, values_parser: value = { }for _, val in section_options.items():
value[key] = values_parser(key, val)value)()
    _parse_section_to_dict = (lambda cls, section_options, values_parser = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def parse_section(self = classmethod, section_options = classmethod):
        '''Parses configuration file section.

        :param dict section_options:
        '''
        for _, value in section_options.items():
            contextlib.suppress(KeyError)
            self[name] = value
            None(None, None)
        return None
        with None:
            if not None:
                pass
        continue

    
    def parse(self = None):
        '''Parses configuration file items from one
        or more related sections.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _deprecated_config_handler(self, func, msg, **kw):
        '''this function will wrap around parameters that are deprecated

        :param msg: deprecation message
        :param func: function to be wrapped around
        '''
        pass
    # WARNING: Decompyle incomplete


ConfigHandler = <NODE:27>(ConfigHandler, 'ConfigHandler', Generic[Target])

def ConfigMetadataHandler():
    '''ConfigMetadataHandler'''
    pass
# WARNING: Decompyle incomplete

ConfigMetadataHandler = <NODE:27>(ConfigMetadataHandler, 'ConfigMetadataHandler', ConfigHandler['DistributionMetadata'])

def ConfigOptionsHandler():
    '''ConfigOptionsHandler'''
    pass
# WARNING: Decompyle incomplete

ConfigOptionsHandler = <NODE:27>(ConfigOptionsHandler, 'ConfigOptionsHandler', ConfigHandler['Distribution'])

class _AmbiguousMarker(SetuptoolsDeprecationWarning):
    _SUMMARY = 'Ambiguous requirement marker.'
    _DETAILS = '\n    One of the parsed requirements in `{field}` looks like a valid environment marker:\n\n        {req!r}\n\n    Please make sure that the configuration file is correct.\n    You can use dangling lines to avoid this problem.\n    '
    _SEE_DOCS = 'userguide/declarative_config.html#opt-2'
    message = (lambda cls: docs = f'''https://setuptools.pypa.io/en/latest/{cls._SEE_DOCS}'''cls._format(cls._SUMMARY, cls._DETAILS, see_url = docs, format_args = kw))()


class _DeprecatedConfig(SetuptoolsDeprecationWarning):
    _SEE_DOCS = 'userguide/declarative_config.html'

