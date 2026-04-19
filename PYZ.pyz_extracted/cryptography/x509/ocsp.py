# Source Generated with Decompyle++
# File: ocsp.pyc (Python 3.12)

from __future__ import annotations
import datetime
from collections.abc import Iterable
from cryptography import utils, x509
from cryptography.hazmat.bindings._rust import ocsp
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.types import CertificateIssuerPrivateKeyTypes
from cryptography.x509.base import _reject_duplicate_extension

class OCSPResponderEncoding(utils.Enum):
    HASH = 'By Hash'
    NAME = 'By Name'


class OCSPResponseStatus(utils.Enum):
    SUCCESSFUL = 0
    MALFORMED_REQUEST = 1
    INTERNAL_ERROR = 2
    TRY_LATER = 3
    SIG_REQUIRED = 5
    UNAUTHORIZED = 6

_ALLOWED_HASHES = (hashes.SHA1, hashes.SHA224, hashes.SHA256, hashes.SHA384, hashes.SHA512)

def _verify_algorithm(algorithm = None):
    if not isinstance(algorithm, _ALLOWED_HASHES):
        raise ValueError('Algorithm must be SHA1, SHA224, SHA256, SHA384, or SHA512')


class OCSPCertStatus(utils.Enum):
    GOOD = 0
    REVOKED = 1
    UNKNOWN = 2


class _SingleResponse:
    
    def __init__(self, resp, resp_hash, algorithm, cert_status, this_update = None, next_update = None, revocation_time = None, revocation_reason = ('resp', 'tuple[x509.Certificate, x509.Certificate] | None', 'resp_hash', 'tuple[bytes, bytes, int] | None', 'algorithm', 'hashes.HashAlgorithm', 'cert_status', 'OCSPCertStatus', 'this_update', 'datetime.datetime', 'next_update', 'datetime.datetime | None', 'revocation_time', 'datetime.datetime | None', 'revocation_reason', 'x509.ReasonFlags | None')):
        _verify_algorithm(algorithm)
        if not isinstance(this_update, datetime.datetime):
            raise TypeError('this_update must be a datetime object')
    # WARNING: Decompyle incomplete


OCSPRequest = ocsp.OCSPRequest
OCSPResponse = ocsp.OCSPResponse
OCSPSingleResponse = ocsp.OCSPSingleResponse

class OCSPRequestBuilder:
    
    def __init__(self = None, request = None, request_hash = None, extensions = (None, None, [])):
        self._request = request
        self._request_hash = request_hash
        self._extensions = extensions

    
    def add_certificate(self = None, cert = None, issuer = None, algorithm = ('cert', 'x509.Certificate', 'issuer', 'x509.Certificate', 'algorithm', 'hashes.HashAlgorithm', 'return', 'OCSPRequestBuilder')):
        pass
    # WARNING: Decompyle incomplete

    
    def add_certificate_by_hash(self, issuer_name_hash = None, issuer_key_hash = None, serial_number = None, algorithm = ('issuer_name_hash', 'bytes', 'issuer_key_hash', 'bytes', 'serial_number', 'int', 'algorithm', 'hashes.HashAlgorithm', 'return', 'OCSPRequestBuilder')):
        pass
    # WARNING: Decompyle incomplete

    
    def add_extension(self = None, extval = None, critical = None):
        if not isinstance(extval, x509.ExtensionType):
            raise TypeError('extension must be an ExtensionType')
        extension = x509.Extension(extval.oid, critical, extval)
        _reject_duplicate_extension(extension, self._extensions)
        return OCSPRequestBuilder(self._request, self._request_hash, self._request_hash[extension])

    
    def build(self = None):
        pass
    # WARNING: Decompyle incomplete



class OCSPResponseBuilder:
    
    def __init__(self = None, response = None, responder_id = None, certs = (None, None, None, []), extensions = ('response', '_SingleResponse | None', 'responder_id', 'tuple[x509.Certificate, OCSPResponderEncoding] | None', 'certs', 'list[x509.Certificate] | None', 'extensions', 'list[x509.Extension[x509.ExtensionType]]')):
        self._response = response
        self._responder_id = responder_id
        self._certs = certs
        self._extensions = extensions

    
    def add_response(self, cert, issuer, algorithm, cert_status, this_update = None, next_update = None, revocation_time = None, revocation_reason = ('cert', 'x509.Certificate', 'issuer', 'x509.Certificate', 'algorithm', 'hashes.HashAlgorithm', 'cert_status', 'OCSPCertStatus', 'this_update', 'datetime.datetime', 'next_update', 'datetime.datetime | None', 'revocation_time', 'datetime.datetime | None', 'revocation_reason', 'x509.ReasonFlags | None', 'return', 'OCSPResponseBuilder')):
        pass
    # WARNING: Decompyle incomplete

    
    def add_response_by_hash(self, issuer_name_hash, issuer_key_hash, serial_number, algorithm, cert_status, this_update = None, next_update = None, revocation_time = None, revocation_reason = ('issuer_name_hash', 'bytes', 'issuer_key_hash', 'bytes', 'serial_number', 'int', 'algorithm', 'hashes.HashAlgorithm', 'cert_status', 'OCSPCertStatus', 'this_update', 'datetime.datetime', 'next_update', 'datetime.datetime | None', 'revocation_time', 'datetime.datetime | None', 'revocation_reason', 'x509.ReasonFlags | None', 'return', 'OCSPResponseBuilder')):
        pass
    # WARNING: Decompyle incomplete

    
    def responder_id(self = None, encoding = None, responder_cert = None):
        pass
    # WARNING: Decompyle incomplete

    
    def certificates(self = None, certs = None):
        pass
    # WARNING: Decompyle incomplete

    
    def add_extension(self = None, extval = None, critical = None):
        if not isinstance(extval, x509.ExtensionType):
            raise TypeError('extension must be an ExtensionType')
        extension = x509.Extension(extval.oid, critical, extval)
        _reject_duplicate_extension(extension, self._extensions)
        return OCSPResponseBuilder(self._response, self._responder_id, self._certs, self._certs[extension])

    
    def sign(self = None, private_key = None, algorithm = None):
        pass
    # WARNING: Decompyle incomplete

    build_unsuccessful = (lambda cls = None, response_status = None: if not isinstance(response_status, OCSPResponseStatus):
raise TypeError('response_status must be an item from OCSPResponseStatus')if response_status is OCSPResponseStatus.SUCCESSFUL:
raise ValueError('response_status cannot be SUCCESSFUL')ocsp.create_ocsp_response(response_status, None, None, None))()

load_der_ocsp_request = ocsp.load_der_ocsp_request
load_der_ocsp_response = ocsp.load_der_ocsp_response
