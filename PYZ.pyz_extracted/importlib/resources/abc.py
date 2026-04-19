# Source Generated with Decompyle++
# File: abc.pyc (Python 3.12)

import abc
import io
import itertools
import os
import pathlib
from typing import Any, BinaryIO, Iterable, Iterator, NoReturn, Text, Optional
from typing import runtime_checkable, Protocol
from typing import Union
StrPath = Union[(str, os.PathLike[str])]
__all__ = [
    'ResourceReader',
    'Traversable',
    'TraversableResources']

def ResourceReader():
    '''ResourceReader'''
    __doc__ = 'Abstract base class for loaders to provide resource reading support.'
    open_resource = (lambda self = None, resource = None: raise FileNotFoundError)()
    resource_path = (lambda self = None, resource = None: raise FileNotFoundError)()
    is_resource = (lambda self = None, path = None: raise FileNotFoundError)()
    contents = (lambda self = None: raise FileNotFoundError)()

ResourceReader = <NODE:27>(ResourceReader, 'ResourceReader', metaclass = abc.ABCMeta)

class TraversalError(Exception):
    pass

Traversable = <NODE:12>()

class TraversableResources(ResourceReader):
    '''
    The required interface for providing traversable
    resources.
    '''
    files = (lambda self = None: pass)()
    
    def open_resource(self = None, resource = None):
        return self.files().joinpath(resource).open('rb')

    
    def resource_path(self = None, resource = None):
        raise FileNotFoundError(resource)

    
    def is_resource(self = None, path = None):
        return self.files().joinpath(path).is_file()

    
    def contents(self = None):
        return self.files().iterdir()()


