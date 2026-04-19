# Source Generated with Decompyle++
# File: readers.pyc (Python 3.12)

import collections
import itertools
import pathlib
import operator
import zipfile
from  import abc
from _itertools import only

def remove_duplicates(items):
    return iter(collections.OrderedDict.fromkeys(items))


class FileReader(abc.TraversableResources):
    
    def __init__(self, loader):
        self.path = pathlib.Path(loader.path).parent

    
    def resource_path(self, resource):
        '''
        Return the file system path to prevent
        `resources.path()` from creating a temporary
        copy.
        '''
        return str(self.path.joinpath(resource))

    
    def files(self):
        return self.path



class ZipReader(abc.TraversableResources):
    pass
# WARNING: Decompyle incomplete


class MultiplexedPath(abc.Traversable):
    pass
# WARNING: Decompyle incomplete


class NamespaceReader(abc.TraversableResources):
    
    def __init__(self, namespace_path):
        if 'NamespacePath' not in str(namespace_path):
            raise ValueError('Invalid path')
    # WARNING: Decompyle incomplete

    
    def resource_path(self, resource):
        '''
        Return the file system path to prevent
        `resources.path()` from creating a temporary
        copy.
        '''
        return str(self.path.joinpath(resource))

    
    def files(self):
        return self.path


