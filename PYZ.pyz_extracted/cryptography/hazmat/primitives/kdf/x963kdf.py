# Source Generated with Decompyle++
# File: x963kdf.pyc (Python 3.12)

from __future__ import annotations
import typing
from cryptography import utils
from cryptography.exceptions import AlreadyFinalized, InvalidKey
from cryptography.hazmat.primitives import constant_time, hashes
from cryptography.hazmat.primitives.kdf import KeyDerivationFunction

def _int_to_u32be(n = None):
    return n.to_bytes(length = 4, byteorder = 'big')


class X963KDF(KeyDerivationFunction):
    
    def __init__(self = None, algorithm = None, length = None, sharedinfo = (None,), backend = ('algorithm', 'hashes.HashAlgorithm', 'length', 'int', 'sharedinfo', 'bytes | None', 'backend', 'typing.Any')):
        max_len = algorithm.digest_size * 0xFFFFFFFF
        if length > max_len:
            raise ValueError(f'''Cannot derive keys larger than {max_len} bits.''')
    # WARNING: Decompyle incomplete

    
    def derive(self = None, key_material = None):
        if self._used:
            raise AlreadyFinalized
        self._used = True
        utils._check_byteslike('key_material', key_material)
        output = [
            b'']
        outlen = 0
        counter = 1
    # WARNING: Decompyle incomplete

    
    def verify(self = None, key_material = None, expected_key = None):
        if not constant_time.bytes_eq(self.derive(key_material), expected_key):
            raise InvalidKey


