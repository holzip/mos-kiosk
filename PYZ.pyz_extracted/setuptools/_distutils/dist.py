# Source Generated with Decompyle++
# File: dist.pyc (Python 3.12)

'''distutils.dist

Provides the Distribution class, which represents the module distribution
being built/installed/distributed.
'''
from __future__ import annotations
import contextlib
import logging
import os
import pathlib
import re
import sys
import warnings
from collections.abc import Iterable, MutableMapping
from email import message_from_file
from typing import IO, TYPE_CHECKING, Any, ClassVar, Literal, TypeVar, Union, overload
from packaging.utils import canonicalize_name, canonicalize_version
from _log import log
from debug import DEBUG
from errors import DistutilsArgError, DistutilsClassError, DistutilsModuleError, DistutilsOptionError
from fancy_getopt import FancyGetopt, translate_longopt
from util import check_environ, rfc822_escape, strtobool
if TYPE_CHECKING:
    from _typeshed import SupportsWrite
    from typing_extensions import TypeAlias
    from cmd import Command
_CommandT = TypeVar('_CommandT', bound = 'Command')
_OptionsList: 'TypeAlias' = list[Union[(tuple[(str, Union[(str, None)], str, int)], tuple[(str, Union[(str, None)], str)])]]
command_re = re.compile('^[a-zA-Z]([a-zA-Z0-9_]*)$')

def _ensure_list(value = None, fieldname = None):
    if isinstance(value, str):
        return value
# WARNING: Decompyle incomplete


class Distribution:
    __module__ = __name__
    __qualname__ = 'Distribution'
    __doc__ = "The core of the Distutils.  Most of the work hiding behind 'setup'\n    is really done within a Distribution instance, which farms the work out\n    to the Distutils commands specified on the command line.\n\n    Setup scripts will almost never instantiate Distribution directly,\n    unless the 'setup()' function is totally inadequate to their needs.\n    However, it is conceivable that a setup script might wish to subclass\n    Distribution for some specialized purpose, and then pass the subclass\n    to 'setup()' as the 'distclass' keyword argument.  If so, it is\n    necessary to respect the expectations that 'setup' has of Distribution.\n    See the code for 'setup()', in core.py, for details.\n    "
    global_options: 'ClassVar[_OptionsList]' = [
        ('verbose', 'v', 'run verbosely (default)', 1),
        ('quiet', 'q', 'run quietly (turns verbosity off)'),
        ('dry-run', 'n', "don't actually do anything"),
        ('help', 'h', 'show detailed help message'),
        ('no-user-cfg', None, 'ignore pydistutils.cfg in your home directory')]
    common_usage: 'ClassVar[str]' = "Common commands: (see '--help-commands' for more)\n\n  setup.py build      will build the package underneath 'build/'\n  setup.py install    will install the package\n"
    display_options: 'ClassVar[_OptionsList]' = [
        ('help-commands', None, 'list all available commands'),
        ('name', None, 'print package name'),
        ('version', 'V', 'print package version'),
        ('fullname', None, 'print <package name>-<version>'),
        ('author', None, "print the author's name"),
        ('author-email', None, "print the author's email address"),
        ('maintainer', None, "print the maintainer's name"),
        ('maintainer-email', None, "print the maintainer's email address"),
        ('contact', None, "print the maintainer's name if known, else the author's"),
        ('contact-email', None, "print the maintainer's email address if known, else the author's"),
        ('url', None, 'print the URL for this package'),
        ('license', None, 'print the license of the package'),
        ('licence', None, 'alias for --license'),
        ('description', None, 'print the package description'),
        ('long-description', None, 'print the long package description'),
        ('platforms', None, 'print the list of platforms'),
        ('classifiers', None, 'print the list of classifiers'),
        ('keywords', None, 'print the list of keywords'),
        ('provides', None, 'print the list of packages/modules provided'),
        ('requires', None, 'print the list of packages/modules required'),
        ('obsoletes', None, 'print the list of packages/modules made obsolete')]
# WARNING: Decompyle incomplete


class DistributionMetadata:
    '''Dummy class to hold the distribution meta-data: name, version,
    author, and so forth.
    '''
    _METHOD_BASENAMES = ('name', 'version', 'author', 'author_email', 'maintainer', 'maintainer_email', 'url', 'license', 'description', 'long_description', 'keywords', 'platforms', 'fullname', 'contact', 'contact_email', 'classifiers', 'download_url', 'provides', 'requires', 'obsoletes')
    
    def __init__(self = None, path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def read_pkg_file(self = None, file = None):
        '''Reads the metadata values from a file object.'''
        pass
    # WARNING: Decompyle incomplete

    
    def write_pkg_info(self = None, base_dir = None):
        '''Write the PKG-INFO file into the release tree.'''
        pkg_info = open(os.path.join(base_dir, 'PKG-INFO'), 'w', encoding = 'UTF-8')
        self.write_pkg_file(pkg_info)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def write_pkg_file(self = None, file = None):
        '''Write the PKG-INFO format data to a file object.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _write_list(self, file, name, values):
        if not values:
            values
        values = []
        for value in values:
            file.write(f'''{name}: {value}\n''')

    
    def get_name(self = None):
        if not self.name:
            self.name
        return 'UNKNOWN'

    
    def get_version(self = None):
        if not self.version:
            self.version
        return '0.0.0'

    
    def get_fullname(self = None):
        return self._fullname(self.get_name(), self.get_version())

    _fullname = (lambda name = None, version = None: '{}-{}'.format(canonicalize_name(name).replace('-', '_'), canonicalize_version(version, strip_trailing_zero = False)))()
    
    def get_author(self = None):
        return self.author

    
    def get_author_email(self = None):
        return self.author_email

    
    def get_maintainer(self = None):
        return self.maintainer

    
    def get_maintainer_email(self = None):
        return self.maintainer_email

    
    def get_contact(self = None):
        if not self.maintainer:
            self.maintainer
        return self.author

    
    def get_contact_email(self = None):
        if not self.maintainer_email:
            self.maintainer_email
        return self.author_email

    
    def get_url(self = None):
        return self.url

    
    def get_license(self = None):
        return self.license

    get_licence = get_license
    
    def get_description(self = None):
        return self.description

    
    def get_long_description(self = None):
        return self.long_description

    
    def get_keywords(self = None):
        if not self.keywords:
            self.keywords
        return []

    
    def set_keywords(self = None, value = None):
        self.keywords = _ensure_list(value, 'keywords')

    
    def get_platforms(self = None):
        return self.platforms

    
    def set_platforms(self = None, value = None):
        self.platforms = _ensure_list(value, 'platforms')

    
    def get_classifiers(self = None):
        if not self.classifiers:
            self.classifiers
        return []

    
    def set_classifiers(self = None, value = None):
        self.classifiers = _ensure_list(value, 'classifiers')

    
    def get_download_url(self = None):
        return self.download_url

    
    def get_requires(self = None):
        if not self.requires:
            self.requires
        return []

    
    def set_requires(self = None, value = None):
        import distutils.versionpredicate as distutils
        for v in value:
            distutils.versionpredicate.VersionPredicate(v)
        self.requires = list(value)

    
    def get_provides(self = None):
        if not self.provides:
            self.provides
        return []

    
    def set_provides(self = None, value = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_obsoletes(self = None):
        if not self.obsoletes:
            self.obsoletes
        return []

    
    def set_obsoletes(self = None, value = None):
        import distutils.versionpredicate as distutils
        for v in value:
            distutils.versionpredicate.VersionPredicate(v)
        self.obsoletes = list(value)



def fix_help_options(options):
    """Convert a 4-tuple 'help_options' list as found in various command
    classes to the 3-tuple form required by FancyGetopt.
    """
    pass
# WARNING: Decompyle incomplete

