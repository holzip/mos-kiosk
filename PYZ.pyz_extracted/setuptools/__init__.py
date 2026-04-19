# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

"""Extensions to the 'distutils' for large or complex distributions"""
from __future__ import annotations
import functools
import os
import re
import sys
from abc import abstractmethod
from collections.abc import Mapping
from typing import TYPE_CHECKING, TypeVar, overload
vendor_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'setuptools', '_vendor')
sys.path.extend((os.path.join(os.path.dirname(os.path.dirname(__file__)), 'setuptools', '_vendor') not in sys.path) * [
    vendor_path])
sys.modules.pop('backports', None)
import _distutils_hack.override as _distutils_hack
from  import logging, monkey
from depends import Require
from discovery import PackageFinder, PEP420PackageFinder
from dist import Distribution
from extension import Extension
from version import __version__
from warnings import SetuptoolsDeprecationWarning
import distutils.core as distutils
from distutils.errors import DistutilsOptionError
__all__ = [
    'setup',
    'Distribution',
    'Command',
    'Extension',
    'Require',
    'SetuptoolsDeprecationWarning',
    'find_packages',
    'find_namespace_packages']
_CommandT = TypeVar('_CommandT', bound = '_Command')
bootstrap_install_from = None
find_packages = PackageFinder.find
find_namespace_packages = PEP420PackageFinder.find

def _install_setup_requires(attrs):
    
    class MinimalDistribution(distutils.core.Distribution):
        pass
    # WARNING: Decompyle incomplete

    dist = MinimalDistribution(attrs)
    dist.parse_config_files(ignore_option_errors = True)
    if dist.setup_requires:
        _fetch_build_eggs(dist)
        return None


def _fetch_build_eggs(dist = None):
    
    try:
        dist.fetch_build_eggs(dist.setup_requires)
        return None
    except Exception:
        ex = None
        msg = "\n        It is possible a package already installed in your system\n        contains an version that is invalid according to PEP 440.\n        You can try `pip install --use-pep517` as a workaround for this problem,\n        or rely on a new virtual environment.\n\n        If the problem refers to a package that is not installed yet,\n        please contact that package's maintainers or distributors.\n        "
        if 'InvalidVersion' in ex.__class__.__name__:
            if hasattr(ex, 'add_note'):
                ex.add_note(msg)
                raise 
            dist.announce(f'''\n{msg}\n''')
        raise 
        ex = None
        del ex



def setup(**attrs):
    logging.configure()
    _install_setup_requires(attrs)
# WARNING: Decompyle incomplete

setup.__doc__ = distutils.core.setup.__doc__
if TYPE_CHECKING:
    from distutils.core import Command as _Command
else:
    _Command = monkey.get_unpatched(distutils.core.Command)

class Command(_Command):
    pass
# WARNING: Decompyle incomplete


def _find_all_simple(path):
    """
    Find all files under 'path'
    """
    results = os.walk(path, followlinks = True)()
    return filter(os.path.isfile, results)


def findall(dir = (os.curdir,)):
    """
    Find all files under 'dir' and return the list of full filenames.
    Unless dir is '.', return full filenames with dir prepended.
    """
    files = _find_all_simple(dir)
    if dir == os.curdir:
        make_rel = functools.partial(os.path.relpath, start = dir)
        files = map(make_rel, files)
    return list(files)


class sic(str):
    '''Treat this string as-is (https://en.wikipedia.org/wiki/Sic)'''
    pass

monkey.patch_all()
