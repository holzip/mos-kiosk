# Source Generated with Decompyle++
# File: binding.pyc (Python 3.12)

from __future__ import annotations
import os
import sys
import threading
import types
import typing
import warnings
from collections.abc import Callable
import cryptography
from cryptography.exceptions import InternalError
from cryptography.hazmat.bindings._rust import _openssl, openssl
from cryptography.hazmat.bindings.openssl._conditional import CONDITIONAL_NAMES
from cryptography.utils import CryptographyDeprecationWarning

def _openssl_assert(ok = None):
    if not ok:
        errors = openssl.capture_error_stack()
        raise InternalError(f'''Unknown OpenSSL error. This error is commonly encountered when another library is not cleaning up the OpenSSL error stack. If you are using cryptography with another library that uses OpenSSL try disabling it before reporting a bug. Otherwise please file an issue at https://github.com/pyca/cryptography/issues with information on how to reproduce this. ({errors!r})''', errors)


def build_conditional_library(lib = None, conditional_names = None):
    conditional_lib = types.ModuleType('lib')
    conditional_lib._original_lib = lib
    excluded_names = set()
    for condition, names_cb in conditional_names.items():
        if getattr(lib, condition):
            continue
        excluded_names.update(names_cb())
    for attr in dir(lib):
        if not attr not in excluded_names:
            continue
        setattr(conditional_lib, attr, getattr(lib, attr))
    return conditional_lib


class Binding:
    '''
    OpenSSL API wrapper.
    '''
    lib: 'typing.ClassVar[typing.Any]' = None
    ffi = _openssl.ffi
    _lib_loaded = False
    _init_lock = threading.Lock()
    
    def __init__(self = None):
        self._ensure_ffi_initialized()

    _ensure_ffi_initialized = (lambda cls = None: cls._init_lockif not cls._lib_loaded:
cls.lib = build_conditional_library(_openssl.lib, CONDITIONAL_NAMES)cls._lib_loaded = TrueNone(None, None)Nonewith None:
if not None:
pass)()
    init_static_locks = (lambda cls = None: cls._ensure_ffi_initialized())()


def _verify_package_version(version = None):
    so_package_version = _openssl.ffi.string(_openssl.lib.CRYPTOGRAPHY_PACKAGE_VERSION)
    if version.encode('ascii') != so_package_version:
        raise ImportError(f'''The version of cryptography does not match the loaded shared object. This can happen if you have multiple copies of cryptography installed in your Python path. Please try creating a new virtual environment to resolve this issue. Loaded python version: {version}, shared object version: {so_package_version}''')
    _openssl_assert(_openssl.lib.OpenSSL_version_num() == openssl.openssl_version())

_verify_package_version(cryptography.__version__)
Binding.init_static_locks()
# WARNING: Decompyle incomplete
