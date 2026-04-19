# Source Generated with Decompyle++
# File: shutil.pyc (Python 3.12)

"""Utility functions for copying and archiving files and directory trees.

XXX The functions here don't copy the resource fork or other metadata on Mac.

"""
import os
import sys
import stat
import fnmatch
import collections
import errno
import warnings

try:
    import zlib
    del zlib
    _ZLIB_SUPPORTED = True
    
    try:
        import bz2
        del bz2
        _BZ2_SUPPORTED = True
        
        try:
            import lzma
            del lzma
            _LZMA_SUPPORTED = True
            _WINDOWS = os.name == 'nt'
            posix = None
            nt = None
            if os.name == 'posix':
                import posix
            elif _WINDOWS:
                import nt
            if sys.platform == 'win32':
                import _winapi
            else:
                _winapi = None
            COPY_BUFSIZE = 1048576 if _WINDOWS else 65536
            if hasattr(os, 'sendfile'):
                hasattr(os, 'sendfile')
            _USE_CP_SENDFILE = sys.platform.startswith('linux')
            if posix:
                posix
            _HAS_FCOPYFILE = hasattr(posix, '_fcopyfile')
            _WIN_DEFAULT_PATHEXT = '.COM;.EXE;.BAT;.CMD;.VBS;.JS;.WS;.MSC'
            __all__ = [
                'copyfileobj',
                'copyfile',
                'copymode',
                'copystat',
                'copy',
                'copy2',
                'copytree',
                'move',
                'rmtree',
                'Error',
                'SpecialFileError',
                'ExecError',
                'make_archive',
                'get_archive_formats',
                'register_archive_format',
                'unregister_archive_format',
                'get_unpack_formats',
                'register_unpack_format',
                'unregister_unpack_format',
                'unpack_archive',
                'ignore_patterns',
                'chown',
                'which',
                'get_terminal_size',
                'SameFileError']
            
            class Error(OSError):
                pass

            
            class SameFileError(Error):
                '''Raised when source and destination are the same file.'''
                pass

            
            class SpecialFileError(OSError):
                '''Raised when trying to do a kind of operation (e.g. copying) which is
    not supported on a special file (e.g. a named pipe)'''
                pass

            
            class ExecError(OSError):
                '''Raised when a command could not be executed'''
                pass

            
            class ReadError(OSError):
                '''Raised when an archive cannot be read'''
                pass

            
            class RegistryError(Exception):
                '''Raised when a registry operation with the archiving
    and unpacking registries fails'''
                pass

            
            class _GiveupOnFastCopy(Exception):
                '''Raised as a signal to fallback on using raw read()/write()
    file copy when fast-copy functions fail to do so.
    '''
                pass

            
            def _fastcopy_fcopyfile(fsrc, fdst, flags):
                '''Copy a regular file content or metadata by using high-performance
    fcopyfile(3) syscall (macOS).
    '''
                
                try:
                    infd = fsrc.fileno()
                    outfd = fdst.fileno()
                    
                    try:
                        posix._fcopyfile(infd, outfd, flags)
                        return None
                        except Exception:
                            err = None
                            raise _GiveupOnFastCopy(err)
                            err = None
                            del err
                    except OSError:
                        err = None
                        err.filename = fsrc.name
                        err.filename2 = fdst.name
                        if err.errno in {
                            errno.EINVAL,
                            errno.ENOTSUP}:
                            raise _GiveupOnFastCopy(err)
                        raise err, None
                        err = None
                        del err



            
            def _fastcopy_sendfile(fsrc, fdst):
                '''Copy data from one regular mmap-like fd to another by using
    high-performance sendfile(2) syscall.
    This should work on Linux >= 2.6.33 only.
    '''
                global _USE_CP_SENDFILE
                
                try:
                    infd = fsrc.fileno()
                    outfd = fdst.fileno()
                    
                    try:
                        blocksize = max(os.fstat(infd).st_size, 8388608)
                        if sys.maxsize < 0x100000000:
                            blocksize = min(blocksize, 1073741824)
                        offset = 0
                        
                        try:
                            sent = os.sendfile(outfd, infd, offset, blocksize)
                            if sent == 0:
                                return None
                            offset += sent
                            continue
                            except Exception:
                                err = None
                                raise _GiveupOnFastCopy(err)
                                err = None
                                del err
                            except OSError:
                                blocksize = 134217728
                                continue
                        except OSError:
                            err = None
                            err.filename = fsrc.name
                            err.filename2 = fdst.name
                            if err.errno == errno.ENOTSOCK:
                                _USE_CP_SENDFILE = False
                                raise _GiveupOnFastCopy(err)
                            if err.errno == errno.ENOSPC:
                                raise err, None
                            if offset == 0 and os.lseek(outfd, 0, os.SEEK_CUR) == 0:
                                raise _GiveupOnFastCopy(err)
                            raise err
                            err = None
                            del err




            
            def _copyfileobj_readinto(fsrc, fdst, length = (COPY_BUFSIZE,)):
                '''readinto()/memoryview() based variant of copyfileobj().
    *fsrc* must support readinto() method and both files must be
    open in binary mode.
    '''
                fsrc_readinto = fsrc.readinto
                fdst_write = fdst.write
                mv = memoryview(bytearray(length))
                n = fsrc_readinto(mv)
                if not n:
                    pass
                elif n < length:
                    smv = mv[:n]
                    fdst_write(smv)
                    None(None, None)
                else:
                    fdst_write(mv)
                None(None, None)
                return None
                with None:
                    if not None:
                        pass
                continue
                with None:
                    if not None:
                        pass

            
            def copyfileobj(fsrc, fdst, length = (0,)):
                '''copy data from file-like object fsrc to file-like object fdst'''
                if not length:
                    length = COPY_BUFSIZE
                fsrc_read = fsrc.read
                fdst_write = fdst.write
                buf = fsrc_read(length)
                if fsrc_read(length):
                    fdst_write(buf)
                    buf = fsrc_read(length)
                    if fsrc_read(length):
                        continue
                    return None

            
            def _samefile(src, dst):
                if isinstance(src, os.DirEntry) and hasattr(os.path, 'samestat'):
                    
                    try:
                        return os.path.samestat(src.stat(), os.stat(dst))
                        if hasattr(os.path, 'samefile'):
                            
                            try:
                                return os.path.samefile(src, dst)
                                return os.path.normcase(os.path.abspath(src)) == os.path.normcase(os.path.abspath(dst))
                                except OSError:
                                    return False
                            except OSError:
                                return False



            
            def _stat(fn):
                if isinstance(fn, os.DirEntry):
                    return fn.stat()
                return None.stat(fn)

            
            def _islink(fn):
                if isinstance(fn, os.DirEntry):
                    return fn.is_symlink()
                return None.path.islink(fn)

            
            def copyfile(src = None, dst = {
                'follow_symlinks': True }, *, follow_symlinks):
                '''Copy data from src to dst in the most efficient way possible.

    If follow_symlinks is not set and src is a symbolic link, a new
    symlink will be created instead of copying the file it points to.

    '''
                sys.audit('shutil.copyfile', src, dst)
                if _samefile(src, dst):
                    raise SameFileError('{!r} and {!r} are the same file'.format(src, dst))
                file_size = 0
                for i, fn in enumerate([
                    src,
                    dst]):
                    st = _stat(fn)
                    if stat.S_ISFIFO(st.st_mode):
                        fn = fn.path if isinstance(fn, os.DirEntry) else fn
                        raise SpecialFileError('`%s` is a named pipe' % fn)
                    if not _WINDOWS:
                        continue
                    if not i == 0:
                        continue
                    file_size = st.st_size
                if follow_symlinks and _islink(src):
                    os.symlink(os.readlink(src), dst)
                    return dst
                fsrc = None(src, 'rb')
                fdst = open(dst, 'wb')
                if _HAS_FCOPYFILE:
                    _fastcopy_fcopyfile(fsrc, fdst, posix._COPYFILE_DATA)
                    None(None, None)
                    None(None, None)
                    return 
                if None:
                    _fastcopy_sendfile(fsrc, fdst)
                    None(None, None)
                    None(None, None)
                    return 
                if None and file_size > 0:
                    _copyfileobj_readinto(fsrc, fdst, min(file_size, COPY_BUFSIZE))
                    None(None, None)
                    None(None, None)
                    return 
                None(fsrc, fdst)
                None(None, None)
                None(None, None)
                return dst
                except OSError:
                    continue
                except _GiveupOnFastCopy:
                    continue
                except _GiveupOnFastCopy:
                    continue
                with None:
                    if not None:
                        pass
                continue
                except IsADirectoryError:
                    if not os.path.exists(dst):
                        raise FileNotFoundError(f'''Directory does not exist: {dst}'''), e
                    raise 
                    None = None
                    del e
                with None:
                    if not None:
                        pass
                return dst

            
            def copymode(src = None, dst = {
                'follow_symlinks': True }, *, follow_symlinks):
                """Copy mode bits from src to dst.

    If follow_symlinks is not set, symlinks aren't followed if and only
    if both `src` and `dst` are symlinks.  If `lchmod` isn't available
    (e.g. Linux) this method does nothing.

    """
                sys.audit('shutil.copymode', src, dst)
                if follow_symlinks and _islink(src) and os.path.islink(dst):
                    if os.name == 'nt':
                        chmod_func = os.chmod
                        stat_func = os.lstat
                    elif hasattr(os, 'lchmod'):
                        chmod_func = os.lchmod
                        stat_func = os.lstat
                    else:
                        return None
                        if os.name == 'nt' and os.path.islink(dst):
                            dst = os.path.realpath(dst, strict = True)
                        chmod_func = os.chmod
                        stat_func = _stat
                st = stat_func(src)
                chmod_func(dst, stat.S_IMODE(st.st_mode))

            
            def copystat(src = None if hasattr(os, 'listxattr') else None, dst = {
                'follow_symlinks': True }, *, follow_symlinks):
                '''Copy file metadata

    Copy the permission bits, last access time, last modification time, and
    flags from `src` to `dst`. On Linux, copystat() also copies the "extended
    attributes" where possible. The file contents, owner, and group are
    unaffected. `src` and `dst` are path-like objects or path names given as
    strings.

    If the optional flag `follow_symlinks` is not set, symlinks aren\'t
    followed if and only if both `src` and `dst` are symlinks.
    '''
                pass
            # WARNING: Decompyle incomplete

            
            def copy(src = None, dst = {
                'follow_symlinks': True }, *, follow_symlinks):
                '''Copy data and mode bits ("cp src dst"). Return the file\'s destination.

    The destination may be a directory.

    If follow_symlinks is false, symlinks won\'t be followed. This
    resembles GNU\'s "cp -P src dst".

    If source and destination are the same file, a SameFileError will be
    raised.

    '''
                if os.path.isdir(dst):
                    dst = os.path.join(dst, os.path.basename(src))
                copyfile(src, dst, follow_symlinks = follow_symlinks)
                copymode(src, dst, follow_symlinks = follow_symlinks)
                return dst

            
            def copy2(src = None, dst = {
                'follow_symlinks': True }, *, follow_symlinks):
                '''Copy data and metadata. Return the file\'s destination.

    Metadata is copied with copystat(). Please see the copystat function
    for more information.

    The destination may be a directory.

    If follow_symlinks is false, symlinks won\'t be followed. This
    resembles GNU\'s "cp -P src dst".
    '''
                if os.path.isdir(dst):
                    dst = os.path.join(dst, os.path.basename(src))
                if hasattr(_winapi, 'CopyFile2'):
                    src_ = os.fsdecode(src)
                    dst_ = os.fsdecode(dst)
                    flags = _winapi.COPY_FILE_ALLOW_DECRYPTED_DESTINATION
                    if not follow_symlinks:
                        flags |= _winapi.COPY_FILE_COPY_SYMLINK
                    
                    try:
                        _winapi.CopyFile2(src_, dst_, flags)
                        return dst
                        copyfile(src, dst, follow_symlinks = follow_symlinks)
                        copystat(src, dst, follow_symlinks = follow_symlinks)
                        return dst
                    except OSError:
                        exc = None
                        if not exc.winerror == _winapi.ERROR_PRIVILEGE_NOT_HELD and follow_symlinks:
                            pass
                        elif exc.winerror == _winapi.ERROR_ACCESS_DENIED:
                            pass
                        else:
                            raise 
                        exc = None
                        del exc
                        continue
                        exc = None
                        del exc


            
            def ignore_patterns(*patterns):
                '''Function that can be used as copytree() ignore parameter.

    Patterns is a sequence of glob-style patterns
    that are used to exclude files'''
                pass
            # WARNING: Decompyle incomplete

            
            def _copytree(entries, src, dst, symlinks, ignore, copy_function, ignore_dangling_symlinks, dirs_exist_ok = (False,)):
                pass
            # WARNING: Decompyle incomplete

            
            def copytree(src, dst, symlinks, ignore, copy_function, ignore_dangling_symlinks, dirs_exist_ok = (False, None, copy2, False, False)):
                """Recursively copy a directory tree and return the destination directory.

    If exception(s) occur, an Error is raised with a list of reasons.

    If the optional symlinks flag is true, symbolic links in the
    source tree result in symbolic links in the destination tree; if
    it is false, the contents of the files pointed to by symbolic
    links are copied. If the file pointed to by the symlink doesn't
    exist, an exception will be added in the list of errors raised in
    an Error exception at the end of the copy process.

    You can set the optional ignore_dangling_symlinks flag to true if you
    want to silence this exception. Notice that this has no effect on
    platforms that don't support os.symlink.

    The optional ignore argument is a callable. If given, it
    is called with the `src` parameter, which is the directory
    being visited by copytree(), and `names` which is the list of
    `src` contents, as returned by os.listdir():

        callable(src, names) -> ignored_names

    Since copytree() is called recursively, the callable will be
    called once for each directory that is copied. It returns a
    list of names relative to the `src` directory that should
    not be copied.

    The optional copy_function argument is a callable that will be used
    to copy each file. It will be called with the source path and the
    destination path as arguments. By default, copy2() is used, but any
    function that supports the same signature (like copy()) can be used.

    If dirs_exist_ok is false (the default) and `dst` already exists, a
    `FileExistsError` is raised. If `dirs_exist_ok` is true, the copying
    operation will continue if it encounters existing directories, and files
    within the `dst` tree will be overwritten by corresponding files from the
    `src` tree.
    """
                sys.audit('shutil.copytree', src, dst)
                itr = os.scandir(src)
                entries = list(itr)
                None(None, None)
            # WARNING: Decompyle incomplete

            if hasattr(os.stat_result, 'st_file_attributes'):
                
                def _rmtree_islink(path):
                    
                    try:
                        st = os.lstat(path)
                        if not stat.S_ISLNK(st.st_mode):
                            stat.S_ISLNK(st.st_mode)
                            if st.st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                                st.st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT
                        return st.st_reparse_tag == stat.IO_REPARSE_TAG_MOUNT_POINT
                    except OSError:
                        return False


            else:
                
                def _rmtree_islink(path):
                    return os.path.islink(path)

            
            def _rmtree_unsafe(path, onexc):
                pass
            # WARNING: Decompyle incomplete

            
            def _rmtree_safe_fd(stack, onexc):
                (func, dirfd, path, orig_entry) = stack.pop()
            # WARNING: Decompyle incomplete

            if {
                os.open,
                os.stat,
                os.unlink,
                os.rmdir} <= os.supports_dir_fd:
                {
                    os.open,
                    os.stat,
                    os.unlink,
                    os.rmdir} <= os.supports_dir_fd
                if os.scandir in os.supports_fd:
                    os.scandir in os.supports_fd
            _use_fd_functions = os.stat in os.supports_follow_symlinks
            
            def rmtree(path = None, ignore_errors = (False, None), onerror = {
                'onexc': None,
                'dir_fd': None }, *, onexc, dir_fd):
                '''Recursively delete a directory tree.

    If dir_fd is not None, it should be a file descriptor open to a directory;
    path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
    If it is unavailable, using it will raise a NotImplementedError.

    If ignore_errors is set, errors are ignored; otherwise, if onexc or
    onerror is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is platform and implementation dependent;
    path is the argument to that function that caused it to fail; and
    the value of exc_info describes the exception. For onexc it is the
    exception instance, and for onerror it is a tuple as returned by
    sys.exc_info().  If ignore_errors is false and both onexc and
    onerror are None, the exception is reraised.

    onerror is deprecated and only remains for backwards compatibility.
    If both onerror and onexc are set, onerror is ignored and onexc is used.
    '''
                pass
            # WARNING: Decompyle incomplete

            rmtree.avoids_symlink_attacks = _use_fd_functions
            
            def _basename(path):
                """A basename() variant which first strips the trailing slash, if present.
    Thus we always get the last component of the path, even for directories.

    path: Union[PathLike, str]

    e.g.
    >>> os.path.basename('/bar/foo')
    'foo'
    >>> os.path.basename('/bar/foo/')
    ''
    >>> _basename('/bar/foo/')
    'foo'
    """
                path = os.fspath(path)
                if not os.path.altsep:
                    os.path.altsep
                sep = os.path.sep + ''
                return os.path.basename(path.rstrip(sep))

            
            def move(src, dst, copy_function = (copy2,)):
                '''Recursively move a file or directory to another location. This is
    similar to the Unix "mv" command. Return the file or directory\'s
    destination.

    If dst is an existing directory or a symlink to a directory, then src is
    moved inside that directory. The destination path in that directory must
    not already exist.

    If dst already exists but is not a directory, it may be overwritten
    depending on os.rename() semantics.

    If the destination is on our current filesystem, then rename() is used.
    Otherwise, src is copied to the destination and then removed. Symlinks are
    recreated under the new name if os.rename() fails because of cross
    filesystem renames.

    The optional `copy_function` argument is a callable that will be used
    to copy the source or it will be delegated to `copytree`.
    By default, copy2() is used, but any function that supports the same
    signature (like copy()) can be used.

    A lot more could be done here...  A look at a mv.c shows a lot of
    the issues this implementation glosses over.

    '''
                sys.audit('shutil.move', src, dst)
                real_dst = dst
                if os.path.isdir(dst):
                    if not _samefile(src, dst) and os.path.islink(src):
                        os.rename(src, dst)
                        return None
                    real_dst = os.path.join(dst, _basename(src))
                    if os.path.exists(real_dst):
                        raise Error("Destination path '%s' already exists" % real_dst)
                
                try:
                    os.rename(src, real_dst)
                    return real_dst
                except OSError:
                    if os.path.islink(src):
                        linkto = os.readlink(src)
                        os.symlink(linkto, real_dst)
                        os.unlink(src)
                        return real_dst
                    if None.path.isdir(src):
                        if _destinsrc(src, dst):
                            raise Error(f'''Cannot move a directory \'{src!s}\' into itself \'{dst!s}\'.''')
                        if (_is_immutable(src) or os.access(src, os.W_OK)) and os.listdir(src) and sys.platform == 'darwin':
                            raise PermissionError(f'''Cannot move the non-empty directory \'{src!s}\': Lacking write permission to \'{src!s}\'.''')
                        copytree(src, real_dst, copy_function = copy_function, symlinks = True)
                        rmtree(src)
                        return real_dst
                    copy_function(src, real_dst)
                    os.unlink(src)
                    return real_dst


            
            def _destinsrc(src, dst):
                src = os.path.abspath(src)
                dst = os.path.abspath(dst)
                if not src.endswith(os.path.sep):
                    src += os.path.sep
                if not dst.endswith(os.path.sep):
                    dst += os.path.sep
                return dst.startswith(src)

            
            def _is_immutable(src):
                st = _stat(src)
                immutable_states = [
                    stat.UF_IMMUTABLE,
                    stat.SF_IMMUTABLE]
                if hasattr(st, 'st_flags'):
                    hasattr(st, 'st_flags')
                return st.st_flags in immutable_states

            
            def _get_gid(name):
                '''Returns a gid, given a group name.'''
                pass
            # WARNING: Decompyle incomplete

            
            def _get_uid(name):
                '''Returns an uid, given a user name.'''
                pass
            # WARNING: Decompyle incomplete

            
            def _make_tarball(base_name, base_dir, compress, verbose, dry_run, owner, group, logger, root_dir = ('gzip', 0, 0, None, None, None, None)):
                '''Create a (possibly compressed) tar file from all the files under
    \'base_dir\'.

    \'compress\' must be "gzip" (the default), "bzip2", "xz", or None.

    \'owner\' and \'group\' can be used to define an owner and a group for the
    archive that is being built. If not provided, the current owner and group
    will be used.

    The output tar file will be named \'base_name\' +  ".tar", possibly plus
    the appropriate compression extension (".gz", ".bz2", or ".xz").

    Returns the output filename.
    '''
                pass
            # WARNING: Decompyle incomplete

            
            def _make_zipfile(base_name, base_dir, verbose, dry_run, logger, owner, group, root_dir = (0, 0, None, None, None, None)):
                '''Create a zip file from all the files under \'base_dir\'.

    The output zip file will be named \'base_name\' + ".zip".  Returns the
    name of the output zip file.
    '''
                import zipfile
                zip_filename = base_name + '.zip'
                archive_dir = os.path.dirname(base_name)
            # WARNING: Decompyle incomplete

            _make_tarball.supports_root_dir = True
            _make_zipfile.supports_root_dir = True
            _ARCHIVE_FORMATS = {
                'tar': (_make_tarball, [
                    ('compress', None)], 'uncompressed tar file') }
            if _ZLIB_SUPPORTED:
                _ARCHIVE_FORMATS['gztar'] = (_make_tarball, [
                    ('compress', 'gzip')], "gzip'ed tar-file")
                _ARCHIVE_FORMATS['zip'] = (_make_zipfile, [], 'ZIP file')
            if _BZ2_SUPPORTED:
                _ARCHIVE_FORMATS['bztar'] = (_make_tarball, [
                    ('compress', 'bzip2')], "bzip2'ed tar-file")
            if _LZMA_SUPPORTED:
                _ARCHIVE_FORMATS['xztar'] = (_make_tarball, [
                    ('compress', 'xz')], "xz'ed tar-file")
            
            def get_archive_formats():
                '''Returns a list of supported formats for archiving and unarchiving.

    Each element of the returned sequence is a tuple (name, description)
    '''
                pass
            # WARNING: Decompyle incomplete

            
            def register_archive_format(name, function, extra_args, description = (None, '')):
                '''Registers an archive format.

    name is the name of the format. function is the callable that will be
    used to create archives. If provided, extra_args is a sequence of
    (name, value) tuples that will be passed as arguments to the callable.
    description can be provided to describe the format, and will be returned
    by the get_archive_formats() function.
    '''
                pass
            # WARNING: Decompyle incomplete

            
            def unregister_archive_format(name):
                del _ARCHIVE_FORMATS[name]

            
            def make_archive(base_name, format, root_dir, base_dir, verbose, dry_run, owner, group, logger = (None, None, 0, 0, None, None, None)):
                '''Create an archive file (eg. zip or tar).

    \'base_name\' is the name of the file to create, minus any format-specific
    extension; \'format\' is the archive format: one of "zip", "tar", "gztar",
    "bztar", or "xztar".  Or any other registered format.

    \'root_dir\' is a directory that will be the root directory of the
    archive; ie. we typically chdir into \'root_dir\' before creating the
    archive.  \'base_dir\' is the directory where we start archiving from;
    ie. \'base_dir\' will be the common prefix of all files and
    directories in the archive.  \'root_dir\' and \'base_dir\' both default
    to the current directory.  Returns the name of the archive file.

    \'owner\' and \'group\' are used when creating a tar archive. By default,
    uses the current owner and group.
    '''
                sys.audit('shutil.make_archive', base_name, format, root_dir, base_dir)
            # WARNING: Decompyle incomplete

            
            def get_unpack_formats():
                '''Returns a list of supported formats for unpacking.

    Each element of the returned sequence is a tuple
    (name, extensions, description)
    '''
                pass
            # WARNING: Decompyle incomplete

            
            def _check_unpack_options(extensions, function, extra_args):
                '''Checks what gets registered as an unpacker.'''
                existing_extensions = { }
                for name, info in _UNPACK_FORMATS.items():
                    for ext in info[0]:
                        existing_extensions[ext] = name
                for extension in extensions:
                    if not extension in existing_extensions:
                        continue
                    msg = '%s is already registered for "%s"'
                    raise RegistryError(msg % (extension, existing_extensions[extension]))
                if not callable(function):
                    raise TypeError('The registered function must be a callable')

            
            def register_unpack_format(name, extensions, function, extra_args, description = (None, '')):
                """Registers an unpack format.

    `name` is the name of the format. `extensions` is a list of extensions
    corresponding to the format.

    `function` is the callable that will be
    used to unpack archives. The callable will receive archives to unpack.
    If it's unable to handle an archive, it needs to raise a ReadError
    exception.

    If provided, `extra_args` is a sequence of
    (name, value) tuples that will be passed as arguments to the callable.
    description can be provided to describe the format, and will be returned
    by the get_unpack_formats() function.
    """
                pass
            # WARNING: Decompyle incomplete

            
            def unregister_unpack_format(name):
                '''Removes the pack format from the registry.'''
                del _UNPACK_FORMATS[name]

            
            def _ensure_directory(path):
                '''Ensure that the parent directory of `path` exists'''
                dirname = os.path.dirname(path)
                if not os.path.isdir(dirname):
                    os.makedirs(dirname)
                    return None

            
            def _unpack_zipfile(filename, extract_dir):
                '''Unpack zip `filename` to `extract_dir`
    '''
                import zipfile
                if not zipfile.is_zipfile(filename):
                    raise ReadError('%s is not a zip file' % filename)
                zip = zipfile.ZipFile(filename)
            # WARNING: Decompyle incomplete

            
            def _unpack_tarfile(filename = None, extract_dir = {
                'filter': None }, *, filter):
                '''Unpack tar/tar.gz/tar.bz2/tar.xz `filename` to `extract_dir`
    '''
                import tarfile
                
                try:
                    tarobj = tarfile.open(filename)
                    
                    try:
                        tarobj.extractall(extract_dir, filter = filter)
                        tarobj.close()
                        return None
                        except tarfile.TarError:
                            raise ReadError('%s is not a compressed or uncompressed tar file' % filename)
                    except:
                        tarobj.close()



            _UNPACK_FORMATS = {
                'tar': ([
                    '.tar'], _unpack_tarfile, [], 'uncompressed tar file'),
                'zip': ([
                    '.zip'], _unpack_zipfile, [], 'ZIP file') }
            if _ZLIB_SUPPORTED:
                _UNPACK_FORMATS['gztar'] = ([
                    '.tar.gz',
                    '.tgz'], _unpack_tarfile, [], "gzip'ed tar-file")
            if _BZ2_SUPPORTED:
                _UNPACK_FORMATS['bztar'] = ([
                    '.tar.bz2',
                    '.tbz2'], _unpack_tarfile, [], "bzip2'ed tar-file")
            if _LZMA_SUPPORTED:
                _UNPACK_FORMATS['xztar'] = ([
                    '.tar.xz',
                    '.txz'], _unpack_tarfile, [], "xz'ed tar-file")
            
            def _find_unpack_format(filename):
                for name, info in _UNPACK_FORMATS.items():
                    for extension in info[0]:
                        if not filename.endswith(extension):
                            continue
                        
                        
                        return _UNPACK_FORMATS.items(), info[0], name

            
            def unpack_archive(filename = None, extract_dir = (None, None), format = {
                'filter': None }, *, filter):
                '''Unpack an archive.

    `filename` is the name of the archive.

    `extract_dir` is the name of the target directory, where the archive
    is unpacked. If not provided, the current working directory is used.

    `format` is the archive format: one of "zip", "tar", "gztar", "bztar",
    or "xztar".  Or any other registered format.  If not provided,
    unpack_archive will use the filename extension and see if an unpacker
    was registered for that extension.

    In case none is found, a ValueError is raised.

    If `filter` is given, it is passed to the underlying
    extraction function.
    '''
                sys.audit('shutil.unpack_archive', filename, extract_dir, format)
            # WARNING: Decompyle incomplete

            if hasattr(os, 'statvfs'):
                __all__.append('disk_usage')
                _ntuple_diskusage = collections.namedtuple('usage', 'total used free')
                _ntuple_diskusage.total.__doc__ = 'Total space in bytes'
                _ntuple_diskusage.used.__doc__ = 'Used space in bytes'
                _ntuple_diskusage.free.__doc__ = 'Free space in bytes'
                
                def disk_usage(path):
                    """Return disk usage statistics about the given path.

        Returned value is a named tuple with attributes 'total', 'used' and
        'free', which are the amount of total, used and free space, in bytes.
        """
                    st = os.statvfs(path)
                    free = st.f_bavail * st.f_frsize
                    total = st.f_blocks * st.f_frsize
                    used = (st.f_blocks - st.f_bfree) * st.f_frsize
                    return _ntuple_diskusage(total, used, free)

            elif _WINDOWS:
                __all__.append('disk_usage')
                _ntuple_diskusage = collections.namedtuple('usage', 'total used free')
                
                def disk_usage(path):
                    """Return disk usage statistics about the given path.

        Returned values is a named tuple with attributes 'total', 'used' and
        'free', which are the amount of total, used and free space, in bytes.
        """
                    (total, free) = nt._getdiskusage(path)
                    used = total - free
                    return _ntuple_diskusage(total, used, free)

            
            def chown(path, user, group = (None, None)):
                '''Change owner user and group of the given path.

    user and group can be the uid/gid or the user/group names, and in that case,
    they are converted to their respective uid/gid.
    '''
                sys.audit('shutil.chown', path, user, group)
            # WARNING: Decompyle incomplete

            
            def get_terminal_size(fallback = ((80, 24),)):
                """Get the size of the terminal window.

    For each of the two dimensions, the environment variable, COLUMNS
    and LINES respectively, is checked. If the variable is defined and
    the value is a positive integer, it is used.

    When COLUMNS or LINES is not defined, which is the common case,
    the terminal connected to sys.__stdout__ is queried
    by invoking os.get_terminal_size.

    If the terminal size cannot be successfully queried, either because
    the system doesn't support querying, or because we are not
    connected to a terminal, the value given in fallback parameter
    is used. Fallback defaults to (80, 24) which is the default
    size used by many terminal emulators.

    The value returned is a named tuple of type os.terminal_size.
    """
                
                try:
                    columns = int(os.environ['COLUMNS'])
                    
                    try:
                        lines = int(os.environ['LINES'])
                        if columns <= 0 or lines <= 0:
                            
                            try:
                                size = os.get_terminal_size(sys.__stdout__.fileno())
                                if columns <= 0:
                                    if not size.columns:
                                        size.columns
                                    columns = fallback[0]
                                if lines <= 0:
                                    if not size.lines:
                                        size.lines
                                    lines = fallback[1]
                                return os.terminal_size((columns, lines))
                                except (KeyError, ValueError):
                                    columns = 0
                                    continue
                                except (KeyError, ValueError):
                                    lines = 0
                                    continue
                            except (AttributeError, ValueError, OSError):
                                size = os.terminal_size(fallback)
                                continue




            
            def _access_check(fn, mode):
                if os.path.exists(fn):
                    os.path.exists(fn)
                    if os.access(fn, mode):
                        os.access(fn, mode)
                return not os.path.isdir(fn)

            
            def _win_path_needs_curdir(cmd, mode):
                '''
    On Windows, we can use NeedCurrentDirectoryForExePath to figure out
    if we should add the cwd to PATH when searching for executables if
    the mode is executable.
    '''
                if not not (mode & os.X_OK):
                    not (mode & os.X_OK)
                return _winapi.NeedCurrentDirectoryForExePath(os.fsdecode(cmd))

            
            def which(cmd, mode, path = (os.F_OK | os.X_OK, None)):
                '''Given a command, mode, and a PATH string, return the path which
    conforms to the given mode on the PATH, or None if there is no such
    file.

    `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
    of os.environ.get("PATH"), or can be overridden with a custom search
    path.

    '''
                pass
            # WARNING: Decompyle incomplete

            return None
            except ImportError:
                _ZLIB_SUPPORTED = False
                continue
            except ImportError:
                _BZ2_SUPPORTED = False
                continue
        except ImportError:
            _LZMA_SUPPORTED = False
            continue



