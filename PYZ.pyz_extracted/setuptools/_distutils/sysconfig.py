# Source Generated with Decompyle++
# File: sysconfig.pyc (Python 3.12)

"""Provide access to Python's configuration information.  The specific
configuration variables available depend heavily on the platform and
configuration.  The values may be retrieved using
get_config_var(name), and the list of variables is available via
get_config_vars().keys().  Additional convenience functions are also
available.

Written by:   Fred L. Drake, Jr.
Email:        <fdrake@acm.org>
"""
from __future__ import annotations
import functools
import os
import pathlib
import re
import sys
import sysconfig
from typing import TYPE_CHECKING, Literal, overload
from jaraco.functools import pass_none
from ccompiler import CCompiler
from compat import py39
from errors import DistutilsPlatformError
from util import is_mingw
if TYPE_CHECKING:
    from typing_extensions import deprecated
else:
    
    def deprecated(message):
        return (lambda fn: fn)

IS_PYPY = '__pypy__' in sys.builtin_module_names
PREFIX = os.path.normpath(sys.prefix)
EXEC_PREFIX = os.path.normpath(sys.exec_prefix)
BASE_PREFIX = os.path.normpath(sys.base_prefix)
BASE_EXEC_PREFIX = os.path.normpath(sys.base_exec_prefix)
if '_PYTHON_PROJECT_BASE' in os.environ:
    project_base = os.path.abspath(os.environ['_PYTHON_PROJECT_BASE'])
elif sys.executable:
    project_base = os.path.dirname(os.path.abspath(sys.executable))
else:
    project_base = os.getcwd()

def _is_python_source_dir(d):
    '''
    Return True if the target directory appears to point to an
    un-installed Python.
    '''
    pass
# WARNING: Decompyle incomplete

_sys_home = getattr(sys, '_home', None)

def _is_parent(dir_a, dir_b):
    '''
    Return True if a is a parent of b.
    '''
    return os.path.normcase(dir_a).startswith(os.path.normcase(dir_b))

if os.name == 'nt':
    _fix_pcbuild = (lambda d: pass# WARNING: Decompyle incomplete
)()
    project_base = _fix_pcbuild(project_base)
    _sys_home = _fix_pcbuild(_sys_home)

def _python_build():
    if _sys_home:
        return _is_python_source_dir(_sys_home)
    return None(project_base)

python_build = _python_build()
build_flags = ''

try:
    if not python_build:
        build_flags = sys.abiflags
    
    def get_python_version():
        """Return a string containing the major and minor Python version,
    leaving off the patchlevel.  Sample return values could be '1.5'
    or '2.2'.
    """
        return f'''{sys.version_info.major}.{sys.version_info.minor}'''

    
    def get_python_inc(plat_specific = None, prefix = None):
        """Return the directory containing installed Python header files.

    If 'plat_specific' is false (the default), this is the path to the
    non-platform-specific header files, i.e. Python.h and so on;
    otherwise, this is the path to platform-specific header files
    (namely pyconfig.h).

    If 'prefix' is supplied, use it instead of sys.base_prefix or
    sys.base_exec_prefix -- i.e., ignore 'plat_specific'.
    """
        default_prefix = BASE_EXEC_PREFIX if plat_specific else BASE_PREFIX
    # WARNING: Decompyle incomplete

    _extant = (lambda path: if os.path.exists(path):
path)()
    
    def _get_python_inc_posix(prefix, spec_prefix, plat_specific):
        if IS_PYPY and sys.version_info < (3, 8):
            return os.path.join(prefix, 'include')
        if not None(plat_specific):
            None(plat_specific)
            if not _extant(_get_python_inc_from_config(plat_specific, spec_prefix)):
                _extant(_get_python_inc_from_config(plat_specific, spec_prefix))
        return _get_python_inc_posix_prefix(prefix)

    
    def _get_python_inc_posix_python(plat_specific):
        '''
    Assume the executable is in the build directory. The
    pyconfig.h file should be in the same directory. Since
    the build directory may not be the source directory,
    use "srcdir" from the makefile to find the "Include"
    directory.
    '''
        if not python_build:
            return None
        if plat_specific:
            if not _sys_home:
                _sys_home
            return project_base
        incdir = None.path.join(get_config_var('srcdir'), 'Include')
        return os.path.normpath(incdir)

    
    def _get_python_inc_from_config(plat_specific, spec_prefix):
        """
    If no prefix was explicitly specified, provide the include
    directory from the config vars. Useful when
    cross-compiling, since the config vars may come from
    the host
    platform Python installation, while the current Python
    executable is from the build platform installation.

    >>> monkeypatch = getfixture('monkeypatch')
    >>> gpifc = _get_python_inc_from_config
    >>> monkeypatch.setitem(gpifc.__globals__, 'get_config_var', str.lower)
    >>> gpifc(False, '/usr/bin/')
    >>> gpifc(False, '')
    >>> gpifc(False, None)
    'includepy'
    >>> gpifc(True, None)
    'confincludepy'
    """
        pass
    # WARNING: Decompyle incomplete

    
    def _get_python_inc_posix_prefix(prefix):
        implementation = 'pypy' if IS_PYPY else 'python'
        python_dir = implementation + get_python_version() + build_flags
        return os.path.join(prefix, 'include', python_dir)

    
    def _get_python_inc_nt(prefix, spec_prefix, plat_specific):
        if python_build:
            return os.path.join(prefix, 'include') + os.path.pathsep + os.path.dirname(sysconfig.get_config_h_filename())
        return None.path.join(prefix, 'include')

    
    def _posix_lib(standard_lib, libpython, early_prefix, prefix):
        if standard_lib:
            return libpython
        return None.path.join(libpython, 'site-packages')

    
    def get_python_lib(plat_specific = None, standard_lib = None, prefix = pass_none):
        """Return the directory containing the Python library (standard or
    site additions).

    If 'plat_specific' is true, return the directory containing
    platform-specific modules, i.e. any module from a non-pure-Python
    module distribution; otherwise, return the platform-shared library
    directory.  If 'standard_lib' is true, return the directory
    containing standard Python library modules; otherwise, return the
    directory for site-specific modules.

    If 'prefix' is supplied, use it instead of sys.base_prefix or
    sys.base_exec_prefix -- i.e., ignore 'plat_specific'.
    """
        pass
    # WARNING: Decompyle incomplete

    _customize_macos = (lambda : if sys.platform == 'darwin':
sys.platform == 'darwin'__import__('_osx_support').customize_compiler(get_config_vars())None)()
    
    def customize_compiler(compiler = None):
        """Do any platform-specific customization of a CCompiler instance.

    Mainly needed on Unix, so we can plug in the information that
    varies across Unices and is stored in Python's Makefile.
    """
        if compiler.compiler_type in ('unix', 'cygwin') or compiler.compiler_type == 'mingw32':
            if is_mingw():
                _customize_macos()
                (cc, cxx, cflags, ccshared, ldshared, ldcxxshared, shlib_suffix, ar, ar_flags) = get_config_vars('CC', 'CXX', 'CFLAGS', 'CCSHARED', 'LDSHARED', 'LDCXXSHARED', 'SHLIB_SUFFIX', 'AR', 'ARFLAGS')
                cxxflags = cflags
                if 'CC' in os.environ:
                    newcc = os.environ['CC']
                    if 'LDSHARED' not in os.environ and ldshared.startswith(cc):
                        ldshared = newcc + ldshared[len(cc):]
                    cc = newcc
                cxx = os.environ.get('CXX', cxx)
                ldshared = os.environ.get('LDSHARED', ldshared)
                ldcxxshared = os.environ.get('LDCXXSHARED', ldcxxshared)
                cpp = os.environ.get('CPP', cc + ' -E')
                ldshared = _add_flags(ldshared, 'LD')
                ldcxxshared = _add_flags(ldcxxshared, 'LD')
                cflags = os.environ.get('CFLAGS', cflags)
                ldshared = _add_flags(ldshared, 'C')
                cxxflags = os.environ.get('CXXFLAGS', cxxflags)
                ldcxxshared = _add_flags(ldcxxshared, 'CXX')
                cpp = _add_flags(cpp, 'CPP')
                cflags = _add_flags(cflags, 'CPP')
                cxxflags = _add_flags(cxxflags, 'CPP')
                ldshared = _add_flags(ldshared, 'CPP')
                ldcxxshared = _add_flags(ldcxxshared, 'CPP')
                ar = os.environ.get('AR', ar)
                archiver = ar + ' ' + os.environ.get('ARFLAGS', ar_flags)
                cc_cmd = cc + ' ' + cflags
                cxx_cmd = cxx + ' ' + cxxflags
                compiler.set_executables(preprocessor = cpp, compiler = cc_cmd, compiler_so = cc_cmd + ' ' + ccshared, compiler_cxx = cxx_cmd, compiler_so_cxx = cxx_cmd + ' ' + ccshared, linker_so = ldshared, linker_so_cxx = ldcxxshared, linker_exe = cc, linker_exe_cxx = cxx, archiver = archiver)
                if 'RANLIB' in os.environ and compiler.executables.get('ranlib', None):
                    compiler.set_executables(ranlib = os.environ['RANLIB'])
                compiler.shared_lib_extension = shlib_suffix
                return None
            return None

    
    def get_config_h_filename():
        '''Return full pathname of installed pyconfig.h file.'''
        return sysconfig.get_config_h_filename()

    
    def get_makefile_filename():
        '''Return full pathname of installed Makefile from the Python build.'''
        return sysconfig.get_makefile_filename()

    
    def parse_config_h(fp, g = (None,)):
        '''Parse a config.h-style file.

    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    '''
        return sysconfig.parse_config_h(fp, vars = g)

    _variable_rx = re.compile('([a-zA-Z][a-zA-Z0-9_]+)\\s*=\\s*(.*)')
    _findvar1_rx = re.compile('\\$\\(([A-Za-z][A-Za-z0-9_]*)\\)')
    _findvar2_rx = re.compile('\\${([A-Za-z][A-Za-z0-9_]*)}')
    
    def parse_makefile(fn, g = (None,)):
        '''Parse a Makefile-style file.

    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    '''
        TextFile = TextFile
        import distutils.text_file
        fp = TextFile(fn, strip_comments = True, skip_blanks = True, join_lines = True, errors = 'surrogateescape')
    # WARNING: Decompyle incomplete

    
    def expand_makefile_vars(s, vars):
        '''Expand Makefile-style variables -- "${foo}" or "$(foo)" -- in
    \'string\' according to \'vars\' (a dictionary mapping variable names to
    values).  Variables not present in \'vars\' are silently expanded to the
    empty string.  The variable values in \'vars\' should not contain further
    variable expansions; if \'vars\' is the output of \'parse_makefile()\',
    you\'re fine.  Returns a variable-expanded version of \'s\'.
    '''
        if not _findvar1_rx.search(s):
            _findvar1_rx.search(s)
        m = _findvar2_rx.search(s)
        if m:
            (beg, end) = m.span()
            s = s[0:beg] + vars.get(m.group(1)) + s[end:]
        else:
            return s

    _config_vars = None
    get_config_vars = (lambda : pass)()
    get_config_vars = (lambda arg = None: pass)()
    
    def get_config_vars(*args):
        """With no arguments, return a dictionary of all configuration
    variables relevant for the current platform.  Generally this includes
    everything needed to build extensions and install both pure modules and
    extensions.  On Unix, this means every variable defined in Python's
    installed Makefile; on Windows it's a much smaller set.

    With arguments, return a list of values that result from looking up
    each argument in the configuration variable dictionary.
    """
        pass
    # WARNING: Decompyle incomplete

    get_config_var = (lambda name = None: pass)()()
    get_config_var = (lambda name = None: pass)()
    
    def get_config_var(name = None):
        """Return the value of a single variable using the dictionary
    returned by 'get_config_vars()'.  Equivalent to
    get_config_vars().get(name)
    """
        if name == 'SO':
            import warnings
            warnings.warn('SO is deprecated, use EXT_SUFFIX', DeprecationWarning, 2)
        return get_config_vars().get(name)

    _add_flags = (lambda value = None, type = None: flags = os.environ.get(f'''{type}FLAGS''')if flags:
f'''{value} {flags}''')()
    return None
except AttributeError:
    continue

