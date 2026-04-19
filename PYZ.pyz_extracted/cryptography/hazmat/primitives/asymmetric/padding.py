# Source Generated with Decompyle++
# File: padding.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives._asymmetric import AsymmetricPadding
from cryptography.hazmat.primitives.asymmetric import rsa

class PKCS1v15(AsymmetricPadding):
    name = 'EMSA-PKCS1-v1_5'


class _MaxLength:
    '''Sentinel value for `MAX_LENGTH`.'''
    pass


class _Auto:
    '''Sentinel value for `AUTO`.'''
    pass


class _DigestLength:
    '''Sentinel value for `DIGEST_LENGTH`.'''
    pass


class PSS(AsymmetricPadding):
    MAX_LENGTH = _MaxLength()
    AUTO = _Auto()
    DIGEST_LENGTH = _DigestLength()
    _salt_length: 'int | _MaxLength | _Auto | _DigestLength' = 'EMSA-PSS'
    
    def __init__(self = None, mgf = None, salt_length = None):
        self._mgf = mgf
        if not isinstance(salt_length, (int, _MaxLength, _Auto, _DigestLength)):
            raise TypeError('salt_length must be an integer, MAX_LENGTH, DIGEST_LENGTH, or AUTO')
        if isinstance(salt_length, int) and salt_length < 0:
            raise ValueError('salt_length must be zero or greater.')
        self._salt_length = salt_length

    mgf = (lambda self = None: self._mgf)()


class OAEP(AsymmetricPadding):
    name = 'EME-OAEP'
    
    def __init__(self = None, mgf = None, algorithm = None, label = ('mgf', 'MGF', 'algorithm', 'hashes.HashAlgorithm', 'label', 'bytes | None')):
        if not isinstance(algorithm, hashes.HashAlgorithm):
            raise TypeError('Expected instance of hashes.HashAlgorithm.')
        self._mgf = mgf
        self._algorithm = algorithm
        self._label = label

    algorithm = (lambda self = None: self._algorithm)()
    mgf = (lambda self = None: self._mgf)()


def MGF():
    '''MGF'''
    _algorithm: 'hashes.HashAlgorithm' = 'MGF'

MGF = <NODE:27>(MGF, 'MGF', metaclass = abc.ABCMeta)

class MGF1(MGF):
    
    def __init__(self = None, algorithm = None):
        if not isinstance(algorithm, hashes.HashAlgorithm):
            raise TypeError('Expected instance of hashes.HashAlgorithm.')
        self._algorithm = algorithm



def calculate_max_pss_salt_length(key = None, hash_algorithm = None):
    if not isinstance(key, (rsa.RSAPrivateKey, rsa.RSAPublicKey)):
        raise TypeError('key must be an RSA public or private key')
    emlen = (key.key_size + 6) // 8
    salt_length = emlen - hash_algorithm.digest_size - 2
# WARNING: Decompyle incomplete

