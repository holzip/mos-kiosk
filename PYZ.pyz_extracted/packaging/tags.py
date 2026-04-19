# Source Generated with Decompyle++
# File: tags.pyc (Python 3.12)

from __future__ import annotations
import logging
import platform
import re
import struct
import subprocess
import sys
import sysconfig
from importlib.machinery import EXTENSION_SUFFIXES
from typing import Any, Iterable, Iterator, Sequence, Tuple, cast
from  import _manylinux, _musllinux
logger = logging.getLogger(__name__)
PythonVersion = Sequence[int]
AppleVersion = Tuple[(int, int)]
INTERPRETER_SHORT_NAMES: 'dict[str, str]' = {
    'python': 'py',
    'cpython': 'cp',
    'pypy': 'pp',
    'ironpython': 'ip',
    'jython': 'jy' }
_32_BIT_INTERPRETER = struct.calcsize('P') == 4

class Tag:
    '''
    A representation of the tag triple for a wheel.

    Instances are considered immutable and thus are hashable. Equality checking
    is also supported.
    '''
    __slots__ = [
        '_abi',
        '_hash',
        '_interpreter',
        '_platform']
    
    def __init__(self = None, interpreter = None, abi = None, platform = ('interpreter', 'str', 'abi', 'str', 'platform', 'str', 'return', 'None')):
        self._interpreter = interpreter.lower()
        self._abi = abi.lower()
        self._platform = platform.lower()
        self._hash = hash((self._interpreter, self._abi, self._platform))

    interpreter = (lambda self = None: self._interpreter)()
    abi = (lambda self = None: self._abi)()
    platform = (lambda self = None: self._platform)()
    
    def __eq__(self = None, other = None):
        if not isinstance(other, Tag):
            return NotImplemented
        if None._hash == other._hash:
            None._hash == other._hash
            if self._platform == other._platform:
                self._platform == other._platform
                if self._abi == other._abi:
                    self._abi == other._abi
        return self._interpreter == other._interpreter

    
    def __hash__(self = None):
        return self._hash

    
    def __str__(self = None):
        return f'''{self._interpreter}-{self._abi}-{self._platform}'''

    
    def __repr__(self = None):
        return f'''<{self} @ {id(self)}>'''

    
    def __setstate__(self = None, state = None):
        (_, slots) = state
        for k, v in slots.items():
            setattr(self, k, v)
        self._hash = hash((self._interpreter, self._abi, self._platform))



def parse_tag(tag = None):
    '''
    Parses the provided tag (e.g. `py3-none-any`) into a frozenset of Tag instances.

    Returning a set is required due to the possibility that the tag is a
    compressed tag set.
    '''
    tags = set()
    (interpreters, abis, platforms) = tag.split('-')
    for interpreter in interpreters.split('.'):
        for abi in abis.split('.'):
            for platform_ in platforms.split('.'):
                tags.add(Tag(interpreter, abi, platform_))
    return frozenset(tags)


def _get_config_var(name = None, warn = None):
    value = sysconfig.get_config_var(name)
# WARNING: Decompyle incomplete


def _normalize_string(string = None):
    return string.replace('.', '_').replace('-', '_').replace(' ', '_')


def _is_threaded_cpython(abis = None):
    '''
    Determine if the ABI corresponds to a threaded (`--disable-gil`) build.

    The threaded builds are indicated by a "t" in the abiflags.
    '''
    if len(abis) == 0:
        return False
    m = re.match('cp\\d+(.*)', abis[0])
    if not m:
        return False
    abiflags = m.group(1)
    return 't' in abiflags


def _abi3_applies(python_version = None, threading = None):
    '''
    Determine if the Python version supports abi3.

    PEP 384 was first implemented in Python 3.2. The threaded (`--disable-gil`)
    builds do not support abi3.
    '''
    if len(python_version) > 1:
        len(python_version) > 1
        if tuple(python_version) >= (3, 2):
            tuple(python_version) >= (3, 2)
    return not threading


def _cpython_abis(py_version = None, warn = None):
    py_version = tuple(py_version)
    abis = []
    version = _version_nodot(py_version[:2])
    threading = ''
    debug = ''
    pymalloc = ''
    ucs4 = ''
    with_debug = _get_config_var('Py_DEBUG', warn)
    has_refcount = hasattr(sys, 'gettotalrefcount')
    has_ext = '_d.pyd' in EXTENSION_SUFFIXES
# WARNING: Decompyle incomplete


def cpython_tags(python_version = None, abis = None, platforms = None, *, warn):
    """
    Yields the tags for a CPython interpreter.

    The tags consist of:
    - cp<python_version>-<abi>-<platform>
    - cp<python_version>-abi3-<platform>
    - cp<python_version>-none-<platform>
    - cp<less than python_version>-abi3-<platform>  # Older Python versions down to 3.2.

    If python_version only specifies a major version then user-provided ABIs and
    the 'none' ABItag will be used.

    If 'abi3' or 'none' are specified in 'abis' then they will be yielded at
    their normal position and not at the beginning.
    """
    pass
# WARNING: Decompyle incomplete


def _generic_abi():
    '''
    Return the ABI tag based on EXT_SUFFIX.
    '''
    ext_suffix = _get_config_var('EXT_SUFFIX', warn = True)
    if isinstance(ext_suffix, str) or ext_suffix[0] != '.':
        raise SystemError("invalid sysconfig.get_config_var('EXT_SUFFIX')")
    parts = ext_suffix.split('.')
    if len(parts) < 3:
        return _cpython_abis(sys.version_info[:2])
    soabi = None[1]
    if soabi.startswith('cpython'):
        abi = 'cp' + soabi.split('-')[1]
    elif soabi.startswith('cp'):
        abi = soabi.split('-')[0]
    elif soabi.startswith('pypy'):
        abi = '-'.join(soabi.split('-')[:2])
    elif soabi.startswith('graalpy'):
        abi = '-'.join(soabi.split('-')[:3])
    elif soabi:
        abi = soabi
    else:
        return []
    return [
        None(abi)]


def generic_tags(interpreter = None, abis = None, platforms = None, *, warn):
    '''
    Yields the tags for a generic interpreter.

    The tags consist of:
    - <interpreter>-<abi>-<platform>

    The "none" ABI will be added if it was not explicitly provided.
    '''
    pass
# WARNING: Decompyle incomplete


def _py_interpreter_range(py_version = None):
    '''
    Yields Python versions in descending order.

    After the latest version, the major-only version will be yielded, and then
    all previous versions of that major version.
    '''
    pass
# WARNING: Decompyle incomplete


def compatible_tags(python_version = None, interpreter = None, platforms = None):
    '''
    Yields the sequence of tags that are compatible with a specific version of Python.

    The tags consist of:
    - py*-none-<platform>
    - <interpreter>-none-any  # ... if `interpreter` is provided.
    - py*-none-any
    '''
    pass
# WARNING: Decompyle incomplete


def _mac_arch(arch = None, is_32bit = None):
    if not is_32bit:
        return arch
    if None.startswith('ppc'):
        return 'ppc'
    return 'i386'


def _mac_binary_formats(version = None, cpu_arch = None):
    formats = [
        cpu_arch]
    if cpu_arch == 'x86_64':
        if version < (10, 4):
            return []
        None.extend([
            'intel',
            'fat64',
            'fat32'])
    elif cpu_arch == 'i386':
        if version < (10, 4):
            return []
        None.extend([
            'intel',
            'fat32',
            'fat'])
    elif cpu_arch == 'ppc64':
        if version > (10, 5) or version < (10, 4):
            return []
        None.append('fat64')
    elif cpu_arch == 'ppc':
        if version > (10, 6):
            return []
        None.extend([
            'fat32',
            'fat'])
    if cpu_arch in frozenset({'arm64', 'x86_64'}):
        formats.append('universal2')
    if cpu_arch in frozenset({'ppc', 'i386', 'intel', 'ppc64', 'x86_64'}):
        formats.append('universal')
    return formats


def mac_platforms(version = None, arch = None):
    '''
    Yields the platform tags for a macOS system.

    The `version` parameter is a two-item tuple specifying the macOS version to
    generate platform tags for. The `arch` parameter is the CPU architecture to
    generate platform tags for. Both parameters default to the appropriate value
    for the current system.
    '''
    pass
# WARNING: Decompyle incomplete


def ios_platforms(version = None, multiarch = None):
    '''
    Yields the platform tags for an iOS system.

    :param version: A two-item tuple specifying the iOS version to generate
        platform tags for. Defaults to the current iOS version.
    :param multiarch: The CPU architecture+ABI to generate platform tags for -
        (the value used by `sys.implementation._multiarch` e.g.,
        `arm64_iphoneos` or `x84_64_iphonesimulator`). Defaults to the current
        multiarch value.
    '''
    pass
# WARNING: Decompyle incomplete


def android_platforms(api_level = None, abi = None):
    """
    Yields the :attr:`~Tag.platform` tags for Android. If this function is invoked on
    non-Android platforms, the ``api_level`` and ``abi`` arguments are required.

    :param int api_level: The maximum `API level
        <https://developer.android.com/tools/releases/platforms>`__ to return. Defaults
        to the current system's version, as returned by ``platform.android_ver``.
    :param str abi: The `Android ABI <https://developer.android.com/ndk/guides/abis>`__,
        e.g. ``arm64_v8a``. Defaults to the current system's ABI , as returned by
        ``sysconfig.get_platform``. Hyphens and periods will be replaced with
        underscores.
    """
    pass
# WARNING: Decompyle incomplete


def _linux_platforms(is_32bit = None):
    pass
# WARNING: Decompyle incomplete


def _generic_platforms():
    pass
# WARNING: Decompyle incomplete


def platform_tags():
    '''
    Provides the platform tags for this installation.
    '''
    if platform.system() == 'Darwin':
        return mac_platforms()
    if None.system() == 'iOS':
        return ios_platforms()
    if None.system() == 'Android':
        return android_platforms()
    if None.system() == 'Linux':
        return _linux_platforms()
    return None()


def interpreter_name():
    '''
    Returns the name of the running interpreter.

    Some implementations have a reserved, two-letter abbreviation which will
    be returned when appropriate.
    '''
    name = sys.implementation.name
    if not INTERPRETER_SHORT_NAMES.get(name):
        INTERPRETER_SHORT_NAMES.get(name)
    return name


def interpreter_version(*, warn):
    '''
    Returns the version of the running interpreter.
    '''
    version = _get_config_var('py_version_nodot', warn = warn)
    if version:
        return str(version)
    return None(sys.version_info[:2])


def _version_nodot(version = None):
    return ''.join(map(str, version))


def sys_tags(*, warn):
    '''
    Returns the sequence of tag triples for the running interpreter.

    The order of the sequence corresponds to priority order for the
    interpreter, from most to least important.
    '''
    pass
# WARNING: Decompyle incomplete

