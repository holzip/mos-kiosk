# Source Generated with Decompyle++
# File: pylock.pyc (Python 3.12)

from __future__ import annotations
import dataclasses
import logging
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Any, Callable, Protocol, TypeVar
from markers import Marker
from specifiers import SpecifierSet
from utils import NormalizedName, is_normalized_name
from version import Version
if TYPE_CHECKING:
    from pathlib import Path
    from typing_extensions import Self
_logger = logging.getLogger(__name__)
__all__ = [
    'Package',
    'PackageArchive',
    'PackageDirectory',
    'PackageSdist',
    'PackageVcs',
    'PackageWheel',
    'Pylock',
    'PylockUnsupportedVersionError',
    'PylockValidationError',
    'is_valid_pylock_path']
_T = TypeVar('_T')
_T2 = TypeVar('_T2')

class _FromMappingProtocol(Protocol):
    _from_dict = (lambda cls = None, d = None: pass)()

_FromMappingProtocolT = TypeVar('_FromMappingProtocolT', bound = _FromMappingProtocol)
_PYLOCK_FILE_NAME_RE = re.compile('^pylock\\.([^.]+)\\.toml$')

def is_valid_pylock_path(path = None):
    '''Check if the given path is a valid pylock file path.'''
    if not path.name == 'pylock.toml':
        path.name == 'pylock.toml'
    return bool(_PYLOCK_FILE_NAME_RE.match(path.name))


def _toml_key(key = None):
    return key.replace('_', '-')


def _toml_value(key = None, value = None):
    if isinstance(value, (Version, Marker, SpecifierSet)):
        return str(value)
# WARNING: Decompyle incomplete


def _toml_dict_factory(data = None):
    pass
# WARNING: Decompyle incomplete


def _get(d = None, expected_type = None, key = None):
    """Get a value from the dictionary and verify it's the expected type."""
    value = d.get(key)
# WARNING: Decompyle incomplete


def _get_required(d = None, expected_type = None, key = None):
    """Get a required value from the dictionary and verify it's the expected type."""
    value = _get(d, expected_type, key)
# WARNING: Decompyle incomplete


def _get_sequence(d = None, expected_item_type = None, key = None):
    """Get a list value from the dictionary and verify it's the expected items type."""
    value = _get(d, Sequence, key)
# WARNING: Decompyle incomplete


def _get_as(d = None, expected_type = None, target_type = None, key = ('d', 'Mapping[str, Any]', 'expected_type', 'type[_T]', 'target_type', 'Callable[[_T], _T2]', 'key', 'str', 'return', '_T2 | None')):
    """Get a value from the dictionary, verify it's the expected type,
    and convert to the target type.

    This assumes the target_type constructor accepts the value.
    """
    value = _get(d, expected_type, key)
# WARNING: Decompyle incomplete


def _get_required_as(d = None, expected_type = None, target_type = None, key = ('d', 'Mapping[str, Any]', 'expected_type', 'type[_T]', 'target_type', 'Callable[[_T], _T2]', 'key', 'str', 'return', '_T2')):
    """Get a required value from the dict, verify it's the expected type,
    and convert to the target type."""
    value = _get_as(d, expected_type, target_type, key)
# WARNING: Decompyle incomplete


def _get_sequence_as(d = None, expected_item_type = None, target_item_type = None, key = ('d', 'Mapping[str, Any]', 'expected_item_type', 'type[_T]', 'target_item_type', 'Callable[[_T], _T2]', 'key', 'str', 'return', 'list[_T2] | None')):
    '''Get list value from dictionary and verify expected items type.'''
    value = _get_sequence(d, expected_item_type, key)
# WARNING: Decompyle incomplete


def _get_object(d = None, target_type = None, key = None):
    '''Get a dictionary value from the dictionary and convert it to a dataclass.'''
    value = _get(d, Mapping, key)
# WARNING: Decompyle incomplete


def _get_sequence_of_objects(d = None, target_item_type = None, key = None):
    '''Get a list value from the dictionary and convert its items to a dataclass.'''
    value = _get_sequence(d, Mapping, key)
# WARNING: Decompyle incomplete


def _get_required_sequence_of_objects(d = None, target_item_type = None, key = None):
    '''Get a required list value from the dictionary and convert its items to a
    dataclass.'''
    result = _get_sequence_of_objects(d, target_item_type, key)
# WARNING: Decompyle incomplete


def _validate_normalized_name(name = None):
    '''Validate that a string is a NormalizedName.'''
    if not is_normalized_name(name):
        raise PylockValidationError(f'''Name {name!r} is not normalized''')
    return NormalizedName(name)


def _validate_path_url(path = None, url = None):
    if not path:
        if not url:
            raise PylockValidationError('path or url must be provided')
        return None


def _validate_hashes(hashes = None):
    if not hashes:
        raise PylockValidationError('At least one hash must be provided')
    if not (lambda .0: pass# WARNING: Decompyle incomplete
)(hashes.values()()):
        raise PylockValidationError('Hash values must be strings')
    return hashes


class PylockValidationError(Exception):
    '''Raised when when input data is not spec-compliant.'''
    message: 'str' = None
    
    def __init__(self = None, cause = None, *, context):
        if isinstance(cause, PylockValidationError):
            if cause.context:
                self.context = f'''{context}.{cause.context}''' if context else cause.context
            else:
                self.context = context
            self.message = cause.message
            return None
        self.context = context
        self.message = str(cause)

    
    def __str__(self = None):
        if self.context:
            return f'''{self.message} in {self.context!r}'''
        return None.message



class _PylockRequiredKeyError(PylockValidationError):
    pass
# WARNING: Decompyle incomplete


class PylockUnsupportedVersionError(PylockValidationError):
    '''Raised when encountering an unsupported `lock_version`.'''
    pass

PackageVcs = <NODE:12>()
PackageDirectory = <NODE:12>()
PackageArchive = <NODE:12>()
PackageSdist = <NODE:12>()
PackageWheel = <NODE:12>()
Package = <NODE:12>()
Pylock = <NODE:12>()
