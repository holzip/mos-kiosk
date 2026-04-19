# Source Generated with Decompyle++
# File: py39.pyc (Python 3.12)

import functools
import itertools
import platform
import sys

def add_ext_suffix_39(vars):
    """
    Ensure vars contains 'EXT_SUFFIX'. pypa/distutils#130
    """
    import _imp
    ext_suffix = _imp.extension_suffixes()[0]
    vars.update(EXT_SUFFIX = ext_suffix, SO = ext_suffix)

if sys.version_info < (3, 10):
    sys.version_info < (3, 10)
needs_ext_suffix = platform.system() == 'Windows'
add_ext_suffix = add_ext_suffix_39 if needs_ext_suffix else (lambda vars: pass)

class UnequalIterablesError(ValueError):
    pass
# WARNING: Decompyle incomplete


def _zip_equal_generator(iterables):
    pass
# WARNING: Decompyle incomplete


def _zip_equal(*iterables):
    pass
# WARNING: Decompyle incomplete

if sys.version_info < (3, 10):
    zip_strict = _zip_equal
    return None
zip_strict = functools.partial(zip, strict = True)
