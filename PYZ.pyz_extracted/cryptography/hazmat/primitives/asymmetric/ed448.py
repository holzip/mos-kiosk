# Source Generated with Decompyle++
# File: ed448.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography.exceptions import UnsupportedAlgorithm, _Reasons
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.primitives import _serialization
from cryptography.utils import Buffer

def Ed448PublicKey():
    '''Ed448PublicKey'''
    from_public_bytes = (lambda cls = None, data = None: backend = backendimport cryptography.hazmat.backends.openssl.backendif not backend.ed448_supported():
raise UnsupportedAlgorithm('ed448 is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_PUBLIC_KEY_ALGORITHM)rust_openssl.ed448.from_public_bytes(data))()
    public_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod: pass)()
    public_bytes_raw = (lambda self = None: pass)()
    verify = (lambda self = None, signature = None, data = abc.abstractmethod: pass)()
    __eq__ = (lambda self = None, other = None: pass)()
    __copy__ = (lambda self = None: pass)()

Ed448PublicKey = <NODE:27>(Ed448PublicKey, 'Ed448PublicKey', metaclass = abc.ABCMeta)
if hasattr(rust_openssl, 'ed448'):
    Ed448PublicKey.register(rust_openssl.ed448.Ed448PublicKey)

def Ed448PrivateKey():
    '''Ed448PrivateKey'''
    generate = (lambda cls = None: backend = backendimport cryptography.hazmat.backends.openssl.backendif not backend.ed448_supported():
raise UnsupportedAlgorithm('ed448 is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_PUBLIC_KEY_ALGORITHM)rust_openssl.ed448.generate_key())()
    from_private_bytes = (lambda cls = None, data = None: backend = backendimport cryptography.hazmat.backends.openssl.backendif not backend.ed448_supported():
raise UnsupportedAlgorithm('ed448 is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_PUBLIC_KEY_ALGORITHM)rust_openssl.ed448.from_private_bytes(data))()
    public_key = (lambda self = None: pass)()
    sign = (lambda self = None, data = None: pass)()
    private_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod, encryption_algorithm = ('encoding', '_serialization.Encoding', 'format', '_serialization.PrivateFormat', 'encryption_algorithm', '_serialization.KeySerializationEncryption', 'return', 'bytes'): pass)()
    private_bytes_raw = (lambda self = None: pass)()
    __copy__ = (lambda self = None: pass)()

Ed448PrivateKey = <NODE:27>(Ed448PrivateKey, 'Ed448PrivateKey', metaclass = abc.ABCMeta)
if hasattr(rust_openssl, 'x448'):
    Ed448PrivateKey.register(rust_openssl.ed448.Ed448PrivateKey)
    return None
