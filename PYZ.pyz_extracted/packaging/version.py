# Source Generated with Decompyle++
# File: version.pyc (Python 3.12)

'''
.. testsetup::

    from packaging.version import parse, Version
'''
from __future__ import annotations
import re
import sys
import typing
from typing import Any, Callable, Literal, NamedTuple, SupportsInt, Tuple, TypedDict, Union
from _structures import Infinity, InfinityType, NegativeInfinity, NegativeInfinityType
if typing.TYPE_CHECKING:
    from typing_extensions import Self, Unpack
if sys.version_info >= (3, 13):
    from warnings import deprecated as _deprecated
elif typing.TYPE_CHECKING:
    from typing_extensions import deprecated as _deprecated
else:
    import functools
    import warnings
    
    def _deprecated(message = None):
        pass
    # WARNING: Decompyle incomplete

_LETTER_NORMALIZATION = {
    'alpha': 'a',
    'beta': 'b',
    'c': 'rc',
    'pre': 'rc',
    'preview': 'rc',
    'rev': 'post',
    'r': 'post' }
__all__ = [
    'VERSION_PATTERN',
    'InvalidVersion',
    'Version',
    'parse']
LocalType = Tuple[(Union[(int, str)], ...)]
CmpPrePostDevType = Union[(InfinityType, NegativeInfinityType, Tuple[(str, int)])]
CmpLocalType = Union[(NegativeInfinityType, Tuple[(Union[(Tuple[(int, str)], Tuple[(NegativeInfinityType, Union[(int, str)])])], ...)])]
CmpKey = Tuple[(int, Tuple[(int, ...)], CmpPrePostDevType, CmpPrePostDevType, CmpPrePostDevType, CmpLocalType)]
VersionComparisonMethod = Callable[([
    CmpKey,
    CmpKey], bool)]

def _VersionReplace():
    '''_VersionReplace'''
    local: 'str | None' = '_VersionReplace'

_VersionReplace = <NODE:27>(_VersionReplace, '_VersionReplace', TypedDict, total = False)

def parse(version = None):
    """Parse the given version string.

    >>> parse('1.0.dev1')
    <Version('1.0.dev1')>

    :param version: The version string to parse.
    :raises InvalidVersion: When the version string is not a valid version.
    """
    return Version(version)


class InvalidVersion(ValueError):
    '''Raised when a version string is not a valid version.

    >>> Version("invalid")
    Traceback (most recent call last):
        ...
    packaging.version.InvalidVersion: Invalid version: \'invalid\'
    '''
    pass


class _BaseVersion:
    __slots__ = ()
    if typing.TYPE_CHECKING:
        _key = (lambda self = None: pass)()
    
    def __hash__(self = None):
        return hash(self._key)

    
    def __lt__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key < other._key

    
    def __le__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key <= other._key

    
    def __eq__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key == other._key

    
    def __ge__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key >= other._key

    
    def __gt__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key > other._key

    
    def __ne__(self = None, other = None):
        if not isinstance(other, _BaseVersion):
            return NotImplemented
        return None._key != other._key


_VERSION_PATTERN = '\n    v?+                                                   # optional leading v\n    (?:\n        (?:(?P<epoch>[0-9]+)!)?+                          # epoch\n        (?P<release>[0-9]+(?:\\.[0-9]+)*+)                 # release segment\n        (?P<pre>                                          # pre-release\n            [._-]?+\n            (?P<pre_l>alpha|a|beta|b|preview|pre|c|rc)\n            [._-]?+\n            (?P<pre_n>[0-9]+)?\n        )?+\n        (?P<post>                                         # post release\n            (?:-(?P<post_n1>[0-9]+))\n            |\n            (?:\n                [._-]?\n                (?P<post_l>post|rev|r)\n                [._-]?\n                (?P<post_n2>[0-9]+)?\n            )\n        )?+\n        (?P<dev>                                          # dev release\n            [._-]?+\n            (?P<dev_l>dev)\n            [._-]?+\n            (?P<dev_n>[0-9]+)?\n        )?+\n    )\n    (?:\\+\n        (?P<local>                                        # local version\n            [a-z0-9]+\n            (?:[._-][a-z0-9]+)*+\n        )\n    )?+\n'
_VERSION_PATTERN_OLD = _VERSION_PATTERN.replace('*+', '*').replace('?+', '?')
if not sys.implementation.name == 'cpython' or sys.version_info < (3, 11, 5):
    pass
VERSION_PATTERN = _VERSION_PATTERN_OLD if sys.implementation.name == 'pypy' or sys.version_info < (3, 11, 13) or sys.version_info < (3, 11) else _VERSION_PATTERN
_LOCAL_PATTERN = re.compile('[a-z0-9]+(?:[._-][a-z0-9]+)*', re.IGNORECASE)

def _validate_epoch(value = None):
    if not value:
        value
    epoch = 0
    if isinstance(epoch, int) and epoch >= 0:
        return epoch
    msg = f'''{epoch}'''
    raise InvalidVersion(msg)


def _validate_release(value = None):
    pass
# WARNING: Decompyle incomplete


def _validate_pre(value = None):
    pass
# WARNING: Decompyle incomplete


def _validate_post(value = None):
    pass
# WARNING: Decompyle incomplete


def _validate_dev(value = None):
    pass
# WARNING: Decompyle incomplete


def _validate_local(value = None):
    pass
# WARNING: Decompyle incomplete


class _Version(NamedTuple):
    local: 'LocalType | None' = '_Version'


class Version(_BaseVersion):
    '''This class abstracts handling of a project\'s versions.

    A :class:`Version` instance is comparison aware and can be compared and
    sorted using the standard Python interfaces.

    >>> v1 = Version("1.0a5")
    >>> v2 = Version("1.0")
    >>> v1
    <Version(\'1.0a5\')>
    >>> v2
    <Version(\'1.0\')>
    >>> v1 < v2
    True
    >>> v1 == v2
    False
    >>> v1 > v2
    False
    >>> v1 >= v2
    False
    >>> v1 <= v2
    True
    '''
    __slots__ = ('_dev', '_epoch', '_key_cache', '_local', '_post', '_pre', '_release')
    __match_args__ = ('_str',)
    _key_cache: 'CmpKey | None' = re.compile('\\s*' + VERSION_PATTERN + '\\s*', re.VERBOSE | re.IGNORECASE)
    
    def __init__(self = None, version = None):
        '''Initialize a Version object.

        :param version:
            The string representation of a version which will be parsed and normalized
            before use.
        :raises InvalidVersion:
            If the ``version`` does not conform to PEP 440 in any way then this
            exception will be raised.
        '''
        match = self._regex.fullmatch(version)
        if not match:
            raise InvalidVersion(f'''Invalid version: {version!r}''')
        self._epoch = int(match.group('epoch')) if match.group('epoch') else 0
        self._release = tuple(map(int, match.group('release').split('.')))
        self._pre = _parse_letter_version(match.group('pre_l'), match.group('pre_n'))
        if not match.group('post_n1'):
            match.group('post_n1')
        self._post = _parse_letter_version(match.group('post_l'), match.group('post_n2'))
        self._dev = _parse_letter_version(match.group('dev_l'), match.group('dev_n'))
        self._local = _parse_local_version(match.group('local'))
        self._key_cache = None

    
    def __replace__(self = None, **kwargs):
        epoch = _validate_epoch(kwargs['epoch']) if 'epoch' in kwargs else self._epoch
        release = _validate_release(kwargs['release']) if 'release' in kwargs else self._release
        pre = _validate_pre(kwargs['pre']) if 'pre' in kwargs else self._pre
        post = _validate_post(kwargs['post']) if 'post' in kwargs else self._post
        dev = _validate_dev(kwargs['dev']) if 'dev' in kwargs else self._dev
        local = _validate_local(kwargs['local']) if 'local' in kwargs else self._local
        if epoch == self._epoch and release == self._release and pre == self._pre and post == self._post and dev == self._dev and local == self._local:
            return self
        new_version = None.__class__.__new__(self.__class__)
        new_version._key_cache = None
        new_version._epoch = epoch
        new_version._release = release
        new_version._pre = pre
        new_version._post = post
        new_version._dev = dev
        new_version._local = local
        return new_version

    _key = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _version = (lambda self = None: _Version(self._epoch, self._release, self._dev, self._pre, self._post, self._local))()()
    _version = (lambda self = None, value = _version.setter: self._epoch = value.epochself._release = value.releaseself._dev = value.devself._pre = value.preself._post = value.postself._local = value.localself._key_cache = None)()()
    
    def __repr__(self = None):
        """A representation of the Version that shows all internal state.

        >>> Version('1.0.0')
        <Version('1.0.0')>
        """
        return f'''<Version(\'{self}\')>'''

    
    def __str__(self = None):
        '''A string representation of the version that can be round-tripped.

        >>> str(Version("1.0a5"))
        \'1.0a5\'
        '''
        version = '.'.join(map(str, self.release))
        if self.epoch:
            version = f'''{self.epoch}!{version}'''
    # WARNING: Decompyle incomplete

    _str = (lambda self = None: str(self))()
    epoch = (lambda self = None: self._epoch)()
    release = (lambda self = None: self._release)()
    pre = (lambda self = None: self._pre)()
    post = (lambda self = None: if self._post:
self._post[1])()
    dev = (lambda self = None: if self._dev:
self._dev[1])()
    local = (lambda self = None: if self._local:
(lambda .0: pass# WARNING: Decompyle incomplete
)(self._local())
)()
    public = (lambda self = None: str(self).split('+', 1)[0])()
    base_version = (lambda self = None: release_segment = '.'.join(map(str, self.release))if self.epoch:
f'''{self.epoch}!{release_segment}''')()
    is_prerelease = (lambda self = None: if not self.dev is not None:
self.dev is not Noneself.pre is not None)()
    is_postrelease = (lambda self = None: self.post is not None)()
    is_devrelease = (lambda self = None: self.dev is not None)()
    major = (lambda self = None: if len(self.release) >= 1:
self.release[0])()
    minor = (lambda self = None: if len(self.release) >= 2:
self.release[1])()
    micro = (lambda self = None: if len(self.release) >= 3:
self.release[2])()


class _TrimmedRelease(Version):
    pass
# WARNING: Decompyle incomplete


def _parse_letter_version(letter = None, number = None):
    if letter:
        letter = letter.lower()
        letter = _LETTER_NORMALIZATION.get(letter, letter)
        if not number:
            number
        return (letter, int(0))
    if None:
        return ('post', int(number))

_local_version_separators = re.compile('[\\._-]')

def _parse_local_version(local = None):
    '''
    Takes a string like abc.1.twelve and turns it into ("abc", 1, "twelve").
    '''
    pass
# WARNING: Decompyle incomplete


def _cmpkey(epoch, release, pre = None, post = None, dev = None, local = ('epoch', 'int', 'release', 'tuple[int, ...]', 'pre', 'tuple[str, int] | None', 'post', 'tuple[str, int] | None', 'dev', 'tuple[str, int] | None', 'local', 'LocalType | None', 'return', 'CmpKey')):
    len_release = len(release)
    i = len_release
    if i and release[i - 1] == 0:
        i -= 1
        if i and release[i - 1] == 0:
            continue
    _release = release if i == len_release else release[:i]
# WARNING: Decompyle incomplete

