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
import stat
import struct
import sys
import sysconfig
import warnings
from email.generator import BytesGenerator, Generator
from email.policy import EmailPolicy
from glob import iglob
from shutil import rmtree
from zipfile import ZIP_DEFLATED, ZIP_STORED
import setuptools
from setuptools import Command
from  import __version__ as wheel_version
from macosx_libfile import calculate_macosx_platform_tag
from metadata import pkginfo_to_metadata
from util import log
from vendored.packaging import tags
from vendored.packaging import version as _packaging_version
from wheelfile import WheelFile

def safe_name(name):
    """Convert an arbitrary string to a standard distribution name
    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    """
    return re.sub('[^A-Za-z0-9.]+', '-', name)


def safe_version(version):
    '''
    Convert an arbitrary string to a standard version string
    '''
    
    try:
        return str(_packaging_version.Version(version))
    except _packaging_version.InvalidVersion:
        version = version.replace(' ', '.')
        return 


setuptools_major_version = int(setuptools.__version__.split('.')[0])
PY_LIMITED_API_PATTERN = 'cp3\\d'

def _is_32bit_interpreter():
    return struct.calcsize('P') == 4


def python_tag():
    return f'''py{sys.version_info[0]}'''


def get_platform(archive_root):
    """Return our platform name 'win32', 'linux_x86_64'"""
    result = sysconfig.get_platform()
# WARNING: Decompyle incomplete


def get_flag(var, fallback, expected, warn = (True, True)):
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
        m = ''
        u = ''
        if get_flag('Py_DEBUG', hasattr(sys, 'gettotalrefcount'), warn = impl == 'cp'):
            d = 'd'
        if impl == 'cp':
            impl == 'cp'
        if get_flag('WITH_PYMALLOC', impl == 'cp', warn = sys.version_info < (3, 8)) and sys.version_info < (3, 8):
            m = 'm'
        abi = f'''{impl}{tags.interpreter_version()}{d}{m}{u}'''
        return abi
    if None and impl == 'cp' and soabi.startswith('cpython'):
        abi = 'cp' + soabi.split('-')[1]
        return abi
    if None and impl == 'cp' and soabi.startswith('cp'):
        abi = soabi.split('-')[0]
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


def safer_name(name):
    return safe_name(name).replace('-', '_')


def safer_version(version):
    return safe_version(version).replace('-', '_')


def remove_readonly(func, path, excinfo):
    remove_readonly_exc(func, path, excinfo[1])


def remove_readonly_exc(func, path, exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


class bdist_wheel(Command):
    description = 'create a wheel distribution'
    supported_compressions = {
        'stored': ZIP_STORED,
        'deflated': ZIP_DEFLATED }
    user_options = [
        ('bdist-dir=', 'b', 'temporary directory for creating the distribution'),
        ('plat-name=', 'p', 'platform name to embed in generated filenames (default: %s)' % get_platform(None)),
        ('keep-temp', 'k', 'keep the pseudo-installation tree around after creating the distribution archive'),
        ('dist-dir=', 'd', 'directory to put final built distributions in'),
        ('skip-build', None, 'skip rebuilding everything (for testing/debugging)'),
        ('relative', None, 'build the archive using relative paths (default: false)'),
        ('owner=', 'u', 'Owner name used when creating a tar file [default: current user]'),
        ('group=', 'g', 'Group name used when creating a tar file [default: current group]'),
        ('universal', None, 'make a universal wheel (default: false)'),
        ('compression=', None, "zipfile compression (one of: {}) (default: 'deflated')".format(', '.join(supported_compressions))),
        ('python-tag=', None, "Python implementation compatibility tag (default: '%s')" % python_tag()),
        ('build-number=', None, 'Build number for this particular version. As specified in PEP-0427, this must start with a digit. [default: None]'),
        ('py-limited-api=', None, 'Python tag (cp32|cp33|cpNN) for abi3 wheel tag (default: false)')]
    boolean_options = [
        'keep-temp',
        'skip-build',
        'relative',
        'universal']
    
    def initialize_options(self):
        self.bdist_dir = None
        self.data_dir = None
        self.plat_name = None
        self.plat_tag = None
        self.format = 'zip'
        self.keep_temp = False
        self.dist_dir = None
        self.egginfo_dir = None
        self.root_is_pure = None
        self.skip_build = None
        self.relative = False
        self.owner = None
        self.group = None
        self.universal = False
        self.compression = 'deflated'
        self.python_tag = python_tag()
        self.build_number = None
        self.py_limited_api = False
        self.plat_name_supplied = False

    
    def finalize_options(self):
        pass
    # WARNING: Decompyle incomplete

    wheel_dist_name = (lambda self: components = (safer_name(self.distribution.get_name()), safer_version(self.distribution.get_version()))if self.build_number:
components += (self.build_number,)'-'.join(components))()
    
    def get_tag(self):
        if self.plat_name_supplied:
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
        self.egg2dist(self.egginfo_dir, distinfo_dir)
        self.write_wheelfile(distinfo_dir)
        if not os.path.exists(self.dist_dir):
            os.makedirs(self.dist_dir)
        wheel_path = os.path.join(self.dist_dir, archive_basename + '.whl')
        wf = WheelFile(wheel_path, 'w', self.compression)
        wf.write_files(archive_root)
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def write_wheelfile(self, wheelfile_base, generator = ('bdist_wheel (' + wheel_version + ')',)):
        Message = Message
        import email.message
        msg = Message()
        msg['Wheel-Version'] = '1.0'
        msg['Generator'] = generator
        msg['Root-Is-Purelib'] = str(self.root_is_pure).lower()
    # WARNING: Decompyle incomplete

    
    def _ensure_relative(self, path):
        (drive, path) = os.path.splitdrive(path)
        if path[0:1] == os.sep:
            path = drive + path[1:]
        return path

    license_paths = (lambda self: if setuptools_major_version >= 57:
if not self.distribution.metadata.license_files:
self.distribution.metadata.license_files()files = None()metadata = self.distribution.get_option_dict('metadata')if setuptools_major_version >= 42:
patterns = self.distribution.metadata.license_fileselif 'license_files' in metadata:
patterns = metadata['license_files'][1].split()else:
patterns = ()if 'license_file' in metadata:
warnings.warn('The "license_file" option is deprecated. Use "license_files" instead.', DeprecationWarning, stacklevel = 2)files.add(metadata['license_file'][1])if not files and patterns and isinstance(patterns, list):
patterns = ('LICEN[CS]E*', 'COPYING*', 'NOTICE*', 'AUTHORS*')for pattern in patterns:
for path in iglob(pattern):
if path.endswith('~'):
log.debug(f'''ignoring license file "{path}" as it looks like a backup''')continueif not path not in files:
continueif not os.path.isfile(path):
continuelog.info(f'''adding license file "{path}" (matched pattern "{pattern}")''')files.add(path)files)()
    
    def egg2dist(self, egginfo_path, distinfo_path):
        '''Convert an .egg-info directory into a .dist-info directory'''
        
        def adios(p):
            '''Appropriately delete directory, file or link.'''
            if os.path.exists(p) and os.path.islink(p) and os.path.isdir(p):
                shutil.rmtree(p)
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
        if os.path.isfile(egginfo_path):
            pkginfo_path = egginfo_path
            pkg_info = pkginfo_to_metadata(egginfo_path, egginfo_path)
            os.mkdir(distinfo_path)
    # WARNING: Decompyle incomplete


