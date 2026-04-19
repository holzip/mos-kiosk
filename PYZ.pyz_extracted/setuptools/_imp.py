# Source Generated with Decompyle++
# File: _imp.pyc (Python 3.12)

'''
Re-implementation of find_module and get_frozen_object
from the deprecated imp module.
'''
import importlib.machinery as importlib
import importlib.util as importlib
import os
import tokenize
from importlib.util import module_from_spec
PY_SOURCE = 1
PY_COMPILED = 2
C_EXTENSION = 3
C_BUILTIN = 6
PY_FROZEN = 7

def find_spec(module, paths):
    finder = importlib.machinery.PathFinder().find_spec if isinstance(paths, list) else importlib.util.find_spec
    return finder(module, paths)


def find_module(module, paths = (None,)):
    """Just like 'imp.find_module()', but with package support"""
    spec = find_spec(module, paths)
# WARNING: Decompyle incomplete


def get_frozen_object(module, paths = (None,)):
    spec = find_spec(module, paths)
    if not spec:
        raise ImportError(f'''Can\'t find {module}''')
    return spec.loader.get_code(module)


def get_module(module, paths, info):
    spec = find_spec(module, paths)
    if not spec:
        raise ImportError(f'''Can\'t find {module}''')
    return module_from_spec(spec)

