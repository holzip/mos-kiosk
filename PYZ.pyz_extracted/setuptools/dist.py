# Source Generated with Decompyle++
# File: dist.pyc (Python 3.12)

from __future__ import annotations
import io
import itertools
import numbers
import os
import re
import sys
from collections.abc import Iterable, MutableMapping, Sequence
from glob import iglob
from pathlib import Path
from typing import TYPE_CHECKING, Any, Union
from more_itertools import partition, unique_everseen
from packaging.markers import InvalidMarker, Marker
from packaging.specifiers import InvalidSpecifier, SpecifierSet
from packaging.version import Version
from  import _entry_points, _reqs, _static, command as _
from _importlib import metadata
from _path import StrPath
from _reqs import _StrOrIter
from config import pyprojecttoml, setupcfg
from discovery import ConfigDiscovery
from monkey import get_unpatched
from warnings import InformationOnly, SetuptoolsDeprecationWarning
import distutils.cmd as distutils
import distutils.command as distutils
import distutils.core as distutils
import distutils.dist as distutils
import distutils.log as distutils
from distutils.debug import DEBUG
from distutils.errors import DistutilsOptionError, DistutilsSetupError
from distutils.fancy_getopt import translate_longopt
from distutils.util import strtobool
if TYPE_CHECKING:
    from typing_extensions import TypeAlias
    from pkg_resources import Distribution as _pkg_resources_Distribution
__all__ = [
    'Distribution']
_sequence = (tuple, list)
_Sequence: 'TypeAlias' = Union[(tuple[(str, ...)], list[str])]
_sequence_type_repr = 'tuple[str, ...] | list[str]'
_OrderedStrSequence: 'TypeAlias' = Union[(str, dict[(str, Any)], Sequence[str])]

def __getattr__(name = None):
    if name == 'sequence':
        SetuptoolsDeprecationWarning.emit('`setuptools.dist.sequence` is an internal implementation detail.', 'Please define your own `sequence = tuple, list` instead.', due_date = (2025, 8, 28))
        return _sequence
    raise None(f'''module {__name__!r} has no attribute {name!r}''')


def check_importable(dist, attr, value):
    pass
# WARNING: Decompyle incomplete


def assert_string_list(dist = None, attr = None, value = None):
    '''Verify that value is a string list'''
    pass
# WARNING: Decompyle incomplete


def check_nsp(dist, attr, value):
    '''Verify that namespace packages are valid'''
    ns_packages = value
    assert_string_list(dist, attr, ns_packages)
    for nsp in ns_packages:
        if not dist.has_contents_for(nsp):
            raise DistutilsSetupError(f'''Distribution contains no modules or packages for namespace package {nsp!r}''')
        (parent, _sep, _child) = nsp.rpartition('.')
        if parent and parent not in ns_packages:
            distutils.log.warn('WARNING: %r is declared as a package namespace, but %r is not: please correct this in setup.py', nsp, parent)
        SetuptoolsDeprecationWarning.emit('The namespace_packages parameter is deprecated.', 'Please replace its usage with implicit namespaces (PEP 420).', see_docs = 'references/keywords.html#keyword-namespace-packages')


def check_extras(dist, attr, value):
    '''Verify that extras_require mapping is valid'''
    
    try:
        list(itertools.starmap(_check_extra, value.items()))
        return None
    except (TypeError, ValueError, AttributeError):
        e = None
        raise DistutilsSetupError("'extras_require' must be a dictionary whose values are strings or lists of strings containing valid project/version requirement specifiers."), e
        e = None
        del e



def _check_extra(extra, reqs):
    (_name, _sep, marker) = extra.partition(':')
    
    try:
        _check_marker(marker)
        list(_reqs.parse(reqs))
        return None
    except InvalidMarker:
        msg = f'''Invalid environment marker: {marker} ({extra!r})'''
        raise DistutilsSetupError(msg), None



def _check_marker(marker):
    if not marker:
        return None
    m = Marker(marker)
    m.evaluate()


def assert_bool(dist, attr, value):
    '''Verify that value is True, False, 0, or 1'''
    if bool(value) != value:
        raise DistutilsSetupError(f'''{attr!r} must be a boolean value (got {value!r})''')


def invalid_unless_false(dist, attr, value):
    if not value:
        DistDeprecationWarning.emit(f'''{attr} is ignored.''')
        return None
    raise DistutilsSetupError(f'''{attr} is invalid.''')


def check_requirements(dist = None, attr = None, value = None):
    '''Verify that install_requires is a valid requirements list'''
    
    try:
        list(_reqs.parse(value))
        if isinstance(value, set):
            raise TypeError('Unordered types are not allowed')
        return None
    except (TypeError, ValueError):
        error = None
        msg = f'''{attr!r} must be a string or iterable of strings containing valid project/version requirement specifiers; {error}'''
        raise DistutilsSetupError(msg), error
        error = None
        del error



def check_specifier(dist, attr, value):
    '''Verify that value is a valid version specifier'''
    
    try:
        SpecifierSet(value)
        return None
    except (InvalidSpecifier, AttributeError):
        error = None
        msg = f'''{attr!r} must be a string containing valid version specifiers; {error}'''
        raise DistutilsSetupError(msg), error
        error = None
        del error



def check_entry_points(dist, attr, value):
    '''Verify that entry_points map is parseable'''
    
    try:
        _entry_points.load(value)
        return None
    except Exception:
        e = None
        raise DistutilsSetupError(e), e
        e = None
        del e



def check_package_data(dist, attr, value):
    '''Verify that value is a dictionary of package names to glob lists'''
    if not isinstance(value, dict):
        raise DistutilsSetupError(f'''{attr!r} must be a dictionary mapping package names to lists of string wildcard patterns''')
    for k, v in value.items():
        if not isinstance(k, str):
            raise DistutilsSetupError(f'''keys of {attr!r} dict must be strings (got {k!r})''')
        assert_string_list(dist, f'''values of {attr!r} dict''', v)


def check_packages(dist, attr, value):
    for pkgname in value:
        if re.match('\\w+(\\.\\w+)*', pkgname):
            continue
        distutils.log.warn('WARNING: %r not a valid package name; please use only .-separated package names in setup.py', pkgname)

if TYPE_CHECKING:
    from distutils.core import Distribution as _Distribution
else:
    _Distribution = get_unpatched(distutils.core.Distribution)

class Distribution(_Distribution):
    pass
# WARNING: Decompyle incomplete


class DistDeprecationWarning(SetuptoolsDeprecationWarning):
    '''Class for warning about deprecations in dist in
    setuptools. Not ignored by default, unlike DeprecationWarning.'''
    pass

