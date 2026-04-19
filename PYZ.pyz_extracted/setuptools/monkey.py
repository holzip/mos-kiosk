# Source Generated with Decompyle++
# File: monkey.pyc (Python 3.12)

'''
Monkey patching of distutils.
'''
from __future__ import annotations
import inspect
import platform
import sys
import types
from typing import TypeVar, cast, overload
import distutils.filelist as distutils
_T = TypeVar('_T')
_UnpatchT = TypeVar('_UnpatchT', type, types.FunctionType)
__all__: 'list[str]' = []

def _get_mro(cls):
    '''
    Returns the bases classes for cls sorted by the MRO.

    Works around an issue on Jython where inspect.getmro will not return all
    base classes if multiple classes share the same name. Instead, this
    function will return a tuple containing the class itself, and the contents
    of cls.__bases__. See https://github.com/pypa/setuptools/issues/1024.
    '''
    if platform.python_implementation() == 'Jython':
        return (cls,) + cls.__bases__
    return None.getmro(cls)

get_unpatched = (lambda item = None: pass)()
get_unpatched = (lambda item = None: pass)()

def get_unpatched(item = None):
    if isinstance(item, type):
        return get_unpatched_class(item)
    if None(item, types.FunctionType):
        return get_unpatched_function(item)


def get_unpatched_class(cls = None):
    '''Protect against re-patching the distutils if reloaded

    Also ensures that no other distutils extension monkeypatched the distutils
    first.
    '''
    external_bases = _get_mro(cls)()
    base = next(external_bases)
    if not base.__module__.startswith('distutils'):
        msg = f'''distutils has already been patched by {cls!r}'''
        raise AssertionError(msg)
    return base


def patch_all():
    import setuptools
    distutils.core.Command = setuptools.Command
    _patch_distribution_metadata()
    for module in (distutils.dist, distutils.core, distutils.cmd):
        module.Distribution = setuptools.dist.Distribution
    distutils.core.Extension = setuptools.extension.Extension
    distutils.extension.Extension = setuptools.extension.Extension
    if 'distutils.command.build_ext' in sys.modules:
        sys.modules['distutils.command.build_ext'].Extension = setuptools.extension.Extension
        return None


def _patch_distribution_metadata():
    _core_metadata = _core_metadata
    import 
    for attr in ('write_pkg_info', 'write_pkg_file', 'read_pkg_file', 'get_metadata_version', 'get_fullname'):
        new_val = getattr(_core_metadata, attr)
        setattr(distutils.dist.DistributionMetadata, attr, new_val)


def patch_func(replacement, target_mod, func_name):
    '''
    Patch func_name in target_mod with replacement

    Important - original must be resolved by name to avoid
    patching an already patched function.
    '''
    original = getattr(target_mod, func_name)
    vars(replacement).setdefault('unpatched', original)
    setattr(target_mod, func_name, replacement)


def get_unpatched_function(candidate):
    return candidate.unpatched

