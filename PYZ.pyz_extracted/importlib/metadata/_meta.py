# Source Generated with Decompyle++
# File: _meta.pyc (Python 3.12)

from typing import Protocol
from typing import Any, Dict, Iterator, List, Optional, TypeVar, Union, overload
_T = TypeVar('_T')

class PackageMetadata(Protocol):
    
    def __len__(self = None):
        pass

    
    def __contains__(self = None, item = None):
        pass

    
    def __getitem__(self = None, key = None):
        pass

    
    def __iter__(self = None):
        pass

    get = (lambda self = None, name = None, failobj = overload: pass)()
    get = (lambda self = None, name = None, failobj = overload: pass)()
    get_all = (lambda self = None, name = None, failobj = overload: pass)()
    get_all = (lambda self = None, name = None, failobj = overload: pass)()
    json = (lambda self = None: pass)()


def SimplePath():
    '''SimplePath'''
    __doc__ = '\n    A minimal subset of pathlib.Path required by PathDistribution.\n    '
    
    def joinpath(self = None):
        pass

    
    def __truediv__(self = None, other = None):
        pass

    parent = (lambda self = None: pass)()
    
    def read_text(self = None):
        pass


SimplePath = <NODE:27>(SimplePath, 'SimplePath', Protocol[_T])
