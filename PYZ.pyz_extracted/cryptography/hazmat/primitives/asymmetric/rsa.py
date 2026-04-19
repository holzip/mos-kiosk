# Source Generated with Decompyle++
# File: rsa.pyc (Python 3.12)

from __future__ import annotations
import abc
import random
import typing
from math import gcd
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.primitives import _serialization, hashes
from cryptography.hazmat.primitives._asymmetric import AsymmetricPadding
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils

def RSAPrivateKey():
    '''RSAPrivateKey'''
    decrypt = (lambda self = None, ciphertext = None, padding = abc.abstractmethod: pass)()
    key_size = (lambda self = None: pass)()()
    public_key = (lambda self = None: pass)()
    sign = (lambda self = None, data = None, padding = abc.abstractmethod, algorithm = ('data', 'bytes', 'padding', 'AsymmetricPadding', 'algorithm', 'asym_utils.Prehashed | hashes.HashAlgorithm', 'return', 'bytes'): pass)()
    private_numbers = (lambda self = None: pass)()
    private_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod, encryption_algorithm = ('encoding', '_serialization.Encoding', 'format', '_serialization.PrivateFormat', 'encryption_algorithm', '_serialization.KeySerializationEncryption', 'return', 'bytes'): pass)()
    __copy__ = (lambda self = None: pass)()

RSAPrivateKey = <NODE:27>(RSAPrivateKey, 'RSAPrivateKey', metaclass = abc.ABCMeta)
RSAPrivateKeyWithSerialization = RSAPrivateKey
RSAPrivateKey.register(rust_openssl.rsa.RSAPrivateKey)

def RSAPublicKey():
    '''RSAPublicKey'''
    encrypt = (lambda self = None, plaintext = None, padding = abc.abstractmethod: pass)()
    key_size = (lambda self = None: pass)()()
    public_numbers = (lambda self = None: pass)()
    public_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod: pass)()
    verify = (lambda self, signature = None, data = None, padding = abc.abstractmethod, algorithm = ('signature', 'bytes', 'data', 'bytes', 'padding', 'AsymmetricPadding', 'algorithm', 'asym_utils.Prehashed | hashes.HashAlgorithm', 'return', 'None'): pass)()
    recover_data_from_signature = (lambda self = None, signature = None, padding = abc.abstractmethod, algorithm = ('signature', 'bytes', 'padding', 'AsymmetricPadding', 'algorithm', 'hashes.HashAlgorithm | None', 'return', 'bytes'): pass)()
    __eq__ = (lambda self = None, other = None: pass)()
    __copy__ = (lambda self = None: pass)()

RSAPublicKey = <NODE:27>(RSAPublicKey, 'RSAPublicKey', metaclass = abc.ABCMeta)
RSAPublicKeyWithSerialization = RSAPublicKey
RSAPublicKey.register(rust_openssl.rsa.RSAPublicKey)
RSAPrivateNumbers = rust_openssl.rsa.RSAPrivateNumbers
RSAPublicNumbers = rust_openssl.rsa.RSAPublicNumbers

def generate_private_key(public_exponent = None, key_size = None, backend = None):
    _verify_rsa_parameters(public_exponent, key_size)
    return rust_openssl.rsa.generate_private_key(public_exponent, key_size)


def _verify_rsa_parameters(public_exponent = None, key_size = None):
    if public_exponent not in (3, 65537):
        raise ValueError('public_exponent must be either 3 (for legacy compatibility) or 65537. Almost everyone should choose 65537 here!')
    if key_size < 1024:
        raise ValueError('key_size must be at least 1024-bits.')


def _modinv(e = None, m = None):
    '''
    Modular Multiplicative Inverse. Returns x such that: (x*e) mod m == 1
    '''
    (x1, x2) = (1, 0)
    b = m
    a = e
    if b > 0:
        (q, r) = divmod(a, b)
        xn = x1 - q * x2
        (a, b, x1, x2) = (b, r, x2, xn)
        if b > 0:
            continue
    return x1 % m


def rsa_crt_iqmp(p = None, q = None):
    '''
    Compute the CRT (q ** -1) % p value from RSA primes p and q.
    '''
    if p <= 1 or q <= 1:
        raise ValueError("Values can't be <= 1")
    return _modinv(q, p)


def rsa_crt_dmp1(private_exponent = None, p = None):
    '''
    Compute the CRT private_exponent % (p - 1) value from the RSA
    private_exponent (d) and p.
    '''
    if private_exponent <= 1 or p <= 1:
        raise ValueError("Values can't be <= 1")
    return private_exponent % (p - 1)


def rsa_crt_dmq1(private_exponent = None, q = None):
    '''
    Compute the CRT private_exponent % (q - 1) value from the RSA
    private_exponent (d) and q.
    '''
    if private_exponent <= 1 or q <= 1:
        raise ValueError("Values can't be <= 1")
    return private_exponent % (q - 1)


def rsa_recover_private_exponent(e = None, p = None, q = None):
    '''
    Compute the RSA private_exponent (d) given the public exponent (e)
    and the RSA primes p and q.

    This uses the Carmichael totient function to generate the
    smallest possible working value of the private exponent.
    '''
    if e <= 1 and p <= 1 or q <= 1:
        raise ValueError("Values can't be <= 1")
    lambda_n = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
    return _modinv(e, lambda_n)

_MAX_RECOVERY_ATTEMPTS = 500

def rsa_recover_prime_factors(n = None, e = None, d = None):
    '''
    Compute factors p and q from the private exponent d. We assume that n has
    no more than two factors. This function is adapted from code in PyCrypto.
    '''
    if d <= 1 or e <= 1:
        raise ValueError("d, e can't be <= 1")
    if 17 != pow(17, e * d, n):
        raise ValueError("n, d, e don't match")
    ktot = d * e - 1
    t = ktot
    if t % 2 == 0:
        t = t // 2
        if t % 2 == 0:
            continue
    spotted = False
    tries = 0
    if spotted and tries < _MAX_RECOVERY_ATTEMPTS:
        a = random.randint(2, n - 1)
        tries += 1
        k = t
        if k < ktot:
            cand = pow(a, k, n)
            if cand != 1 and cand != n - 1 and pow(cand, 2, n) == 1:
                p = gcd(cand + 1, n)
                spotted = True
            else:
                k *= 2
                if k < ktot:
                    continue
        if spotted and tries < _MAX_RECOVERY_ATTEMPTS:
            continue
    if not spotted:
        raise ValueError('Unable to compute factors p and q from exponent d.')
# WARNING: Decompyle incomplete

