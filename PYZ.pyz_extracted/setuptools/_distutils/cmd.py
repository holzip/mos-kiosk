# Source Generated with Decompyle++
# File: cmd.pyc (Python 3.12)

'''distutils.cmd

Provides the Command class, the base class for the command classes
in the distutils.command package.
'''
from __future__ import annotations
import logging
import os
import re
import sys
from abc import abstractmethod
from collections.abc import Callable, MutableSequence
from typing import TYPE_CHECKING, Any, ClassVar, TypeVar, overload
from  import _modified, archive_util, dir_util, file_util, util
from _log import log
from errors import DistutilsOptionError
if TYPE_CHECKING:
    from distutils.dist import Distribution
    from typing_extensions import TypeVarTuple, Unpack
    _Ts = TypeVarTuple('_Ts')
_StrPathT = TypeVar('_StrPathT', bound = 'str | os.PathLike[str]')
_BytesPathT = TypeVar('_BytesPathT', bound = 'bytes | os.PathLike[bytes]')
_CommandT = TypeVar('_CommandT', bound = 'Command')

class Command:
    '''Abstract base class for defining command classes, the "worker bees"
    of the Distutils.  A useful analogy for command classes is to think of
    them as subroutines with local variables called "options".  The options
    are "declared" in \'initialize_options()\' and "defined" (given their
    final values, aka "finalized") in \'finalize_options()\', both of which
    must be defined by every command class.  The distinction between the
    two is necessary because option values might come from the outside
    world (command line, config file, ...), and any options dependent on
    other options must be computed *after* these outside influences have
    been processed -- hence \'finalize_options()\'.  The "body" of the
    subroutine, where it does all its work based on the values of its
    options, is the \'run()\' method, which must also be implemented by every
    command class.
    '''
    sub_commands: 'ClassVar[list[tuple[str, Callable[[Any], bool] | None]]]' = []
    user_options: 'ClassVar[list[tuple[str, str, str]] | list[tuple[str, str | None, str]]]' = []
    
    def __init__(self = None, dist = None):
        """Create and initialize a new Command object.  Most importantly,
        invokes the 'initialize_options()' method, which is the real
        initializer and depends on the actual command being
        instantiated.
        """
        Distribution = Distribution
        import distutils.dist
        if not isinstance(dist, Distribution):
            raise TypeError('dist must be a Distribution instance')
        if self.__class__ is Command:
            raise RuntimeError('Command is an abstract class')
        self.distribution = dist
        self.initialize_options()
        self._dry_run = None
        self.verbose = dist.verbose
        self.force = None
        self.help = False
        self.finalized = False

    
    def __getattr__(self, attr):
        pass
    # WARNING: Decompyle incomplete

    
    def ensure_finalized(self = None):
        if not self.finalized:
            self.finalize_options()
        self.finalized = True

    initialize_options = (lambda self = None: raise RuntimeError(f'''abstract method -- subclass {self.__class__} must override'''))()
    finalize_options = (lambda self = None: raise RuntimeError(f'''abstract method -- subclass {self.__class__} must override'''))()
    
    def dump_options(self, header, indent = (None, '')):
        longopt_xlate = longopt_xlate
        import distutils.fancy_getopt
    # WARNING: Decompyle incomplete

    run = (lambda self = None: raise RuntimeError(f'''abstract method -- subclass {self.__class__} must override'''))()
    
    def announce(self = None, msg = None, level = None):
        log.log(level, msg)

    
    def debug_print(self = None, msg = None):
        """Print 'msg' to stdout if the global DEBUG (taken from the
        DISTUTILS_DEBUG environment variable) flag is true.
        """
        DEBUG = DEBUG
        import distutils.debug
        if DEBUG:
            print(msg)
            sys.stdout.flush()
            return None

    
    def _ensure_stringlike(self, option, what, default = (None,)):
        val = getattr(self, option)
    # WARNING: Decompyle incomplete

    
    def ensure_string(self = None, option = None, default = None):
        """Ensure that 'option' is a string; if not defined, set it to
        'default'.
        """
        self._ensure_stringlike(option, 'string', default)

    
    def ensure_string_list(self = None, option = None):
        '''Ensure that \'option\' is a list of strings.  If \'option\' is
        currently a string, we split it either on /,\\s*/ or /\\s+/, so
        "foo bar baz", "foo,bar,baz", and "foo,   bar baz" all become
        ["foo", "bar", "baz"].
        '''
        val = getattr(self, option)
    # WARNING: Decompyle incomplete

    
    def _ensure_tested_string(self, option, tester, what, error_fmt, default = (None,)):
        val = self._ensure_stringlike(option, what, default)
    # WARNING: Decompyle incomplete

    
    def ensure_filename(self = None, option = None):
        """Ensure that 'option' is the name of an existing file."""
        self._ensure_tested_string(option, os.path.isfile, 'filename', "'%s' does not exist or is not a file")

    
    def ensure_dirname(self = None, option = None):
        self._ensure_tested_string(option, os.path.isdir, 'directory name', "'%s' does not exist or is not a directory")

    
    def get_command_name(self = None):
        if hasattr(self, 'command_name'):
            return self.command_name
        return None.__class__.__name__

    
    def set_undefined_options(self = None, src_cmd = None, *option_pairs):
        '''Set the values of any "undefined" options from corresponding
        option values in some other command object.  "Undefined" here means
        "is None", which is the convention used to indicate that an option
        has not been changed between \'initialize_options()\' and
        \'finalize_options()\'.  Usually called from \'finalize_options()\' for
        options that depend on some other command rather than another
        option of the same command.  \'src_cmd\' is the other command from
        which option values will be taken (a command object will be created
        for it if necessary); the remaining arguments are
        \'(src_option,dst_option)\' tuples which mean "take the value of
        \'src_option\' in the \'src_cmd\' command object, and copy it to
        \'dst_option\' in the current command object".
        '''
        src_cmd_obj = self.distribution.get_command_obj(src_cmd)
        src_cmd_obj.ensure_finalized()
    # WARNING: Decompyle incomplete

    
    def get_finalized_command(self = None, command = None, create = None):
        """Wrapper around Distribution's 'get_command_obj()' method: find
        (create if necessary and 'create' is true) the command object for
        'command', call its 'ensure_finalized()' method, and return the
        finalized command object.
        """
        cmd_obj = self.distribution.get_command_obj(command, create)
        cmd_obj.ensure_finalized()
        return cmd_obj

    reinitialize_command = (lambda self = None, command = None, reinit_subcommands = overload: pass)()
    reinitialize_command = (lambda self = None, command = None, reinit_subcommands = overload: pass)()
    
    def reinitialize_command(self = None, command = None, reinit_subcommands = None):
        return self.distribution.reinitialize_command(command, reinit_subcommands)

    
    def run_command(self = None, command = None):
        """Run some other command: uses the 'run_command()' method of
        Distribution, which creates and finalizes the command object if
        necessary and then invokes its 'run()' method.
        """
        self.distribution.run_command(command)

    
    def get_sub_commands(self = None):
        """Determine the sub-commands that are relevant in the current
        distribution (ie., that need to be run).  This is based on the
        'sub_commands' class attribute: each tuple in that list may include
        a method that we call to determine if the subcommand needs to be
        run for the current distribution.  Return a list of command names.
        """
        commands = []
    # WARNING: Decompyle incomplete

    
    def warn(self = None, msg = None):
        log.warning('warning: %s: %s\n', self.get_command_name(), msg)

    
    def execute(self = None, func = None, args = None, msg = (None, 1), level = ('func', 'Callable[[Unpack[_Ts]], object]', 'args', 'tuple[Unpack[_Ts]]', 'msg', 'object', 'level', 'int', 'return', 'None')):
        util.execute(func, args, msg, dry_run = self.dry_run)

    
    def mkpath(self = None, name = None, mode = None):
        dir_util.mkpath(name, mode, dry_run = self.dry_run)

    copy_file = (lambda self, infile, outfile = None, preserve_mode = None, preserve_times = overload, link = (True, True, None, 1), level = ('infile', 'str | os.PathLike[str]', 'outfile', '_StrPathT', 'preserve_mode', 'bool', 'preserve_times', 'bool', 'link', 'str | None', 'level', 'int', 'return', 'tuple[_StrPathT | str, bool]'): pass)()
    copy_file = (lambda self, infile, outfile = None, preserve_mode = None, preserve_times = overload, link = (True, True, None, 1), level = ('infile', 'bytes | os.PathLike[bytes]', 'outfile', '_BytesPathT', 'preserve_mode', 'bool', 'preserve_times', 'bool', 'link', 'str | None', 'level', 'int', 'return', 'tuple[_BytesPathT | bytes, bool]'): pass)()
    
    def copy_file(self, infile, outfile = None, preserve_mode = None, preserve_times = None, link = (True, True, None, 1), level = ('infile', 'str | os.PathLike[str] | bytes | os.PathLike[bytes]', 'outfile', 'str | os.PathLike[str] | bytes | os.PathLike[bytes]', 'preserve_mode', 'bool', 'preserve_times', 'bool', 'link', 'str | None', 'level', 'int', 'return', 'tuple[str | os.PathLike[str] | bytes | os.PathLike[bytes], bool]')):
        """Copy a file respecting verbose, dry-run and force flags.  (The
        former two default to whatever is in the Distribution object, and
        the latter defaults to false for commands that don't define it.)"""
        return file_util.copy_file(infile, outfile, preserve_mode, preserve_times, not (self.force), link, dry_run = self.dry_run)

    
    def copy_tree(self, infile, outfile = None, preserve_mode = None, preserve_times = None, preserve_symlinks = (True, True, False, 1), level = ('infile', 'str | os.PathLike[str]', 'outfile', 'str', 'preserve_mode', 'bool', 'preserve_times', 'bool', 'preserve_symlinks', 'bool', 'level', 'int', 'return', 'list[str]')):
        '''Copy an entire directory tree respecting verbose, dry-run,
        and force flags.
        '''
        return dir_util.copy_tree(infile, outfile, preserve_mode, preserve_times, preserve_symlinks, not (self.force), dry_run = self.dry_run)

    move_file = (lambda self = None, src = None, dst = overload, level = (1,): pass)()
    move_file = (lambda self = None, src = None, dst = overload, level = (1,): pass)()
    
    def move_file(self = None, src = None, dst = None, level = (1,)):
        '''Move a file respecting dry-run flag.'''
        return file_util.move_file(src, dst, dry_run = self.dry_run)

    
    def spawn(self = None, cmd = None, search_path = None, level = (True, 1)):
        '''Spawn an external command respecting dry-run flag.'''
        spawn = spawn
        import distutils.spawn
        spawn(cmd, search_path, dry_run = self.dry_run)

    make_archive = (lambda self, base_name, format = None, root_dir = None, base_dir = overload, owner = (None, None, None, None), group = ('base_name', 'str', 'format', 'str', 'root_dir', 'str | os.PathLike[str] | bytes | os.PathLike[bytes] | None', 'base_dir', 'str | None', 'owner', 'str | None', 'group', 'str | None', 'return', 'str'): pass)()
    make_archive = (lambda self, base_name, format = None, root_dir = None, base_dir = overload, owner = (None, None, None), group = ('base_name', 'str | os.PathLike[str]', 'format', 'str', 'root_dir', 'str | os.PathLike[str] | bytes | os.PathLike[bytes]', 'base_dir', 'str | None', 'owner', 'str | None', 'group', 'str | None', 'return', 'str'): pass)()
    
    def make_archive(self, base_name, format = None, root_dir = None, base_dir = None, owner = (None, None, None, None), group = ('base_name', 'str | os.PathLike[str]', 'format', 'str', 'root_dir', 'str | os.PathLike[str] | bytes | os.PathLike[bytes] | None', 'base_dir', 'str | None', 'owner', 'str | None', 'group', 'str | None', 'return', 'str')):
        return archive_util.make_archive(base_name, format, root_dir, base_dir, dry_run = self.dry_run, owner = owner, group = group)

    
    def make_file(self, infiles, outfile, func = None, args = None, exec_msg = None, skip_msg = (None, None, 1), level = ('infiles', 'str | list[str] | tuple[str, ...]', 'outfile', 'str | os.PathLike[str] | bytes | os.PathLike[bytes]', 'func', 'Callable[[Unpack[_Ts]], object]', 'args', 'tuple[Unpack[_Ts]]', 'exec_msg', 'object', 'skip_msg', 'object', 'level', 'int', 'return', 'None')):
        """Special case of 'execute()' for operations that process one or
        more input files and generate one output file.  Works just like
        'execute()', except the operation is skipped and a different
        message printed if 'outfile' already exists and is newer than all
        files listed in 'infiles'.  If the command defined 'self.force',
        and it is true, then the command is unconditionally run -- does no
        timestamp checks.
        """
        pass
    # WARNING: Decompyle incomplete


