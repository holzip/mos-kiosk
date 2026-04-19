# Source Generated with Decompyle++
# File: build.pyc (Python 3.12)

"""distutils.command.build

Implements the Distutils 'build' command."""
from __future__ import annotations
import os
import sys
import sysconfig
from collections.abc import Callable
from typing import ClassVar
from ccompiler import show_compilers
from core import Command
from errors import DistutilsOptionError
from util import get_platform

class build(Command):
    description = 'build everything needed to install'
    user_options = [
        ('build-base=', 'b', 'base directory for build library'),
        ('build-purelib=', None, 'build directory for platform-neutral distributions'),
        ('build-platlib=', None, 'build directory for platform-specific distributions'),
        ('build-lib=', None, 'build directory for all distribution (defaults to either build-purelib or build-platlib'),
        ('build-scripts=', None, 'build directory for scripts'),
        ('build-temp=', 't', 'temporary build directory'),
        ('plat-name=', 'p', f'''platform name to build for, if supported [default: {get_platform()}]'''),
        ('compiler=', 'c', 'specify the compiler type'),
        ('parallel=', 'j', 'number of parallel build jobs'),
        ('debug', 'g', 'compile extensions and libraries with debugging information'),
        ('force', 'f', 'forcibly build everything (ignore file timestamps)'),
        ('executable=', 'e', 'specify final destination interpreter path (build.py)')]
    boolean_options: 'ClassVar[list[str]]' = [
        'debug',
        'force']
    help_options: 'ClassVar[list[tuple[str, str | None, str, Callable[[], object]]]]' = [
        ('help-compiler', None, 'list available compilers', show_compilers)]
    
    def initialize_options(self):
        self.build_base = 'build'
        self.build_purelib = None
        self.build_platlib = None
        self.build_lib = None
        self.build_temp = None
        self.build_scripts = None
        self.compiler = None
        self.plat_name = None
        self.debug = None
        self.force = False
        self.executable = None
        self.parallel = None

    
    def finalize_options(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def run(self = None):
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

    
    def has_pure_modules(self):
        return self.distribution.has_pure_modules()

    
    def has_c_libraries(self):
        return self.distribution.has_c_libraries()

    
    def has_ext_modules(self):
        return self.distribution.has_ext_modules()

    
    def has_scripts(self):
        return self.distribution.has_scripts()

    sub_commands = [
        ('build_py', has_pure_modules),
        ('build_clib', has_c_libraries),
        ('build_ext', has_ext_modules),
        ('build_scripts', has_scripts)]

