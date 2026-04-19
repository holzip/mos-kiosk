# Source Generated with Decompyle++
# File: metadata.pyc (Python 3.12)

'''
Tools for converting old- to new-style metadata.
'''
from __future__ import annotations
import functools
import itertools
import os.path as os
import re
import textwrap
from email.message import Message
from email.parser import Parser
from typing import Iterator
from vendored.packaging.requirements import Requirement

def _nonblank(str):
    if str:
        str
    return not str.startswith('#')

yield_lines = (lambda iterable: itertools.chain.from_iterable(map(yield_lines, iterable)))()
_ = (lambda text: filter(_nonblank, map(str.strip, text.splitlines())))()

def split_sections(s):
    '''Split a string or iterable thereof into (section, content) pairs
    Each ``section`` is a stripped version of the section header ("[section]")
    and each ``content`` is a list of stripped lines excluding blank lines and
    comment-only lines.  If there are any such lines before the first section
    header, they\'re returned in a first ``section`` of ``None``.
    '''
    pass
# WARNING: Decompyle incomplete


def safe_extra(extra):
    """Convert an arbitrary string to a standard 'extra' name
    Any runs of non-alphanumeric characters are replaced with a single '_',
    and the result is always lowercased.
    """
    return re.sub('[^A-Za-z0-9.-]+', '_', extra).lower()


def safe_name(name):
    """Convert an arbitrary string to a standard distribution name
    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    """
    return re.sub('[^A-Za-z0-9.]+', '-', name)


def requires_to_requires_dist(requirement = None):
    '''Return the version specifier for a requirement in PEP 345/566 fashion.'''
    if getattr(requirement, 'url', None):
        return ' @ ' + requirement.url
    requires_dist = None
    for spec in requirement.specifier:
        requires_dist.append(spec.operator + spec.version)
    if requires_dist:
        return ' ' + ','.join(sorted(requires_dist))


def convert_requirements(requirements = None):
    '''Yield Requires-Dist: strings for parsed requirements strings.'''
    pass
# WARNING: Decompyle incomplete


def generate_requirements(extras_require = None):
    """
    Convert requirements from a setup()-style dictionary to
    ('Requires-Dist', 'requirement') and ('Provides-Extra', 'extra') tuples.

    extras_require is a dictionary of {extra: [requirements]} as passed to setup(),
    using the empty extra {'': [requirements]} to hold install_requires.
    """
    pass
# WARNING: Decompyle incomplete


def pkginfo_to_metadata(egg_info_path = None, pkginfo_path = None):
    '''
    Convert .egg-info directory with PKG-INFO to the Metadata 2.1 format
    '''
    headers = open(pkginfo_path, encoding = 'utf-8')
    pkg_info = Parser().parse(headers)
    None(None, None)
# WARNING: Decompyle incomplete

