# Source Generated with Decompyle++
# File: convert.pyc (Python 3.12)

from __future__ import annotations
import os.path as os
import re
import shutil
import tempfile
import zipfile
from glob import iglob
from bdist_wheel import bdist_wheel
from wheelfile import WheelFile
from  import WheelError

try:
    from setuptools import Distribution
    egg_info_re = re.compile('\n    (?P<name>.+?)-(?P<ver>.+?)\n    (-(?P<pyver>py\\d\\.\\d+)\n     (-(?P<arch>.+?))?\n    )?.egg$', re.VERBOSE)
    
    class _bdist_wheel_tag(bdist_wheel):
        full_tag_supplied = False
        full_tag = None
        
        def get_tag(self):
            pass
        # WARNING: Decompyle incomplete


    
    def egg2wheel(egg_path = None, dest_dir = None):
        filename = os.path.basename(egg_path)
        match = egg_info_re.match(filename)
        if not match:
            raise WheelError(f'''Invalid egg file name: {filename}''')
        egg_info = match.groupdict()
        dir = tempfile.mkdtemp(suffix = '_e2w')
        if os.path.isfile(egg_path):
            egg = zipfile.ZipFile(egg_path)
            egg.extractall(dir)
            None(None, None)
        else:
            for pth in os.listdir(egg_path):
                src = os.path.join(egg_path, pth)
                if os.path.isfile(src):
                    shutil.copy2(src, dir)
                    continue
                shutil.copytree(src, os.path.join(dir, pth))
        pyver = egg_info['pyver']
        if pyver:
            pyver = pyver.replace('.', '')
            egg_info['pyver'] = pyver.replace('.', '')
        if not egg_info['arch']:
            egg_info['arch']
        arch = 'any'.replace('.', '_').replace('-', '_')
        abi = 'cp' + pyver[2:] if arch != 'any' else 'none'
        root_is_purelib = egg_info['arch'] is None
        if root_is_purelib:
            bw = bdist_wheel(Distribution())
        else:
            bw = _bdist_wheel_tag(Distribution())
        bw.root_is_pure = root_is_purelib
        bw.python_tag = pyver
        bw.plat_name_supplied = True
        if not egg_info['arch']:
            egg_info['arch']
        bw.plat_name = 'any'
        if not root_is_purelib:
            bw.full_tag_supplied = True
            bw.full_tag = (pyver, abi, arch)
    # WARNING: Decompyle incomplete

    
    def parse_wininst_info(wininfo_name, egginfo_name):
        """Extract metadata from filenames.

    Extracts the 4 metadataitems needed (name, version, pyversion, arch) from
    the installer filename and the name of the egg-info directory embedded in
    the zipfile (if any).

    The egginfo filename has the format::

        name-ver(-pyver)(-arch).egg-info

    The installer filename has the format::

        name-ver.arch(-pyver).exe

    Some things to note:

    1. The installer filename is not definitive. An installer can be renamed
       and work perfectly well as an installer. So more reliable data should
       be used whenever possible.
    2. The egg-info data should be preferred for the name and version, because
       these come straight from the distutils metadata, and are mandatory.
    3. The pyver from the egg-info data should be ignored, as it is
       constructed from the version of Python used to build the installer,
       which is irrelevant - the installer filename is correct here (even to
       the point that when it's not there, any version is implied).
    4. The architecture must be taken from the installer filename, as it is
       not included in the egg-info data.
    5. Architecture-neutral installers still have an architecture because the
       installer format itself (being executable) is architecture-specific. We
       should therefore ignore the architecture if the content is pure-python.
    """
        egginfo = None
        if egginfo_name:
            egginfo = egg_info_re.search(egginfo_name)
            if not egginfo:
                raise ValueError(f'''Egg info filename {egginfo_name} is not valid''')
        (w_name, sep, rest) = wininfo_name.partition('-')
        if not sep:
            raise ValueError(f'''Installer filename {wininfo_name} is not valid''')
        rest = rest[:-4]
        (rest2, sep, w_pyver) = rest.rpartition('-')
        if sep and w_pyver.startswith('py'):
            rest = rest2
            w_pyver = w_pyver.replace('.', '')
        else:
            w_pyver = 'py2.py3'
        (w_ver, sep, w_arch) = rest.rpartition('.')
        if not sep:
            raise ValueError(f'''Installer filename {wininfo_name} is not valid''')
        if egginfo:
            w_name = egginfo.group('name')
            w_ver = egginfo.group('ver')
        return {
            'name': w_name,
            'ver': w_ver,
            'arch': w_arch,
            'pyver': w_pyver }

    
    def wininst2wheel(path, dest_dir):
        bdw = zipfile.ZipFile(path)
        egginfo_name = None
        for filename in bdw.namelist():
            if not '.egg-info' in filename:
                continue
            egginfo_name = filename
            bdw.namelist()
        info = parse_wininst_info(os.path.basename(path), egginfo_name)
        root_is_purelib = True
        for zipinfo in bdw.infolist():
            if not zipinfo.filename.startswith('PLATLIB'):
                continue
            root_is_purelib = False
            bdw.infolist()
        if root_is_purelib:
            paths = {
                'purelib': '' }
        else:
            paths = {
                'platlib': '' }
    # WARNING: Decompyle incomplete

    
    def convert(files, dest_dir, verbose):
        for pat in files:
            for installer in iglob(pat):
                if verbose:
                    print(f'''{installer}... ''', flush = True)
                conv(installer, dest_dir)
                if not verbose:
                    continue
                print('OK')

    return None
except ImportError:
    from distutils.dist import Distribution
    continue

