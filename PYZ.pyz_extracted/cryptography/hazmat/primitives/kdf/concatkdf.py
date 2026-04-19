# Source Generated with Decompyle++
# File: concatkdf.pyc (Python 3.12)

from __future__ import annotations
import typing
from collections.abc import Callable
from cryptography import utils
from cryptography.exceptions import AlreadyFinalized, InvalidKey
from cryptography.hazmat.primitives import constant_time, hashes, hmac
from cryptography.hazmat.primitives.kdf import KeyDerivationFunction

def _int_to_u32be(n = None):
    return n.to_bytes(length = 4, byteorder = 'big')


def _common_args_checks(algorithm = None, length = None, otherinfo = None):
    max_length = algorithm.digest_size * 0xFFFFFFFF
    if length > max_length:
        raise ValueError(f'''Cannot derive keys larger than {max_length} bits.''')
# WARNING: Decompyle incomplete


def _concatkdf_derive(key_material = None, length = None, auxfn = None, otherinfo = ('key_material', 'utils.Buffer', 'length', 'int', 'auxfn', 'Callable[[], hashes.HashContext]', 'otherinfo', 'bytes', 'return', 'bytes')):
    utils._check_byteslike('key_material', key_material)
    output = [
        b'']
    outlen = 0
    counter = 1
    if length > outlen:
        h = auxfn()
        h.update(_int_to_u32be(counter))
        h.update(key_material)
        h.update(otherinfo)
        output.append(h.finalize())
        outlen += len(output[-1])
        counter += 1
        if length > outlen:
            continue
    return b''.join(output)[:length]


class ConcatKDFHash(KeyDerivationFunction):
    
    def __init__(self = None, algorithm = None, length = None, otherinfo = (None,), backend = ('algorithm', 'hashes.HashAlgorithm', 'length', 'int', 'otherinfo', 'bytes | None', 'backend', 'typing.Any')):
        _common_args_checks(algorithm, length, otherinfo)
        self._algorithm = algorithm
        self._length = length
    # WARNING: Decompyle incomplete

    
    def _hash(self = None):
        return hashes.Hash(self._algorithm)

    
    def derive(self = None, key_material = None):
        if self._used:
            raise AlreadyFinalized
        self._used = True
        return _concatkdf_derive(key_material, self._length, self._hash, self._otherinfo)

    
    def verify(self = None, key_material = None, expected_key = None):
        if not constant_time.bytes_eq(self.derive(key_material), expected_key):
            raise InvalidKey



class ConcatKDFHMAC(KeyDerivationFunction):
    
    def __init__(self, algorithm = None, length = None, salt = None, otherinfo = (None,), backend = ('algorithm', 'hashes.HashAlgorithm', 'length', 'int', 'salt', 'bytes | None', 'otherinfo', 'bytes | None', 'backend', 'typing.Any')):
        _common_args_checks(algorithm, length, otherinfo)
        self._algorithm = algorithm
        self._length = length
    # WARNING: Decompyle incomplete

    
    def _hmac(self = None):
        return hmac.HMAC(self._salt, self._algorithm)

    
    def derive(self = None, key_material = None):
        if self._used:
            raise AlreadyFinalized
        self._used = True
        return _concatkdf_derive(key_material, self._length, self._hmac, self._otherinfo)

    
    def verify(self = None, key_material = None, expected_key = None):
        if not constant_time.bytes_eq(self.derive(key_material), expected_key):
            raise InvalidKey


