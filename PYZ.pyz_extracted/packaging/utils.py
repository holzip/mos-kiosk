# Source Generated with Decompyle++
# File: utils.pyc (Python 3.12)

from __future__ import annotations
import re
from typing import NewType, Tuple, Union, cast
from tags import Tag, parse_tag
from version import InvalidVersion, Version, _TrimmedRelease
BuildTag = Union[(Tuple[()], Tuple[(int, str)])]
NormalizedName = NewType('NormalizedName', str)

class InvalidName(ValueError):
    '''
    An invalid distribution name; users should refer to the packaging user guide.
    '''
    pass


class InvalidWheelFilename(ValueError):
    '''
    An invalid wheel filename was found, users should refer to PEP 427.
    '''
    pass


class InvalidSdistFilename(ValueError):
    '''
    An invalid sdist filename was found, users should refer to the packaging user guide.
    '''
    pass

_validate_regex = re.compile('[A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9]', re.IGNORECASE)
_normalized_regex = re.compile('[a-z0-9]|[a-z0-9]([a-z0-9-](?!--))*[a-z0-9]')
_build_tag_regex = re.compile('(\\d+)(.*)')

def canonicalize_name(name = None, *, validate):
    if not validate and _validate_regex.fullmatch(name):
        raise InvalidName(f'''name is invalid: {name!r}''')
    value = name.lower().replace('_', '-').replace('.', '-')
    if '--' in value:
        value = value.replace('--', '-')
        if '--' in value:
            continue
    return cast('NormalizedName', value)


def is_normalized_name(name = None):
    return _normalized_regex.fullmatch(name) is not None


def canonicalize_version(version = None, *, strip_trailing_zero):
    """
    Return a canonical form of a version as a string.

    >>> canonicalize_version('1.0.1')
    '1.0.1'

    Per PEP 625, versions may have multiple canonical forms, differing
    only by trailing zeros.

    >>> canonicalize_version('1.0.0')
    '1'
    >>> canonicalize_version('1.0.0', strip_trailing_zero=False)
    '1.0.0'

    Invalid versions are returned unaltered.

    >>> canonicalize_version('foo bar baz')
    'foo bar baz'
    """
    if isinstance(version, str):
        
        try:
            version = Version(version)
            if strip_trailing_zero:
                return str(_TrimmedRelease(version))
            return None(str)
        except InvalidVersion:
            return 



def parse_wheel_filename(filename = None):
    if not filename.endswith('.whl'):
        raise InvalidWheelFilename(f'''Invalid wheel filename (extension must be \'.whl\'): {filename!r}''')
    filename = filename[:-4]
    dashes = filename.count('-')
    if dashes not in (4, 5):
        raise InvalidWheelFilename(f'''Invalid wheel filename (wrong number of parts): {filename!r}''')
    parts = filename.split('-', dashes - 2)
    name_part = parts[0]
# WARNING: Decompyle incomplete


def parse_sdist_filename(filename = None):
    if filename.endswith('.tar.gz'):
        file_stem = filename[:-len('.tar.gz')]
    elif filename.endswith('.zip'):
        file_stem = filename[:-len('.zip')]
    else:
        raise InvalidSdistFilename(f'''Invalid sdist filename (extension must be \'.tar.gz\' or \'.zip\'): {filename!r}''')
    (name_part, sep, version_part) = file_stem.rpartition('-')
    if not sep:
        raise InvalidSdistFilename(f'''Invalid sdist filename: {filename!r}''')
    name = canonicalize_name(name_part)
    
    try:
        version = Version(version_part)
        return (name, version)
    except InvalidVersion:
        e = None
        raise InvalidSdistFilename(f'''Invalid sdist filename (invalid version): {filename!r}'''), e
        e = None
        del e


