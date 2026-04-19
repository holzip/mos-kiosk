# Source Generated with Decompyle++
# File: base.pyc (Python 3.12)

from __future__ import annotations
import abc
import typing
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.primitives._cipheralgorithm import CipherAlgorithm
from cryptography.hazmat.primitives.ciphers import modes
from cryptography.utils import Buffer

def CipherContext():
    '''CipherContext'''
    update = (lambda self = None, data = None: pass)()
    update_into = (lambda self = None, data = None, buf = abc.abstractmethod: pass)()
    finalize = (lambda self = None: pass)()
    reset_nonce = (lambda self = None, nonce = None: pass)()

CipherContext = <NODE:27>(CipherContext, 'CipherContext', metaclass = abc.ABCMeta)

def AEADCipherContext():
    '''AEADCipherContext'''
    authenticate_additional_data = (lambda self = None, data = None: pass)()

AEADCipherContext = <NODE:27>(AEADCipherContext, 'AEADCipherContext', CipherContext, metaclass = abc.ABCMeta)

def AEADDecryptionContext():
    '''AEADDecryptionContext'''
    finalize_with_tag = (lambda self = None, tag = None: pass)()

AEADDecryptionContext = <NODE:27>(AEADDecryptionContext, 'AEADDecryptionContext', AEADCipherContext, metaclass = abc.ABCMeta)

def AEADEncryptionContext():
    '''AEADEncryptionContext'''
    tag = (lambda self = None: pass)()()

AEADEncryptionContext = <NODE:27>(AEADEncryptionContext, 'AEADEncryptionContext', AEADCipherContext, metaclass = abc.ABCMeta)
Mode = typing.TypeVar('Mode', bound = typing.Optional[modes.Mode], covariant = True)

def Cipher():
    '''Cipher'''
    
    def __init__(self = None, algorithm = None, mode = None, backend = (None,)):
        if not isinstance(algorithm, CipherAlgorithm):
            raise TypeError('Expected interface of CipherAlgorithm.')
    # WARNING: Decompyle incomplete

    encryptor = (lambda self = None: pass)()
    encryptor = (lambda self = None: pass)()
    
    def encryptor(self):
        pass
    # WARNING: Decompyle incomplete

    decryptor = (lambda self = None: pass)()
    decryptor = (lambda self = None: pass)()
    
    def decryptor(self):
        return rust_openssl.ciphers.create_decryption_ctx(self.algorithm, self.mode)


Cipher = <NODE:27>(Cipher, 'Cipher', typing.Generic[Mode])
_CIPHER_TYPE = Cipher[typing.Union[(modes.ModeWithNonce, modes.ModeWithTweak, modes.ECB, modes.ModeWithInitializationVector, None)]]
CipherContext.register(rust_openssl.ciphers.CipherContext)
AEADEncryptionContext.register(rust_openssl.ciphers.AEADEncryptionContext)
AEADDecryptionContext.register(rust_openssl.ciphers.AEADDecryptionContext)
