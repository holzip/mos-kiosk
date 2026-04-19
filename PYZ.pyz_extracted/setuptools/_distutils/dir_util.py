# Source Generated with Decompyle++
# File: dir_util.pyc (Python 3.12)

'''distutils.dir_util

Utility functions for manipulating directories and directory trees.'''
import functools
import itertools
import os
import pathlib
from  import file_util
from _log import log
from errors import DistutilsFileError, DistutilsInternalError

class SkipRepeatAbsolutePaths(set):
    pass
# WARNING: Decompyle incomplete

wrapper = SkipRepeatAbsolutePaths().wrap
mkpath = (lambda name = None, mode = functools.singledispatch, verbose = wrapper, dry_run = (511, True, False): if not verbose and name.is_dir():
log.info('creating %s', name)try:
if not dry_run:
dry_runname.mkdir(mode = mode, parents = True, exist_ok = True)Nonetry:
Noneexcept OSError:
exc = Noneraise DistutilsFileError(f'''could not create \'{name}\': {exc.args[-1]}''')exc = Nonedel exc)()()
_ = (lambda name = None: pass# WARNING: Decompyle incomplete
)()
_ = (lambda name = None: raise DistutilsInternalError(f'''mkpath: \'name\' must be a string (got {name!r})'''))()

def create_tree(base_dir, files, mode, verbose, dry_run = (511, True, False)):
    """Create all the empty directories under 'base_dir' needed to put 'files'
    there.

    'base_dir' is just the name of a directory which doesn't necessarily
    exist yet; 'files' is a list of filenames to be interpreted relative to
    'base_dir'.  'base_dir' + the directory portion of every file in 'files'
    will be created if it doesn't already exist.  'mode', 'verbose' and
    'dry_run' flags are as for 'mkpath()'.
    """
    pass
# WARNING: Decompyle incomplete


def copy_tree(src, dst, preserve_mode, preserve_times, preserve_symlinks, update, verbose, dry_run = (True, True, False, False, True, False)):
    """Copy an entire directory tree 'src' to a new location 'dst'.

    Both 'src' and 'dst' must be directory names.  If 'src' is not a
    directory, raise DistutilsFileError.  If 'dst' does not exist, it is
    created with 'mkpath()'.  The end result of the copy is that every
    file in 'src' is copied to 'dst', and directories under 'src' are
    recursively copied to 'dst'.  Return the list of files that were
    copied or might have been copied, using their output name.  The
    return value is unaffected by 'update' or 'dry_run': it is simply
    the list of all files under 'src', with the names changed to be
    under 'dst'.

    'preserve_mode' and 'preserve_times' are the same as for
    'copy_file'; note that they only apply to regular files, not to
    directories.  If 'preserve_symlinks' is true, symlinks will be
    copied as symlinks (on platforms that support them!); otherwise
    (the default), the destination of the symlink will be copied.
    'update' and 'verbose' are the same as for 'copy_file'.
    """
    if not dry_run and os.path.isdir(src):
        raise DistutilsFileError(f'''cannot copy tree \'{src}\': not a directory''')
    
    try:
        names = os.listdir(src)
        if not dry_run:
            mkpath(dst, verbose = verbose)
        copy_one = functools.partial(_copy_one, src = src, dst = dst, preserve_symlinks = preserve_symlinks, verbose = verbose, dry_run = dry_run, preserve_mode = preserve_mode, preserve_times = preserve_times, update = update)
        return list(itertools.chain.from_iterable(map(copy_one, names)))
    except OSError:
        e = None
        if dry_run:
            names = []
        else:
            raise DistutilsFileError(f'''error listing files in \'{src}\': {e.strerror}''')
        e = None
        del e
        continue
        e = None
        del e



def _copy_one(name, *, src, dst, preserve_symlinks, verbose, dry_run, preserve_mode, preserve_times, update):
    pass
# WARNING: Decompyle incomplete


def _build_cmdtuple(path, cmdtuples):
    '''Helper for remove_tree().'''
    for f in os.listdir(path):
        real_f = os.path.join(path, f)
        if not os.path.isdir(real_f) and os.path.islink(real_f):
            _build_cmdtuple(real_f, cmdtuples)
            continue
        cmdtuples.append((os.remove, real_f))
    cmdtuples.append((os.rmdir, path))


def remove_tree(directory, verbose, dry_run = (True, False)):
    """Recursively remove an entire directory tree.

    Any errors are ignored (apart from being reported to stdout if 'verbose'
    is true).
    """
    if verbose >= 1:
        log.info("removing '%s' (and everything under it)", directory)
    if dry_run:
        return None
    cmdtuples = []
    _build_cmdtuple(directory, cmdtuples)
    for cmd in cmdtuples:
        cmd[0](cmd[1])
        SkipRepeatAbsolutePaths.clear()
    return None
    except OSError:
        exc = None
        log.warning('error removing %s: %s', directory, exc)
        exc = None
        del exc
        continue
        exc = None
        del exc


def ensure_relative(path):
    """Take the full path 'path', and make it a relative path.

    This is useful to make 'path' the second argument to os.path.join().
    """
    (drive, path) = os.path.splitdrive(path)
    if path[0:1] == os.sep:
        path = drive + path[1:]
    return path

