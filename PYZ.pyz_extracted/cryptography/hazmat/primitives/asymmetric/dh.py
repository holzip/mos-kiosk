# Source Generated with Decompyle++
# File: dh.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.primitives import _serialization
generate_parameters = rust_openssl.dh.generate_parameters
DHPrivateNumbers = rust_openssl.dh.DHPrivateNumbers
DHPublicNumbers = rust_openssl.dh.DHPublicNumbers
DHParameterNumbers = rust_openssl.dh.DHParameterNumbers

def DHParameters():
    '''DHParameters'''
    generate_private_key = (lambda self = None: pass)()
    parameter_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod: pass)()
    parameter_numbers = (lambda self = None: pass)()

DHParameters = <NODE:27>(DHParameters, 'DHParameters', metaclass = abc.ABCMeta)
DHParametersWithSerialization = DHParameters
DHParameters.register(rust_openssl.dh.DHParameters)

def DHPublicKey():
    '''DHPublicKey'''
    key_size = (lambda self = None: pass)()()
    parameters = (lambda self = None: pass)()
    public_numbers = (lambda self = None: pass)()
    public_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod: pass)()
    __eq__ = (lambda self = None, other = None: pass)()
    __copy__ = (lambda self = None: pass)()

DHPublicKey = <NODE:27>(DHPublicKey, 'DHPublicKey', metaclass = abc.ABCMeta)
DHPublicKeyWithSerialization = DHPublicKey
DHPublicKey.register(rust_openssl.dh.DHPublicKey)

def DHPrivateKey():
    '''DHPrivateKey'''
    key_size = (lambda self = None: pass)()()
    public_key = (lambda self = None: pass)()
    parameters = (lambda self = None: pass)()
    exchange = (lambda self = None, peer_public_key = None: pass)()
    private_numbers = (lambda self = None: pass)()
    private_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod, encryption_algorithm = ('encoding', '_serialization.Encoding', 'format', '_serialization.PrivateFormat', 'encryption_algorithm', '_serialization.KeySerializationEncryption', 'return', 'bytes'): pass)()
    __copy__ = (lambda self = None: pass)()

DHPrivateKey = <NODE:27>(DHPrivateKey, 'DHPrivateKey', metaclass = abc.ABCMeta)
DHPrivateKeyWithSerialization = DHPrivateKey
DHPrivateKey.register(rust_openssl.dh.DHPrivateKey)
