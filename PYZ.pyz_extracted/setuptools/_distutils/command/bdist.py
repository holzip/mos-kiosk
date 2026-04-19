# Source Generated with Decompyle++
# File: bdist.pyc (Python 3.12)

"""distutils.command.bdist

Implements the Distutils 'bdist' command (create a built [binary]
distribution)."""
from __future__ import annotations
import os
import warnings
from collections.abc import Callable
from typing import TYPE_CHECKING, ClassVar
from core import Command
from errors import DistutilsOptionError, DistutilsPlatformError
from util import get_platform
if TYPE_CHECKING:
    from typing_extensions import deprecated
else:
    
    def deprecated(message):
        return (lambda fn: fn)


def show_formats():
    '''Print list of available formats (arguments to "--format" option).'''
    FancyGetopt = FancyGetopt
    import fancy_getopt
# WARNING: Decompyle incomplete


def ListCompat():
    '''ListCompat'''
    append = (lambda self = None, item = None: warnings.warn('format_commands is now a dict. append is deprecated.', DeprecationWarning, stacklevel = 2))()

ListCompat = <NODE:27>(ListCompat, 'ListCompat', dict[(str, tuple[(str, str)])])

class bdist(Command):
    description = 'create a built (binary) distribution'
    user_options = [
        ('bdist-base=', 'b', 'temporary directory for creating built distributions'),
        ('plat-name=', 'p', f'''platform name to embed in generated filenames [default: {get_platform()}]'''),
        ('formats=', None, 'formats for distribution (comma-separated list)'),
        ('dist-dir=', 'd', 'directory to put final built distributions in [default: dist]'),
        ('skip-build', None, 'skip rebuilding everything (for testing/debugging)'),
        ('owner=', 'u', 'Owner name used when creating a tar file [default: current user]'),
        ('group=', 'g', 'Group name used when creating a tar file [default: current group]')]
    boolean_options: 'ClassVar[list[str]]' = [
        'skip-build']
    help_options: 'ClassVar[list[tuple[str, str | None, str, Callable[[], object]]]]' = [
        ('help-formats', None, 'lists available distribution formats', show_formats)]
    no_format_option: 'ClassVar[tuple[str, ...]]' = ('bdist_rpm',)
    default_format: 'ClassVar[dict[str, str]]' = {
        'posix': 'gztar',
        'nt': 'zip' }
    format_commands = ListCompat({
        'rpm': ('bdist_rpm', 'RPM distribution'),
        'gztar': ('bdist_dumb', "gzip'ed tar file"),
        'bztar': ('bdist_dumb', "bzip2'ed tar file"),
        'xztar': ('bdist_dumb', "xz'ed tar file"),
        'ztar': ('bdist_dumb', 'compressed tar file'),
        'tar': ('bdist_dumb', 'tar file'),
        'zip': ('bdist_dumb', 'ZIP file') })
    format_command = format_commands
    
    def initialize_options(self):
        self.bdist_base = None
        self.plat_name = None
        self.formats = None
        self.dist_dir = None
        self.skip_build = False
        self.group = None
        self.owner = None

    
    def finalize_options(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def run(self = None):
        commands = []
        for format in self.formats:
            commands.append(self.format_commands[format][0])
        for i in range(len(self.formats)):
            cmd_name = commands[i]
            sub_cmd = self.reinitialize_command(cmd_name)
            if cmd_name not in self.no_format_option:
                sub_cmd.format = self.formats[i]
            if cmd_name == 'bdist_dumb':
                sub_cmd.owner = self.owner
                sub_cmd.group = self.group
            if cmd_name in commands[i + 1:]:
                sub_cmd.keep_temp = True
            self.run_command(cmd_name)
        return None
        except KeyError:
            raise DistutilsOptionError(f'''invalid format \'{format}\'''')


