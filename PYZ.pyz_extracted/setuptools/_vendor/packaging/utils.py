# Source Generated with Decompyle++
# File: utils.pyc (Python 3.12)

from __future__ import annotations
import functools
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

_validate_regex = re.compile('^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$', re.IGNORECASE)
_canonicalize_regex = re.compile('[-_.]+')
_normalized_regex = re.compile('^([a-z0-9]|[a-z0-9]([a-z0-9-](?!--))*[a-z0-9])$')
_build_tag_regex = re.compile('(\\d+)(.*)')

def canonicalize_name(name = None, *, validate):
    if not validate and _validate_regex.match(name):
        raise InvalidName(f'''name is invalid: {name!r}''')
    value = _canonicalize_regex.sub('-', name).lower()
    return cast(NormalizedName, value)


def is_normalized_name(name = None):
    return _normalized_regex.match(name) is not None

canonicalize_version = (lambda version = None, *, strip_trailing_zero: if strip_trailing_zero:
str(_TrimmedRelease(str(version)))None(str))()
_ = (lambda version = None, *, strip_trailing_zero: try:
parsed = Version(version)canonicalize_version(parsed, strip_trailing_zero = strip_trailing_zero)except InvalidVersion:
)()

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


