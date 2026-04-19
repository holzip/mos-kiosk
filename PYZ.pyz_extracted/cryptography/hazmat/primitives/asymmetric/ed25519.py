# Source Generated with Decompyle++
# File: ed25519.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography.exceptions import UnsupportedAlgorithm, _Reasons
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.primitives import _serialization
from cryptography.utils import Buffer

def Ed25519PublicKey():
    '''Ed25519PublicKey'''
    from_public_bytes = (lambda cls = None, data = None: backend = backendimport cryptography.hazmat.backends.openssl.backendif not backend.ed25519_supported():
raise UnsupportedAlgorithm('ed25519 is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_PUBLIC_KEY_ALGORITHM)rust_openssl.ed25519.from_public_bytes(data))()
    public_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod: pass)()
    public_bytes_raw = (lambda self = None: pass)()
    verify = (lambda self = None, signature = None, data = abc.abstractmethod: pass)()
    __eq__ = (lambda self = None, other = None: pass)()
    __copy__ = (lambda self = None: pass)()

Ed25519PublicKey = <NODE:27>(Ed25519PublicKey, 'Ed25519PublicKey', metaclass = abc.ABCMeta)
Ed25519PublicKey.register(rust_openssl.ed25519.Ed25519PublicKey)

def Ed25519PrivateKey():
    '''Ed25519PrivateKey'''
    generate = (lambda cls = None: backend = backendimport cryptography.hazmat.backends.openssl.backendif not backend.ed25519_supported():
raise UnsupportedAlgorithm('ed25519 is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_PUBLIC_KEY_ALGORITHM)rust_openssl.ed25519.generate_key())()
    from_private_bytes = (lambda cls = None, data = None: backend = backendimport cryptography.hazmat.backends.openssl.backendif not backend.ed25519_supported():
raise UnsupportedAlgorithm('ed25519 is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_PUBLIC_KEY_ALGORITHM)rust_openssl.ed25519.from_private_bytes(data))()
    public_key = (lambda self = None: pass)()
    private_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod, encryption_algorithm = ('encoding', '_serialization.Encoding', 'format', '_serialization.PrivateFormat', 'encryption_algorithm', '_serialization.KeySerializationEncryption', 'return', 'bytes'): pass)()
    private_bytes_raw = (lambda self = None: pass)()
    sign = (lambda self = None, data = None: pass)()
    __copy__ = (lambda self = None: pass)()

Ed25519PrivateKey = <NODE:27>(Ed25519PrivateKey, 'Ed25519PrivateKey', metaclass = abc.ABCMeta)
Ed25519PrivateKey.register(rust_openssl.ed25519.Ed25519PrivateKey)
