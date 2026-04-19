# Source Generated with Decompyle++
# File: keywrap.pyc (Python 3.12)

from __future__ import annotations
import typing
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB
from cryptography.hazmat.primitives.constant_time import bytes_eq

def _wrap_core(wrapping_key = None, a = None, r = None):
    encryptor = Cipher(AES(wrapping_key), ECB()).encryptor()
    n = len(r)
    for j in range(6):
        for i in range(n):
            b = encryptor.update(a + r[i])
            a = (int.from_bytes(b[:8], byteorder = 'big') ^ n * j + i + 1).to_bytes(length = 8, byteorder = 'big')
            r[i] = b[-8:]
# WARNING: Decompyle incomplete


def aes_key_wrap(wrapping_key = None, key_to_wrap = None, backend = None):
    if len(wrapping_key) not in (16, 24, 32):
        raise ValueError('The wrapping key must be a valid AES key length')
    if len(key_to_wrap) < 16:
        raise ValueError('The key to wrap must be at least 16 bytes')
    if len(key_to_wrap) % 8 != 0:
        raise ValueError('The key to wrap must be a multiple of 8 bytes')
    a = b'\xa6\xa6\xa6\xa6\xa6\xa6\xa6\xa6'
# WARNING: Decompyle incomplete


def _unwrap_core(wrapping_key = None, a = None, r = None):
    decryptor = Cipher(AES(wrapping_key), ECB()).decryptor()
    n = len(r)
    for j in reversed(range(6)):
        for i in reversed(range(n)):
            atr = (int.from_bytes(a, byteorder = 'big') ^ n * j + i + 1).to_bytes(length = 8, byteorder = 'big') + r[i]
            b = decryptor.update(atr)
            a = b[:8]
            r[i] = b[-8:]
# WARNING: Decompyle incomplete


def aes_key_wrap_with_padding(wrapping_key = None, key_to_wrap = None, backend = None):
    if len(wrapping_key) not in (16, 24, 32):
        raise ValueError('The wrapping key must be a valid AES key length')
    aiv = b'\xa6YY\xa6' + len(key_to_wrap).to_bytes(length = 4, byteorder = 'big')
    pad = (8 - len(key_to_wrap) % 8) % 8
    key_to_wrap = key_to_wrap + b'\x00' * pad
# WARNING: Decompyle incomplete


def aes_key_unwrap_with_padding(wrapping_key = None, wrapped_key = None, backend = None):
    if len(wrapped_key) < 16:
        raise InvalidUnwrap('Must be at least 16 bytes')
    if len(wrapping_key) not in (16, 24, 32):
        raise ValueError('The wrapping key must be a valid AES key length')
# WARNING: Decompyle incomplete


def aes_key_unwrap(wrapping_key = None, wrapped_key = None, backend = None):
    if len(wrapped_key) < 24:
        raise InvalidUnwrap('Must be at least 24 bytes')
    if len(wrapped_key) % 8 != 0:
        raise InvalidUnwrap('The wrapped key must be a multiple of 8 bytes')
    if len(wrapping_key) not in (16, 24, 32):
        raise ValueError('The wrapping key must be a valid AES key length')
    aiv = b'\xa6\xa6\xa6\xa6\xa6\xa6\xa6\xa6'
# WARNING: Decompyle incomplete


class InvalidUnwrap(Exception):
    pass

