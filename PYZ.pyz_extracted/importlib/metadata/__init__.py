# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

import os
import re
import abc
import csv
import sys
import email
import pathlib
import zipfile
import operator
import textwrap
import warnings
import functools
import itertools
import posixpath
import contextlib
import collections
import inspect
from  import _adapters, _meta
from _collections import FreezableDefaultDict, Pair
from _functools import method_cache, pass_none
from _itertools import always_iterable, unique_everseen
from _meta import PackageMetadata, SimplePath
from contextlib import suppress
from importlib import import_module
from importlib.abc import MetaPathFinder
from itertools import starmap
from typing import List, Mapping, Optional, cast
__all__ = [
    'Distribution',
    'DistributionFinder',
    'PackageMetadata',
    'PackageNotFoundError',
    'distribution',
    'distributions',
    'entry_points',
    'files',
    'metadata',
    'packages_distributions',
    'requires',
    'version']

class PackageNotFoundError(ModuleNotFoundError):
    '''The package was not found.'''
    
    def __str__(self):
        return f'''No package metadata was found for {self.name}'''

    name = (lambda self: (name,) = self.argsname)()


class Sectioned:
    """
    A simple entry point config parser for performance

    >>> for item in Sectioned.read(Sectioned._sample):
    ...     print(item)
    Pair(name='sec1', value='# comments ignored')
    Pair(name='sec1', value='a = 1')
    Pair(name='sec1', value='b = 2')
    Pair(name='sec2', value='a = 2')

    >>> res = Sectioned.section_pairs(Sectioned._sample)
    >>> item = next(res)
    >>> item.name
    'sec1'
    >>> item.value
    Pair(name='a', value='1')
    >>> item = next(res)
    >>> item.value
    Pair(name='b', value='2')
    >>> item = next(res)
    >>> item.name
    'sec2'
    >>> item.value
    Pair(name='a', value='2')
    >>> list(res)
    []
    """
    _sample = textwrap.dedent('\n        [sec1]\n        # comments ignored\n        a = 1\n        b = 2\n\n        [sec2]\n        a = 2\n        ').lstrip()
    section_pairs = (lambda cls, text: cls.read(text, filter_ = cls.valid)())()
    read = (lambda text, filter_ = (None,): pass# WARNING: Decompyle incomplete
)()
    valid = (lambda line: if line:
linenot line.startswith('#'))()


class DeprecatedTuple:
    """
    Provide subscript item access for backward compatibility.

    >>> recwarn = getfixture('recwarn')
    >>> ep = EntryPoint(name='name', value='value', group='group')
    >>> ep[:]
    ('name', 'value', 'group')
    >>> ep[0]
    'name'
    >>> len(recwarn)
    1
    """
    _warn = functools.partial(warnings.warn, 'EntryPoint tuple interface is deprecated. Access members by name.', DeprecationWarning, stacklevel = 2)
    
    def __getitem__(self, item):
        self._warn()
        return self._key()[item]



class EntryPoint(DeprecatedTuple):
    """An entry point as defined by Python packaging conventions.

    See `the packaging docs on entry points
    <https://packaging.python.org/specifications/entry-points/>`_
    for more information.

    >>> ep = EntryPoint(
    ...     name=None, group=None, value='package.module:attr [extra1, extra2]')
    >>> ep.module
    'package.module'
    >>> ep.attr
    'attr'
    >>> ep.extras
    ['extra1', 'extra2']
    """
    group: str = re.compile('(?P<module>[\\w.]+)\\s*(:\\s*(?P<attr>[\\w.]+)\\s*)?((?P<extras>\\[.*\\])\\s*)?$')
    dist: Optional['Distribution'] = None
    
    def __init__(self, name, value, group):
        vars(self).update(name = name, value = value, group = group)

    
    def load(self):
        '''Load the entry point from its definition. If only a module
        is indicated by the value, return that module. Otherwise,
        return the named object.
        '''
        match = self.pattern.match(self.value)
        module = import_module(match.group('module'))
        if not match.group('attr'):
            match.group('attr')
        attrs = filter(None, ''.split('.'))
        return functools.reduce(getattr, attrs, module)

    module = (lambda self: match = self.pattern.match(self.value)match.group('module'))()
    attr = (lambda self: match = self.pattern.match(self.value)match.group('attr'))()
    extras = (lambda self: match = self.pattern.match(self.value)if not match.group('extras'):
match.group('extras')re.findall('\\w+', ''))()
    
    def _for(self, dist):
        vars(self).update(dist = dist)
        return self

    
    def matches(self, **params):
        """
        EntryPoint matches the given parameters.

        >>> ep = EntryPoint(group='foo', name='bar', value='bing:bong [extra1, extra2]')
        >>> ep.matches(group='foo')
        True
        >>> ep.matches(name='bar', value='bing:bong [extra1, extra2]')
        True
        >>> ep.matches(group='foo', name='other')
        False
        >>> ep.matches()
        True
        >>> ep.matches(extras=['extra1', 'extra2'])
        True
        >>> ep.matches(module='bing')
        True
        >>> ep.matches(attr='bong')
        True
        """
        pass
    # WARNING: Decompyle incomplete

    
    def _key(self):
        return (self.name, self.value, self.group)

    
    def __lt__(self, other):
        return self._key() < other._key()

    
    def __eq__(self, other):
        return self._key() == other._key()

    
    def __setattr__(self, name, value):
        raise AttributeError('EntryPoint objects are immutable.')

    
    def __repr__(self):
        return f'''EntryPoint(name={self.name!r}, value={self.value!r}, group={self.group!r})'''

    
    def __hash__(self):
        return hash(self._key())



class EntryPoints(tuple):
    '''
    An immutable collection of selectable EntryPoint objects.
    '''
    __slots__ = ()
    
    def __getitem__(self, name):
        '''
        Get the EntryPoint in self matching name.
        '''
        
        try:
            return next(iter(self.select(name = name)))
        except StopIteration:
            raise KeyError(name)


    
    def select(self, **params):
        '''
        Select entry points from self that match the
        given parameters (typically group and/or name).
        '''
        pass
    # WARNING: Decompyle incomplete

    names = (lambda self: pass# WARNING: Decompyle incomplete
)()
    groups = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _from_text_for = (lambda cls, text, dist: pass# WARNING: Decompyle incomplete
)()
    _from_text = (lambda text: if not text:
textSectioned.section_pairs('')())()


class PackagePath(pathlib.PurePosixPath):
    '''A reference to a path in a package'''
    
    def read_text(self, encoding = ('utf-8',)):
        stream = self.locate().open(encoding = encoding)
        None(None, None)
        return 
        with None:
            if not None, stream.read():
                pass

    
    def read_binary(self):
        stream = self.locate().open('rb')
        None(None, None)
        return 
        with None:
            if not None, stream.read():
                pass

    
    def locate(self):
        '''Return a path-like object for this path'''
        return self.dist.locate_file(self)



class FileHash:
    
    def __init__(self, spec):
        (self.mode, _, self.value) = spec.partition('=')

    
    def __repr__(self):
        return f'''<FileHash mode: {self.mode} value: {self.value}>'''



class DeprecatedNonAbstract:
    pass
# WARNING: Decompyle incomplete


class Distribution(DeprecatedNonAbstract):
    '''A Python distribution package.'''
    read_text = (lambda self = None, filename = None: pass)()
    locate_file = (lambda self, path: pass)()
    from_name = (lambda cls = None, name = abc.abstractmethod: if not name:
raise ValueError('A distribution name is required.')try:
next(cls.discover(name = name))except StopIteration:
raise PackageNotFoundError(name))()
    discover = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    at = (lambda path: PathDistribution(pathlib.Path(path)))()
    _discover_resolvers = (lambda : declared = sys.meta_path()filter(None, declared))()
    metadata = (lambda self = staticmethod: if not self.read_text('METADATA'):
self.read_text('METADATA')if not self.read_text('PKG-INFO'):
self.read_text('PKG-INFO')opt_text = self.read_text('')text = cast(str, opt_text)_adapters.Message(email.message_from_string(text)))()
    name = (lambda self: self.metadata['Name'])()
    _normalized_name = (lambda self: Prepared.normalize(self.name))()
    version = (lambda self: self.metadata['Version'])()
    entry_points = (lambda self: EntryPoints._from_text_for(self.read_text('entry_points.txt'), self))()
    files = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def _read_files_distinfo(self):
        '''
        Read the lines of RECORD
        '''
        text = self.read_text('RECORD')
        if text:
            text
        return text.splitlines()

    
    def _read_files_egginfo_installed(self):
        '''
        Read installed-files.txt and return lines in a similar
        CSV-parsable format as RECORD: each file must be placed
        relative to the site-packages directory and must also be
        quoted (since file names can contain literal commas).

        This file is written when the package is installed by pip,
        but it might not be written for other installation methods.
        Assume the file is accurate if it exists.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _read_files_egginfo_sources(self):
        '''
        Read SOURCES.txt and return lines in a similar CSV-parsable
        format as RECORD: each file name must be quoted (since it
        might contain literal commas).

        Note that SOURCES.txt is not a reliable source for what
        files are installed by a package. This file is generated
        for a source archive, and the files that are present
        there (e.g. setup.py) may not correctly reflect the files
        that are present after the package has been installed.
        '''
        text = self.read_text('SOURCES.txt')
        if text:
            text
        return map('"{}"'.format, text.splitlines())

    requires = (lambda self: if not self._read_dist_info_reqs():
self._read_dist_info_reqs()reqs = self._read_egg_info_reqs()if reqs:
reqslist(reqs))()
    
    def _read_dist_info_reqs(self):
        return self.metadata.get_all('Requires-Dist')

    
    def _read_egg_info_reqs(self):
        source = self.read_text('requires.txt')
        return pass_none(self._deps_from_requires_text)(source)

    _deps_from_requires_text = (lambda cls, source: cls._convert_egg_info_reqs_to_simple_reqs(Sectioned.read(source)))()
    _convert_egg_info_reqs_to_simple_reqs = (lambda sections: pass# WARNING: Decompyle incomplete
)()


class DistributionFinder(MetaPathFinder):
    '''
    A MetaPathFinder capable of discovering installed distributions.
    '''
    
    class Context:
        '''
        Keyword arguments presented by the caller to
        ``distributions()`` or ``Distribution.discover()``
        to narrow the scope of a search for distributions
        in all DistributionFinders.

        Each DistributionFinder may expect any parameters
        and should attempt to honor the canonical
        parameters defined below when appropriate.
        '''
        name = None
        
        def __init__(self, **kwargs):
            vars(self).update(kwargs)

        path = (lambda self: vars(self).get('path', sys.path))()

    find_distributions = (lambda self, context = (Context(),): pass)()


class FastPath:
    pass
# WARNING: Decompyle incomplete


class Lookup:
    
    def __init__(self = None, path = None):
        base = os.path.basename(path.root).lower()
        base_is_egg = base.endswith('.egg')
        self.infos = FreezableDefaultDict(list)
        self.eggs = FreezableDefaultDict(list)
        for child in path.children():
            low = child.lower()
            if low.endswith(('.dist-info', '.egg-info')):
                name = low.rpartition('.')[0].partition('-')[0]
                normalized = Prepared.normalize(name)
                self.infos[normalized].append(path.joinpath(child))
                continue
            if not base_is_egg:
                continue
            if not low == 'egg-info':
                continue
            name = base.rpartition('.')[0].partition('-')[0]
            legacy_normalized = Prepared.legacy_normalize(name)
            self.eggs[legacy_normalized].append(path.joinpath(child))
        self.infos.freeze()
        self.eggs.freeze()

    
    def search(self, prepared):
        infos = self.infos[prepared.normalized] if prepared else itertools.chain.from_iterable(self.infos.values())
        eggs = self.eggs[prepared.legacy_normalized] if prepared else itertools.chain.from_iterable(self.eggs.values())
        return itertools.chain(infos, eggs)



class Prepared:
    '''
    A prepared search for metadata on a possibly-named package.
    '''
    normalized = None
    legacy_normalized = None
    
    def __init__(self, name):
        self.name = name
    # WARNING: Decompyle incomplete

    normalize = (lambda name: re.sub('[-_.]+', '-', name).lower().replace('-', '_'))()
    legacy_normalize = (lambda name: name.lower().replace('-', '_'))()
    
    def __bool__(self):
        return bool(self.name)



class MetadataPathFinder(DistributionFinder):
    find_distributions = (lambda cls, context = (DistributionFinder.Context(),): found = cls._search_paths(context.name, context.path)map(PathDistribution, found))()
    _search_paths = (lambda cls, name, paths: pass# WARNING: Decompyle incomplete
)()
    invalidate_caches = (lambda cls: FastPath.__new__.cache_clear())()


class PathDistribution(Distribution):
    pass
# WARNING: Decompyle incomplete


def distribution(distribution_name):
    '''Get the ``Distribution`` instance for the named package.

    :param distribution_name: The name of the distribution package as a string.
    :return: A ``Distribution`` instance (or subclass thereof).
    '''
    return Distribution.from_name(distribution_name)


def distributions(**kwargs):
    '''Get all ``Distribution`` instances in the current environment.

    :return: An iterable of ``Distribution`` instances.
    '''
    pass
# WARNING: Decompyle incomplete


def metadata(distribution_name = None):
    '''Get the metadata for the named package.

    :param distribution_name: The name of the distribution package to query.
    :return: A PackageMetadata containing the parsed metadata.
    '''
    return Distribution.from_name(distribution_name).metadata


def version(distribution_name):
    '''Get the version string for the named package.

    :param distribution_name: The name of the distribution package to query.
    :return: The version string for the package as defined in the package\'s
        "Version" metadata key.
    '''
    return distribution(distribution_name).version

_unique = functools.partial(unique_everseen, key = operator.attrgetter('_normalized_name'))

def entry_points(**params):
    '''Return EntryPoint objects for all installed packages.

    Pass selection parameters (group or name) to filter the
    result to entry points matching those properties (see
    EntryPoints.select()).

    :return: EntryPoints for all installed packages.
    '''
    eps = (lambda .0: pass# WARNING: Decompyle incomplete
)(_unique(distributions())())
# WARNING: Decompyle incomplete


def files(distribution_name):
    '''Return a list of files for the named package.

    :param distribution_name: The name of the distribution package to query.
    :return: List of files composing the distribution.
    '''
    return distribution(distribution_name).files


def requires(distribution_name):
    '''
    Return a list of requirements for the named package.

    :return: An iterator of requirements, suitable for
        packaging.requirement.Requirement.
    '''
    return distribution(distribution_name).requires


def packages_distributions():
    '''
    Return a mapping of top-level packages to their
    distributions.

    >>> import collections.abc
    >>> pkgs = packages_distributions()
    >>> all(isinstance(dist, collections.abc.Sequence) for dist in pkgs.values())
    True
    '''
    pkg_to_dist = collections.defaultdict(list)
    for dist in distributions():
        if not _top_level_declared(dist):
            _top_level_declared(dist)
        for pkg in _top_level_inferred(dist):
            pkg_to_dist[pkg].append(dist.metadata['Name'])
    return dict(pkg_to_dist)


def _top_level_declared(dist):
    if not dist.read_text('top_level.txt'):
        dist.read_text('top_level.txt')
    return ''.split()


def _top_level_inferred(dist):
    pass
# WARNING: Decompyle incomplete

