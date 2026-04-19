# Source Generated with Decompyle++
# File: ec.pyc (Python 3.12)

from __future__ import annotations
import abc
import typing
from cryptography import utils
from cryptography.exceptions import UnsupportedAlgorithm, _Reasons
from cryptography.hazmat._oid import ObjectIdentifier
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.primitives import _serialization, hashes
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils

class EllipticCurveOID:
    SECP192R1 = ObjectIdentifier('1.2.840.10045.3.1.1')
    SECP224R1 = ObjectIdentifier('1.3.132.0.33')
    SECP256K1 = ObjectIdentifier('1.3.132.0.10')
    SECP256R1 = ObjectIdentifier('1.2.840.10045.3.1.7')
    SECP384R1 = ObjectIdentifier('1.3.132.0.34')
    SECP521R1 = ObjectIdentifier('1.3.132.0.35')
    BRAINPOOLP256R1 = ObjectIdentifier('1.3.36.3.3.2.8.1.1.7')
    BRAINPOOLP384R1 = ObjectIdentifier('1.3.36.3.3.2.8.1.1.11')
    BRAINPOOLP512R1 = ObjectIdentifier('1.3.36.3.3.2.8.1.1.13')
    SECT163K1 = ObjectIdentifier('1.3.132.0.1')
    SECT163R2 = ObjectIdentifier('1.3.132.0.15')
    SECT233K1 = ObjectIdentifier('1.3.132.0.26')
    SECT233R1 = ObjectIdentifier('1.3.132.0.27')
    SECT283K1 = ObjectIdentifier('1.3.132.0.16')
    SECT283R1 = ObjectIdentifier('1.3.132.0.17')
    SECT409K1 = ObjectIdentifier('1.3.132.0.36')
    SECT409R1 = ObjectIdentifier('1.3.132.0.37')
    SECT571K1 = ObjectIdentifier('1.3.132.0.38')
    SECT571R1 = ObjectIdentifier('1.3.132.0.39')


def EllipticCurve():
    '''EllipticCurve'''
    name = (lambda self = None: pass)()()
    key_size = (lambda self = None: pass)()()
    group_order = (lambda self = None: pass)()()

EllipticCurve = <NODE:27>(EllipticCurve, 'EllipticCurve', metaclass = abc.ABCMeta)

def EllipticCurveSignatureAlgorithm():
    '''EllipticCurveSignatureAlgorithm'''
    algorithm = (lambda self = None: pass)()()

EllipticCurveSignatureAlgorithm = <NODE:27>(EllipticCurveSignatureAlgorithm, 'EllipticCurveSignatureAlgorithm', metaclass = abc.ABCMeta)

def EllipticCurvePrivateKey():
    '''EllipticCurvePrivateKey'''
    exchange = (lambda self = None, algorithm = None, peer_public_key = abc.abstractmethod: pass)()
    public_key = (lambda self = None: pass)()
    curve = (lambda self = None: pass)()()
    key_size = (lambda self = None: pass)()()
    sign = (lambda self = None, data = None, signature_algorithm = abc.abstractmethod: pass)()
    private_numbers = (lambda self = None: pass)()
    private_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod, encryption_algorithm = ('encoding', '_serialization.Encoding', 'format', '_serialization.PrivateFormat', 'encryption_algorithm', '_serialization.KeySerializationEncryption', 'return', 'bytes'): pass)()
    __copy__ = (lambda self = None: pass)()

EllipticCurvePrivateKey = <NODE:27>(EllipticCurvePrivateKey, 'EllipticCurvePrivateKey', metaclass = abc.ABCMeta)
EllipticCurvePrivateKeyWithSerialization = EllipticCurvePrivateKey
EllipticCurvePrivateKey.register(rust_openssl.ec.ECPrivateKey)

def EllipticCurvePublicKey():
    '''EllipticCurvePublicKey'''
    curve = (lambda self = None: pass)()()
    key_size = (lambda self = None: pass)()()
    public_numbers = (lambda self = None: pass)()
    public_bytes = (lambda self = None, encoding = None, format = abc.abstractmethod: pass)()
    verify = (lambda self = None, signature = None, data = abc.abstractmethod, signature_algorithm = ('signature', 'utils.Buffer', 'data', 'utils.Buffer', 'signature_algorithm', 'EllipticCurveSignatureAlgorithm', 'return', 'None'): pass)()
    from_encoded_point = (lambda cls = None, curve = None, data = classmethod: utils._check_bytes('data', data)if len(data) == 0:
raise ValueError('data must not be an empty byte string')if data[0] not in (2, 3, 4):
raise ValueError('Unsupported elliptic curve point type')rust_openssl.ec.from_public_bytes(curve, data))()
    __eq__ = (lambda self = None, other = None: pass)()
    __copy__ = (lambda self = None: pass)()

EllipticCurvePublicKey = <NODE:27>(EllipticCurvePublicKey, 'EllipticCurvePublicKey', metaclass = abc.ABCMeta)
EllipticCurvePublicKeyWithSerialization = EllipticCurvePublicKey
EllipticCurvePublicKey.register(rust_openssl.ec.ECPublicKey)
EllipticCurvePrivateNumbers = rust_openssl.ec.EllipticCurvePrivateNumbers
EllipticCurvePublicNumbers = rust_openssl.ec.EllipticCurvePublicNumbers

class SECT571R1(EllipticCurve):
    name = 'sect571r1'
    key_size = 570
    group_order = 0x3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE661CE18FF55987308059B186823851EC7DD9CA1161DE93D5174D66E8382E9BB2FE84E47


class SECT409R1(EllipticCurve):
    name = 'sect409r1'
    key_size = 409
    group_order = 0x10000000000000000000000000000000000000000000000000001E2AAD6A612F33307BE5FA47C3C9E052F838164CD37D9A21173


class SECT283R1(EllipticCurve):
    name = 'sect283r1'
    key_size = 283
    group_order = 0x3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEF90399660FC938A90165B042A7CEFADB307


class SECT233R1(EllipticCurve):
    name = 'sect233r1'
    key_size = 233
    group_order = 0x1000000000000000000000000000013E974E72F8A6922031D2603CFE0D7


class SECT163R2(EllipticCurve):
    name = 'sect163r2'
    key_size = 163
    group_order = 0x40000000000000000000292FE77E70C12A4234C33


class SECT571K1(EllipticCurve):
    name = 'sect571k1'
    key_size = 571
    group_order = 0x20000000000000000000000000000000000000000000000000000000000000000000000131850E1F19A63E4B391A8DB917F4138B630D84BE5D639381E91DEB45CFE778F637C1001


class SECT409K1(EllipticCurve):
    name = 'sect409k1'
    key_size = 409
    group_order = 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE5F83B2D4EA20400EC4557D5ED3E3E7CA5B4B5C83B8E01E5FCF


class SECT283K1(EllipticCurve):
    name = 'sect283k1'
    key_size = 283
    group_order = 0x1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9AE2ED07577265DFF7F94451E061E163C61


class SECT233K1(EllipticCurve):
    name = 'sect233k1'
    key_size = 233
    group_order = 0x8000000000000000000000000000069D5BB915BCD46EFB1AD5F173ABDF


class SECT163K1(EllipticCurve):
    name = 'sect163k1'
    key_size = 163
    group_order = 0x4000000000000000000020108A2E0CC0D99F8A5EF


class SECP521R1(EllipticCurve):
    name = 'secp521r1'
    key_size = 521
    group_order = 0x1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA51868783BF2F966B7FCC0148F709A5D03BB5C9B8899C47AEBB6FB71E91386409


class SECP384R1(EllipticCurve):
    name = 'secp384r1'
    key_size = 384
    group_order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC7634D81F4372DDF581A0DB248B0A77AECEC196ACCC52973


class SECP256R1(EllipticCurve):
    name = 'secp256r1'
    key_size = 256
    group_order = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551


class SECP256K1(EllipticCurve):
    name = 'secp256k1'
    key_size = 256
    group_order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


class SECP224R1(EllipticCurve):
    name = 'secp224r1'
    key_size = 224
    group_order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF16A2E0B8F03E13DD29455C5C2A3D


class SECP192R1(EllipticCurve):
    name = 'secp192r1'
    key_size = 192
    group_order = 0xFFFFFFFFFFFFFFFFFFFFFFFF99DEF836146BC9B1B4D22831


class BrainpoolP256R1(EllipticCurve):
    name = 'brainpoolP256r1'
    key_size = 256
    group_order = 0xA9FB57DBA1EEA9BC3E660A909D838D718C397AA3B561A6F7901E0E82974856A7


class BrainpoolP384R1(EllipticCurve):
    name = 'brainpoolP384r1'
    key_size = 384
    group_order = 0x8CB91E82A3386D280F5D6F7E50E641DF152F7109ED5456B31F166E6CAC0425A7CF3AB6AF6B7FC3103B883202E9046565


class BrainpoolP512R1(EllipticCurve):
    name = 'brainpoolP512r1'
    key_size = 512
    group_order = 0xAADD9DB8DBE9C48B3FD4E6AE33C9FC07CB308DB3B3C9D20ED6639CCA70330870553E5C414CA92619418661197FAC10471DB1D381085DDADDB58796829CA90069

# WARNING: Decompyle incomplete
