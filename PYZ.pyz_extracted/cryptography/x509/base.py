# Source Generated with Decompyle++
# File: base.pyc (Python 3.12)

from __future__ import annotations
import abc
import datetime
import os
import typing
import warnings
from collections.abc import Iterable
from cryptography import utils
from cryptography.hazmat.bindings._rust import x509 as rust_x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa, ec, ed448, ed25519, padding, rsa, x448, x25519
from cryptography.hazmat.primitives.asymmetric.types import CertificateIssuerPrivateKeyTypes, CertificatePublicKeyTypes
from cryptography.x509.extensions import Extension, Extensions, ExtensionType, _make_sequence_methods
from cryptography.x509.name import Name, _ASN1Type
from cryptography.x509.oid import ObjectIdentifier
_EARLIEST_UTC_TIME = datetime.datetime(1950, 1, 1)
_AllowedHashTypes = typing.Union[(hashes.SHA224, hashes.SHA256, hashes.SHA384, hashes.SHA512, hashes.SHA3_224, hashes.SHA3_256, hashes.SHA3_384, hashes.SHA3_512)]

class AttributeNotFound(Exception):
    pass
# WARNING: Decompyle incomplete


def _reject_duplicate_extension(extension = None, extensions = None):
    for e in extensions:
        if not e.oid == extension.oid:
            continue
        raise ValueError('This extension has already been set.')


def _reject_duplicate_attribute(oid = None, attributes = None):
    for attr_oid, _, _ in attributes:
        if not attr_oid == oid:
            continue
        raise ValueError('This attribute has already been set.')


def _convert_to_naive_utc_time(time = None):
    '''Normalizes a datetime to a naive datetime in UTC.

    time -- datetime to normalize. Assumed to be in UTC if not timezone
            aware.
    '''
    pass
# WARNING: Decompyle incomplete


class Attribute:
    
    def __init__(self = None, oid = None, value = None, _type = (_ASN1Type.UTF8String.value,)):
        self._oid = oid
        self._value = value
        self._type = _type

    oid = (lambda self = None: self._oid)()
    value = (lambda self = None: self._value)()
    
    def __repr__(self = None):
        return f'''<Attribute(oid={self.oid}, value={self.value!r})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, Attribute):
            return NotImplemented
        if None.oid == other.oid:
            None.oid == other.oid
            if self.value == other.value:
                self.value == other.value
        return self._type == other._type

    
    def __hash__(self = None):
        return hash((self.oid, self.value, self._type))



class Attributes:
    
    def __init__(self = None, attributes = None):
        self._attributes = list(attributes)

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_attributes')
    
    def __repr__(self = None):
        return f'''<Attributes({self._attributes})>'''

    
    def get_attribute_for_oid(self = None, oid = None):
        for attr in self:
            if not attr.oid == oid:
                continue
            
            return self, attr
        raise AttributeNotFound(f'''No {oid} attribute was found''', oid)



class Version(utils.Enum):
    v1 = 0
    v3 = 2


class InvalidVersion(Exception):
    pass
# WARNING: Decompyle incomplete

Certificate = rust_x509.Certificate

def RevokedCertificate():
    '''RevokedCertificate'''
    serial_number = (lambda self = None: pass)()()
    revocation_date = (lambda self = None: pass)()()
    revocation_date_utc = (lambda self = None: pass)()()
    extensions = (lambda self = None: pass)()()

RevokedCertificate = <NODE:27>(RevokedCertificate, 'RevokedCertificate', metaclass = abc.ABCMeta)
RevokedCertificate.register(rust_x509.RevokedCertificate)

class _RawRevokedCertificate(RevokedCertificate):
    
    def __init__(self = None, serial_number = None, revocation_date = None, extensions = ('serial_number', 'int', 'revocation_date', 'datetime.datetime', 'extensions', 'Extensions')):
        self._serial_number = serial_number
        self._revocation_date = revocation_date
        self._extensions = extensions

    serial_number = (lambda self = None: self._serial_number)()
    revocation_date = (lambda self = None: warnings.warn('Properties that return a naïve datetime object have been deprecated. Please switch to revocation_date_utc.', utils.DeprecatedIn42, stacklevel = 2)self._revocation_date)()
    revocation_date_utc = (lambda self = None: self._revocation_date.replace(tzinfo = datetime.timezone.utc))()
    extensions = (lambda self = None: self._extensions)()

CertificateRevocationList = rust_x509.CertificateRevocationList
CertificateSigningRequest = rust_x509.CertificateSigningRequest
load_pem_x509_certificate = rust_x509.load_pem_x509_certificate
load_der_x509_certificate = rust_x509.load_der_x509_certificate
load_pem_x509_certificates = rust_x509.load_pem_x509_certificates
load_pem_x509_csr = rust_x509.load_pem_x509_csr
load_der_x509_csr = rust_x509.load_der_x509_csr
load_pem_x509_crl = rust_x509.load_pem_x509_crl
load_der_x509_crl = rust_x509.load_der_x509_crl

class CertificateSigningRequestBuilder:
    
    def __init__(self = None, subject_name = None, extensions = None, attributes = (None, [], [])):
        '''
        Creates an empty X.509 certificate request (v1).
        '''
        self._subject_name = subject_name
        self._extensions = extensions
        self._attributes = attributes

    
    def subject_name(self = None, name = None):
        """
        Sets the certificate requestor's distinguished name.
        """
        if not isinstance(name, Name):
            raise TypeError('Expecting x509.Name object.')
    # WARNING: Decompyle incomplete

    
    def add_extension(self = None, extval = None, critical = None):
        '''
        Adds an X.509 extension to the certificate request.
        '''
        if not isinstance(extval, ExtensionType):
            raise TypeError('extension must be an ExtensionType')
        extension = Extension(extval.oid, critical, extval)
        _reject_duplicate_extension(extension, self._extensions)
        return CertificateSigningRequestBuilder(self._subject_name, self._subject_name[extension], self._attributes)

    
    def add_attribute(self = None, oid = None, value = None, *, _tag):
        '''
        Adds an X.509 attribute with an OID and associated value.
        '''
        if not isinstance(oid, ObjectIdentifier):
            raise TypeError('oid must be an ObjectIdentifier')
        if not isinstance(value, bytes):
            raise TypeError('value must be bytes')
    # WARNING: Decompyle incomplete

    
    def sign(self = None, private_key = None, algorithm = None, backend = None, *, rsa_padding, ecdsa_deterministic):
        """
        Signs the request using the requestor's private key.
        """
        pass
    # WARNING: Decompyle incomplete



class CertificateBuilder:
    _extensions: 'list[Extension[ExtensionType]]' = 'CertificateBuilder'
    
    def __init__(self, issuer_name, subject_name, public_key = None, serial_number = None, not_valid_before = None, not_valid_after = (None, None, None, None, None, None, []), extensions = ('issuer_name', 'Name | None', 'subject_name', 'Name | None', 'public_key', 'CertificatePublicKeyTypes | None', 'serial_number', 'int | None', 'not_valid_before', 'datetime.datetime | None', 'not_valid_after', 'datetime.datetime | None', 'extensions', 'list[Extension[ExtensionType]]', 'return', 'None')):
        self._version = Version.v3
        self._issuer_name = issuer_name
        self._subject_name = subject_name
        self._public_key = public_key
        self._serial_number = serial_number
        self._not_valid_before = not_valid_before
        self._not_valid_after = not_valid_after
        self._extensions = extensions

    
    def issuer_name(self = None, name = None):
        """
        Sets the CA's distinguished name.
        """
        if not isinstance(name, Name):
            raise TypeError('Expecting x509.Name object.')
    # WARNING: Decompyle incomplete

    
    def subject_name(self = None, name = None):
        """
        Sets the requestor's distinguished name.
        """
        if not isinstance(name, Name):
            raise TypeError('Expecting x509.Name object.')
    # WARNING: Decompyle incomplete

    
    def public_key(self = None, key = None):
        """
        Sets the requestor's public key (as found in the signing request).
        """
        if not isinstance(key, (dsa.DSAPublicKey, rsa.RSAPublicKey, ec.EllipticCurvePublicKey, ed25519.Ed25519PublicKey, ed448.Ed448PublicKey, x25519.X25519PublicKey, x448.X448PublicKey)):
            raise TypeError('Expecting one of DSAPublicKey, RSAPublicKey, EllipticCurvePublicKey, Ed25519PublicKey, Ed448PublicKey, X25519PublicKey, or X448PublicKey.')
    # WARNING: Decompyle incomplete

    
    def serial_number(self = None, number = None):
        '''
        Sets the certificate serial number.
        '''
        if not isinstance(number, int):
            raise TypeError('Serial number must be of integral type.')
    # WARNING: Decompyle incomplete

    
    def not_valid_before(self = None, time = None):
        '''
        Sets the certificate activation time.
        '''
        if not isinstance(time, datetime.datetime):
            raise TypeError('Expecting datetime object.')
    # WARNING: Decompyle incomplete

    
    def not_valid_after(self = None, time = None):
        '''
        Sets the certificate expiration time.
        '''
        if not isinstance(time, datetime.datetime):
            raise TypeError('Expecting datetime object.')
    # WARNING: Decompyle incomplete

    
    def add_extension(self = None, extval = None, critical = None):
        '''
        Adds an X.509 extension to the certificate.
        '''
        if not isinstance(extval, ExtensionType):
            raise TypeError('extension must be an ExtensionType')
        extension = Extension(extval.oid, critical, extval)
        _reject_duplicate_extension(extension, self._extensions)
        return CertificateBuilder(self._issuer_name, self._subject_name, self._public_key, self._serial_number, self._not_valid_before, self._not_valid_after, self._not_valid_after[extension])

    
    def sign(self = None, private_key = None, algorithm = None, backend = None, *, rsa_padding, ecdsa_deterministic):
        """
        Signs the certificate using the CA's private key.
        """
        pass
    # WARNING: Decompyle incomplete



class CertificateRevocationListBuilder:
    _revoked_certificates: 'list[RevokedCertificate]' = 'CertificateRevocationListBuilder'
    
    def __init__(self, issuer_name = None, last_update = None, next_update = None, extensions = (None, None, None, [], []), revoked_certificates = ('issuer_name', 'Name | None', 'last_update', 'datetime.datetime | None', 'next_update', 'datetime.datetime | None', 'extensions', 'list[Extension[ExtensionType]]', 'revoked_certificates', 'list[RevokedCertificate]')):
        self._issuer_name = issuer_name
        self._last_update = last_update
        self._next_update = next_update
        self._extensions = extensions
        self._revoked_certificates = revoked_certificates

    
    def issuer_name(self = None, issuer_name = None):
        if not isinstance(issuer_name, Name):
            raise TypeError('Expecting x509.Name object.')
    # WARNING: Decompyle incomplete

    
    def last_update(self = None, last_update = None):
        if not isinstance(last_update, datetime.datetime):
            raise TypeError('Expecting datetime object.')
    # WARNING: Decompyle incomplete

    
    def next_update(self = None, next_update = None):
        if not isinstance(next_update, datetime.datetime):
            raise TypeError('Expecting datetime object.')
    # WARNING: Decompyle incomplete

    
    def add_extension(self = None, extval = None, critical = None):
        '''
        Adds an X.509 extension to the certificate revocation list.
        '''
        if not isinstance(extval, ExtensionType):
            raise TypeError('extension must be an ExtensionType')
        extension = Extension(extval.oid, critical, extval)
        _reject_duplicate_extension(extension, self._extensions)
        return CertificateRevocationListBuilder(self._issuer_name, self._last_update, self._next_update, self._next_update[extension], self._revoked_certificates)

    
    def add_revoked_certificate(self = None, revoked_certificate = None):
        '''
        Adds a revoked certificate to the CRL.
        '''
        if not isinstance(revoked_certificate, RevokedCertificate):
            raise TypeError('Must be an instance of RevokedCertificate')
        return CertificateRevocationListBuilder(self._issuer_name, self._last_update, self._next_update, self._extensions, self._extensions[revoked_certificate])

    
    def sign(self = None, private_key = None, algorithm = None, backend = None, *, rsa_padding, ecdsa_deterministic):
        pass
    # WARNING: Decompyle incomplete



class RevokedCertificateBuilder:
    
    def __init__(self = None, serial_number = None, revocation_date = None, extensions = (None, None, [])):
        self._serial_number = serial_number
        self._revocation_date = revocation_date
        self._extensions = extensions

    
    def serial_number(self = None, number = None):
        if not isinstance(number, int):
            raise TypeError('Serial number must be of integral type.')
    # WARNING: Decompyle incomplete

    
    def revocation_date(self = None, time = None):
        if not isinstance(time, datetime.datetime):
            raise TypeError('Expecting datetime object.')
    # WARNING: Decompyle incomplete

    
    def add_extension(self = None, extval = None, critical = None):
        if not isinstance(extval, ExtensionType):
            raise TypeError('extension must be an ExtensionType')
        extension = Extension(extval.oid, critical, extval)
        _reject_duplicate_extension(extension, self._extensions)
        return RevokedCertificateBuilder(self._serial_number, self._revocation_date, self._revocation_date[extension])

    
    def build(self = None, backend = None):
        pass
    # WARNING: Decompyle incomplete



def random_serial_number():
    return int.from_bytes(os.urandom(20), 'big') >> 1

