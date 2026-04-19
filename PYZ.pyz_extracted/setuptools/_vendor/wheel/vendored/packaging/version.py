# Source Generated with Decompyle++
# File: version.pyc (Python 3.12)

'''
.. testsetup::

    from packaging.version import parse, Version
'''
import itertools
import re
from typing import Any, Callable, NamedTuple, Optional, SupportsInt, Tuple, Union
from _structures import Infinity, InfinityType, NegativeInfinity, NegativeInfinityType
__all__ = [
    'VERSION_PATTERN',
    'parse',
    'Version',
    'InvalidVersion']
LocalType = Tuple[(Union[(int, str)], ...)]
CmpPrePostDevType = Union[(InfinityType, NegativeInfinityType, Tuple[(str, int)])]
CmpLocalType = Union[(NegativeInfinityType, Tuple[(Union[(Tuple[(int, str)], Tuple[(NegativeInfinityType, Union[(int, str)])])], ...)])]
CmpKey = Tuple[(int, Tuple[(int, ...)], CmpPrePostDevType, CmpPrePostDevType, CmpPrePostDevType, CmpLocalType)]
VersionComparisonMethod = Callable[([
    CmpKey,
    CmpKey], bool)]

class _Version(NamedTuple):
    local: Optional[LocalType] = '_Version'


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
    _key: Tuple[(Any, ...)] = '_BaseVersion'
    
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


_VERSION_PATTERN = '\n    v?\n    (?:\n        (?:(?P<epoch>[0-9]+)!)?                           # epoch\n        (?P<release>[0-9]+(?:\\.[0-9]+)*)                  # release segment\n        (?P<pre>                                          # pre-release\n            [-_\\.]?\n            (?P<pre_l>alpha|a|beta|b|preview|pre|c|rc)\n            [-_\\.]?\n            (?P<pre_n>[0-9]+)?\n        )?\n        (?P<post>                                         # post release\n            (?:-(?P<post_n1>[0-9]+))\n            |\n            (?:\n                [-_\\.]?\n                (?P<post_l>post|rev|r)\n                [-_\\.]?\n                (?P<post_n2>[0-9]+)?\n            )\n        )?\n        (?P<dev>                                          # dev release\n            [-_\\.]?\n            (?P<dev_l>dev)\n            [-_\\.]?\n            (?P<dev_n>[0-9]+)?\n        )?\n    )\n    (?:\\+(?P<local>[a-z0-9]+(?:[-_\\.][a-z0-9]+)*))?       # local version\n'
VERSION_PATTERN = _VERSION_PATTERN

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
    _key: CmpKey = re.compile('^\\s*' + VERSION_PATTERN + '\\s*$', re.VERBOSE | re.IGNORECASE)
    
    def __init__(self = None, version = None):
        '''Initialize a Version object.

        :param version:
            The string representation of a version which will be parsed and normalized
            before use.
        :raises InvalidVersion:
            If the ``version`` does not conform to PEP 440 in any way then this
            exception will be raised.
        '''
        match = self._regex.search(version)
        if not match:
            raise InvalidVersion(f'''Invalid version: \'{version}\'''')
        if not match.group('post_n1'):
            match.group('post_n1')
        self._version = None(epoch = tuple, release = (lambda .0: pass# WARNING: Decompyle incomplete
)(match.group('release').split('.')()), pre = _parse_letter_version(match.group('pre_l'), match.group('pre_n')), post = _parse_letter_version(match.group('post_l'), match.group('post_n2')), dev = _parse_letter_version(match.group('dev_l'), match.group('dev_n')), local = _parse_local_version(match.group('local')))
        self._key = _cmpkey(self._version.epoch, self._version.release, self._version.pre, self._version.post, self._version.dev, self._version.local)

    
    def __repr__(self = None):
        """A representation of the Version that shows all internal state.

        >>> Version('1.0.0')
        <Version('1.0.0')>
        """
        return f'''<Version(\'{self}\')>'''

    
    def __str__(self = None):
        '''A string representation of the version that can be rounded-tripped.

        >>> str(Version("1.0a5"))
        \'1.0a5\'
        '''
        parts = []
        if self.epoch != 0:
            parts.append(f'''{self.epoch}!''')
        '.'.join((lambda .0: pass# WARNING: Decompyle incomplete
)(self.release()))
    # WARNING: Decompyle incomplete

    epoch = (lambda self = None: self._version.epoch)()
    release = (lambda self = None: self._version.release)()
    pre = (lambda self = None: self._version.pre)()
    post = (lambda self = None: if self._version.post:
self._version.post[1])()
    dev = (lambda self = None: if self._version.dev:
self._version.dev[1])()
    local = (lambda self = None: if self._version.local:
(lambda .0: pass# WARNING: Decompyle incomplete
)(self._version.local())
)()
    public = (lambda self = None: str(self).split('+', 1)[0])()
    base_version = (lambda self = None: parts = []if self.epoch != 0:
parts.append(f'''{self.epoch}!''')'.'.join((lambda .0: pass# WARNING: Decompyle incomplete
)(self.release()))
        return ''.join(parts)
)()
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


def _parse_letter_version(letter = None, number = None):
    pass
# WARNING: Decompyle incomplete

_local_version_separators = re.compile('[\\._-]')

def _parse_local_version(local = None):
    '''
    Takes a string like abc.1.twelve and turns it into ("abc", 1, "twelve").
    '''
    pass
# WARNING: Decompyle incomplete


def _cmpkey(epoch, release, pre = None, post = None, dev = None, local = ('epoch', int, 'release', Tuple[(int, ...)], 'pre', Optional[Tuple[(str, int)]], 'post', Optional[Tuple[(str, int)]], 'dev', Optional[Tuple[(str, int)]], 'local', Optional[LocalType], 'return', CmpKey)):
    _release = tuple(reversed(list(itertools.dropwhile((lambda x: x == 0), reversed(release)))))
# WARNING: Decompyle incomplete

