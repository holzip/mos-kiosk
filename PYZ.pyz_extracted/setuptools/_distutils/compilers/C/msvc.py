# Source Generated with Decompyle++
# File: msvc.pyc (Python 3.12)

'''distutils._msvccompiler

Contains MSVCCompiler, an implementation of the abstract CCompiler class
for Microsoft Visual Studio 2015.

This module requires VS 2015 or later.
'''
from __future__ import annotations
import contextlib
import os
import subprocess
from unittest.mock import mock
import warnings
from collections.abc import Iterable
contextlib.suppress(ImportError)
import winreg
None(None, None)
from itertools import count
from _log import log
from errors import DistutilsExecError, DistutilsPlatformError
from util import get_host_platform, get_platform
from  import base
from base import gen_lib_options
from errors import CompileError, LibError, LinkError

def _find_vc2015():
    
    try:
        key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\VisualStudio\\SxS\\VC7', access = winreg.KEY_READ | winreg.KEY_WOW64_32KEY)
        best_version = 0
        best_dir = None
        key
        for i in count():
            (v, vc_dir, vt) = winreg.EnumValue(key, i)
            if not v:
                continue
            if not vt == winreg.REG_SZ:
                continue
            if not os.path.isdir(vc_dir):
                continue
            version = int(float(v))
            if not version >= 14:
                continue
            if not version > best_version:
                continue
            best_dir = vc_dir
            best_version = version
        None(None, None)
        return (best_version, best_dir)
    except OSError:
        log.debug('Visual C++ is not registered')
        return (None, None)
        except OSError:
            continue
        except (ValueError, TypeError):
            continue
        with None:
            if not None:
                pass
        return (best_version, best_dir)



def _find_vc2017():
    '''Returns "15, path" based on the result of invoking vswhere.exe
    If no install is found, returns "None, None"

    The version is returned to avoid unnecessarily changing the function
    result. It may be ignored when the path is not None.

    If vswhere.exe is not available, by definition, VS 2017 is not
    installed.
    '''
    if not os.environ.get('ProgramFiles(x86)'):
        os.environ.get('ProgramFiles(x86)')
    root = os.environ.get('ProgramFiles')
    if not root:
        return (None, None)
    variant = 'arm64' if get_platform() == 'win-arm64' else 'x86.x64'
    suitable_components = (f'''Microsoft.VisualStudio.Component.VC.Tools.{variant}''', 'Microsoft.VisualStudio.Workload.WDExpress')
    for component in suitable_components:
        contextlib.suppress(subprocess.CalledProcessError, OSError, UnicodeDecodeError)
        path = subprocess.check_output([
            os.path.join(root, 'Microsoft Visual Studio', 'Installer', 'vswhere.exe'),
            '-latest',
            '-prerelease',
            '-requires',
            component,
            '-property',
            'installationPath',
            '-products',
            '*']).decode(encoding = 'mbcs', errors = 'strict').strip()
        path = os.path.join(path, 'VC', 'Auxiliary', 'Build')
        if os.path.isdir(path):
            None(None, None)
            
            return suitable_components, (15, path), 
        None(None, None)
    return (None, None)
    with None:
        if not None:
            pass
    continue

PLAT_SPEC_TO_RUNTIME = {
    'x86': 'x86',
    'x86_amd64': 'x64',
    'x86_arm': 'arm',
    'x86_arm64': 'arm64' }

def _find_vcvarsall(plat_spec):
    (_, best_dir) = _find_vc2017()
    if not best_dir:
        (best_version, best_dir) = _find_vc2015()
    if not best_dir:
        log.debug('No suitable Visual C++ version found')
        return (None, None)
    vcvarsall = os.path.join(best_dir, 'vcvarsall.bat')
    if not os.path.isfile(vcvarsall):
        log.debug('%s cannot be found', vcvarsall)
        return (None, None)
    return (vcvarsall, None)


def _get_vc_env(plat_spec):
    pass
# WARNING: Decompyle incomplete


def _find_exe(exe, paths = (None,)):
    """Return path to an MSVC executable program.

    Tries to find the program in several places: first, one of the
    MSVC program search paths from the registry; next, the directories
    in the PATH environment variable.  If any of those work, return an
    absolute path that is known to exist.  If none of them work, just
    return the original program name, 'exe'.
    """
    if not paths:
        paths = os.getenv('path').split(os.pathsep)
    for p in paths:
        fn = os.path.join(os.path.abspath(p), exe)
        if not os.path.isfile(fn):
            continue
        
        return paths, fn
    return exe

_vcvars_names = {
    'win32': 'x86',
    'win-amd64': 'amd64',
    'win-arm32': 'arm',
    'win-arm64': 'arm64' }

def _get_vcvars_spec(host_platform, platform):
    """
    Given a host platform and platform, determine the spec for vcvarsall.

    Uses the native MSVC host if the host platform would need expensive
    emulation for x86.

    >>> _get_vcvars_spec('win-arm64', 'win32')
    'arm64_x86'
    >>> _get_vcvars_spec('win-arm64', 'win-amd64')
    'arm64_amd64'

    Otherwise, always cross-compile from x86 to work with the
    lighter-weight MSVC installs that do not include native 64-bit tools.

    >>> _get_vcvars_spec('win32', 'win32')
    'x86'
    >>> _get_vcvars_spec('win-arm32', 'win-arm32')
    'x86_arm'
    >>> _get_vcvars_spec('win-amd64', 'win-arm64')
    'x86_arm64'
    """
    if host_platform != 'win-arm64':
        host_platform = 'win32'
    vc_hp = _vcvars_names[host_platform]
    vc_plat = _vcvars_names[platform]
    if vc_hp == vc_plat:
        return vc_hp
    return f'''{None}_{vc_plat}'''


class Compiler(base.Compiler):
    pass
# WARNING: Decompyle incomplete

return None
with None:
    if not None:
        pass
continue
