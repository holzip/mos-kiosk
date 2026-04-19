# Source Generated with Decompyle++
# File: filelist.pyc (Python 3.12)

'''distutils.filelist

Provides the FileList class, used for poking about the filesystem
and building lists of files.
'''
from __future__ import annotations
import fnmatch
import functools
import os
import re
from collections.abc import Iterable
from typing import Literal, overload
from _log import log
from errors import DistutilsInternalError, DistutilsTemplateError
from util import convert_path

class FileList:
    """A list of files built by on exploring the filesystem and filtered by
    applying various patterns to what we find there.

    Instance attributes:
      dir
        directory from which files will be taken -- only used if
        'allfiles' not supplied to constructor
      files
        list of filenames currently being built/filtered/manipulated
      allfiles
        complete list of files under consideration (ie. without any
        filtering applied)
    """
    
    def __init__(self = None, warn = None, debug_print = None):
        self.allfiles = None
        self.files = []

    
    def set_allfiles(self = None, allfiles = None):
        self.allfiles = allfiles

    
    def findall(self = None, dir = None):
        self.allfiles = findall(dir)

    
    def debug_print(self = None, msg = None):
        """Print 'msg' to stdout if the global DEBUG (taken from the
        DISTUTILS_DEBUG environment variable) flag is true.
        """
        DEBUG = DEBUG
        import distutils.debug
        if DEBUG:
            print(msg)
            return None

    
    def append(self = None, item = None):
        self.files.append(item)

    
    def extend(self = None, items = None):
        self.files.extend(items)

    
    def sort(self = None):
        sortable_files = sorted(map(os.path.split, self.files))
        self.files = []
    # WARNING: Decompyle incomplete

    
    def remove_duplicates(self = None):
        for i in range(len(self.files) - 1, 0, -1):
            if not self.files[i] == self.files[i - 1]:
                continue
            del self.files[i]

    
    def _parse_template_line(self, line):
        words = line.split()
        action = words[0]
        patterns = None
        dir = None
        dir_pattern = None
    # WARNING: Decompyle incomplete

    
    def process_template_line(self = None, line = None):
        (action, patterns, dir, dir_pattern) = self._parse_template_line(line)
        if action == 'include':
            self.debug_print('include ' + ' '.join(patterns))
            for pattern in patterns:
                if self.include_pattern(pattern, anchor = True):
                    continue
                log.warning("warning: no files found matching '%s'", pattern)
            return None
        if action == 'exclude':
            self.debug_print('exclude ' + ' '.join(patterns))
            for pattern in patterns:
                if self.exclude_pattern(pattern, anchor = True):
                    continue
                log.warning("warning: no previously-included files found matching '%s'", pattern)
            return None
        if action == 'global-include':
            self.debug_print('global-include ' + ' '.join(patterns))
            for pattern in patterns:
                if self.include_pattern(pattern, anchor = False):
                    continue
                log.warning("warning: no files found matching '%s' anywhere in distribution", pattern)
            return None
        if action == 'global-exclude':
            self.debug_print('global-exclude ' + ' '.join(patterns))
            for pattern in patterns:
                if self.exclude_pattern(pattern, anchor = False):
                    continue
                log.warning("warning: no previously-included files matching '%s' found anywhere in distribution", pattern)
            return None
        if action == 'recursive-include':
            self.debug_print('recursive-include {} {}'.format(dir, ' '.join(patterns)))
            for pattern in patterns:
                if self.include_pattern(pattern, prefix = dir):
                    continue
                msg = "warning: no files found matching '%s' under directory '%s'"
                log.warning(msg, pattern, dir)
            return None
        if action == 'recursive-exclude':
            self.debug_print('recursive-exclude {} {}'.format(dir, ' '.join(patterns)))
            for pattern in patterns:
                if self.exclude_pattern(pattern, prefix = dir):
                    continue
                log.warning("warning: no previously-included files matching '%s' found under directory '%s'", pattern, dir)
            return None
        if action == 'graft':
            self.debug_print('graft ' + dir_pattern)
            if not self.include_pattern(None, prefix = dir_pattern):
                log.warning("warning: no directories found matching '%s'", dir_pattern)
                return None
            return None
        if action == 'prune':
            self.debug_print('prune ' + dir_pattern)
            if not self.exclude_pattern(None, prefix = dir_pattern):
                log.warning("no previously-included directories found matching '%s'", dir_pattern)
                return None
            return None
        raise DistutilsInternalError(f'''this cannot happen: invalid action \'{action}\'''')

    include_pattern = (lambda self = None, pattern = None, anchor = overload, prefix = (True, None, False), is_regex = ('pattern', 'str', 'anchor', 'bool', 'prefix', 'str | None', 'is_regex', 'Literal[False]', 'return', 'bool'): pass)()
    include_pattern = (lambda self = None, pattern = None, anchor = overload, prefix = (True, None), *, is_regex, 