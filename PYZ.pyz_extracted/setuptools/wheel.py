# Source Generated with Decompyle++
# File: wheel.pyc (Python 3.12)

'''Wheels support.'''
import contextlib
import email
import functools
import itertools
import os
import posixpath
import re
import zipfile
from packaging.tags import sys_tags
from packaging.utils import canonicalize_name
from packaging.version import Version as parse_version
import setuptools
from setuptools.archive_util import _unpack_zipfile_obj
from setuptools.command.egg_info import _egg_basename, write_requirements
from unicode_utils import _read_utf8_with_fallback
from distutils.util import get_platform
WHEEL_NAME = re.compile('^(?P<project_name>.+?)-(?P<version>\\d.*?)\n    ((-(?P<build>\\d.*?))?-(?P<py_version>.+?)-(?P<abi>.+?)-(?P<platform>.+?)\n    )\\.whl$', re.VERBOSE).match
NAMESPACE_PACKAGE_INIT = "__import__('pkg_resources').declare_namespace(__name__)\n"
_get_supported_tags = (lambda : pass# WARNING: Decompyle incomplete
)()

def unpack(src_dir = None, dst_dir = None):
    '''Move everything under `src_dir` to `dst_dir`, and delete the former.'''
    for dirpath, dirnames, filenames in os.walk(src_dir):
        subdir = os.path.relpath(dirpath, src_dir)
        for f in filenames:
            src = os.path.join(dirpath, f)
            dst = os.path.join(dst_dir, subdir, f)
            os.renames(src, dst)
        for n, d in reversed(list(enumerate(dirnames))):
            src = os.path.join(dirpath, d)
            dst = os.path.join(dst_dir, subdir, d)
            if os.path.exists(dst):
                continue
            os.renames(src, dst)
            del dirnames[n]
# WARNING: Decompyle incomplete

disable_info_traces = (lambda : pass# WARNING: Decompyle incomplete
)()

class Wheel:
    
    def __init__(self = None, filename = None):
        match = WHEEL_NAME(os.path.basename(filename))
    # WARNING: Decompyle incomplete

    
    def tags(self):
        '''List tags (py_version, abi, platform) supported by this wheel.'''
        return itertools.product(self.py_version.split('.'), self.abi.split('.'), self.platform.split('.'))

    
    def is_compatible(self):
        '''Is the wheel compatible with the current platform?'''
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.tags()(), False)

    
    def egg_name(self):
        return _egg_basename(self.project_name, self.version, platform = None if self.platform == 'any' else get_platform()) + '.egg'

    
    def get_dist_info(self, zf):
        for member in zf.namelist():
            dirname = posixpath.dirname(member)
            if not dirname.endswith('.dist-info'):
                continue
            if not canonicalize_name(dirname).startswith(canonicalize_name(self.project_name)):
                continue
            
            return zf.namelist(), dirname
        raise ValueError('unsupported wheel format. .dist-info not found')

    
    def install_as_egg(self = None, destination_eggdir = None):
        '''Install wheel as an egg directory.'''
        zf = zipfile.ZipFile(self.filename)
        self._install_as_egg(destination_eggdir, zf)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _install_as_egg(self, destination_eggdir, zf):
        dist_basename = f'''{self.project_name}-{self.version}'''
        dist_info = self.get_dist_info(zf)
        dist_data = f'''{dist_basename}.data'''
        egg_info = os.path.join(destination_eggdir, 'EGG-INFO')
        self._convert_metadata(zf, destination_eggdir, dist_info, egg_info)
        self._move_data_entries(destination_eggdir, dist_data)
        self._fix_namespace_packages(egg_info, destination_eggdir)

    _convert_metadata = (lambda zf, destination_eggdir, dist_info, egg_info: pass# WARNING: Decompyle incomplete
)()
    _move_data_entries = (lambda destination_eggdir, dist_data: pass# WARNING: Decompyle incomplete
)()
    _fix_namespace_packages = (lambda egg_info, destination_eggdir: namespace_packages = os.path.join(egg_info, 'namespace_packages.txt')# WARNING: Decompyle incomplete
)()

