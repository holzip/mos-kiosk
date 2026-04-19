# Source Generated with Decompyle++
# File: fernet.pyc (Python 3.12)

from __future__ import annotations
import base64
import binascii
import os
import time
import typing
from collections.abc import Iterable
from cryptography import utils
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.hmac import HMAC

class InvalidToken(Exception):
    pass

_MAX_CLOCK_SKEW = 60

class Fernet:
    
    def __init__(self = None, key = None, backend = None):
        
        try:
            key = base64.urlsafe_b64decode(key)
            if len(key) != 32:
                raise ValueError('Fernet key must be 32 url-safe base64-encoded bytes.')
            self._signing_key = key[:16]
            self._encryption_key = key[16:]
            return None
        except binascii.Error:
            exc = None
            raise ValueError('Fernet key must be 32 url-safe base64-encoded bytes.'), exc
            exc = None
            del exc


    generate_key = (lambda cls = None: base64.urlsafe_b64encode(os.urandom(32)))()
    
    def encrypt(self = None, data = None):
        return self.encrypt_at_time(data, int(time.time()))

    
    def encrypt_at_time(self = None, data = None, current_time = None):
        iv = os.urandom(16)
        return self._encrypt_from_parts(data, current_time, iv)

    
    def _encrypt_from_parts(self = None, data = None, current_time = None, iv = ('data', 'bytes', 'current_time', 'int', 'iv', 'bytes', 'return', 'bytes')):
        utils._check_bytes('data', data)
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        encryptor = Cipher(algorithms.AES(self._encryption_key), modes.CBC(iv)).encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        basic_parts = b'\x80' + current_time.to_bytes(length = 8, byteorder = 'big') + iv + ciphertext
        h = HMAC(self._signing_key, hashes.SHA256())
        h.update(basic_parts)
        hmac = h.finalize()
        return base64.urlsafe_b64encode(basic_parts + hmac)

    
    def decrypt(self = None, token = None, ttl = None):
        (timestamp, data) = Fernet._get_unverified_token_data(token)
    # WARNING: Decompyle incomplete

    
    def decrypt_at_time(self = None, token = None, ttl = None, current_time = ('token', 'bytes | str', 'ttl', 'int', 'current_time', 'int', 'return', 'bytes')):
        pass
    # WARNING: Decompyle incomplete

    
    def extract_timestamp(self = None, token = None):
        (timestamp, data) = Fernet._get_unverified_token_data(token)
        self._verify_signature(data)
        return timestamp

    _get_unverified_token_data = (lambda token = None: if not isinstance(token, (str, bytes)):
raise TypeError('token must be bytes or str')try:
data = base64.urlsafe_b64decode(token)if data or data[0] != 128:
raise InvalidTokenif len(data) < 9:
raise InvalidTokentimestamp = int.from_bytes(data[1:9], byteorder = 'big')(timestamp, data)except (TypeError, binascii.Error):
raise InvalidToken)()
    
    def _verify_signature(self = None, data = None):
        h = HMAC(self._signing_key, hashes.SHA256())
        h.update(data[:-32])
        
        try:
            h.verify(data[-32:])
            return None
        except InvalidSignature:
            raise InvalidToken


    
    def _decrypt_data(self = None, data = None, timestamp = None, time_info = ('data', 'bytes', 'timestamp', 'int', 'time_info', 'tuple[int, int] | None', 'return', 'bytes')):
        pass
    # WARNING: Decompyle incomplete



class MultiFernet:
    
    def __init__(self = None, fernets = None):
        fernets = list(fernets)
        if not fernets:
            raise ValueError('MultiFernet requires at least one Fernet instance')
        self._fernets = fernets

    
    def encrypt(self = None, msg = None):
        return self.encrypt_at_time(msg, int(time.time()))

    
    def encrypt_at_time(self = None, msg = None, current_time = None):
        return self._fernets[0].encrypt_at_time(msg, current_time)

    
    def rotate(self = None, msg = None):
        (timestamp, data) = Fernet._get_unverified_token_data(msg)
        for f in self._fernets:
            p = f._decrypt_data(data, timestamp, None)
            self._fernets
        raise InvalidToken
        iv = os.urandom(16)
        return self._fernets[0]._encrypt_from_parts(p, timestamp, iv)
        except InvalidToken:
            continue

    
    def decrypt(self = None, msg = None, ttl = None):
        for f in self._fernets:
            
            return self._fernets, f.decrypt(msg, ttl)
        raise InvalidToken
        except InvalidToken:
            continue

    
    def decrypt_at_time(self = None, msg = None, ttl = None, current_time = ('msg', 'bytes | str', 'ttl', 'int', 'current_time', 'int', 'return', 'bytes')):
        for f in self._fernets:
            
            return self._fernets, f.decrypt_at_time(msg, ttl, current_time)
        raise InvalidToken
        except InvalidToken:
            continue

    
    def extract_timestamp(self = None, msg = None):
        for f in self._fernets:
            
            return self._fernets, f.extract_timestamp(msg)
        raise InvalidToken
        except InvalidToken:
            continue


