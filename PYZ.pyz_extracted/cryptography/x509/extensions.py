# Source Generated with Decompyle++
# File: extensions.pyc (Python 3.12)

from __future__ import annotations
import abc
import datetime
import hashlib
import ipaddress
import typing
from collections.abc import Iterable, Iterator
from cryptography import utils
from cryptography.hazmat.bindings._rust import asn1
from cryptography.hazmat.bindings._rust import x509 as rust_x509
from cryptography.hazmat.primitives import constant_time, serialization
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.asymmetric.types import CertificateIssuerPublicKeyTypes, CertificatePublicKeyTypes
from cryptography.x509.certificate_transparency import SignedCertificateTimestamp
from cryptography.x509.general_name import DirectoryName, DNSName, GeneralName, IPAddress, OtherName, RegisteredID, RFC822Name, UniformResourceIdentifier, _IPAddressTypes
from cryptography.x509.name import Name, RelativeDistinguishedName
from cryptography.x509.oid import CRLEntryExtensionOID, ExtensionOID, ObjectIdentifier, OCSPExtensionOID
ExtensionTypeVar = typing.TypeVar('ExtensionTypeVar', bound = 'ExtensionType', covariant = True)

def _key_identifier_from_public_key(public_key = None):
    if isinstance(public_key, RSAPublicKey):
        data = public_key.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.PKCS1)
    elif isinstance(public_key, EllipticCurvePublicKey):
        data = public_key.public_bytes(serialization.Encoding.X962, serialization.PublicFormat.UncompressedPoint)
    else:
        serialized = public_key.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
        data = asn1.parse_spki_for_data(serialized)
    return hashlib.sha1(data).digest()


def _make_sequence_methods(field_name = None):
    pass
# WARNING: Decompyle incomplete


class DuplicateExtension(Exception):
    pass
# WARNING: Decompyle incomplete


class ExtensionNotFound(Exception):
    pass
# WARNING: Decompyle incomplete


def ExtensionType():
    '''ExtensionType'''
    oid: 'typing.ClassVar[ObjectIdentifier]' = 'ExtensionType'
    
    def public_bytes(self = None):
        '''
        Serializes the extension type to DER.
        '''
        raise NotImplementedError(f'''public_bytes is not implemented for extension type {self!r}''')


ExtensionType = <NODE:27>(ExtensionType, 'ExtensionType', metaclass = abc.ABCMeta)

class Extensions:
    
    def __init__(self = None, extensions = None):
        self._extensions = list(extensions)

    
    def get_extension_for_oid(self = None, oid = None):
        for ext in self:
            if not ext.oid == oid:
                continue
            
            return self, ext
        raise ExtensionNotFound(f'''No {oid} extension was found''', oid)

    
    def get_extension_for_class(self = None, extclass = None):
        if extclass is UnrecognizedExtension:
            raise TypeError("UnrecognizedExtension can't be used with get_extension_for_class because more than one instance of the class may be present.")
        for ext in self:
            if not isinstance(ext.value, extclass):
                continue
            
            return self, ext
        raise ExtensionNotFound(f'''No {extclass} extension was found''', extclass.oid)

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_extensions')
    
    def __repr__(self = None):
        return f'''<Extensions({self._extensions})>'''



class CRLNumber(ExtensionType):
    oid = ExtensionOID.CRL_NUMBER
    
    def __init__(self = None, crl_number = None):
        if not isinstance(crl_number, int):
            raise TypeError('crl_number must be an integer')
        self._crl_number = crl_number

    
    def __eq__(self = None, other = None):
        if not isinstance(other, CRLNumber):
            return NotImplemented
        return None.crl_number == other.crl_number

    
    def __hash__(self = None):
        return hash(self.crl_number)

    
    def __repr__(self = None):
        return f'''<CRLNumber({self.crl_number})>'''

    crl_number = (lambda self = None: self._crl_number)()
    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class AuthorityKeyIdentifier(ExtensionType):
    oid = ExtensionOID.AUTHORITY_KEY_IDENTIFIER
    
    def __init__(self = None, key_identifier = None, authority_cert_issuer = None, authority_cert_serial_number = ('key_identifier', 'bytes | None', 'authority_cert_issuer', 'Iterable[GeneralName] | None', 'authority_cert_serial_number', 'int | None', 'return', 'None')):
        if (authority_cert_issuer is None) != (authority_cert_serial_number is None):
            raise ValueError('authority_cert_issuer and authority_cert_serial_number must both be present or both None')
    # WARNING: Decompyle incomplete

    from_issuer_public_key = (lambda cls = None, public_key = None: digest = _key_identifier_from_public_key(public_key)cls(key_identifier = digest, authority_cert_issuer = None, authority_cert_serial_number = None))()
    from_issuer_subject_key_identifier = (lambda cls = None, ski = None: cls(key_identifier = ski.digest, authority_cert_issuer = None, authority_cert_serial_number = None))()
    
    def __repr__(self = None):
        return f'''<AuthorityKeyIdentifier(key_identifier={self.key_identifier!r}, authority_cert_issuer={self.authority_cert_issuer}, authority_cert_serial_number={self.authority_cert_serial_number})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, AuthorityKeyIdentifier):
            return NotImplemented
        if None.key_identifier == other.key_identifier:
            None.key_identifier == other.key_identifier
            if self.authority_cert_issuer == other.authority_cert_issuer:
                self.authority_cert_issuer == other.authority_cert_issuer
        return self.authority_cert_serial_number == other.authority_cert_serial_number

    
    def __hash__(self = None):
        pass
    # WARNING: Decompyle incomplete

    key_identifier = (lambda self = None: self._key_identifier)()
    authority_cert_issuer = (lambda self = None: self._authority_cert_issuer)()
    authority_cert_serial_number = (lambda self = None: self._authority_cert_serial_number)()
    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class SubjectKeyIdentifier(ExtensionType):
    oid = ExtensionOID.SUBJECT_KEY_IDENTIFIER
    
    def __init__(self = None, digest = None):
        self._digest = digest

    from_public_key = (lambda cls = None, public_key = None: cls(_key_identifier_from_public_key(public_key)))()
    digest = (lambda self = None: self._digest)()
    key_identifier = (lambda self = None: self._digest)()
    
    def __repr__(self = None):
        return f'''<SubjectKeyIdentifier(digest={self.digest!r})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, SubjectKeyIdentifier):
            return NotImplemented
        return None.bytes_eq(self.digest, other.digest)

    
    def __hash__(self = None):
        return hash(self.digest)

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class AuthorityInformationAccess(ExtensionType):
    oid = ExtensionOID.AUTHORITY_INFORMATION_ACCESS
    
    def __init__(self = None, descriptions = None):
        descriptions = list(descriptions)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(descriptions()):
            raise TypeError('Every item in the descriptions list must be an AccessDescription')
        self._descriptions = descriptions

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_descriptions')
    
    def __repr__(self = None):
        return f'''<AuthorityInformationAccess({self._descriptions})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, AuthorityInformationAccess):
            return NotImplemented
        return None._descriptions == other._descriptions

    
    def __hash__(self = None):
        return hash(tuple(self._descriptions))

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class SubjectInformationAccess(ExtensionType):
    oid = ExtensionOID.SUBJECT_INFORMATION_ACCESS
    
    def __init__(self = None, descriptions = None):
        descriptions = list(descriptions)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(descriptions()):
            raise TypeError('Every item in the descriptions list must be an AccessDescription')
        self._descriptions = descriptions

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_descriptions')
    
    def __repr__(self = None):
        return f'''<SubjectInformationAccess({self._descriptions})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, SubjectInformationAccess):
            return NotImplemented
        return None._descriptions == other._descriptions

    
    def __hash__(self = None):
        return hash(tuple(self._descriptions))

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class AccessDescription:
    
    def __init__(self = None, access_method = None, access_location = None):
        if not isinstance(access_method, ObjectIdentifier):
            raise TypeError('access_method must be an ObjectIdentifier')
        if not isinstance(access_location, GeneralName):
            raise TypeError('access_location must be a GeneralName')
        self._access_method = access_method
        self._access_location = access_location

    
    def __repr__(self = None):
        return f'''<AccessDescription(access_method={self.access_method}, access_location={self.access_location})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, AccessDescription):
            return NotImplemented
        if None.access_method == other.access_method:
            None.access_method == other.access_method
        return self.access_location == other.access_location

    
    def __hash__(self = None):
        return hash((self.access_method, self.access_location))

    access_method = (lambda self = None: self._access_method)()
    access_location = (lambda self = None: self._access_location)()


class BasicConstraints(ExtensionType):
    oid = ExtensionOID.BASIC_CONSTRAINTS
    
    def __init__(self = None, ca = None, path_length = None):
        if not isinstance(ca, bool):
            raise TypeError('ca must be a boolean value')
    # WARNING: Decompyle incomplete

    ca = (lambda self = None: self._ca)()
    path_length = (lambda self = None: self._path_length)()
    
    def __repr__(self = None):
        return f'''<BasicConstraints(ca={self.ca}, path_length={self.path_length})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, BasicConstraints):
            return NotImplemented
        if None.ca == other.ca:
            None.ca == other.ca
        return self.path_length == other.path_length

    
    def __hash__(self = None):
        return hash((self.ca, self.path_length))

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class DeltaCRLIndicator(ExtensionType):
    oid = ExtensionOID.DELTA_CRL_INDICATOR
    
    def __init__(self = None, crl_number = None):
        if not isinstance(crl_number, int):
            raise TypeError('crl_number must be an integer')
        self._crl_number = crl_number

    crl_number = (lambda self = None: self._crl_number)()
    
    def __eq__(self = None, other = None):
        if not isinstance(other, DeltaCRLIndicator):
            return NotImplemented
        return None.crl_number == other.crl_number

    
    def __hash__(self = None):
        return hash(self.crl_number)

    
    def __repr__(self = None):
        return f'''<DeltaCRLIndicator(crl_number={self.crl_number})>'''

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class CRLDistributionPoints(ExtensionType):
    oid = ExtensionOID.CRL_DISTRIBUTION_POINTS
    
    def __init__(self = None, distribution_points = None):
        distribution_points = list(distribution_points)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(distribution_points()):
            raise TypeError('distribution_points must be a list of DistributionPoint objects')
        self._distribution_points = distribution_points

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_distribution_points')
    
    def __repr__(self = None):
        return f'''<CRLDistributionPoints({self._distribution_points})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, CRLDistributionPoints):
            return NotImplemented
        return None._distribution_points == other._distribution_points

    
    def __hash__(self = None):
        return hash(tuple(self._distribution_points))

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class FreshestCRL(ExtensionType):
    oid = ExtensionOID.FRESHEST_CRL
    
    def __init__(self = None, distribution_points = None):
        distribution_points = list(distribution_points)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(distribution_points()):
            raise TypeError('distribution_points must be a list of DistributionPoint objects')
        self._distribution_points = distribution_points

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_distribution_points')
    
    def __repr__(self = None):
        return f'''<FreshestCRL({self._distribution_points})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, FreshestCRL):
            return NotImplemented
        return None._distribution_points == other._distribution_points

    
    def __hash__(self = None):
        return hash(tuple(self._distribution_points))

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class DistributionPoint:
    
    def __init__(self, full_name = None, relative_name = None, reasons = None, crl_issuer = ('full_name', 'Iterable[GeneralName] | None', 'relative_name', 'RelativeDistinguishedName | None', 'reasons', 'frozenset[ReasonFlags] | None', 'crl_issuer', 'Iterable[GeneralName] | None', 'return', 'None')):
        if full_name and relative_name:
            raise ValueError('You cannot provide both full_name and relative_name, at least one must be None.')
        if not full_name and relative_name and crl_issuer:
            raise ValueError('Either full_name, relative_name or crl_issuer must be provided.')
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return '<DistributionPoint(full_name={0.full_name}, relative_name={0.relative_name}, reasons={0.reasons}, crl_issuer={0.crl_issuer})>'.format(self)

    
    def __eq__(self = None, other = None):
        if not isinstance(other, DistributionPoint):
            return NotImplemented
        if None.full_name == other.full_name:
            None.full_name == other.full_name
            if self.relative_name == other.relative_name:
                self.relative_name == other.relative_name
                if self.reasons == other.reasons:
                    self.reasons == other.reasons
        return self.crl_issuer == other.crl_issuer

    
    def __hash__(self = None):
        pass
    # WARNING: Decompyle incomplete

    full_name = (lambda self = None: self._full_name)()
    relative_name = (lambda self = None: self._relative_name)()
    reasons = (lambda self = None: self._reasons)()
    crl_issuer = (lambda self = None: self._crl_issuer)()


class ReasonFlags(utils.Enum):
    unspecified = 'unspecified'
    key_compromise = 'keyCompromise'
    ca_compromise = 'cACompromise'
    affiliation_changed = 'affiliationChanged'
    superseded = 'superseded'
    cessation_of_operation = 'cessationOfOperation'
    certificate_hold = 'certificateHold'
    privilege_withdrawn = 'privilegeWithdrawn'
    aa_compromise = 'aACompromise'
    remove_from_crl = 'removeFromCRL'

_REASON_BIT_MAPPING = {
    1: ReasonFlags.key_compromise,
    2: ReasonFlags.ca_compromise,
    3: ReasonFlags.affiliation_changed,
    4: ReasonFlags.superseded,
    5: ReasonFlags.cessation_of_operation,
    6: ReasonFlags.certificate_hold,
    7: ReasonFlags.privilege_withdrawn,
    8: ReasonFlags.aa_compromise }
_CRLREASONFLAGS = {
    ReasonFlags.aa_compromise: 8,
    ReasonFlags.privilege_withdrawn: 7,
    ReasonFlags.certificate_hold: 6,
    ReasonFlags.cessation_of_operation: 5,
    ReasonFlags.superseded: 4,
    ReasonFlags.affiliation_changed: 3,
    ReasonFlags.ca_compromise: 2,
    ReasonFlags.key_compromise: 1 }
_CRL_ENTRY_REASON_ENUM_TO_CODE = {
    ReasonFlags.aa_compromise: 10,
    ReasonFlags.privilege_withdrawn: 9,
    ReasonFlags.remove_from_crl: 8,
    ReasonFlags.certificate_hold: 6,
    ReasonFlags.cessation_of_operation: 5,
    ReasonFlags.superseded: 4,
    ReasonFlags.affiliation_changed: 3,
    ReasonFlags.ca_compromise: 2,
    ReasonFlags.key_compromise: 1,
    ReasonFlags.unspecified: 0 }

class PolicyConstraints(ExtensionType):
    oid = ExtensionOID.POLICY_CONSTRAINTS
    
    def __init__(self = None, require_explicit_policy = None, inhibit_policy_mapping = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return '<PolicyConstraints(require_explicit_policy={0.require_explicit_policy}, inhibit_policy_mapping={0.inhibit_policy_mapping})>'.format(self)

    
    def __eq__(self = None, other = None):
        if not isinstance(other, PolicyConstraints):
            return NotImplemented
        if None.require_explicit_policy == other.require_explicit_policy:
            None.require_explicit_policy == other.require_explicit_policy
        return self.inhibit_policy_mapping == other.inhibit_policy_mapping

    
    def __hash__(self = None):
        return hash((self.require_explicit_policy, self.inhibit_policy_mapping))

    require_explicit_policy = (lambda self = None: self._require_explicit_policy)()
    inhibit_policy_mapping = (lambda self = None: self._inhibit_policy_mapping)()
    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class CertificatePolicies(ExtensionType):
    oid = ExtensionOID.CERTIFICATE_POLICIES
    
    def __init__(self = None, policies = None):
        policies = list(policies)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(policies()):
            raise TypeError('Every item in the policies list must be a PolicyInformation')
        self._policies = policies

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_policies')
    
    def __repr__(self = None):
        return f'''<CertificatePolicies({self._policies})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, CertificatePolicies):
            return NotImplemented
        return None._policies == other._policies

    
    def __hash__(self = None):
        return hash(tuple(self._policies))

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class PolicyInformation:
    
    def __init__(self = None, policy_identifier = None, policy_qualifiers = None):
        if not isinstance(policy_identifier, ObjectIdentifier):
            raise TypeError('policy_identifier must be an ObjectIdentifier')
        self._policy_identifier = policy_identifier
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<PolicyInformation(policy_identifier={self.policy_identifier}, policy_qualifiers={self.policy_qualifiers})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, PolicyInformation):
            return NotImplemented
        if None.policy_identifier == other.policy_identifier:
            None.policy_identifier == other.policy_identifier
        return self.policy_qualifiers == other.policy_qualifiers

    
    def __hash__(self = None):
        pass
    # WARNING: Decompyle incomplete

    policy_identifier = (lambda self = None: self._policy_identifier)()
    policy_qualifiers = (lambda self = None: self._policy_qualifiers)()


class UserNotice:
    
    def __init__(self = None, notice_reference = None, explicit_text = None):
        if not notice_reference and isinstance(notice_reference, NoticeReference):
            raise TypeError('notice_reference must be None or a NoticeReference')
        self._notice_reference = notice_reference
        self._explicit_text = explicit_text

    
    def __repr__(self = None):
        return f'''<UserNotice(notice_reference={self.notice_reference}, explicit_text={self.explicit_text!r})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, UserNotice):
            return NotImplemented
        if None.notice_reference == other.notice_reference:
            None.notice_reference == other.notice_reference
        return self.explicit_text == other.explicit_text

    
    def __hash__(self = None):
        return hash((self.notice_reference, self.explicit_text))

    notice_reference = (lambda self = None: self._notice_reference)()
    explicit_text = (lambda self = None: self._explicit_text)()


class NoticeReference:
    
    def __init__(self = None, organization = None, notice_numbers = None):
        self._organization = organization
        notice_numbers = list(notice_numbers)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(notice_numbers()):
            raise TypeError('notice_numbers must be a list of integers')
        self._notice_numbers = notice_numbers

    
    def __repr__(self = None):
        return f'''<NoticeReference(organization={self.organization!r}, notice_numbers={self.notice_numbers})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, NoticeReference):
            return NotImplemented
        if None.organization == other.organization:
            None.organization == other.organization
        return self.notice_numbers == other.notice_numbers

    
    def __hash__(self = None):
        return hash((self.organization, tuple(self.notice_numbers)))

    organization = (lambda self = None: self._organization)()
    notice_numbers = (lambda self = None: self._notice_numbers)()


class ExtendedKeyUsage(ExtensionType):
    oid = ExtensionOID.EXTENDED_KEY_USAGE
    
    def __init__(self = None, usages = None):
        usages = list(usages)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(usages()):
            raise TypeError('Every item in the usages list must be an ObjectIdentifier')
        self._usages = usages

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_usages')
    
    def __repr__(self = None):
        return f'''<ExtendedKeyUsage({self._usages})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, ExtendedKeyUsage):
            return NotImplemented
        return None._usages == other._usages

    
    def __hash__(self = None):
        return hash(tuple(self._usages))

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class OCSPNoCheck(ExtensionType):
    oid = ExtensionOID.OCSP_NO_CHECK
    
    def __eq__(self = None, other = None):
        if not isinstance(other, OCSPNoCheck):
            return NotImplemented

    
    def __hash__(self = None):
        return hash(OCSPNoCheck)

    
    def __repr__(self = None):
        return '<OCSPNoCheck()>'

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class PrecertPoison(ExtensionType):
    oid = ExtensionOID.PRECERT_POISON
    
    def __eq__(self = None, other = None):
        if not isinstance(other, PrecertPoison):
            return NotImplemented

    
    def __hash__(self = None):
        return hash(PrecertPoison)

    
    def __repr__(self = None):
        return '<PrecertPoison()>'

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class TLSFeature(ExtensionType):
    oid = ExtensionOID.TLS_FEATURE
    
    def __init__(self = None, features = None):
        features = list(features)
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(features()) or len(features) == 0:
            raise TypeError('features must be a list of elements from the TLSFeatureType enum')
        self._features = features

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_features')
    
    def __repr__(self = None):
        return f'''<TLSFeature(features={self._features})>'''

    
    def __eq__(self = None, other = None):
        if not isinstance(other, TLSFeature):
            return NotImplemented
        return None._features == other._features

    
    def __hash__(self = None):
        return hash(tuple(self._features))

    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class TLSFeatureType(utils.Enum):
    status_request = 5
    status_request_v2 = 17

# WARNING: Decompyle incomplete
