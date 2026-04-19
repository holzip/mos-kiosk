# Source Generated with Decompyle++
# File: modes.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography import utils
from cryptography.exceptions import UnsupportedAlgorithm, _Reasons
from cryptography.hazmat.primitives._cipheralgorithm import BlockCipherAlgorithm, CipherAlgorithm
from cryptography.hazmat.primitives.ciphers import algorithms

def Mode():
    '''Mode'''
    name = (lambda self = None: pass)()()
    validate_for_algorithm = (lambda self = None, algorithm = None: pass)()

Mode = <NODE:27>(Mode, 'Mode', metaclass = abc.ABCMeta)

def ModeWithInitializationVector():
    '''ModeWithInitializationVector'''
    initialization_vector = (lambda self = None: pass)()()

ModeWithInitializationVector = <NODE:27>(ModeWithInitializationVector, 'ModeWithInitializationVector', Mode, metaclass = abc.ABCMeta)

def ModeWithTweak():
    '''ModeWithTweak'''
    tweak = (lambda self = None: pass)()()

ModeWithTweak = <NODE:27>(ModeWithTweak, 'ModeWithTweak', Mode, metaclass = abc.ABCMeta)

def ModeWithNonce():
    '''ModeWithNonce'''
    nonce = (lambda self = None: pass)()()

ModeWithNonce = <NODE:27>(ModeWithNonce, 'ModeWithNonce', Mode, metaclass = abc.ABCMeta)

def ModeWithAuthenticationTag():
    '''ModeWithAuthenticationTag'''
    tag = (lambda self = None: pass)()()

ModeWithAuthenticationTag = <NODE:27>(ModeWithAuthenticationTag, 'ModeWithAuthenticationTag', Mode, metaclass = abc.ABCMeta)

def _check_aes_key_length(self = None, algorithm = None):
    if algorithm.key_size > 256:
        if algorithm.name == 'AES':
            raise ValueError('Only 128, 192, and 256 bit keys are allowed for this AES mode')
        return None


def _check_iv_length(self = None, algorithm = None):
    iv_len = len(self.initialization_vector)
    if iv_len * 8 != algorithm.block_size:
        raise ValueError(f'''Invalid IV size ({iv_len}) for {self.name}.''')


def _check_nonce_length(nonce = None, name = None, algorithm = None):
    if not isinstance(algorithm, BlockCipherAlgorithm):
        raise UnsupportedAlgorithm(f'''{name} requires a block cipher algorithm''', _Reasons.UNSUPPORTED_CIPHER)
    if len(nonce) * 8 != algorithm.block_size:
        raise ValueError(f'''Invalid nonce size ({len(nonce)}) for {name}.''')


def _check_iv_and_key_length(self = None, algorithm = None):
    if not isinstance(algorithm, BlockCipherAlgorithm):
        raise UnsupportedAlgorithm(f'''{self} requires a block cipher algorithm''', _Reasons.UNSUPPORTED_CIPHER)
    _check_aes_key_length(self, algorithm)
    _check_iv_length(self, algorithm)


class CBC(ModeWithInitializationVector):
    name = 'CBC'
    
    def __init__(self = None, initialization_vector = None):
        utils._check_byteslike('initialization_vector', initialization_vector)
        self._initialization_vector = initialization_vector

    initialization_vector = (lambda self = None: self._initialization_vector)()
    validate_for_algorithm = _check_iv_and_key_length


class XTS(ModeWithTweak):
    name = 'XTS'
    
    def __init__(self = None, tweak = None):
        utils._check_byteslike('tweak', tweak)
        if len(tweak) != 16:
            raise ValueError('tweak must be 128-bits (16 bytes)')
        self._tweak = tweak

    tweak = (lambda self = None: self._tweak)()
    
    def validate_for_algorithm(self = None, algorithm = None):
        if isinstance(algorithm, (algorithms.AES128, algorithms.AES256)):
            raise TypeError('The AES128 and AES256 classes do not support XTS, please use the standard AES class instead.')
        if algorithm.key_size not in (256, 512):
            raise ValueError('The XTS specification requires a 256-bit key for AES-128-XTS and 512-bit key for AES-256-XTS')



class ECB(Mode):
    name = 'ECB'
    validate_for_algorithm = _check_aes_key_length


class OFB(ModeWithInitializationVector):
    name = 'OFB'
    
    def __init__(self = None, initialization_vector = None):
        utils._check_byteslike('initialization_vector', initialization_vector)
        self._initialization_vector = initialization_vector

    initialization_vector = (lambda self = None: self._initialization_vector)()
    validate_for_algorithm = _check_iv_and_key_length


class CFB(ModeWithInitializationVector):
    name = 'CFB'
    
    def __init__(self = None, initialization_vector = None):
        utils._check_byteslike('initialization_vector', initialization_vector)
        self._initialization_vector = initialization_vector

    initialization_vector = (lambda self = None: self._initialization_vector)()
    validate_for_algorithm = _check_iv_and_key_length


class CFB8(ModeWithInitializationVector):
    name = 'CFB8'
    
    def __init__(self = None, initialization_vector = None):
        utils._check_byteslike('initialization_vector', initialization_vector)
        self._initialization_vector = initialization_vector

    initialization_vector = (lambda self = None: self._initialization_vector)()
    validate_for_algorithm = _check_iv_and_key_length


class CTR(ModeWithNonce):
    name = 'CTR'
    
    def __init__(self = None, nonce = None):
        utils._check_byteslike('nonce', nonce)
        self._nonce = nonce

    nonce = (lambda self = None: self._nonce)()
    
    def validate_for_algorithm(self = None, algorithm = None):
        _check_aes_key_length(self, algorithm)
        _check_nonce_length(self.nonce, self.name, algorithm)



class GCM(ModeWithAuthenticationTag, ModeWithInitializationVector):
    name = 'GCM'
    _MAX_ENCRYPTED_BYTES = 0xFFFFFFFE0
    _MAX_AAD_BYTES = 0x2000000000000000
    
    def __init__(self = None, initialization_vector = None, tag = None, min_tag_length = (None, 16)):
        utils._check_byteslike('initialization_vector', initialization_vector)
        if len(initialization_vector) < 8 or len(initialization_vector) > 128:
            raise ValueError('initialization_vector must be between 8 and 128 bytes (64 and 1024 bits).')
        self._initialization_vector = initialization_vector
    # WARNING: Decompyle incomplete

    tag = (lambda self = None: self._tag)()
    initialization_vector = (lambda self = None: self._initialization_vector)()
    
    def validate_for_algorithm(self = None, algorithm = None):
        _check_aes_key_length(self, algorithm)
        if not isinstance(algorithm, BlockCipherAlgorithm):
            raise UnsupportedAlgorithm('GCM requires a block cipher algorithm', _Reasons.UNSUPPORTED_CIPHER)
        block_size_bytes = algorithm.block_size // 8
    # WARNING: Decompyle incomplete


