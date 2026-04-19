# Source Generated with Decompyle++
# File: kbkdf.pyc (Python 3.12)

from __future__ import annotations
import typing
from collections.abc import Callable
from cryptography import utils
from cryptography.exceptions import AlreadyFinalized, InvalidKey, UnsupportedAlgorithm, _Reasons
from cryptography.hazmat.primitives import ciphers, cmac, constant_time, hashes, hmac
from cryptography.hazmat.primitives.kdf import KeyDerivationFunction

class Mode(utils.Enum):
    CounterMode = 'ctr'


class CounterLocation(utils.Enum):
    BeforeFixed = 'before_fixed'
    AfterFixed = 'after_fixed'
    MiddleFixed = 'middle_fixed'


class _KBKDFDeriver:
    
    def __init__(self, prf, mode, length, rlen, llen, location, break_location = None, label = None, context = None, fixed = ('prf', 'Callable', 'mode', 'Mode', 'length', 'int', 'rlen', 'int', 'llen', 'int | None', 'location', 'CounterLocation', 'break_location', 'int | None', 'label', 'bytes | None', 'context', 'bytes | None', 'fixed', 'bytes | None')):
        pass
    # WARNING: Decompyle incomplete

    _valid_byte_length = (lambda value = None: if not isinstance(value, int):
raise TypeError('value must be of type int')value_bin = utils.int_to_bytes(1, value)if  <= 1, len(value_bin):
 <= 1, len(value_bin)1, len(value_bin) <= 4 <= 1, len(value_bin)1, len(value_bin))()
    
    def derive(self = None, key_material = None, prf_output_size = None):
        if self._used:
            raise AlreadyFinalized
        utils._check_byteslike('key_material', key_material)
        self._used = True
        rounds = -(-(self._length) // prf_output_size)
        output = [
            b'']
        r_bin = utils.int_to_bytes(1, self._rlen)
        if rounds > pow(2, len(r_bin) * 8) - 1:
            raise ValueError('There are too many iterations.')
        fixed = self._generate_fixed_input()
        if self._location == CounterLocation.BeforeFixed:
            data_before_ctr = b''
            data_after_ctr = fixed
        elif self._location == CounterLocation.AfterFixed:
            data_before_ctr = fixed
            data_after_ctr = b''
        elif isinstance(self._break_location, int) and self._break_location > len(fixed):
            raise ValueError('break_location offset > len(fixed)')
        data_before_ctr = fixed[:self._break_location]
        data_after_ctr = fixed[self._break_location:]
        for i in range(1, rounds + 1):
            h = self._prf(key_material)
            counter = utils.int_to_bytes(i, self._rlen)
            input_data = data_before_ctr + counter + data_after_ctr
            h.update(input_data)
            output.append(h.finalize())
        return b''.join(output)[:self._length]

    
    def _generate_fixed_input(self = None):
        if self._fixed_data and isinstance(self._fixed_data, bytes):
            return self._fixed_data
        l_val = None.int_to_bytes(self._length * 8, self._llen)
        return b''.join([
            self._label,
            b'\x00',
            self._context,
            l_val])



class KBKDFHMAC(KeyDerivationFunction):
    
    def __init__(self, algorithm, mode, length, rlen = None, llen = None, location = None, label = None, context = (None,), fixed = {
        'break_location': None }, backend = ('algorithm', 'hashes.HashAlgorithm', 'mode', 'Mode', 'length', 'int', 'rlen', 'int', 'llen', 'int | None', 'location', 'CounterLocation', 'label', 'bytes | None', 'context', 'bytes | None', 'fixed', 'bytes | None', 'backend', 'typing.Any', 'break_location', 'int | None'), *, break_location):
        if not isinstance(algorithm, hashes.HashAlgorithm):
            raise UnsupportedAlgorithm('Algorithm supplied is not a supported hash algorithm.', _Reasons.UNSUPPORTED_HASH)
        ossl = backend
        import cryptography.hazmat.backends.openssl.backend
        if not ossl.hmac_supported(algorithm):
            raise UnsupportedAlgorithm('Algorithm supplied is not a supported hmac algorithm.', _Reasons.UNSUPPORTED_HASH)
        self._algorithm = algorithm
        self._deriver = _KBKDFDeriver(self._prf, mode, length, rlen, llen, location, break_location, label, context, fixed)

    
    def _prf(self = None, key_material = None):
        return hmac.HMAC(key_material, self._algorithm)

    
    def derive(self = None, key_material = None):
        return self._deriver.derive(key_material, self._algorithm.digest_size)

    
    def verify(self = None, key_material = None, expected_key = None):
        if not constant_time.bytes_eq(self.derive(key_material), expected_key):
            raise InvalidKey



class KBKDFCMAC(KeyDerivationFunction):
    
    def __init__(self, algorithm, mode, length, rlen = None, llen = None, location = None, label = None, context = (None,), fixed = {
        'break_location': None }, backend = ('mode', 'Mode', 'length', 'int', 'rlen', 'int', 'llen', 'int | None', 'location', 'CounterLocation', 'label', 'bytes | None', 'context', 'bytes | None', 'fixed', 'bytes | None', 'backend', 'typing.Any', 'break_location', 'int | None'), *, break_location):
        if not issubclass(algorithm, ciphers.BlockCipherAlgorithm) or issubclass(algorithm, ciphers.CipherAlgorithm):
            raise UnsupportedAlgorithm('Algorithm supplied is not a supported cipher algorithm.', _Reasons.UNSUPPORTED_CIPHER)
        self._algorithm = algorithm
        self._cipher = None
        self._deriver = _KBKDFDeriver(self._prf, mode, length, rlen, llen, location, break_location, label, context, fixed)

    
    def _prf(self = None, _ = None):
        pass
    # WARNING: Decompyle incomplete

    
    def derive(self = None, key_material = None):
        self._cipher = self._algorithm(key_material)
    # WARNING: Decompyle incomplete

    
    def verify(self = None, key_material = None, expected_key = None):
        if not constant_time.bytes_eq(self.derive(key_material), expected_key):
            raise InvalidKey


