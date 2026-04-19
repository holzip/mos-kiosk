# Source Generated with Decompyle++
# File: wheelfile.pyc (Python 3.12)

from __future__ import annotations
import csv
import hashlib
import os.path as os
import re
import stat
import time
from io import StringIO, TextIOWrapper
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
from wheel.cli import WheelError
from wheel.util import log, urlsafe_b64decode, urlsafe_b64encode
WHEEL_INFO_RE = re.compile('^(?P<namever>(?P<name>[^\\s-]+?)-(?P<ver>[^\\s-]+?))(-(?P<build>\\d[^\\s-]*))?\n     -(?P<pyver>[^\\s-]+?)-(?P<abi>[^\\s-]+?)-(?P<plat>\\S+)\\.whl$', re.VERBOSE)
MINIMUM_TIMESTAMP = 315532800

def get_zipinfo_datetime(timestamp = (None,)):
    if not timestamp:
        timestamp
    timestamp = int(os.environ.get('SOURCE_DATE_EPOCH', time.time()))
    timestamp = max(timestamp, MINIMUM_TIMESTAMP)
    return time.gmtime(timestamp)[0:6]


class WheelFile(ZipFile):
    '''A ZipFile derivative class that also reads SHA-256 hashes from
    .dist-info/RECORD and checks any read files against those.
    '''
    _default_algorithm = hashlib.sha256
    
    def __init__(self, file, mode, compression = ('r', ZIP_DEFLATED)):
        basename = os.path.basename(file)
        self.parsed_filename = WHEEL_INFO_RE.match(basename)
    # WARNING: Decompyle incomplete

    
    def open(self, name_or_info, mode, pwd = ('r', None)):
        pass
    # WARNING: Decompyle incomplete

    
    def write_files(self, base_dir):
        log.info(f'''creating \'{self.filename}\' and adding \'{base_dir}\' to it''')
        deferred = []
        for root, dirnames, filenames in os.walk(base_dir):
            dirnames.sort()
            for name in sorted(filenames):
                path = os.path.normpath(os.path.join(root, name))
                if not os.path.isfile(path):
                    continue
                arcname = os.path.relpath(path, base_dir).replace(os.path.sep, '/')
                if arcname == self.record_path:
                    continue
                if root.endswith('.dist-info'):
                    deferred.append((path, arcname))
                    continue
                self.write(path, arcname)
        deferred.sort()
        for path, arcname in deferred:
            self.write(path, arcname)

    
    def write(self, filename, arcname, compress_type = (None, None)):
        f = open(filename, 'rb')
        st = os.fstat(f.fileno())
        data = f.read()
        None(None, None)
        if not arcname:
            arcname
    # WARNING: Decompyle incomplete

    
    def writestr(self, zinfo_or_arcname, data, compress_type = (None,)):
        if isinstance(zinfo_or_arcname, str):
            zinfo_or_arcname = ZipInfo(zinfo_or_arcname, date_time = get_zipinfo_datetime())
            zinfo_or_arcname.compress_type = self.compression
            zinfo_or_arcname.external_attr = (436 | stat.S_IFREG) << 16
        if isinstance(data, str):
            data = data.encode('utf-8')
        ZipFile.writestr(self, zinfo_or_arcname, data, compress_type)
        fname = zinfo_or_arcname.filename if isinstance(zinfo_or_arcname, ZipInfo) else zinfo_or_arcname
        log.info(f'''adding \'{fname}\'''')
        if fname != self.record_path:
            hash_ = self._default_algorithm(data)
            self._file_hashes[fname] = (hash_.name, urlsafe_b64encode(hash_.digest()).decode('ascii'))
            self._file_sizes[fname] = len(data)
            return None

    
    def close(self):
        pass
    # WARNING: Decompyle incomplete


