# Source Generated with Decompyle++
# File: dsa.pyc (Python 3.12)

from __future__ import annotations
import abc
import typing
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.primitives import _serialization, hashes
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils
from cryptography.utils import Buffer

def DSAParameters():
    '''DSAParameters'''
    generate_private_key = (lambda self = None: pass)()
    parameter_numbers = (lambda self = None: pass)()

DSAParameters = <NODE:27>(DSAParameters, 'DSAParameters', metaclass = abc.ABCMeta)
DSAParametersWithNumbers = DSAParameters
DSAParameters.register(rust_openssl.dsa.DSAParameters)

def DSAPrivateKey():
    '''DSAPrivateKey'''
    key_size = (lambda self = None: pass)()()
    public_key = (lambda self = None: pass)()
    parameters = (lambda self = None: pass)()
    sign = (lambda self = None, data = None, algorithm = abc.abstractmethod: pass)()
    private_numbers = (lambda self = None: pass)()
    private_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod, encryption_algorithm = ('encoding', '_serialization.Encoding', 'format', '_serialization.PrivateFormat', 'encryption_algorithm', '_serialization.KeySerializationEncryption', 'return', 'bytes'): pass)()
    __copy__ = (lambda self = None: pass)()

DSAPrivateKey = <NODE:27>(DSAPrivateKey, 'DSAPrivateKey', metaclass = abc.ABCMeta)
DSAPrivateKeyWithSerialization = DSAPrivateKey
DSAPrivateKey.register(rust_openssl.dsa.DSAPrivateKey)

def DSAPublicKey():
    '''DSAPublicKey'''
    key_size = (lambda self = None: pass)()()
    parameters = (lambda self = None: pass)()
    public_numbers = (lambda self = None: pass)()
    public_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod: pass)()
    verify = (lambda self = None, signature = None, data = abc.abstractmethod, algorithm = ('signature', 'Buffer', 'data', 'Buffer', 'algorithm', 'asym_utils.Prehashed | hashes.HashAlgorithm', 'return', 'None'): pass)()
    __eq__ = (lambda self = None, other = None: pass)()
    __copy__ = (lambda self = None: pass)()

DSAPublicKey = <NODE:27>(DSAPublicKey, 'DSAPublicKey', metaclass = abc.ABCMeta)
DSAPublicKeyWithSerialization = DSAPublicKey
DSAPublicKey.register(rust_openssl.dsa.DSAPublicKey)
DSAPrivateNumbers = rust_openssl.dsa.DSAPrivateNumbers
DSAPublicNumbers = rust_openssl.dsa.DSAPublicNumbers
DSAParameterNumbers = rust_openssl.dsa.DSAParameterNumbers

def generate_parameters(key_size = None, backend = None):
    if key_size not in (1024, 2048, 3072, 4096):
        raise ValueError('Key size must be 1024, 2048, 3072, or 4096 bits.')
    return rust_openssl.dsa.generate_parameters(key_size)


def generate_private_key(key_size = None, backend = None):
    parameters = generate_parameters(key_size)
    return parameters.generate_private_key()

