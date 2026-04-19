# Source Generated with Decompyle++
# File: totp.pyc (Python 3.12)

from __future__ import annotations
import typing
from cryptography.hazmat.primitives import constant_time
from cryptography.hazmat.primitives.twofactor import InvalidToken
from cryptography.hazmat.primitives.twofactor.hotp import HOTP, HOTPHashTypes, _generate_uri
from cryptography.utils import Buffer

class TOTP:
    
    def __init__(self, key, length = None, algorithm = None, time_step = None, backend = (None, True), enforce_key_length = ('key', 'Buffer', 'length', 'int', 'algorithm', 'HOTPHashTypes', 'time_step', 'int', 'backend', 'typing.Any', 'enforce_key_length', 'bool')):
        self._time_step = time_step
        self._hotp = HOTP(key, length, algorithm, enforce_key_length = enforce_key_length)

    
    def generate(self = None, time = None):
        if not isinstance(time, (int, float)):
            raise TypeError('Time parameter must be an integer type or float type.')
        counter = int(time / self._time_step)
        return self._hotp.generate(counter)

    
    def verify(self = None, totp = None, time = None):
        if not constant_time.bytes_eq(self.generate(time), totp):
            raise InvalidToken('Supplied TOTP value does not match.')

    
    def get_provisioning_uri(self = None, account_name = None, issuer = None):
        return _generate_uri(self._hotp, 'totp', account_name, issuer, [
            ('period', int(self._time_step))])


