# Source Generated with Decompyle++
# File: bdist_wheel.pyc (Python 3.12)

'''
Create a wheel (.whl) distribution.

A wheel is a built archive format.
'''
from __future__ import annotations
import os
import re
import shutil
import struct
import sys
import sysconfig
import warnings
from collections.abc import Iterable, Sequence
from email.generator import BytesGenerator
from glob import iglob
from typing import Literal, cast
from zipfile import ZIP_DEFLATED, ZIP_STORED
from packaging import tags, version as _packaging_version
from wheel.wheelfile import WheelFile
from  import Command, __version__, _shutil
from _normalization import safer_name
from warnings import SetuptoolsDeprecationWarning
from egg_info import egg_info as egg_info_cls
from distutils import log

def safe_version(version = None):
    '''
    Convert an arbitrary string to a standard version string
    '''
    
    try:
        return str(_packaging_version.Version(version))
    except _packaging_version.InvalidVersion:
        version = version.replace(' ', '.')
        return 


setuptools_major_version = int(__version__.split('.')[0])
PY_LIMITED_API_PATTERN = 'cp3\\d'

def _is_32bit_interpreter():
    return struct.calcsize('P') == 4


def python_tag():
    return f'''py{sys.version_info.major}'''


def get_platform(archive_root = None):
    """Return our platform name 'win32', 'linux_x86_64'"""
    result = sysconfig.get_platform()
# WARNING: Decompyle incomplete


def get_flag(var = None, fallback = None, expected = None, warn = (True, True)):
    '''Use a fallback value for determining SOABI flags if the needed config
    var is unset or unavailable.'''
    val = sysconfig.get_config_var(var)
# WARNING: Decompyle incomplete


def get_abi_tag():
    '''Return the ABI tag based on SOABI (if available) or emulate SOABI (PyPy2).'''
    soabi = sysconfig.get_config_var('SOABI')
    impl = tags.interpreter_name()
    if soabi and impl in ('cp', 'pp') and hasattr(sys, 'maxunicode'):
        d = ''
        u = ''
        if get_flag('Py_DEBUG', hasattr(sys, 'gettotalrefcount'), warn = impl == 'cp'):
            d = 'd'
        abi = f'''{impl}{tags.interpreter_version()}{d}{u}'''
        return abi
    if None and impl == 'cp' and soabi.startswith('cpython'):
        abi = 'cp' + soabi.split('-')[1]
        return abi
    if None and impl == 'cp' and soabi.startswith('cp'):
        abi = soabi.split('-')[0]
        if hasattr(sys, 'gettotalrefcount'):
            abi += 'd'
        return abi
    if None and impl == 'pp':
        abi = '-'.join(soabi.split('-')[:2])
        abi = abi.replace('.', '_').replace('-', '_')
        return abi
    if None and impl == 'graalpy':
        abi = '-'.join(soabi.split('-')[:3])
        abi = abi.replace('.', '_').replace('-', '_')
        return abi
    if None:
        abi = soabi.replace('.', '_').replace('-', '_')
        return abi
    abi = None
    return abi


def safer_version(version = None):
    return safe_version(version).replace('-', '_')


class bdist_wheel(Command):
    description = 'create a wheel distribution'
    supported_compressions = {
        'stored': ZIP_STORED,
        'deflated': ZIP_DEFLATED }
    user_options = [
        ('bdist-dir=', 'b', 'temporary directory for creating the distribution'),
        ('plat-name=', 'p', f'''platform name to embed in generated filenames [default: {get_platform(None)}]'''),
        ('keep-temp', 'k', 'keep the pseudo-installation tree around after creating the distribution archive'),
        ('dist-dir=', 'd', 'directory to put final built distributions in'),
        ('skip-build', None, 'skip rebuilding everything (for testing/debugging)'),
        ('relative', None, 'build the archive using relative paths [default: false]'),
        ('owner=', 'u', 'Owner name used when creating a tar file [default: current user]'),
        ('group=', 'g', 'Group name used when creating a tar file [default: current group]'),
        ('universal', None, '*DEPRECATED* make a universal wheel [default: false]'),
        ('compression=', None, f'''zipfile compression (one of: {', '.join(supported_compressions)}) [default: \'deflated\']'''),
        ('python-tag=', None, f'''Python implementation compatibility tag [default: \'{python_tag()}\']'''),
        ('build-number=', None, 'Build number for this particular version. As specified in PEP-0427, this must start with a digit. [default: None]'),
        ('py-limited-api=', None, 'Python tag (cp32|cp33|cpNN) for abi3 wheel tag [default: false]'),
        ('dist-info-dir=', None, "directory where a pre-generated dist-info can be found (e.g. as a result of calling the PEP517 'prepare_metadata_for_build_wheel' method)")]
    boolean_options = [
        'keep-temp',
        'skip-build',
        'relative',
        'universal']
    
    def initialize_options(self = None):
        self.bdist_dir = None
        self.data_dir = ''
        self.plat_name = None
        self.plat_tag = None
        self.format = 'zip'
        self.keep_temp = False
        self.dist_dir = None
        self.dist_info_dir = None
        self.egginfo_dir = None
        self.root_is_pure = None
        self.skip_build = False
        self.relative = False
        self.owner = None
        self.group = None
        self.universal = False
        self.compression = 'deflated'
        self.python_tag = python_tag()
        self.build_number = None
        self.py_limited_api = False
        self.plat_name_supplied = False

    
    def finalize_options(self = None):
        if not self.bdist_dir:
            bdist_base = self.get_finalized_command('bdist').bdist_base
            self.bdist_dir = os.path.join(bdist_base, 'wheel')
    # WARNING: Decompyle incomplete

    
    def _validate_py_limited_api(self = None):
        if not self.py_limited_api:
            return None
        if not re.match(PY_LIMITED_API_PATTERN, self.py_limited_api):
            raise ValueError(f'''py-limited-api must match \'{PY_LIMITED_API_PATTERN}\'''')
        if sysconfig.get_config_var('Py_GIL_DISABLED'):
            raise ValueError(f'''`py_limited_api={self.py_limited_api!r}` not supported. `Py_LIMITED_API` is currently incompatible with `Py_GIL_DISABLED`.See https://github.com/python/cpython/issues/111506.''')

    wheel_dist_name = (lambda self = None: components = [
safer_name(self.distribution.get_name()),
safer_version(self.distribution.get_version())]if self.build_number:
components.append(self.build_number)'-'.join(components))()
    
    def get_tag(self = None):
        if self.plat_name_supplied and self.plat_name:
            plat_name = self.plat_name
        elif self.root_is_pure:
            plat_name = 'any'
        elif not self.plat_name and self.plat_name.startswith('macosx'):
            plat_name = self.plat_name
        else:
            plat_name = get_platform(self.bdist_dir)
        if _is_32bit_interpreter():
            if plat_name in ('linux-x86_64', 'linux_x86_64'):
                plat_name = 'linux_i686'
            if plat_name in ('linux-aarch64', 'linux_aarch64'):
                plat_name = 'linux_armv7l'
        plat_name = plat_name.lower().replace('-', '_').replace('.', '_').replace(' ', '_')
        if self.root_is_pure:
            if self.universal:
                impl = 'py2.py3'
            else:
                impl = self.python_tag
            tag = (impl, 'none', plat_name)
            return tag
        impl_name = None.interpreter_name()
        impl_ver = tags.interpreter_version()
        impl = impl_name + impl_ver
        if self.py_limited_api and (impl_name + impl_ver).startswith('cp3'):
            impl = self.py_limited_api
            abi_tag = 'abi3'
        else:
            abi_tag = str(get_abi_tag()).lower()
        tag = (impl, abi_tag, plat_name)
    # WARNING: Decompyle incomplete

    
    def run(self):
        build_scripts = self.reinitialize_command('build_scripts')
        build_scripts.executable = 'python'
        build_scripts.force = True
        build_ext = self.reinitialize_command('build_ext')
        build_ext.inplace = False
        if not self.skip_build:
            self.run_command('build')
        install = self.reinitialize_command('install', reinit_subcommands = True)
        install.root = self.bdist_dir
        install.compile = False
        install.skip_build = self.skip_build
        install.warn_dir = False
        install_scripts = self.reinitialize_command('install_scripts')
        install_scripts.no_ep = True
        for key in ('headers', 'scripts', 'data', 'purelib', 'platlib'):
            setattr(install, 'install_' + key, os.path.join(self.data_dir, key))
        basedir_observed = ''
        if os.name == 'nt':
            basedir_observed = os.path.normpath(os.path.join(self.data_dir, '..'))
            self.install_libbase = basedir_observed
            self.install_lib = basedir_observed
        setattr(install, 'install_purelib' if self.root_is_pure else 'install_platlib', basedir_observed)
        log.info(f'''installing to {self.bdist_dir}''')
        self.run_command('install')
        (impl_tag, abi_tag, plat_tag) = self.get_tag()
        archive_basename = f'''{self.wheel_dist_name}-{impl_tag}-{abi_tag}-{plat_tag}'''
        if not self.relative:
            archive_root = self.bdist_dir
        else:
            archive_root = os.path.join(self.bdist_dir, self._ensure_relative(install.install_base))
        self.set_undefined_options('install_egg_info', ('target', 'egginfo_dir'))
        distinfo_dirname = f'''{safer_name(self.distribution.get_name())}-{safer_version(self.distribution.get_version())}.dist-info'''
        distinfo_dir = os.path.join(self.bdist_dir, distinfo_dirname)
        if self.dist_info_dir:
            log.debug(f'''reusing {self.dist_info_dir}''')
            shutil.copytree(self.dist_info_dir, distinfo_dir)
            _shutil.rmtree(self.egginfo_dir)
        else:
            self.egg2dist(self.egginfo_dir, distinfo_dir)
        self.write_wheelfile(distinfo_dir)
        if not os.path.exists(self.dist_dir):
            os.makedirs(self.dist_dir)
        wheel_path = os.path.join(self.dist_dir, archive_basename + '.whl')
        wf = WheelFile(wheel_path, 'w', self._zip_compression())
        wf.write_files(archive_root)
        None(None, None)
        getattr(self.distribution, 'dist_files', []).append(('bdist_wheel', f'''{sys.version_info.major}.{sys.version_info.minor}''', wheel_path))
        if not self.keep_temp:
            log.info(f'''removing {self.bdist_dir}''')
            if not self.dry_run:
                _shutil.rmtree(self.bdist_dir)
                return None
            return None
        return None
        with None:
            if not None:
                pass
        continue

    
    def write_wheelfile(self = None, wheelfile_base = None, generator = None):
        Message = Message
        import email.message
        msg = Message()
        msg['Wheel-Version'] = '1.0'
        msg['Generator'] = generator
        msg['Root-Is-Purelib'] = str(self.root_is_pure).lower()
    # WARNING: Decompyle incomplete

    
    def _ensure_relative(self = None, path = None):
        (drive, path) = os.path.splitdrive(path)
        if path[0:1] == os.sep:
            path = drive + path[1:]
        return path

    license_paths = (lambda self = None: if setuptools_major_version >= 57:
if not self.distribution.metadata.license_files:
self.distribution.metadata.license_files()files = None[str]()metadata = self.distribution.get_option_dict('metadata')if setuptools_major_version >= 42:
patterns = cast(Sequence[str], self.distribution.metadata.license_files)elif 'license_files' in metadata:
patterns = metadata['license_files'][1].split()else:
patterns = ()if 'license_file' in metadata:
warnings.warn('The "license_file" option is deprecated. Use "license_files" instead.', DeprecationWarning, stacklevel = 2)files.add(metadata['license_file'][1])if not files and patterns and isinstance(patterns, list):
patterns = ('LICEN[CS]E*', 'COPYING*', 'NOTICE*', 'AUTHORS*')for pattern in patterns:
for path in iglob(pattern):
if path.endswith('~'):
log.debug(f'''ignoring license file "{path}" as it looks like a backup''')continueif not path not in files:
continueif not os.path.isfile(path):
continuelog.info(f'''adding license file "{path}" (matched pattern "{pattern}")''')files.add(path)files)()
    
    def egg2dist(self = None, egginfo_path = None, distinfo_path = None):
        '''Convert an .egg-info directory into a .dist-info directory'''
        
        def adios(p = None):
            '''Appropriately delete directory, file or link.'''
            if os.path.exists(p) and os.path.islink(p) and os.path.isdir(p):
                _shutil.rmtree(p)
                return None
            if os.path.exists(p):
                os.unlink(p)
                return None

        adios(distinfo_path)
        if not os.path.exists(egginfo_path):
            import glob
            pat = os.path.join(os.path.dirname(egginfo_path), '*.egg-info')
            possible = glob.glob(pat)
            err = f'''Egg metadata expected at {egginfo_path} but not found'''
            if possible:
                alt = os.path.basename(possible[0])
                err += f''' ({alt} found - possible misnamed archive file?)'''
            raise ValueError(err)
        pkginfo_path = os.path.join(egginfo_path, 'PKG-INFO')
        shutil.copytree(egginfo_path, distinfo_path, ignore = (lambda x, y: {
'SOURCES.txt',
'not-zip-safe',
'requires.txt',
'PKG-INFO'}))
        dependency_links_path = os.path.join(distinfo_path, 'dependency_links.txt')
        dependency_links_file = open(dependency_links_path, encoding = 'utf-8')
        dependency_links = dependency_links_file.read().strip()
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def _zip_compression(self = None):
        if isinstance(self.compression, int) and self.compression in self.supported_compressions.values():
            return self.compression
        compression = None.supported_compressions.get(str(self.compression))
    # WARNING: Decompyle incomplete


