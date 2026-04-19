# Source Generated with Decompyle++
# File: _serialization.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography import utils
from cryptography.hazmat.primitives.hashes import HashAlgorithm

class PBES(utils.Enum):
    PBESv1SHA1And3KeyTripleDESCBC = 'PBESv1 using SHA1 and 3-Key TripleDES'
    PBESv2SHA256AndAES256CBC = 'PBESv2 using SHA256 PBKDF2 and AES256 CBC'


class Encoding(utils.Enum):
    PEM = 'PEM'
    DER = 'DER'
    OpenSSH = 'OpenSSH'
    Raw = 'Raw'
    X962 = 'ANSI X9.62'
    SMIME = 'S/MIME'


class PrivateFormat(utils.Enum):
    PKCS8 = 'PKCS8'
    TraditionalOpenSSL = 'TraditionalOpenSSL'
    Raw = 'Raw'
    OpenSSH = 'OpenSSH'
    PKCS12 = 'PKCS12'
    
    def encryption_builder(self = None):
        if self not in (PrivateFormat.OpenSSH, PrivateFormat.PKCS12):
            raise ValueError('encryption_builder only supported with PrivateFormat.OpenSSH and PrivateFormat.PKCS12')
        return KeySerializationEncryptionBuilder(self)



class PublicFormat(utils.Enum):
    SubjectPublicKeyInfo = 'X.509 subjectPublicKeyInfo with PKCS#1'
    PKCS1 = 'Raw PKCS#1'
    OpenSSH = 'OpenSSH'
    Raw = 'Raw'
    CompressedPoint = 'X9.62 Compressed Point'
    UncompressedPoint = 'X9.62 Uncompressed Point'


class ParameterFormat(utils.Enum):
    PKCS3 = 'PKCS3'


def KeySerializationEncryption():
    '''KeySerializationEncryption'''
    pass

KeySerializationEncryption = <NODE:27>(KeySerializationEncryption, 'KeySerializationEncryption', metaclass = abc.ABCMeta)

class BestAvailableEncryption(KeySerializationEncryption):
    
    def __init__(self = None, password = None):
        if isinstance(password, bytes) or len(password) == 0:
            raise ValueError('Password must be 1 or more bytes.')
        self.password = password



class NoEncryption(KeySerializationEncryption):
    pass


class KeySerializationEncryptionBuilder:
    
    def __init__(self = None, format = None, *, _kdf_rounds, _hmac_hash, _key_cert_algorithm):
        self._format = format
        self._kdf_rounds = _kdf_rounds
        self._hmac_hash = _hmac_hash
        self._key_cert_algorithm = _key_cert_algorithm

    
    def kdf_rounds(self = None, rounds = None):
        pass
    # WARNING: Decompyle incomplete

    
    def hmac_hash(self = None, algorithm = None):
        if self._format is not PrivateFormat.PKCS12:
            raise TypeError('hmac_hash only supported with PrivateFormat.PKCS12')
    # WARNING: Decompyle incomplete

    
    def key_cert_algorithm(self = None, algorithm = None):
        if self._format is not PrivateFormat.PKCS12:
            raise TypeError('key_cert_algorithm only supported with PrivateFormat.PKCS12')
    # WARNING: Decompyle incomplete

    
    def build(self = None, password = None):
        if isinstance(password, bytes) or len(password) == 0:
            raise ValueError('Password must be 1 or more bytes.')
        return _KeySerializationEncryption(self._format, password, kdf_rounds = self._kdf_rounds, hmac_hash = self._hmac_hash, key_cert_algorithm = self._key_cert_algorithm)



class _KeySerializationEncryption(KeySerializationEncryption):
    
    def __init__(self = None, format = None, password = None, *, kdf_rounds, hmac_hash, key_cert_algorithm):
        self._format = format
        self.password = password
        self._kdf_rounds = kdf_rounds
        self._hmac_hash = hmac_hash
        self._key_cert_algorithm = key_cert_algorithm


