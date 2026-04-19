# Source Generated with Decompyle++
# File: sysconfig.pyc (Python 3.12)

"""Access to Python's configuration information."""
import os
import sys
import threading
from os.path import realpath
__all__ = [
    'get_config_h_filename',
    'get_config_var',
    'get_config_vars',
    'get_makefile_filename',
    'get_path',
    'get_path_names',
    'get_paths',
    'get_platform',
    'get_python_version',
    'get_scheme_names',
    'parse_config_h']
_ALWAYS_STR = {
    'MACOSX_DEPLOYMENT_TARGET'}
_INSTALL_SCHEMES = {
    'posix_prefix': {
        'stdlib': '{installed_base}/{platlibdir}/python{py_version_short}',
        'platstdlib': '{platbase}/{platlibdir}/python{py_version_short}',
        'purelib': '{base}/lib/python{py_version_short}/site-packages',
        'platlib': '{platbase}/{platlibdir}/python{py_version_short}/site-packages',
        'include': '{installed_base}/include/python{py_version_short}{abiflags}',
        'platinclude': '{installed_platbase}/include/python{py_version_short}{abiflags}',
        'scripts': '{base}/bin',
        'data': '{base}' },
    'posix_home': {
        'stdlib': '{installed_base}/lib/python',
        'platstdlib': '{base}/lib/python',
        'purelib': '{base}/lib/python',
        'platlib': '{base}/lib/python',
        'include': '{installed_base}/include/python',
        'platinclude': '{installed_base}/include/python',
        'scripts': '{base}/bin',
        'data': '{base}' },
    'nt': {
        'stdlib': '{installed_base}/Lib',
        'platstdlib': '{base}/Lib',
        'purelib': '{base}/Lib/site-packages',
        'platlib': '{base}/Lib/site-packages',
        'include': '{installed_base}/Include',
        'platinclude': '{installed_base}/Include',
        'scripts': '{base}/Scripts',
        'data': '{base}' },
    'posix_venv': {
        'stdlib': '{installed_base}/{platlibdir}/python{py_version_short}',
        'platstdlib': '{platbase}/{platlibdir}/python{py_version_short}',
        'purelib': '{base}/lib/python{py_version_short}/site-packages',
        'platlib': '{platbase}/{platlibdir}/python{py_version_short}/site-packages',
        'include': '{installed_base}/include/python{py_version_short}{abiflags}',
        'platinclude': '{installed_platbase}/include/python{py_version_short}{abiflags}',
        'scripts': '{base}/bin',
        'data': '{base}' },
    'nt_venv': {
        'stdlib': '{installed_base}/Lib',
        'platstdlib': '{base}/Lib',
        'purelib': '{base}/Lib/site-packages',
        'platlib': '{base}/Lib/site-packages',
        'include': '{installed_base}/Include',
        'platinclude': '{installed_base}/Include',
        'scripts': '{base}/Scripts',
        'data': '{base}' } }
if os.name == 'nt':
    _INSTALL_SCHEMES['venv'] = _INSTALL_SCHEMES['nt_venv']
else:
    _INSTALL_SCHEMES['venv'] = _INSTALL_SCHEMES['posix_venv']

def _getuserbase():
    env_base = os.environ.get('PYTHONUSERBASE', None)
    if env_base:
        return env_base
    if None.platform in frozenset({'wasi', 'vxworks', 'emscripten'}):
        return None
    
    def joinuser(*args):
        pass
    # WARNING: Decompyle incomplete

    if os.name == 'nt':
        if not os.environ.get('APPDATA'):
            os.environ.get('APPDATA')
        base = '~'
        return joinuser(base, 'Python')
    if None.platform == 'darwin' and sys._framework:
        return joinuser('~', 'Library', sys._framework, f'''{sys.version_info[0]}.{sys.version_info[1]}''')
    return joinuser('~', '.local')

_HAS_USER_BASE = _getuserbase() is not None
if _HAS_USER_BASE:
    _INSTALL_SCHEMES |= {
        'nt_user': {
            'stdlib': '{userbase}/Python{py_version_nodot_plat}',
            'platstdlib': '{userbase}/Python{py_version_nodot_plat}',
            'purelib': '{userbase}/Python{py_version_nodot_plat}/site-packages',
            'platlib': '{userbase}/Python{py_version_nodot_plat}/site-packages',
            'include': '{userbase}/Python{py_version_nodot_plat}/Include',
            'scripts': '{userbase}/Python{py_version_nodot_plat}/Scripts',
            'data': '{userbase}' },
        'posix_user': {
            'stdlib': '{userbase}/{platlibdir}/python{py_version_short}',
            'platstdlib': '{userbase}/{platlibdir}/python{py_version_short}',
            'purelib': '{userbase}/lib/python{py_version_short}/site-packages',
            'platlib': '{userbase}/lib/python{py_version_short}/site-packages',
            'include': '{userbase}/include/python{py_version_short}',
            'scripts': '{userbase}/bin',
            'data': '{userbase}' },
        'osx_framework_user': {
            'stdlib': '{userbase}/lib/python',
            'platstdlib': '{userbase}/lib/python',
            'purelib': '{userbase}/lib/python/site-packages',
            'platlib': '{userbase}/lib/python/site-packages',
            'include': '{userbase}/include/python{py_version_short}',
            'scripts': '{userbase}/bin',
            'data': '{userbase}' } }
_SCHEME_KEYS = ('stdlib', 'platstdlib', 'purelib', 'platlib', 'include', 'scripts', 'data')
_PY_VERSION = sys.version.split()[0]
_PY_VERSION_SHORT = f'''{sys.version_info[0]}.{sys.version_info[1]}'''
_PY_VERSION_SHORT_NO_DOT = f'''{sys.version_info[0]}{sys.version_info[1]}'''
_BASE_PREFIX = os.path.normpath(sys.base_prefix)
_BASE_EXEC_PREFIX = os.path.normpath(sys.base_exec_prefix)
_CONFIG_VARS_LOCK = threading.RLock()
_CONFIG_VARS = None
_CONFIG_VARS_INITIALIZED = False
_USER_BASE = None
_variable_rx = '([a-zA-Z][a-zA-Z0-9_]+)\\s*=\\s*(.*)'
_findvar1_rx = '\\$\\(([A-Za-z][A-Za-z0-9_]*)\\)'
_findvar2_rx = '\\${([A-Za-z][A-Za-z0-9_]*)}'

def _safe_realpath(path):
    
    try:
        return realpath(path)
    except OSError:
        return 


if sys.executable:
    _PROJECT_BASE = os.path.dirname(_safe_realpath(sys.executable))
else:
    _PROJECT_BASE = _safe_realpath(os.getcwd())
_sys_home = getattr(sys, '_home', None)
if _sys_home:
    _PROJECT_BASE = _sys_home
if os.name == 'nt' and _safe_realpath(_PROJECT_BASE).startswith(_safe_realpath(f'''{_BASE_PREFIX}\\PCbuild''')):
    _PROJECT_BASE = _BASE_PREFIX
if '_PYTHON_PROJECT_BASE' in os.environ:
    _PROJECT_BASE = _safe_realpath(os.environ['_PYTHON_PROJECT_BASE'])

def is_python_build(check_home = (None,)):
    pass
# WARNING: Decompyle incomplete

_PYTHON_BUILD = is_python_build()
if _PYTHON_BUILD:
    for scheme in ('posix_prefix', 'posix_home'):
        scheme = _INSTALL_SCHEMES[scheme]
        scheme['headers'] = scheme['include']
        scheme['include'] = '{srcdir}/Include'
        scheme['platinclude'] = '{projectbase}/.'
    del scheme

def _subst_vars(s, local_vars):
    pass
# WARNING: Decompyle incomplete


def _extend_dict(target_dict, other_dict):
    target_keys = target_dict.keys()
    for key, value in other_dict.items():
        if key in target_keys:
            continue
        target_dict[key] = value


def _expand_vars(scheme, vars):
    res = { }
# WARNING: Decompyle incomplete


def _get_preferred_schemes():
    if os.name == 'nt':
        return {
            'prefix': 'nt',
            'home': 'posix_home',
            'user': 'nt_user' }
    if None.platform == 'darwin' and sys._framework:
        return {
            'prefix': 'posix_prefix',
            'home': 'posix_home',
            'user': 'osx_framework_user' }
    return {
        'prefix': None,
        'home': 'posix_home',
        'user': 'posix_user' }


def get_preferred_scheme(key):
    if key == 'prefix' and sys.prefix != sys.base_prefix:
        return 'venv'
    scheme = _get_preferred_schemes()[key]
    if scheme not in _INSTALL_SCHEMES:
        raise ValueError(f'''{key!r} returned {scheme!r}, which is not a valid scheme on this platform''')
    return scheme


def get_default_scheme():
    return get_preferred_scheme('prefix')


def _parse_makefile(filename, vars, keep_unresolved = (None, True)):
    '''Parse a Makefile-style file.

    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    '''
    import re
# WARNING: Decompyle incomplete


def get_makefile_filename():
    '''Return the path of the Makefile.'''
    if _PYTHON_BUILD:
        return os.path.join(_PROJECT_BASE, 'Makefile')
    if None(sys, 'abiflags'):
        config_dir_name = f'''config-{_PY_VERSION_SHORT}{sys.abiflags}'''
    else:
        config_dir_name = 'config'
    if hasattr(sys.implementation, '_multiarch'):
        config_dir_name += f'''-{sys.implementation._multiarch}'''
    return os.path.join(get_path('stdlib'), config_dir_name, 'Makefile')


def _get_sysconfigdata_name():
    multiarch = getattr(sys.implementation, '_multiarch', '')
    return os.environ.get('_PYTHON_SYSCONFIGDATA_NAME', f'''_sysconfigdata_{sys.abiflags}_{sys.platform}_{multiarch}''')


def _generate_posix_vars():
    '''Generate the Python module containing build-time variables.'''
    import pprint
    vars = { }
    makefile = get_makefile_filename()
    
    try:
        _parse_makefile(makefile, vars)
        config_h = get_config_h_filename()
        
        try:
            f = open(config_h, encoding = 'utf-8')
            parse_config_h(f, vars)
            
            try:
                None(None, None)
                if _PYTHON_BUILD:
                    vars['BLDSHARED'] = vars['LDSHARED']
                name = _get_sysconfigdata_name()
                if 'darwin' in sys.platform:
                    import types
                    module = types.ModuleType(name)
                    module.build_time_vars = vars
                    sys.modules[name] = module
                pybuilddir = f'''build/lib.{get_platform()}-{_PY_VERSION_SHORT}'''
                if hasattr(sys, 'gettotalrefcount'):
                    pybuilddir += '-pydebug'
                os.makedirs(pybuilddir, exist_ok = True)
                destfile = os.path.join(pybuilddir, name + '.py')
                f = open(destfile, 'w', encoding = 'utf8')
                f.write('# system configuration generated and used by the sysconfig module\n')
                f.write('build_time_vars = ')
                pprint.pprint(vars, stream = f)
                None(None, None)
                f = open('pybuilddir.txt', 'w', encoding = 'utf8')
                f.write(pybuilddir)
                None(None, None)
                return None
                except OSError:
                    e = None
                    msg = f'''invalid Python installation: unable to open {makefile}'''
                    if hasattr(e, 'strerror'):
                        msg = f'''{msg} ({e.strerror})'''
                    raise OSError(msg)
                    e = None
                    del e
                with None:
                    if not None:
                        pass
                
                try:
                    continue
                except OSError:
                    e = None
                    msg = f'''invalid Python installation: unable to open {config_h}'''
                    if hasattr(e, 'strerror'):
                        msg = f'''{msg} ({e.strerror})'''
                    raise OSError(msg)
                    e = None
                    del e
                    with None:
                        if not None:
                            pass
                    continue
                    with None:
                        if not None:
                            pass
                    return None






def _init_posix(vars):
    '''Initialize the module as appropriate for POSIX systems.'''
    name = _get_sysconfigdata_name()
    _temp = __import__(name, globals(), locals(), [
        'build_time_vars'], 0)
    build_time_vars = _temp.build_time_vars
    vars.update(build_time_vars)


def _init_non_posix(vars):
    '''Initialize the module as appropriate for NT'''
    import _imp
    vars['LIBDEST'] = get_path('stdlib')
    vars['BINLIBDEST'] = get_path('platstdlib')
    vars['INCLUDEPY'] = get_path('include')
    
    try:
        vars['EXT_SUFFIX'] = _imp.extension_suffixes()[0]
        vars['EXE'] = '.exe'
        vars['VERSION'] = _PY_VERSION_SHORT_NO_DOT
        vars['BINDIR'] = os.path.dirname(_safe_realpath(sys.executable))
        vars['TZPATH'] = ''
        return None
    except IndexError:
        continue



def parse_config_h(fp, vars = (None,)):
    '''Parse a config.h-style file.

    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    '''
    pass
# WARNING: Decompyle incomplete


def get_config_h_filename():
    '''Return the path of pyconfig.h.'''
    if _PYTHON_BUILD:
        if os.name == 'nt':
            inc_dir = os.path.join(_PROJECT_BASE, 'PC')
        else:
            inc_dir = _PROJECT_BASE
    else:
        inc_dir = get_path('platinclude')
    return os.path.join(inc_dir, 'pyconfig.h')


def get_scheme_names():
    '''Return a tuple containing the schemes names.'''
    return tuple(sorted(_INSTALL_SCHEMES))


def get_path_names():
    '''Return a tuple containing the paths names.'''
    return _SCHEME_KEYS


def get_paths(scheme, vars, expand = (get_default_scheme(), None, True)):
    '''Return a mapping containing an install scheme.

    ``scheme`` is the install scheme name. If not provided, it will
    return the default scheme for the current platform.
    '''
    if expand:
        return _expand_vars(scheme, vars)
    return None[scheme]


def get_path(name, scheme, vars, expand = (get_default_scheme(), None, True)):
    '''Return a path corresponding to the scheme.

    ``scheme`` is the install scheme name.
    '''
    return get_paths(scheme, vars, expand)[name]


def _init_config_vars():
    global _CONFIG_VARS, _CONFIG_VARS_INITIALIZED
    _CONFIG_VARS = { }
    _PREFIX = os.path.normpath(sys.prefix)
    _EXEC_PREFIX = os.path.normpath(sys.exec_prefix)
    _CONFIG_VARS['prefix'] = _PREFIX
    _CONFIG_VARS['exec_prefix'] = _EXEC_PREFIX
    _CONFIG_VARS['py_version'] = _PY_VERSION
    _CONFIG_VARS['py_version_short'] = _PY_VERSION_SHORT
    _CONFIG_VARS['py_version_nodot'] = _PY_VERSION_SHORT_NO_DOT
    _CONFIG_VARS['installed_base'] = _BASE_PREFIX
    _CONFIG_VARS['base'] = _PREFIX
    _CONFIG_VARS['installed_platbase'] = _BASE_EXEC_PREFIX
    _CONFIG_VARS['platbase'] = _EXEC_PREFIX
    _CONFIG_VARS['projectbase'] = _PROJECT_BASE
    _CONFIG_VARS['platlibdir'] = sys.platlibdir
    
    try:
        _CONFIG_VARS['abiflags'] = sys.abiflags
        
        try:
            _CONFIG_VARS['py_version_nodot_plat'] = sys.winver.replace('.', '')
            if os.name == 'nt':
                _init_non_posix(_CONFIG_VARS)
                _CONFIG_VARS['VPATH'] = sys._vpath
            if os.name == 'posix':
                _init_posix(_CONFIG_VARS)
            if _HAS_USER_BASE:
                _CONFIG_VARS['userbase'] = _getuserbase()
            srcdir = _CONFIG_VARS.get('srcdir', _PROJECT_BASE)
            if os.name == 'posix':
                if _PYTHON_BUILD:
                    base = os.path.dirname(get_makefile_filename())
                    srcdir = os.path.join(base, srcdir)
                else:
                    srcdir = os.path.dirname(get_makefile_filename())
            _CONFIG_VARS['srcdir'] = _safe_realpath(srcdir)
            if sys.platform == 'darwin':
                import _osx_support
                _osx_support.customize_config_vars(_CONFIG_VARS)
            _CONFIG_VARS_INITIALIZED = True
            return None
            except AttributeError:
                _CONFIG_VARS['abiflags'] = ''
                continue
        except AttributeError:
            _CONFIG_VARS['py_version_nodot_plat'] = ''
            continue




def get_config_vars(*args):
    """With no arguments, return a dictionary of all configuration
    variables relevant for the current platform.

    On Unix, this means every variable defined in Python's installed Makefile;
    On Windows it's a much smaller set.

    With arguments, return a list of values that result from looking up
    each argument in the configuration variable dictionary.
    """
    pass
# WARNING: Decompyle incomplete


def get_config_var(name):
    """Return the value of a single variable using the dictionary returned by
    'get_config_vars()'.

    Equivalent to get_config_vars().get(name)
    """
    return get_config_vars().get(name)


def get_platform():
    """Return a string that identifies the current platform.

    This is used mainly to distinguish platform-specific build directories and
    platform-specific built distributions.  Typically includes the OS name and
    version and the architecture (as supplied by 'os.uname()'), although the
    exact information included depends on the OS; on Linux, the kernel version
    isn't particularly important.

    Examples of returned values:
       linux-i586
       linux-alpha (?)
       solaris-2.6-sun4u

    Windows will return one of:
       win-amd64 (64-bit Windows on AMD64 (aka x86_64, Intel64, EM64T, etc)
       win-arm64 (64-bit Windows on ARM64 (aka AArch64)
       win32 (all others - specifically, sys.platform is returned)

    For other non-POSIX platforms, currently just returns 'sys.platform'.

    """
    if os.name == 'nt':
        if 'amd64' in sys.version.lower():
            return 'win-amd64'
        if '(arm)' in sys.version.lower():
            return 'win-arm32'
        if '(arm64)' in sys.version.lower():
            return 'win-arm64'
        return sys.platform
    if not None.name != 'posix' or hasattr(os, 'uname'):
        return sys.platform
    if None in os.environ:
        return os.environ['_PYTHON_HOST_PLATFORM']
    (osname, host, release, version, machine) = None.uname()
    osname = osname.lower().replace('/', '')
    machine = machine.replace(' ', '_')
    machine = machine.replace('/', '-')
    if osname[:5] == 'linux':
        return f'''{osname}-{machine}'''
    if None[:5] == 'sunos' or release[0] >= '5':
        osname = 'solaris'
        release = f'''{int(release[0]) - 3}.{release[2:]}'''
        bitness = {
            2147483647: '32bit',
            0x7FFFFFFFFFFFFFFF: '64bit' }
        machine += f'''.{bitness[sys.maxsize]}'''
    elif osname[:3] == 'aix':
        aix_platform = aix_platform
        import _aix_support
        return aix_platform()
    if osname[:6] == 'cygwin':
        osname = 'cygwin'
        import re
        rel_re = re.compile('[\\d.]+')
        m = rel_re.match(release)
        if m:
            release = m.group()
        elif osname[:6] == 'darwin':
            import _osx_support
            (osname, release, machine) = _osx_support.get_platform_osx(get_config_vars(), osname, release, machine)
    return f'''{osname}-{release}-{machine}'''


def get_python_version():
    return _PY_VERSION_SHORT


def expand_makefile_vars(s, vars):
    '''Expand Makefile-style variables -- "${foo}" or "$(foo)" -- in
    \'string\' according to \'vars\' (a dictionary mapping variable names to
    values).  Variables not present in \'vars\' are silently expanded to the
    empty string.  The variable values in \'vars\' should not contain further
    variable expansions; if \'vars\' is the output of \'parse_makefile()\',
    you\'re fine.  Returns a variable-expanded version of \'s\'.
    '''
    import re
    if not re.search(_findvar1_rx, s):
        re.search(_findvar1_rx, s)
    m = re.search(_findvar2_rx, s)
    if m:
        (beg, end) = m.span()
        s = s[0:beg] + vars.get(m.group(1)) + s[end:]
    else:
        return s


def _print_dict(title, data):
    for key, value in enumerate(sorted(data.items())):
        if index == 0:
            print(f'''{title}: ''')
        print(f'''\t{key} = "{value}"''')


def _main():
    '''Display all information sysconfig detains.'''
    if '--generate-posix-vars' in sys.argv:
        _generate_posix_vars()
        return None
    print(f'''Platform: "{get_platform()}"''')
    print(f'''Python version: "{get_python_version()}"''')
    print(f'''Current installation scheme: "{get_default_scheme()}"''')
    print()
    _print_dict('Paths', get_paths())
    print()
    _print_dict('Variables', get_config_vars())

if __name__ == '__main__':
    _main()
    return None
