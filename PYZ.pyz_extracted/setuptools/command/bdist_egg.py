# Source Generated with Decompyle++
# File: bdist_egg.pyc (Python 3.12)

'''setuptools.command.bdist_egg

Build .egg distributions'''
from __future__ import annotations
import marshal
import os
import re
import sys
import textwrap
from sysconfig import get_path, get_python_version
from types import CodeType
from typing import TYPE_CHECKING, Literal
from setuptools import Command
from setuptools.extension import Library
from _path import StrPathT, ensure_directory
from distutils import log
from distutils.dir_util import mkpath, remove_tree
if TYPE_CHECKING:
    from typing_extensions import TypeAlias
_ZipFileMode: 'TypeAlias' = Literal[('r', 'w', 'x', 'a')]

def _get_purelib():
    return get_path('purelib')


def strip_module(filename):
    if '.' in filename:
        filename = os.path.splitext(filename)[0]
    if filename.endswith('module'):
        filename = filename[:-6]
    return filename


def sorted_walk(dir):
    '''Do os.walk in a reproducible way,
    independent of indeterministic filesystem readdir order
    '''
    pass
# WARNING: Decompyle incomplete


def write_stub(resource = None, pyfile = None):
    _stub_template = textwrap.dedent('\n        def __bootstrap__():\n            global __bootstrap__, __loader__, __file__\n            import sys, pkg_resources, importlib.util\n            __file__ = pkg_resources.resource_filename(__name__, %r)\n            __loader__ = None; del __bootstrap__, __loader__\n            spec = importlib.util.spec_from_file_location(__name__,__file__)\n            mod = importlib.util.module_from_spec(spec)\n            spec.loader.exec_module(mod)\n        __bootstrap__()\n        ').lstrip()
    f = open(pyfile, 'w', encoding = 'utf-8')
    f.write(_stub_template % resource)
    None(None, None)
    return None
    with None:
        if not None:
            pass


class bdist_egg(Command):
    description = 'create an "egg" distribution'
    user_options = [
        ('bdist-dir=', 'b', 'temporary directory for creating the distribution'),
        ('plat-name=', 'p', 'platform name to embed in generated filenames (by default uses `pkg_resources.get_build_platform()`)'),
        ('exclude-source-files', None, 'remove all .py files from the generated egg'),
        ('keep-temp', 'k', 'keep the pseudo-installation tree around after creating the distribution archive'),
        ('dist-dir=', 'd', 'directory to put final built distributions in'),
        ('skip-build', None, 'skip rebuilding everything (for testing/debugging)')]
    boolean_options = [
        'keep-temp',
        'skip-build',
        'exclude-source-files']
    
    def initialize_options(self):
        self.bdist_dir = None
        self.plat_name = None
        self.keep_temp = False
        self.dist_dir = None
        self.skip_build = False
        self.egg_output = None
        self.exclude_source_files = None

    
    def finalize_options(self = None):
        ei_cmd = self.get_finalized_command('egg_info')
        self.ei_cmd = self.get_finalized_command('egg_info')
        self.egg_info = ei_cmd.egg_info
    # WARNING: Decompyle incomplete

    
    def do_install_data(self = None):
        self.get_finalized_command('install').install_lib = self.bdist_dir
        site_packages = os.path.normcase(os.path.realpath(_get_purelib()))
        old, self.distribution.data_files = self.distribution.data_files, []
        for item in old:
            if isinstance(item, tuple) and len(item) == 2 and os.path.isabs(item[0]):
                realpath = os.path.realpath(item[0])
                normalized = os.path.normcase(realpath)
                if normalized == site_packages or normalized.startswith(site_packages + os.sep):
                    item = (realpath[len(site_packages) + 1:], item[1])
            self.distribution.data_files.append(item)
        
        try:
            log.info('installing package data to %s', self.bdist_dir)
            self.call_command('install_data', force = False, root = None)
            self.distribution.data_files = old
            return None
        except:
            self.distribution.data_files = old


    
    def get_outputs(self):
        return [
            self.egg_output]

    
    def call_command(self, cmdname, **kw):
        '''Invoke reinitialized command `cmdname` with keyword args'''
        for dirname in INSTALL_DIRECTORY_ATTRS:
            kw.setdefault(dirname, self.bdist_dir)
        kw.setdefault('skip_build', self.skip_build)
        kw.setdefault('dry_run', self.dry_run)
    # WARNING: Decompyle incomplete

    
    def run(self):
        self.run_command('egg_info')
        log.info('installing library code to %s', self.bdist_dir)
        instcmd = self.get_finalized_command('install')
        old_root = instcmd.root
        instcmd.root = None
        if not self.distribution.has_c_libraries() and self.skip_build:
            self.run_command('build_clib')
        cmd = self.call_command('install_lib', warn_dir = False)
        instcmd.root = old_root
        (all_outputs, ext_outputs) = self.get_ext_outputs()
        self.stubs = []
        to_compile = []
        for p, ext_name in enumerate(ext_outputs):
            (filename, _ext) = os.path.splitext(ext_name)
            pyfile = os.path.join(self.bdist_dir, strip_module(filename) + '.py')
            self.stubs.append(pyfile)
            log.info('creating stub loader for %s', ext_name)
            if not self.dry_run:
                write_stub(os.path.basename(ext_name), pyfile)
            to_compile.append(pyfile)
            ext_outputs[p] = ext_name.replace(os.sep, '/')
        if to_compile:
            cmd.byte_compile(to_compile)
        if self.distribution.data_files:
            self.do_install_data()
        archive_root = self.bdist_dir
        egg_info = os.path.join(archive_root, 'EGG-INFO')
        self.mkpath(egg_info)
        if self.distribution.scripts:
            script_dir = os.path.join(egg_info, 'scripts')
            log.info('installing scripts to %s', script_dir)
            self.call_command('install_scripts', install_dir = script_dir, no_ep = True)
        self.copy_metadata_to(egg_info)
        native_libs = os.path.join(egg_info, 'native_libs.txt')
        if all_outputs:
            log.info('writing %s', native_libs)
            if not self.dry_run:
                ensure_directory(native_libs)
                libs_file = open(native_libs, 'wt', encoding = 'utf-8')
                libs_file.write('\n'.join(all_outputs))
                libs_file.write('\n')
                None(None, None)
            elif os.path.isfile(native_libs):
                log.info('removing %s', native_libs)
                if not self.dry_run:
                    os.unlink(native_libs)
        write_safety_flag(os.path.join(archive_root, 'EGG-INFO'), self.zip_safe())
        if os.path.exists(os.path.join(self.egg_info, 'depends.txt')):
            log.warn("WARNING: 'depends.txt' will not be used by setuptools 0.6!\nUse the install_requires/extras_require setup() args instead.")
        if self.exclude_source_files:
            self.zap_pyfiles()
        make_zipfile(self.egg_output, archive_root, verbose = self.verbose, dry_run = self.dry_run, mode = self.gen_header())
        if not self.keep_temp:
            remove_tree(self.bdist_dir, dry_run = self.dry_run)
        getattr(self.distribution, 'dist_files', []).append(('bdist_egg', get_python_version(), self.egg_output))
        return None
        with None:
            if not None:
                pass
        continue

    
    def zap_pyfiles(self):
        log.info('Removing .py files from temporary directory')
        for base, dirs, files in walk_egg(self.bdist_dir):
            for name in files:
                path = os.path.join(base, name)
                if name.endswith('.py'):
                    log.debug('Deleting %s', path)
                    os.unlink(path)
                if not base.endswith('__pycache__'):
                    continue
                path_old = path
                pattern = '(?P<name>.+)\\.(?P<magic>[^.]+)\\.pyc'
                m = re.match(pattern, name)
                path_new = os.path.join(base, os.pardir, m.group('name') + '.pyc')
                log.info(f'''Renaming file from [{path_old}] to [{path_new}]''')
                os.remove(path_new)
                os.rename(path_old, path_new)
        return None
        except OSError:
            continue

    
    def zip_safe(self):
        safe = getattr(self.distribution, 'zip_safe', None)
    # WARNING: Decompyle incomplete

    
    def gen_header(self = None):
        return 'w'

    
    def copy_metadata_to(self = None, target_dir = None):
        '''Copy metadata (egg info) to the target_dir'''
        norm_egg_info = os.path.normpath(self.egg_info)
        prefix = os.path.join(norm_egg_info, '')
        for path in self.ei_cmd.filelist.files:
            if not path.startswith(prefix):
                continue
            target = os.path.join(target_dir, path[len(prefix):])
            ensure_directory(target)
            self.copy_file(path, target)

    
    def get_ext_outputs(self):
        '''Get a list of relative paths to C extensions in the output distro'''
        pass
    # WARNING: Decompyle incomplete


NATIVE_EXTENSIONS: 'dict[str, None]' = dict.fromkeys('.dll .so .dylib .pyd'.split())

def walk_egg(egg_dir):
    """Walk an unpacked egg's contents, skipping the metadata directory"""
    pass
# WARNING: Decompyle incomplete


def analyze_egg(egg_dir, stubs):
    for flag, fn in safety_flags.items():
        if not os.path.exists(os.path.join(egg_dir, 'EGG-INFO', fn)):
            continue
        
        return safety_flags.items(), flag
    if not can_scan():
        return False
    for base, dirs, files in walk_egg(egg_dir):
        for name in files:
            if name.endswith('.py') or name.endswith('.pyw'):
                continue
            if not name.endswith('.pyc') and name.endswith('.pyo'):
                continue
            if scan_module(egg_dir, base, name, stubs):
                scan_module(egg_dir, base, name, stubs)
            safe = safe
    return safe


def write_safety_flag(egg_dir = None, safe = None):
    pass
# WARNING: Decompyle incomplete

safety_flags = {
    True: 'zip-safe',
    False: 'not-zip-safe' }

def scan_module(egg_dir, base, name, stubs):
    '''Check whether module possibly uses unsafe-for-zipfile stuff'''
    filename = os.path.join(base, name)
    if filename[:-1] in stubs:
        return True
    pkg = base[len(egg_dir) + 1:].replace(os.sep, '.')
    if pkg:
        pkg
    if not '.':
        '.'
    module = pkg + '' + os.path.splitext(name)[0]
    skip = 16
    f = open(filename, 'rb')
    f.read(skip)
    code = marshal.load(f)
    f.close()
    safe = True
    symbols = dict.fromkeys(iter_symbols(code))
    for bad in ('__file__', '__path__'):
        if not bad in symbols:
            continue
        log.warn('%s: module references %s', module, bad)
        safe = False
    if 'inspect' in symbols:
        for bad in ('getsource', 'getabsfile', 'getfile', 'getsourcefile', 'getsourcelines', 'findsource', 'getcomments', 'getframeinfo', 'getinnerframes', 'getouterframes', 'stack', 'trace'):
            if not bad in symbols:
                continue
            log.warn('%s: module MAY be using inspect.%s', module, bad)
            safe = False
    return safe


def iter_symbols(code):
    '''Yield names and strings used by `code` and its nested code objects'''
    pass
# WARNING: Decompyle incomplete


def can_scan():
    if sys.platform.startswith('java') and sys.platform != 'cli':
        return True
    log.warn('Unable to analyze compiled code on this platform.')
    log.warn("Please ask the author to include a 'zip_safe' setting (either True or False) in the package's setup.py")
    return False

INSTALL_DIRECTORY_ATTRS = [
    'install_lib',
    'install_dir',
    'install_data',
    'install_base']

def make_zipfile(zip_filename, base_dir = None, verbose = None, dry_run = None, compress = (False, False, True, 'w'), mode = ('zip_filename', 'StrPathT', 'verbose', 'bool', 'dry_run', 'bool', 'mode', '_ZipFileMode', 'return', 'StrPathT')):
    '''Create a zip file from all the files under \'base_dir\'.  The output
    zip file will be named \'base_dir\' + ".zip".  Uses either the "zipfile"
    Python module (if available) or the InfoZIP "zip" utility (if installed
    and found on the default search path).  If neither tool is available,
    raises DistutilsExecError.  Returns the name of the output zip file.
    '''
    pass
# WARNING: Decompyle incomplete

