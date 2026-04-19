# Source Generated with Decompyle++
# File: _manylinux.pyc (Python 3.12)

from __future__ import annotations
import collections
import contextlib
import functools
import os
import re
import sys
import warnings
from typing import Generator, Iterator, NamedTuple, Sequence
from _elffile import EIClass, EIData, ELFFile, EMachine
EF_ARM_ABIMASK = 0xFF000000
EF_ARM_ABI_VER5 = 83886080
EF_ARM_ABI_FLOAT_HARD = 1024
_ALLOWED_ARCHS = {
    'ppc64',
    's390x',
    'x86_64',
    'aarch64',
    'ppc64le',
    'riscv64',
    'loongarch64'}
_parse_elf = (lambda path = None: pass# WARNING: Decompyle incomplete
)()

def _is_linux_armhf(executable = None):
    f = _parse_elf(executable)
    if f is not None:
        f is not None
        if f.capacity == EIClass.C32:
            f.capacity == EIClass.C32
            if f.encoding == EIData.Lsb:
                f.encoding == EIData.Lsb
                if f.machine == EMachine.Arm:
                    f.machine == EMachine.Arm
                    if f.flags & EF_ARM_ABIMASK == EF_ARM_ABI_VER5:
                        f.flags & EF_ARM_ABIMASK == EF_ARM_ABI_VER5
    None(None, None)
    return 
    with None:
        if not None, f.flags & EF_ARM_ABI_FLOAT_HARD == EF_ARM_ABI_FLOAT_HARD:
            pass


def _is_linux_i686(executable = None):
    f = _parse_elf(executable)
    if f is not None:
        f is not None
        if f.capacity == EIClass.C32:
            f.capacity == EIClass.C32
            if f.encoding == EIData.Lsb:
                f.encoding == EIData.Lsb
    None(None, None)
    return 
    with None:
        if not None, f.machine == EMachine.I386:
            pass


def _have_compatible_abi(executable = None, archs = None):
    if 'armv7l' in archs:
        return _is_linux_armhf(executable)
    if None in archs:
        return _is_linux_i686(executable)
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(archs())

_LAST_GLIBC_MINOR: 'dict[int, int]' = collections.defaultdict((lambda : 50))

class _GLibCVersion(NamedTuple):
    minor: 'int' = '_GLibCVersion'


def _glibc_version_string_confstr():
    '''
    Primary implementation of glibc_version_string using os.confstr.
    '''
    pass
# WARNING: Decompyle incomplete


def _glibc_version_string_ctypes():
    '''
    Fallback implementation of glibc_version_string using ctypes.
    '''
    
    try:
        import ctypes
        
        try:
            process_namespace = ctypes.CDLL(None)
            
            try:
                gnu_get_libc_version = process_namespace.gnu_get_libc_version
                gnu_get_libc_version.restype = ctypes.c_char_p
                version_str = gnu_get_libc_version()
                if not isinstance(version_str, str):
                    version_str = version_str.decode('ascii')
                return version_str
                except ImportError:
                    return None
                except OSError:
                    return None
            except AttributeError:
                return None





def _glibc_version_string():
    '''Returns glibc version string, or None if not using glibc.'''
    if not _glibc_version_string_confstr():
        _glibc_version_string_confstr()
    return _glibc_version_string_ctypes()


def _parse_glibc_version(version_str = None):
    '''Parse glibc version.

    We use a regexp instead of str.split because we want to discard any
    random junk that might come after the minor version -- this might happen
    in patched/forked versions of glibc (e.g. Linaro\'s version of glibc
    uses version strings like "2.20-2014.11"). See gh-3588.
    '''
    m = re.match('(?P<major>[0-9]+)\\.(?P<minor>[0-9]+)', version_str)
    if not m:
        warnings.warn(f'''Expected glibc version with 2 components major.minor, got: {version_str}''', RuntimeWarning, stacklevel = 2)
        return _GLibCVersion(-1, -1)
    return None(int(m.group('major')), int(m.group('minor')))

_get_glibc_version = (lambda : version_str = _glibc_version_string()# WARNING: Decompyle incomplete
)()

def _is_compatible(arch = None, version = None):
    sys_glibc = _get_glibc_version()
    if sys_glibc < version:
        return False
# WARNING: Decompyle incomplete

_LEGACY_MANYLINUX_MAP: 'dict[_GLibCVersion, str]' = {
    _GLibCVersion(2, 5): 'manylinux1',
    _GLibCVersion(2, 12): 'manylinux2010',
    _GLibCVersion(2, 17): 'manylinux2014' }

def platform_tags(archs = None):
    '''Generate manylinux tags compatible to the current platform.

    :param archs: Sequence of compatible architectures.
        The first one shall be the closest to the actual architecture and be the part of
        platform tag after the ``linux_`` prefix, e.g. ``x86_64``.
        The ``linux_`` prefix is assumed as a prerequisite for the current platform to
        be manylinux-compatible.

    :returns: An iterator of compatible manylinux tags.
    '''
    pass
# WARNING: Decompyle incomplete

