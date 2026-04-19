# Source Generated with Decompyle++
# File: x448.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography.exceptions import UnsupportedAlgorithm, _Reasons
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.primitives import _serialization
from cryptography.utils import Buffer

def X448PublicKey():
    '''X448PublicKey'''
    from_public_bytes = (lambda cls = None, data = None: backend = backendimport cryptography.hazmat.backends.openssl.backendif not backend.x448_supported():
raise UnsupportedAlgorithm('X448 is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_EXCHANGE_ALGORITHM)rust_openssl.x448.from_public_bytes(data))()
    public_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod: pass)()
    public_bytes_raw = (lambda self = None: pass)()
    __eq__ = (lambda self = None, other = None: pass)()
    __copy__ = (lambda self = None: pass)()

X448PublicKey = <NODE:27>(X448PublicKey, 'X448PublicKey', metaclass = abc.ABCMeta)
if hasattr(rust_openssl, 'x448'):
    X448PublicKey.register(rust_openssl.x448.X448PublicKey)

def X448PrivateKey():
    '''X448PrivateKey'''
    generate = (lambda cls = None: backend = backendimport cryptography.hazmat.backends.openssl.backendif not backend.x448_supported():
raise UnsupportedAlgorithm('X448 is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_EXCHANGE_ALGORITHM)rust_openssl.x448.generate_key())()
    from_private_bytes = (lambda cls = None, data = None: backend = backendimport cryptography.hazmat.backends.openssl.backendif not backend.x448_supported():
raise UnsupportedAlgorithm('X448 is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_EXCHANGE_ALGORITHM)rust_openssl.x448.from_private_bytes(data))()
    public_key = (lambda self = None: pass)()
    private_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod, encryption_algorithm = ('encoding', '_serialization.Encoding', 'format', '_serialization.PrivateFormat', 'encryption_algorithm', '_serialization.KeySerializationEncryption', 'return', 'bytes'): pass)()
    private_bytes_raw = (lambda self = None: pass)()
    exchange = (lambda self = None, peer_public_key = None: pass)()
    __copy__ = (lambda self = None: pass)()

X448PrivateKey = <NODE:27>(X448PrivateKey, 'X448PrivateKey', metaclass = abc.ABCMeta)
if hasattr(rust_openssl, 'x448'):
    X448PrivateKey.register(rust_openssl.x448.X448PrivateKey)
    return None
