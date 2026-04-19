# Source Generated with Decompyle++
# File: archive_util.pyc (Python 3.12)

'''Utilities for extracting common archive formats'''
import contextlib
import os
import posixpath
import shutil
import tarfile
import zipfile
from _path import ensure_directory
from distutils.errors import DistutilsError
__all__ = [
    'unpack_archive',
    'unpack_zipfile',
    'unpack_tarfile',
    'default_filter',
    'UnrecognizedFormat',
    'extraction_drivers',
    'unpack_directory']

class UnrecognizedFormat(DistutilsError):
    """Couldn't recognize the archive type"""
    pass


def default_filter(src, dst):
    '''The default progress/filter callback; returns True for all files'''
    return dst


def unpack_archive(filename = None, extract_dir = None, progress_filter = None, drivers = (default_filter, None)):
    """Unpack `filename` to `extract_dir`, or raise ``UnrecognizedFormat``

    `progress_filter` is a function taking two arguments: a source path
    internal to the archive ('/'-separated), and a filesystem path where it
    will be extracted.  The callback must return the desired extract path
    (which may be the same as the one passed in), or else ``None`` to skip
    that file or directory.  The callback can thus be used to report on the
    progress of the extraction, as well as to filter the items extracted or
    alter their extraction paths.

    `drivers`, if supplied, must be a non-empty sequence of functions with the
    same signature as this function (minus the `drivers` argument), that raise
    ``UnrecognizedFormat`` if they do not support extracting the designated
    archive type.  The `drivers` are tried in sequence until one is found that
    does not raise an error, or until all are exhausted (in which case
    ``UnrecognizedFormat`` is raised).  If you do not supply a sequence of
    drivers, the module's ``extraction_drivers`` constant will be used, which
    means that ``unpack_zipfile`` and ``unpack_tarfile`` will be tried, in that
    order.
    """
    if not drivers:
        drivers
    for driver in extraction_drivers:
        driver(filename, extract_dir, progress_filter)
        extraction_drivers
        return None
    raise UnrecognizedFormat(f'''Not a recognized archive type: {filename}''')
    except UnrecognizedFormat:
        continue


def unpack_directory(filename = None, extract_dir = None, progress_filter = None):
    ''' "Unpack" a directory, using the same interface as for archives

    Raises ``UnrecognizedFormat`` if `filename` is not a directory
    '''
    if not os.path.isdir(filename):
        raise UnrecognizedFormat(f'''{filename} is not a directory''')
    paths = {
        filename: ('', extract_dir) }
    for base, dirs, files in os.walk(filename):
        (src, dst) = paths[base]
        for d in dirs:
            paths[os.path.join(base, d)] = (src + d + '/', os.path.join(dst, d))
        for f in files:
            target = os.path.join(dst, f)
            target = progress_filter(src + f, target)
            if not target:
                continue
            ensure_directory(target)
            f = os.path.join(base, f)
            shutil.copyfile(f, target)
            shutil.copystat(f, target)


def unpack_zipfile(filename = None, extract_dir = None, progress_filter = None):
    '''Unpack zip `filename` to `extract_dir`

    Raises ``UnrecognizedFormat`` if `filename` is not a zipfile (as determined
    by ``zipfile.is_zipfile()``).  See ``unpack_archive()`` for an explanation
    of the `progress_filter` argument.
    '''
    if not zipfile.is_zipfile(filename):
        raise UnrecognizedFormat(f'''{filename} is not a zip file''')
    z = zipfile.ZipFile(filename)
    _unpack_zipfile_obj(z, extract_dir, progress_filter)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def _unpack_zipfile_obj(zipfile_obj, extract_dir, progress_filter = (default_filter,)):
    '''Internal/private API used by other parts of setuptools.
    Similar to ``unpack_zipfile``, but receives an already opened :obj:`zipfile.ZipFile`
    object instead of a filename.
    '''
    pass
# WARNING: Decompyle incomplete


def _resolve_tar_file_or_dir(tar_obj, tar_member_obj):
    '''Resolve any links and extract link targets as normal files.'''
    pass
# WARNING: Decompyle incomplete


def _iter_open_tar(tar_obj, extract_dir, progress_filter):
    '''Emit member-destination pairs from a tar archive.'''
    pass
# WARNING: Decompyle incomplete


def unpack_tarfile(filename = None, extract_dir = None, progress_filter = None):
    '''Unpack tar/tar.gz/tar.bz2 `filename` to `extract_dir`

    Raises ``UnrecognizedFormat`` if `filename` is not a tarfile (as determined
    by ``tarfile.open()``).  See ``unpack_archive()`` for an explanation
    of the `progress_filter` argument.
    '''
    
    try:
        tarobj = tarfile.open(filename)
        for member, final_dst in _iter_open_tar(tarobj, extract_dir, progress_filter):
            tarobj._extract_member(member, final_dst)
        return True
    except tarfile.TarError:
        e = None
        raise UnrecognizedFormat(f'''{filename} is not a compressed or uncompressed tar file'''), e
        e = None
        del e
        except tarfile.ExtractError:
            continue


extraction_drivers = (unpack_directory, unpack_zipfile, unpack_tarfile)
