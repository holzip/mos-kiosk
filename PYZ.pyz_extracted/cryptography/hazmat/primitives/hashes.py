# Source Generated with Decompyle++
# File: hashes.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.utils import Buffer
__all__ = [
    'MD5',
    'SHA1',
    'SHA3_224',
    'SHA3_256',
    'SHA3_384',
    'SHA3_512',
    'SHA224',
    'SHA256',
    'SHA384',
    'SHA512',
    'SHA512_224',
    'SHA512_256',
    'SHAKE128',
    'SHAKE256',
    'SM3',
    'BLAKE2b',
    'BLAKE2s',
    'ExtendableOutputFunction',
    'Hash',
    'HashAlgorithm',
    'HashContext',
    'XOFHash']

def HashAlgorithm():
    '''HashAlgorithm'''
    name = (lambda self = None: pass)()()
    digest_size = (lambda self = None: pass)()()
    block_size = (lambda self = None: pass)()()

HashAlgorithm = <NODE:27>(HashAlgorithm, 'HashAlgorithm', metaclass = abc.ABCMeta)

def HashContext():
    '''HashContext'''
    algorithm = (lambda self = None: pass)()()
    update = (lambda self = None, data = None: pass)()
    finalize = (lambda self = None: pass)()
    copy = (lambda self = None: pass)()

HashContext = <NODE:27>(HashContext, 'HashContext', metaclass = abc.ABCMeta)
Hash = rust_openssl.hashes.Hash
HashContext.register(Hash)
XOFHash = rust_openssl.hashes.XOFHash

def ExtendableOutputFunction():
    '''ExtendableOutputFunction'''
    __doc__ = '\n    An interface for extendable output functions.\n    '

ExtendableOutputFunction = <NODE:27>(ExtendableOutputFunction, 'ExtendableOutputFunction', metaclass = abc.ABCMeta)

class SHA1(HashAlgorithm):
    name = 'sha1'
    digest_size = 20
    block_size = 64


class SHA512_224(HashAlgorithm):
    name = 'sha512-224'
    digest_size = 28
    block_size = 128


class SHA512_256(HashAlgorithm):
    name = 'sha512-256'
    digest_size = 32
    block_size = 128


class SHA224(HashAlgorithm):
    name = 'sha224'
    digest_size = 28
    block_size = 64


class SHA256(HashAlgorithm):
    name = 'sha256'
    digest_size = 32
    block_size = 64


class SHA384(HashAlgorithm):
    name = 'sha384'
    digest_size = 48
    block_size = 128


class SHA512(HashAlgorithm):
    name = 'sha512'
    digest_size = 64
    block_size = 128


class SHA3_224(HashAlgorithm):
    name = 'sha3-224'
    digest_size = 28
    block_size = None


class SHA3_256(HashAlgorithm):
    name = 'sha3-256'
    digest_size = 32
    block_size = None


class SHA3_384(HashAlgorithm):
    name = 'sha3-384'
    digest_size = 48
    block_size = None


class SHA3_512(HashAlgorithm):
    name = 'sha3-512'
    digest_size = 64
    block_size = None


class SHAKE128(ExtendableOutputFunction, HashAlgorithm):
    name = 'shake128'
    block_size = None
    
    def __init__(self = None, digest_size = None):
        if not isinstance(digest_size, int):
            raise TypeError('digest_size must be an integer')
        if digest_size < 1:
            raise ValueError('digest_size must be a positive integer')
        self._digest_size = digest_size

    digest_size = (lambda self = None: self._digest_size)()


class SHAKE256(ExtendableOutputFunction, HashAlgorithm):
    name = 'shake256'
    block_size = None
    
    def __init__(self = None, digest_size = None):
        if not isinstance(digest_size, int):
            raise TypeError('digest_size must be an integer')
        if digest_size < 1:
            raise ValueError('digest_size must be a positive integer')
        self._digest_size = digest_size

    digest_size = (lambda self = None: self._digest_size)()


class MD5(HashAlgorithm):
    name = 'md5'
    digest_size = 16
    block_size = 64


class BLAKE2b(HashAlgorithm):
    name = 'blake2b'
    _max_digest_size = 64
    _min_digest_size = 1
    block_size = 128
    
    def __init__(self = None, digest_size = None):
        if digest_size != 64:
            raise ValueError('Digest size must be 64')
        self._digest_size = digest_size

    digest_size = (lambda self = None: self._digest_size)()


class BLAKE2s(HashAlgorithm):
    name = 'blake2s'
    block_size = 64
    _max_digest_size = 32
    _min_digest_size = 1
    
    def __init__(self = None, digest_size = None):
        if digest_size != 32:
            raise ValueError('Digest size must be 32')
        self._digest_size = digest_size

    digest_size = (lambda self = None: self._digest_size)()


class SM3(HashAlgorithm):
    name = 'sm3'
    digest_size = 32
    block_size = 64

