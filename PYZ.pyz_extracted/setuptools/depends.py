# Source Generated with Decompyle++
# File: depends.pyc (Python 3.12)

from __future__ import annotations
import contextlib
import dis
import marshal
import sys
from types import CodeType
from typing import Any, Literal, TypeVar
from packaging.version import Version
from  import _imp
from _imp import PY_COMPILED, PY_FROZEN, PY_SOURCE, find_module
_T = TypeVar('_T')
__all__ = [
    'Require',
    'find_module']

class Require:
    '''A prerequisite to building or installing a distribution'''
    
    def __init__(self, name, requested_version = None, module = None, homepage = None, attribute = ('', None, None), format = ('homepage', 'str', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def full_name(self):
        '''Return full package/distribution name, w/version'''
        pass
    # WARNING: Decompyle incomplete

    
    def version_ok(self, version):
        """Is 'version' sufficiently up-to-date?"""
        if not self.attribute is None:
            self.attribute is None
            if not self.format is None:
                self.format is None
                if str(version) != 'unknown':
                    str(version) != 'unknown'
        return self.format(version) >= self.requested_version

    
    def get_version(self = None, paths = None, default = None):
        """Get version number of installed module, 'None', or 'default'

        Search 'paths' for module.  If not found, return 'None'.  If found,
        return the extracted version attribute, or 'default' if no version
        attribute was specified, or the value cannot be determined without
        importing the module.  The version is formatted according to the
        requirement's version format (if any), unless it is 'None' or the
        supplied 'default'.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def is_present(self, paths = (None,)):
        """Return true if dependency is present on 'paths'"""
        return self.get_version(paths) is not None

    
    def is_current(self, paths = (None,)):
        """Return true if dependency is present and up-to-date on 'paths'"""
        version = self.get_version(paths)
    # WARNING: Decompyle incomplete



def maybe_close(f):
    empty = (lambda : pass# WARNING: Decompyle incomplete
)()
    if not f:
        return empty()
    return contextlib.contextmanager.closing(f)

if not sys.platform.startswith('java'):
    if sys.platform != 'cli':
        
        def get_module_constant(module = None, symbol = None, default = None, paths = (-1, None)):
            """Find 'module' by searching 'paths', and extract 'symbol'

        Return 'None' if 'module' does not exist on 'paths', or it does not define
        'symbol'.  If the module defines 'symbol' as a constant, return the
        constant.  Otherwise, return 'default'."""
            pass
        # WARNING: Decompyle incomplete

        
        def extract_constant(code = None, symbol = None, default = None):
            '''Extract the constant value of \'symbol\' from \'code\'

        If the name \'symbol\' is bound to a constant value by the Python code
        object \'code\', return that value.  If \'symbol\' is bound to an expression,
        return \'default\'.  Otherwise, return \'None\'.

        Return value is based on the first assignment to \'symbol\'.  \'symbol\' must
        be a global, or at least a non-"fast" local in the code block.  That is,
        only \'STORE_NAME\' and \'STORE_GLOBAL\' opcodes are checked, and \'symbol\'
        must be present in \'code.co_names\'.
        '''
            if symbol not in code.co_names:
                return None
            name_idx = list(code.co_names).index(symbol)
            STORE_NAME = dis.opmap['STORE_NAME']
            STORE_GLOBAL = dis.opmap['STORE_GLOBAL']
            LOAD_CONST = dis.opmap['LOAD_CONST']
            const = default
        # WARNING: Decompyle incomplete

        __all__ += [
            'get_module_constant',
            'extract_constant']
        return None
    return None
