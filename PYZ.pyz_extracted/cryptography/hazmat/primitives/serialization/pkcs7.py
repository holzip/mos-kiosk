# Source Generated with Decompyle++
# File: pkcs7.pyc (Python 3.12)

from __future__ import annotations
import email.base64mime as email
import email.generator as email
import email.message as email
import email.policy as email
import io
import typing
from collections.abc import Iterable
from cryptography import utils, x509
from cryptography.exceptions import UnsupportedAlgorithm, _Reasons
from cryptography.hazmat.bindings._rust import pkcs7 as rust_pkcs7
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.utils import _check_byteslike
load_pem_pkcs7_certificates = rust_pkcs7.load_pem_pkcs7_certificates
load_der_pkcs7_certificates = rust_pkcs7.load_der_pkcs7_certificates
serialize_certificates = rust_pkcs7.serialize_certificates
PKCS7HashTypes = typing.Union[(hashes.SHA224, hashes.SHA256, hashes.SHA384, hashes.SHA512)]
PKCS7PrivateKeyTypes = typing.Union[(rsa.RSAPrivateKey, ec.EllipticCurvePrivateKey)]
ContentEncryptionAlgorithm = typing.Union[(typing.Type[algorithms.AES128], typing.Type[algorithms.AES256])]

class PKCS7Options(utils.Enum):
    Text = 'Add text/plain MIME type'
    Binary = "Don't translate input data into canonical MIME format"
    DetachedSignature = "Don't embed data in the PKCS7 structure"
    NoCapabilities = "Don't embed SMIME capabilities"
    NoAttributes = "Don't embed authenticatedAttributes"
    NoCerts = "Don't embed signer certificate"


class PKCS7SignatureBuilder:
    
    def __init__(self = None, data = None, signers = None, additional_certs = (None, [], [])):
        self._data = data
        self._signers = signers
        self._additional_certs = additional_certs

    
    def set_data(self = None, data = None):
        _check_byteslike('data', data)
    # WARNING: Decompyle incomplete

    
    def add_signer(self = None, certificate = None, private_key = None, hash_algorithm = None, *, rsa_padding):
        if not isinstance(hash_algorithm, (hashes.SHA224, hashes.SHA256, hashes.SHA384, hashes.SHA512)):
            raise TypeError('hash_algorithm must be one of hashes.SHA224, SHA256, SHA384, or SHA512')
        if not isinstance(certificate, x509.Certificate):
            raise TypeError('certificate must be a x509.Certificate')
        if not isinstance(private_key, (rsa.RSAPrivateKey, ec.EllipticCurvePrivateKey)):
            raise TypeError('Only RSA & EC keys are supported at this time.')
    # WARNING: Decompyle incomplete

    
    def add_certificate(self = None, certificate = None):
        if not isinstance(certificate, x509.Certificate):
            raise TypeError('certificate must be a x509.Certificate')
        return PKCS7SignatureBuilder(self._data, self._signers, self._signers[certificate])

    
    def sign(self = None, encoding = None, options = None, backend = (None,)):
        if len(self._signers) == 0:
            raise ValueError('Must have at least one signer')
    # WARNING: Decompyle incomplete



class PKCS7EnvelopeBuilder:
    
    def __init__(self = None, *, _data, _recipients, _content_encryption_algorithm):
        ossl = backend
        import cryptography.hazmat.backends.openssl.backend
        if not ossl.rsa_encryption_supported(padding = padding.PKCS1v15()):
            raise UnsupportedAlgorithm('RSA with PKCS1 v1.5 padding is not supported by this version of OpenSSL.', _Reasons.UNSUPPORTED_PADDING)
        self._data = _data
    # WARNING: Decompyle incomplete

    
    def set_data(self = None, data = None):
        _check_byteslike('data', data)
    # WARNING: Decompyle incomplete

    
    def add_recipient(self = None, certificate = None):
        if not isinstance(certificate, x509.Certificate):
            raise TypeError('certificate must be a x509.Certificate')
        if not isinstance(certificate.public_key(), rsa.RSAPublicKey):
            raise TypeError('Only RSA keys are supported at this time.')
        return PKCS7EnvelopeBuilder(_data = self._data, _recipients = self._data[certificate], _content_encryption_algorithm = self._content_encryption_algorithm)

    
    def set_content_encryption_algorithm(self = None, content_encryption_algorithm = None):
        pass
    # WARNING: Decompyle incomplete

    
    def encrypt(self = None, encoding = None, options = None):
        if len(self._recipients) == 0:
            raise ValueError('Must have at least one recipient')
    # WARNING: Decompyle incomplete


pkcs7_decrypt_der = rust_pkcs7.decrypt_der
pkcs7_decrypt_pem = rust_pkcs7.decrypt_pem
pkcs7_decrypt_smime = rust_pkcs7.decrypt_smime

def _smime_signed_encode(data = None, signature = None, micalg = None, text_mode = ('data', 'bytes', 'signature', 'bytes', 'micalg', 'str', 'text_mode', 'bool', 'return', 'bytes')):
    m = email.message.Message()
    m.add_header('MIME-Version', '1.0')
    m.add_header('Content-Type', 'multipart/signed', protocol = 'application/x-pkcs7-signature', micalg = micalg)
    m.preamble = 'This is an S/MIME signed message\n'
    msg_part = OpenSSLMimePart()
    msg_part.set_payload(data)
    if text_mode:
        msg_part.add_header('Content-Type', 'text/plain')
    m.attach(msg_part)
    sig_part = email.message.MIMEPart()
    sig_part.add_header('Content-Type', 'application/x-pkcs7-signature', name = 'smime.p7s')
    sig_part.add_header('Content-Transfer-Encoding', 'base64')
    sig_part.add_header('Content-Disposition', 'attachment', filename = 'smime.p7s')
    sig_part.set_payload(email.base64mime.body_encode(signature, maxlinelen = 65))
    del sig_part['MIME-Version']
    m.attach(sig_part)
    fp = io.BytesIO()
    g = email.generator.BytesGenerator(fp, maxheaderlen = 0, mangle_from_ = False, policy = m.policy.clone(linesep = '\r\n'))
    g.flatten(m)
    return fp.getvalue()


def _smime_enveloped_encode(data = None):
    m = email.message.Message()
    m.add_header('MIME-Version', '1.0')
    m.add_header('Content-Disposition', 'attachment', filename = 'smime.p7m')
    m.add_header('Content-Type', 'application/pkcs7-mime', smime_type = 'enveloped-data', name = 'smime.p7m')
    m.add_header('Content-Transfer-Encoding', 'base64')
    m.set_payload(email.base64mime.body_encode(data, maxlinelen = 65))
    return m.as_bytes(policy = m.policy.clone(linesep = '\n', max_line_length = 0))


def _smime_enveloped_decode(data = None):
    m = email.message_from_bytes(data)
    if m.get_content_type() not in frozenset({'application/x-pkcs7-mime', 'application/pkcs7-mime'}):
        raise ValueError('Not an S/MIME enveloped message')
    return bytes(m.get_payload(decode = True))


def _smime_remove_text_headers(data = None):
    m = email.message_from_bytes(data)
    content_type = m.get('content-type')
# WARNING: Decompyle incomplete


class OpenSSLMimePart(email.message.MIMEPart):
    
    def _write_headers(self = None, generator = None):
        if list(self.raw_items()):
            generator._write_headers(self)
            return None


