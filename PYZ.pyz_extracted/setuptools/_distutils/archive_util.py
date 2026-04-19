# Source Generated with Decompyle++
# File: archive_util.pyc (Python 3.12)

'''distutils.archive_util

Utility functions for creating archive files (tarballs, zip files,
that sort of thing).'''
from __future__ import annotations
import os
from typing import Literal, overload

try:
    import zipfile
    from _log import log
    from dir_util import mkpath
    from errors import DistutilsExecError
    from spawn import spawn
    
    try:
        from pwd import getpwnam
        
        try:
            from grp import getgrnam
            
            def _get_gid(name):
                '''Returns a gid, given a group name.'''
                pass
            # WARNING: Decompyle incomplete

            
            def _get_uid(name):
                '''Returns an uid, given a user name.'''
                pass
            # WARNING: Decompyle incomplete

            
            def make_tarball(base_name, base_dir, compress = None, verbose = None, dry_run = None, owner = ('gzip', False, False, None, None), group = ('base_name', 'str', 'base_dir', 'str | os.PathLike[str]', 'compress', "Literal['gzip', 'bzip2', 'xz'] | None", 'verbose', 'bool', 'dry_run', 'bool', 'owner', 'str | None', 'group', 'str | None', 'return', 'str')):
                '''Create a (possibly compressed) tar file from all the files under
    \'base_dir\'.

    \'compress\' must be "gzip" (the default), "bzip2", "xz", or None.

    \'owner\' and \'group\' can be used to define an owner and a group for the
    archive that is being built. If not provided, the current owner and group
    will be used.

    The output tar file will be named \'base_dir\' +  ".tar", possibly plus
    the appropriate compression extension (".gz", ".bz2", ".xz" or ".Z").

    Returns the output filename.
    '''
                pass
            # WARNING: Decompyle incomplete

            
            def make_zipfile(base_name = None, base_dir = None, verbose = None, dry_run = (False, False)):
                '''Create a zip file from all the files under \'base_dir\'.

    The output zip file will be named \'base_name\' + ".zip".  Uses either the
    "zipfile" Python module (if available) or the InfoZIP "zip" utility
    (if installed and found on the default search path).  If neither tool is
    available, raises DistutilsExecError.  Returns the name of the output zip
    file.
    '''
                zip_filename = base_name + '.zip'
                mkpath(os.path.dirname(zip_filename), dry_run = dry_run)
            # WARNING: Decompyle incomplete

            ARCHIVE_FORMATS = {
                'gztar': (make_tarball, [
                    ('compress', 'gzip')], "gzip'ed tar-file"),
                'bztar': (make_tarball, [
                    ('compress', 'bzip2')], "bzip2'ed tar-file"),
                'xztar': (make_tarball, [
                    ('compress', 'xz')], "xz'ed tar-file"),
                'ztar': (make_tarball, [
                    ('compress', 'compress')], 'compressed tar file'),
                'tar': (make_tarball, [
                    ('compress', None)], 'uncompressed tar file'),
                'zip': (make_zipfile, [], 'ZIP file') }
            
            def check_archive_formats(formats):
                """Returns the first format from the 'format' list that is unknown.

    If all formats are known, returns None
    """
                for format in formats:
                    if not format not in ARCHIVE_FORMATS:
                        continue
                    
                    return formats, format

            make_archive = (lambda base_name, format, root_dir, base_dir = None, verbose = None, dry_run = overload, owner = (None, None, False, False, None, None), group = ('base_name', 'str', 'format', 'str', 'root_dir', 'str | os.PathLike[str] | bytes | os.PathLike[bytes] | None', 'base_dir', 'str | None', 'verbose', 'bool', 'dry_run', 'bool', 'owner', 'str | None', 'group', 'str | None', 'return', 'str'): pass)()
            make_archive = (lambda base_name, format, root_dir, base_dir = None, verbose = None, dry_run = overload, owner = (None, False, False, None, None), group = ('base_name', 'str | os.PathLike[str]', 'format', 'str', 'root_dir', 'str | os.PathLike[str] | bytes | os.PathLike[bytes]', 'base_dir', 'str | None', 'verbose', 'bool', 'dry_run', 'bool', 'owner', 'str | None', 'group', 'str | None', 'return', 'str'): pass)()
            
            def make_archive(base_name, format, root_dir, base_dir = None, verbose = None, dry_run = None, owner = (None, None, False, False, None, None), group = ('base_name', 'str | os.PathLike[str]', 'format', 'str', 'root_dir', 'str | os.PathLike[str] | bytes | os.PathLike[bytes] | None', 'base_dir', 'str | None', 'verbose', 'bool', 'dry_run', 'bool', 'owner', 'str | None', 'group', 'str | None', 'return', 'str')):
                '''Create an archive file (eg. zip or tar).

    \'base_name\' is the name of the file to create, minus any format-specific
    extension; \'format\' is the archive format: one of "zip", "tar", "gztar",
    "bztar", "xztar", or "ztar".

    \'root_dir\' is a directory that will be the root directory of the
    archive; ie. we typically chdir into \'root_dir\' before creating the
    archive.  \'base_dir\' is the directory where we start archiving from;
    ie. \'base_dir\' will be the common prefix of all files and
    directories in the archive.  \'root_dir\' and \'base_dir\' both default
    to the current directory.  Returns the name of the archive file.

    \'owner\' and \'group\' are used when creating a tar archive. By default,
    uses the current owner and group.
    '''
                save_cwd = os.getcwd()
            # WARNING: Decompyle incomplete

            return None
            except ImportError:
                zipfile = None
                continue
            except ImportError:
                getpwnam = None
                continue
        except ImportError:
            getgrnam = None
            continue



