# Source Generated with Decompyle++
# File: util.pyc (Python 3.12)

"""distutils.util

Miscellaneous utility functions -- anything that doesn't fit into
one of the other *util.py modules.
"""
from __future__ import annotations
import functools
import importlib.util as importlib
import os
import pathlib
import re
import string
import subprocess
import sys
import sysconfig
import tempfile
from collections.abc import Callable, Iterable, Mapping
from typing import TYPE_CHECKING, AnyStr
from jaraco.functools import pass_none
from _log import log
from _modified import newer
from errors import DistutilsByteCompileError, DistutilsPlatformError
from spawn import spawn
if TYPE_CHECKING:
    from typing_extensions import TypeVarTuple, Unpack
    _Ts = TypeVarTuple('_Ts')

def get_host_platform():
    '''
    Return a string that identifies the current platform. Use this
    function to distinguish platform-specific build directories and
    platform-specific built distributions.
    '''
    return sysconfig.get_platform()


def get_platform():
    if os.name == 'nt':
        TARGET_TO_PLAT = {
            'x86': 'win32',
            'x64': 'win-amd64',
            'arm': 'win-arm32',
            'arm64': 'win-arm64' }
        target = os.environ.get('VSCMD_ARG_TGT_ARCH')
        if not TARGET_TO_PLAT.get(target):
            TARGET_TO_PLAT.get(target)
        return get_host_platform()
    return None()

if sys.platform == 'darwin':
    _syscfg_macosx_ver = None
MACOSX_VERSION_VAR = 'MACOSX_DEPLOYMENT_TARGET'

def _clear_cached_macosx_ver():
    '''For testing only. Do not call.'''
    global _syscfg_macosx_ver
    _syscfg_macosx_ver = None


def get_macosx_target_ver_from_syscfg():
    """Get the version of macOS latched in the Python interpreter configuration.
    Returns the version as a string or None if can't obtain one. Cached."""
    pass
# WARNING: Decompyle incomplete


def get_macosx_target_ver():
    '''Return the version of macOS for which we are building.

    The target version defaults to the version in sysconfig latched at time
    the Python interpreter was built, unless overridden by an environment
    variable. If neither source has a value, then None is returned'''
    syscfg_ver = get_macosx_target_ver_from_syscfg()
    env_ver = os.environ.get(MACOSX_VERSION_VAR)
    if env_ver:
        if syscfg_ver and split_version(syscfg_ver) >= [
            10,
            3] and split_version(env_ver) < [
            10,
            3]:
            my_msg = '$' + MACOSX_VERSION_VAR + f''' mismatch: now "{env_ver}" but "{syscfg_ver}" during configure; must use 10.3 or later'''
            raise DistutilsPlatformError(my_msg)
        return env_ver


def split_version(s = None):
    '''Convert a dot-separated string into a list of numbers for comparisons'''
    pass
# WARNING: Decompyle incomplete

convert_path = (lambda pathname = None: os.fspath(pathlib.PurePath(pathname)))()

def change_root(new_root = None, pathname = None):
    '''Return \'pathname\' with \'new_root\' prepended.  If \'pathname\' is
    relative, this is equivalent to "os.path.join(new_root,pathname)".
    Otherwise, it requires making \'pathname\' relative and then joining the
    two, which is tricky on DOS/Windows and Mac OS.
    '''
    if os.name == 'posix':
        if not os.path.isabs(pathname):
            return os.path.join(new_root, pathname)
        return None.path.join(new_root, pathname[1:])
    if None.name == 'nt':
        (drive, path) = os.path.splitdrive(pathname)
        if path[0] == os.sep:
            path = path[1:]
        return os.path.join(new_root, path)
    raise None(f'''nothing known about platform \'{os.name}\'''')

check_environ = (lambda : if os.name == 'posix' and 'HOME' not in os.environ:
try:
import pwdos.environ['HOME'] = pwd.getpwuid(os.getuid())[5]if 'PLAT' not in os.environ:
os.environ['PLAT'] = get_platform()NoneNoneexcept (ImportError, KeyError):
continue)()

def subst_vars(s = None, local_vars = None):
    '''
    Perform variable substitution on \'string\'.
    Variables are indicated by format-style braces ("{var}").
    Variable is substituted by the value found in the \'local_vars\'
    dictionary or in \'os.environ\' if it\'s not in \'local_vars\'.
    \'os.environ\' is first checked/augmented to guarantee that it contains
    certain values: see \'check_environ()\'.  Raise ValueError for any
    variables not found in either \'local_vars\' or \'os.environ\'.
    '''
    check_environ()
    lookup = dict(os.environ)
    (lambda .0: pass# WARNING: Decompyle incomplete
)(local_vars.items()())
    
    try:
        return _subst_compat(s).format_map(lookup)
    except KeyError:
        var = None
        raise ValueError(f'''invalid variable {var}''')
        var = None
        del var



def _subst_compat(s):
    '''
    Replace shell/Perl-style variable substitution with
    format-style. For compatibility.
    '''
    
    def _subst(match):
        return f'''{{{match.group(1)}}}'''

    repl = re.sub('\\$([a-zA-Z_][a-zA-Z_0-9]*)', _subst, s)
    if repl != s:
        import warnings
        warnings.warn('shell/Perl-style substitutions are deprecated', DeprecationWarning)
    return repl


def grok_environment_error(exc = None, prefix = None):
    return prefix + str(exc)

_wordchars_re = None
_squote_re = None
_dquote_re = None

def _init_regex():
    global _wordchars_re, _squote_re, _dquote_re
    _wordchars_re = re.compile(f'''[^\\\\\\\'\\"{string.whitespace} ]*''')
    _squote_re = re.compile("'(?:[^'\\\\]|\\\\.)*'")
    _dquote_re = re.compile('"(?:[^"\\\\]|\\\\.)*"')


def split_quoted(s = None):
    '''Split a string up according to Unix shell-like rules for quotes and
    backslashes.  In short: words are delimited by spaces, as long as those
    spaces are not escaped by a backslash, or inside a quoted string.
    Single and double quotes are equivalent, and the quote characters can
    be backslash-escaped.  The backslash is stripped from any two-character
    escape sequence, leaving only the escaped character.  The quote
    characters are stripped from any quoted string.  Returns a list of
    words.
    '''
    pass
# WARNING: Decompyle incomplete


def execute(func = None, args = None, msg = None, verbose = (None, False, False), dry_run = ('func', 'Callable[[Unpack[_Ts]], object]', 'args', 'tuple[Unpack[_Ts]]', 'msg', 'object', 'verbose', 'bool', 'dry_run', 'bool', 'return', 'None')):
    '''
    Perform some action that affects the outside world (e.g. by
    writing to the filesystem). Such actions are special because they
    are disabled by the \'dry_run\' flag. This method handles that
    complication; simply supply the
    function to call and an argument tuple for it (to embody the
    "external action" being performed) and an optional message to
    emit.
    '''
    pass
# WARNING: Decompyle incomplete


def strtobool(val = None):
    """Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    if val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    raise ValueError(f'''invalid truth value {val!r}''')


def byte_compile(py_files, optimize, force, prefix = None, base_dir = None, verbose = None, dry_run = (0, False, None, None, True, False, None), direct = ('py_files', 'Iterable[str]', 'optimize', 'int', 'force', 'bool', 'prefix', 'str | None', 'base_dir', 'str | None', 'verbose', 'bool', 'dry_run', 'bool', 'direct', 'bool | None', 'return', 'None')):
    '''Byte-compile a collection of Python source files to .pyc
    files in a __pycache__ subdirectory.  \'py_files\' is a list
    of files to compile; any files that don\'t end in ".py" are silently
    skipped.  \'optimize\' must be one of the following:
      0 - don\'t optimize
      1 - normal optimization (like "python -O")
      2 - extra optimization (like "python -OO")
    If \'force\' is true, all files are recompiled regardless of
    timestamps.

    The source filename encoded in each bytecode file defaults to the
    filenames listed in \'py_files\'; you can modify these with \'prefix\' and
    \'basedir\'.  \'prefix\' is a string that will be stripped off of each
    source filename, and \'base_dir\' is a directory name that will be
    prepended (after \'prefix\' is stripped).  You can supply either or both
    (or neither) of \'prefix\' and \'base_dir\', as you wish.

    If \'dry_run\' is true, doesn\'t actually do anything that would
    affect the filesystem.

    Byte-compilation is either done directly in this interpreter process
    with the standard py_compile module, or indirectly by writing a
    temporary script and executing it.  Normally, you should let
    \'byte_compile()\' figure out to use direct compilation or not (see
    the source for details).  The \'direct\' flag is used by the script
    generated in indirect mode; unless you know what you\'re doing, leave
    it set to None.
    '''
    if sys.dont_write_bytecode:
        raise DistutilsByteCompileError('byte-compiling is disabled.')
# WARNING: Decompyle incomplete


def rfc822_escape(header = None):
    '''Return a version of the string escaped for inclusion in an
    RFC-822 header, by ensuring there are 8 spaces space after each newline.
    '''
    indent = '        '
    lines = header.splitlines(keepends = True)
    if lines:
        lines
    ends_in_newline = lines[-1].splitlines()[0] != lines[-1]
    suffix = indent if ends_in_newline else ''
    return indent.join(lines) + suffix


def is_mingw():
    """Returns True if the current platform is mingw.

    Python compiled with Mingw-w64 has sys.platform == 'win32' and
    get_platform() starts with 'mingw'.
    """
    if sys.platform == 'win32':
        sys.platform == 'win32'
    return get_platform().startswith('mingw')


def is_freethreaded():
    '''Return True if the Python interpreter is built with free threading support.'''
    return bool(sysconfig.get_config_var('Py_GIL_DISABLED'))

