# Source Generated with Decompyle++
# File: pkcs12.pyc (Python 3.12)

from __future__ import annotations
import typing
from collections.abc import Iterable
from cryptography import x509
from cryptography.hazmat.bindings._rust import pkcs12 as rust_pkcs12
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives._serialization import PBES
from cryptography.hazmat.primitives.asymmetric import dsa, ec, ed448, ed25519, rsa
from cryptography.hazmat.primitives.asymmetric.types import PrivateKeyTypes
__all__ = [
    'PBES',
    'PKCS12Certificate',
    'PKCS12KeyAndCertificates',
    'PKCS12PrivateKeyTypes',
    'load_key_and_certificates',
    'load_pkcs12',
    'serialize_java_truststore',
    'serialize_key_and_certificates']
PKCS12PrivateKeyTypes = typing.Union[(rsa.RSAPrivateKey, dsa.DSAPrivateKey, ec.EllipticCurvePrivateKey, ed25519.Ed25519PrivateKey, ed448.Ed448PrivateKey)]
PKCS12Certificate = rust_pkcs12.PKCS12Certificate

class PKCS12KeyAndCertificates:
    
    def __init__(self = None, key = None, cert = None, additional_certs = ('key', 'PrivateKeyTypes | None', 'cert', 'PKCS12Certificate | None', 'additional_certs', 'list[PKCS12Certificate]')):
        pass
    # WARNING: Decompyle incomplete

    key = (lambda self = None: self._key)()
    cert = (lambda self = None: self._cert)()
    additional_certs = (lambda self = None: self._additional_certs)()
    
    def __eq__(self = None, other = None):
        if not isinstance(other, PKCS12KeyAndCertificates):
            return NotImplemented
        if None.key == other.key:
            None.key == other.key
            if self.cert == other.cert:
                self.cert == other.cert
        return self.additional_certs == other.additional_certs

    
    def __hash__(self = None):
        return hash((self.key, self.cert, tuple(self.additional_certs)))

    
    def __repr__(self = None):
        fmt = '<PKCS12KeyAndCertificates(key={}, cert={}, additional_certs={})>'
        return fmt.format(self.key, self.cert, self.additional_certs)


load_key_and_certificates = rust_pkcs12.load_key_and_certificates
load_pkcs12 = rust_pkcs12.load_pkcs12
_PKCS12CATypes = typing.Union[(x509.Certificate, PKCS12Certificate)]

def serialize_java_truststore(certs = None, encryption_algorithm = None):
    if not certs:
        raise ValueError('You must supply at least one cert')
    if not isinstance(encryption_algorithm, serialization.KeySerializationEncryption):
        raise TypeError('Key encryption algorithm must be a KeySerializationEncryption instance')
    return rust_pkcs12.serialize_java_truststore(certs, encryption_algorithm)


def serialize_key_and_certificates(name, key = None, cert = None, cas = None, encryption_algorithm = ('name', 'bytes | None', 'key', 'PKCS12PrivateKeyTypes | None', 'cert', 'x509.Certificate | None', 'cas', 'Iterable[_PKCS12CATypes] | None', 'encryption_algorithm', 'serialization.KeySerializationEncryption', 'return', 'bytes')):
    pass
# WARNING: Decompyle incomplete

