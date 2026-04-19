# Source Generated with Decompyle++
# File: egg_info.pyc (Python 3.12)

"""setuptools.command.egg_info

Create a distribution's .egg-info directory and contents"""
import functools
import os
import re
import sys
import time
from collections.abc import Callable
import packaging
import packaging.requirements as packaging
import packaging.version as packaging
from setuptools.unicode_utils import unicode_utils
from setuptools import Command
from setuptools.command import bdist_egg
from setuptools.command.sdist import sdist, walk_revctrl
from setuptools.command.setopt import edit_config
from setuptools.glob import glob
from  import _entry_points, _normalization
from _importlib import metadata
from warnings import SetuptoolsDeprecationWarning
from  import _requirestxt
import distutils.errors as distutils
import distutils.filelist as distutils
from distutils import log
from distutils.errors import DistutilsInternalError
from distutils.filelist import FileList as _FileList
from distutils.util import convert_path
PY_MAJOR = f'''{sys.version_info.major}.{sys.version_info.minor}'''

def translate_pattern(glob):
    """
    Translate a file path glob like '*.txt' in to a regular expression.
    This differs from fnmatch.translate which allows wildcards to match
    directory separators. It also knows about '**/' which matches any number of
    directories.
    """
    pat = ''
    chunks = glob.split(os.path.sep)
    sep = re.escape(os.sep)
    valid_char = f'''[^{sep}]'''
    for c, chunk in enumerate(chunks):
        last_chunk = c == len(chunks) - 1
        if chunk == '**':
            continue
        i = 0
        chunk_len = len(chunk)
        if i < chunk_len:
            char = chunk[i]
            if char == '*':
                pat += valid_char + '*'
            elif char == '?':
                pat += valid_char
            elif char == '[':
                inner_i = i + 1
                if inner_i < chunk_len and chunk[inner_i] == '!':
                    inner_i = inner_i + 1
                if inner_i < chunk_len and chunk[inner_i] == ']':
                    inner_i = inner_i + 1
                if inner_i < chunk_len and chunk[inner_i] != ']':
                    inner_i = inner_i + 1
                    if inner_i < chunk_len and chunk[inner_i] != ']':
                        continue
                if inner_i >= chunk_len:
                    pat += re.escape(char)
                else:
                    inner = chunk[i + 1:inner_i]
                    char_class = ''
                    if inner[0] == '!':
                        char_class = '^'
                        inner = inner[1:]
                    char_class += re.escape(inner)
                    pat += f'''[{char_class}]'''
                    i = inner_i
            else:
                pat += re.escape(char)
            i += 1
            if i < chunk_len:
                continue
        if last_chunk:
            continue
        pat += sep
    pat += '\\Z'
    return re.compile(pat, flags = re.MULTILINE | re.DOTALL)


class InfoCommon:
    tag_build = None
    tag_date = None
    name = (lambda self: _normalization.safe_name(self.distribution.get_name()))()
    
    def tagged_version(self):
        tagged = self._maybe_tag(self.distribution.get_version())
        return _normalization.safe_version(tagged)

    
    def _maybe_tag(self, version):
        '''
        egg_info may be called more than once for a distribution,
        in which case the version string already contains all tags.
        '''
        if self.vtags and self._already_tagged(version):
            return version
        return None + self.vtags

    
    def _already_tagged(self = None, version = None):
        if not version.endswith(self.vtags):
            version.endswith(self.vtags)
        return version.endswith(self._safe_tags())

    
    def _safe_tags(self = None):
        
        try:
            return _normalization.safe_version(f'''0{self.vtags}''')[1:]
        except packaging.version.InvalidVersion:
            return 


    
    def tags(self = None):
        version = ''
        if self.tag_build:
            version += self.tag_build
        if self.tag_date:
            version += time.strftime('%Y%m%d')
        return version

    vtags = property(tags)


class egg_info(Command, InfoCommon):
    description = "create a distribution's .egg-info directory"
    user_options = [
        ('egg-base=', 'e', 'directory containing .egg-info directories [default: top of the source tree]'),
        ('tag-date', 'd', 'Add date stamp (e.g. 20050528) to version number'),
        ('tag-build=', 'b', 'Specify explicit tag to add to version number'),
        ('no-date', 'D', "Don't include date stamp [default]")]
    boolean_options = [
        'tag-date']
    negative_opt = {
        'no-date': 'tag-date' }
    
    def initialize_options(self):
        self.egg_base = None
        self.egg_name = None
        self.egg_info = None
        self.egg_version = None
        self.ignore_egg_info_in_manifest = False

    tag_svn_revision = (lambda self = None: pass)()
    tag_svn_revision = (lambda self, value: pass)()
    
    def save_version_info(self = None, filename = None):
        '''
        Materialize the value of date into the
        build tag. Install build keys in a deterministic order
        to avoid arbitrary reordering on subsequent builds.
        '''
        egg_info = dict(tag_build = self.tags(), tag_date = 0)
        edit_config(filename, dict(egg_info = egg_info))

    
    def finalize_options(self = None):
        self.egg_name = self.name
        self.egg_version = self.tagged_version()
        parsed_version = packaging.version.Version(self.egg_version)
    # WARNING: Decompyle incomplete

    
    def _get_egg_basename(self, py_version, platform = (PY_MAJOR, None)):
        '''Compute filename of the output egg. Private API.'''
        return _egg_basename(self.egg_name, self.egg_version, py_version, platform)

    
    def write_or_delete_file(self = None, what = None, filename = None, data = (False,), force = ('force', bool, 'return', None)):
        '''Write `data` to `filename` or delete if empty

        If `data` is non-empty, this routine is the same as ``write_file()``.
        If `data` is empty but not ``None``, this is the same as calling
        ``delete_file(filename)`.  If `data` is ``None``, then this is a no-op
        unless `filename` exists, in which case a warning is issued about the
        orphaned file (if `force` is false), or deleted (if `force` is true).
        '''
        if data:
            self.write_file(what, filename, data)
            return None
    # WARNING: Decompyle incomplete

    
    def write_file(self = None, what = None, filename = None, data = ('return', None)):
        '''Write `data` to `filename` (if not a dry run) after announcing it

        `what` is used in a log message to identify what is being written
        to the file.
        '''
        log.info('writing %s to %s', what, filename)
        data = data.encode('utf-8')
        if not self.dry_run:
            f = open(filename, 'wb')
            f.write(data)
            f.close()
            return None

    
    def delete_file(self = None, filename = None):
        '''Delete `filename` (if not a dry run) after announcing it'''
        log.info('deleting %s', filename)
        if not self.dry_run:
            os.unlink(filename)
            return None

    
    def run(self = None):
        writers = list(metadata.entry_points(group = 'egg_info.writers'))
        self.mkpath(self.egg_info)
        
        try:
            os.utime(self.egg_info, None)
            for ep in writers:
                writer = ep.load()
                writer(self, ep.name, os.path.join(self.egg_info, ep.name))
            nl = os.path.join(self.egg_info, 'native_libs.txt')
            if os.path.exists(nl):
                self.delete_file(nl)
            self.find_sources()
            return None
        except OSError:
            e = None
            msg = f'''Cannot update time stamp of directory \'{self.egg_info}\''''
            raise distutils.errors.DistutilsFileError(msg), e
            e = None
            del e


    
    def find_sources(self = None):
        '''Generate SOURCES.txt manifest file'''
        manifest_filename = os.path.join(self.egg_info, 'SOURCES.txt')
        mm = manifest_maker(self.distribution)
        mm.ignore_egg_info_dir = self.ignore_egg_info_in_manifest
        mm.manifest = manifest_filename
        mm.run()
        self.filelist = mm.filelist



class FileList(_FileList):
    pass
# WARNING: Decompyle incomplete


class manifest_maker(sdist):
    template = 'MANIFEST.in'
    
    def initialize_options(self = None):
        self.use_defaults = True
        self.prune = True
        self.manifest_only = True
        self.force_manifest = True
        self.ignore_egg_info_dir = False

    
    def finalize_options(self = None):
        pass

    
    def run(self = None):
        self.filelist = FileList(ignore_egg_info_dir = self.ignore_egg_info_dir)
        if not os.path.exists(self.manifest):
            self.write_manifest()
        self.add_defaults()
        if os.path.exists(self.template):
            self.read_template()
        self.add_license_files()
        self._add_referenced_files()
        self.prune_file_list()
        self.filelist.sort()
        self.filelist.remove_duplicates()
        self.write_manifest()

    
    def _manifest_normalize(self, path):
        path = unicode_utils.filesys_decode(path)
        return path.replace(os.sep, '/')

    
    def write_manifest(self = None):
        """
        Write the file list in 'self.filelist' to the manifest file
        named by 'self.manifest'.
        """
        self.filelist._repair()
    # WARNING: Decompyle incomplete

    
    def warn(self = None, msg = None):
        if not self._should_suppress_warning(msg):
            sdist.warn(self, msg)
            return None

    _should_suppress_warning = (lambda msg: re.match('standard file .*not found', msg))()
    
    def add_defaults(self = None):
        sdist.add_defaults(self)
        self.filelist.append(self.template)
        self.filelist.append(self.manifest)
        rcfiles = list(walk_revctrl())
        if rcfiles:
            self.filelist.extend(rcfiles)
        elif os.path.exists(self.manifest):
            self.read_manifest()
        if os.path.exists('setup.py'):
            self.filelist.append('setup.py')
        ei_cmd = self.get_finalized_command('egg_info')
        self.filelist.graft(ei_cmd.egg_info)

    
    def add_license_files(self = None):
        if not self.distribution.metadata.license_files:
            self.distribution.metadata.license_files
        license_files = []
        for lf in license_files:
            log.info("adding license file '%s'", lf)
        self.filelist.extend(license_files)

    
    def _add_referenced_files(self):
        '''Add files referenced by the config (e.g. `file:` directive) to filelist'''
        referenced = getattr(self.distribution, '_referenced_files', [])
        for rf in referenced:
            log.debug("adding file referenced by config '%s'", rf)
        self.filelist.extend(referenced)

    
    def _safe_data_files(self, build_py):
        '''
        The parent class implementation of this method
        (``sdist``) will try to include data files, which
        might cause recursion problems when
        ``include_package_data=True``.

        Therefore, avoid triggering any attempt of
        analyzing/building the manifest again.
        '''
        if hasattr(build_py, 'get_data_files_without_manifest'):
            return build_py.get_data_files_without_manifest()
        None.emit("`build_py` command does not inherit from setuptools' `build_py`.", "\n            Custom 'build_py' does not implement 'get_data_files_without_manifest'.\n            Please extend command classes from setuptools instead of distutils.\n            ", see_url = 'https://peps.python.org/pep-0632/')
        return build_py.get_data_files()



def write_file(filename = None, contents = None):
    """Create a file with the specified name and write 'contents' (a
    sequence of strings without line terminators) to it.
    """
    contents = '\n'.join(contents)
    contents = contents.encode('utf-8')
    f = open(filename, 'wb')
    f.write(contents)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def write_pkg_info(cmd = None, basename = None, filename = None):
    log.info('writing %s', filename)
    if not cmd.dry_run:
        metadata = cmd.distribution.metadata
        metadata.version, oldver = cmd.egg_version, metadata.version
        metadata.name, oldname = cmd.egg_name, metadata.name
        
        try:
            metadata.write_pkg_info(cmd.egg_info)
            metadata.name, metadata.version = oldname, oldver
            safe = getattr(cmd.distribution, 'zip_safe', None)
            bdist_egg.write_safety_flag(cmd.egg_info, safe)
            return None
            return None
        except:
            metadata.name, metadata.version = oldname, oldver



def warn_depends_obsolete(cmd = None, basename = None, filename = None):
    '''
    Unused: left to avoid errors when updating (from source) from <= 67.8.
    Old installations have a .dist-info directory with the entry-point
    ``depends.txt = setuptools.command.egg_info:warn_depends_obsolete``.
    This may trigger errors when running the first egg_info in build_meta.
    TODO: Remove this function in a version sufficiently > 68.
    '''
    pass

write_requirements = _requirestxt.write_requirements
write_setup_requirements = _requirestxt.write_setup_requirements

def write_toplevel_names(cmd = None, basename = None, filename = None):
    pass
# WARNING: Decompyle incomplete


def overwrite_arg(cmd = None, basename = None, filename = None):
    write_arg(cmd, basename, filename, True)


def write_arg(cmd = None, basename = None, filename = None, force = (False,)):
    argname = os.path.splitext(basename)[0]
    value = getattr(cmd.distribution, argname, None)
# WARNING: Decompyle incomplete


def write_entries(cmd = None, basename = None, filename = None):
    eps = _entry_points.load(cmd.distribution.entry_points)
    defn = _entry_points.render(eps)
    cmd.write_or_delete_file('entry points', filename, defn, True)


def _egg_basename(egg_name, egg_version, py_version, platform = (None, None)):
    '''Compute filename of the output egg. Private API.'''
    name = _normalization.filename_component(egg_name)
    version = _normalization.filename_component(egg_version)
    if not py_version:
        py_version
    egg = f'''{name}-{version}-py{PY_MAJOR}'''
    if platform:
        egg += f'''-{platform}'''
    return egg


class EggInfoDeprecationWarning(SetuptoolsDeprecationWarning):
    '''Deprecated behavior warning for EggInfo, bypassing suppression.'''
    pass

