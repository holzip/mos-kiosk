# Source Generated with Decompyle++
# File: ssh.pyc (Python 3.12)

from __future__ import annotations
import binascii
import enum
import os
import re
import typing
import warnings
from base64 import encodebytes as _base64_encode
from dataclasses import dataclass
from cryptography import utils
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa, ec, ed25519, padding, rsa
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils
from cryptography.hazmat.primitives.ciphers import AEADDecryptionContext, Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import Encoding, KeySerializationEncryption, NoEncryption, PrivateFormat, PublicFormat, _KeySerializationEncryption

try:
    from bcrypt import kdf as _bcrypt_kdf
    _bcrypt_supported = True
    _SSH_ED25519 = b'ssh-ed25519'
    _SSH_RSA = b'ssh-rsa'
    _SSH_DSA = b'ssh-dss'
    _ECDSA_NISTP256 = b'ecdsa-sha2-nistp256'
    _ECDSA_NISTP384 = b'ecdsa-sha2-nistp384'
    _ECDSA_NISTP521 = b'ecdsa-sha2-nistp521'
    _CERT_SUFFIX = b'-cert-v01@openssh.com'
    _SK_SSH_ED25519 = b'sk-ssh-ed25519@openssh.com'
    _SK_SSH_ECDSA_NISTP256 = b'sk-ecdsa-sha2-nistp256@openssh.com'
    _SSH_RSA_SHA256 = b'rsa-sha2-256'
    _SSH_RSA_SHA512 = b'rsa-sha2-512'
    _SSH_PUBKEY_RC = re.compile(b'\\A(\\S+)[ \\t]+(\\S+)')
    _SK_MAGIC = b'openssh-key-v1\x00'
    _SK_START = b'-----BEGIN OPENSSH PRIVATE KEY-----'
    _SK_END = b'-----END OPENSSH PRIVATE KEY-----'
    _BCRYPT = b'bcrypt'
    _NONE = b'none'
    _DEFAULT_CIPHER = b'aes256-ctr'
    _DEFAULT_ROUNDS = 16
    _PEM_RC = re.compile(_SK_START + b'(.*?)' + _SK_END, re.DOTALL)
    _PADDING = memoryview(bytearray(range(1, 17)))
    _SSHCipher = <NODE:12>()
    _SSH_CIPHERS: 'dict[bytes, _SSHCipher]' = {
        b'aes256-ctr': _SSHCipher(alg = algorithms.AES, key_len = 32, mode = modes.CTR, block_len = 16, iv_len = 16, tag_len = None, is_aead = False),
        b'aes256-cbc': _SSHCipher(alg = algorithms.AES, key_len = 32, mode = modes.CBC, block_len = 16, iv_len = 16, tag_len = None, is_aead = False),
        b'aes256-gcm@openssh.com': _SSHCipher(alg = algorithms.AES, key_len = 32, mode = modes.GCM, block_len = 16, iv_len = 12, tag_len = 16, is_aead = True) }
    _ECDSA_KEY_TYPE = {
        'secp256r1': _ECDSA_NISTP256,
        'secp384r1': _ECDSA_NISTP384,
        'secp521r1': _ECDSA_NISTP521 }
    
    def _get_ssh_key_type(key = None):
        if isinstance(key, ec.EllipticCurvePrivateKey):
            key_type = _ecdsa_key_type(key.public_key())
            return key_type
        if None(key, ec.EllipticCurvePublicKey):
            key_type = _ecdsa_key_type(key)
            return key_type
        if None(key, (rsa.RSAPrivateKey, rsa.RSAPublicKey)):
            key_type = _SSH_RSA
            return key_type
        if None(key, (dsa.DSAPrivateKey, dsa.DSAPublicKey)):
            key_type = _SSH_DSA
            return key_type
        if None(key, (ed25519.Ed25519PrivateKey, ed25519.Ed25519PublicKey)):
            key_type = _SSH_ED25519
            return key_type
        raise None('Unsupported key type')

    
    def _ecdsa_key_type(public_key = None):
        '''Return SSH key_type and curve_name for private key.'''
        curve = public_key.curve
        if curve.name not in _ECDSA_KEY_TYPE:
            raise ValueError(f'''Unsupported curve for ssh private key: {curve.name!r}''')
        return _ECDSA_KEY_TYPE[curve.name]

    
    def _ssh_pem_encode(data = None, prefix = None, suffix = None):
        return b''.join([
            prefix,
            _base64_encode(data),
            suffix])

    
    def _check_block_size(data = None, block_len = None):
        '''Require data to be full blocks'''
        if data or len(data) % block_len != 0:
            raise ValueError('Corrupt data: missing padding')

    
    def _check_empty(data = None):
        '''All data should have been parsed.'''
        if data:
            raise ValueError('Corrupt data: unparsed data')

    
    def _init_cipher(ciphername = None, password = None, salt = None, rounds = ('ciphername', 'bytes', 'password', 'bytes | None', 'salt', 'bytes', 'rounds', 'int', 'return', 'Cipher[modes.CBC | modes.CTR | modes.GCM]')):
        '''Generate key + iv and return cipher.'''
        if not password:
            raise TypeError('Key is password-protected, but password was not provided.')
        ciph = _SSH_CIPHERS[ciphername]
        seed = _bcrypt_kdf(password, salt, ciph.key_len + ciph.iv_len, rounds, True)
        return Cipher(ciph.alg(seed[:ciph.key_len]), ciph.mode(seed[ciph.key_len:]))

    
    def _get_u32(data = None):
        '''Uint32'''
        if len(data) < 4:
            raise ValueError('Invalid data')
        return (int.from_bytes(data[:4], byteorder = 'big'), data[4:])

    
    def _get_u64(data = None):
        '''Uint64'''
        if len(data) < 8:
            raise ValueError('Invalid data')
        return (int.from_bytes(data[:8], byteorder = 'big'), data[8:])

    
    def _get_sshstr(data = None):
        '''Bytes with u32 length prefix'''
        (n, data) = _get_u32(data)
        if n > len(data):
            raise ValueError('Invalid data')
        return (data[:n], data[n:])

    
    def _get_mpint(data = None):
        '''Big integer.'''
        (val, data) = _get_sshstr(data)
        if val and val[0] > 127:
            raise ValueError('Invalid data')
        return (int.from_bytes(val, 'big'), data)

    
    def _to_mpint(val = None):
        '''Storage format for signed bigint.'''
        if val < 0:
            raise ValueError('negative mpint not allowed')
        if not val:
            return b''
        nbytes = (val.bit_length() + 8) // 8
        return utils.int_to_bytes(val, nbytes)

    
    class _FragList:
        flist: 'list[utils.Buffer]' = 'Build recursive structure without data copy.'
        
        def __init__(self = None, init = None):
            self.flist = []
            if init:
                self.flist.extend(init)
                return None

        
        def put_raw(self = None, val = None):
            '''Add plain bytes'''
            self.flist.append(val)

        
        def put_u32(self = None, val = None):
            '''Big-endian uint32'''
            self.flist.append(val.to_bytes(length = 4, byteorder = 'big'))

        
        def put_u64(self = None, val = None):
            '''Big-endian uint64'''
            self.flist.append(val.to_bytes(length = 8, byteorder = 'big'))

        
        def put_sshstr(self = None, val = None):
            '''Bytes prefixed with u32 length'''
            if isinstance(val, (bytes, memoryview, bytearray)):
                self.put_u32(len(val))
                self.flist.append(val)
                return None
            self.put_u32(val.size())
            self.flist.extend(val.flist)

        
        def put_mpint(self = None, val = None):
            '''Big-endian bigint prefixed with u32 length'''
            self.put_sshstr(_to_mpint(val))

        
        def size(self = None):
            '''Current number of bytes'''
            return sum(map(len, self.flist))

        
        def render(self = None, dstbuf = None, pos = None):
            '''Write into bytearray'''
            for frag in self.flist:
                flen = len(frag)
                pos = pos + flen
                start = pos
                dstbuf[start:pos] = frag
            return pos

        
        def tobytes(self = None):
            '''Return as bytes'''
            buf = memoryview(bytearray(self.size()))
            self.render(buf)
            return buf.tobytes()


    
    class _SSHFormatRSA:
        '''Format for RSA keys.

    Public:
        mpint e, n
    Private:
        mpint n, e, d, iqmp, p, q
    '''
        
        def get_public(self = None, data = None):
            '''RSA public fields'''
            (e, data) = _get_mpint(data)
            (n, data) = _get_mpint(data)
            return ((e, n), data)

        
        def load_public(self = None, data = None):
            '''Make RSA public key from data.'''
            (e, n) = ()
            data = self.get_public(data)
            public_numbers = rsa.RSAPublicNumbers(e, n)
            public_key = public_numbers.public_key()
            return (public_key, data)

        
        def load_private(self = None, data = None, pubfields = None, unsafe_skip_rsa_key_validation = ('data', 'memoryview', 'unsafe_skip_rsa_key_validation', 'bool', 'return', 'tuple[rsa.RSAPrivateKey, memoryview]')):
            '''Make RSA private key from data.'''
            (n, data) = _get_mpint(data)
            (e, data) = _get_mpint(data)
            (d, data) = _get_mpint(data)
            (iqmp, data) = _get_mpint(data)
            (p, data) = _get_mpint(data)
            (q, data) = _get_mpint(data)
            if (e, n) != pubfields:
                raise ValueError('Corrupt data: rsa field mismatch')
            dmp1 = rsa.rsa_crt_dmp1(d, p)
            dmq1 = rsa.rsa_crt_dmq1(d, q)
            public_numbers = rsa.RSAPublicNumbers(e, n)
            private_numbers = rsa.RSAPrivateNumbers(p, q, d, dmp1, dmq1, iqmp, public_numbers)
            private_key = private_numbers.private_key(unsafe_skip_rsa_key_validation = unsafe_skip_rsa_key_validation)
            return (private_key, data)

        
        def encode_public(self = None, public_key = None, f_pub = None):
            '''Write RSA public key'''
            pubn = public_key.public_numbers()
            f_pub.put_mpint(pubn.e)
            f_pub.put_mpint(pubn.n)

        
        def encode_private(self = None, private_key = None, f_priv = None):
            '''Write RSA private key'''
            private_numbers = private_key.private_numbers()
            public_numbers = private_numbers.public_numbers
            f_priv.put_mpint(public_numbers.n)
            f_priv.put_mpint(public_numbers.e)
            f_priv.put_mpint(private_numbers.d)
            f_priv.put_mpint(private_numbers.iqmp)
            f_priv.put_mpint(private_numbers.p)
            f_priv.put_mpint(private_numbers.q)


    
    class _SSHFormatDSA:
        '''Format for DSA keys.

    Public:
        mpint p, q, g, y
    Private:
        mpint p, q, g, y, x
    '''
        
        def get_public(self = None, data = None):
            '''DSA public fields'''
            (p, data) = _get_mpint(data)
            (q, data) = _get_mpint(data)
            (g, data) = _get_mpint(data)
            (y, data) = _get_mpint(data)
            return ((p, q, g, y), data)

        
        def load_public(self = None, data = None):
            '''Make DSA public key from data.'''
            (p, q, g, y) = ()
            data = self.get_public(data)
            parameter_numbers = dsa.DSAParameterNumbers(p, q, g)
            public_numbers = dsa.DSAPublicNumbers(y, parameter_numbers)
            self._validate(public_numbers)
            public_key = public_numbers.public_key()
            return (public_key, data)

        
        def load_private(self = None, data = None, pubfields = None, unsafe_skip_rsa_key_validation = ('data', 'memoryview', 'unsafe_skip_rsa_key_validation', 'bool', 'return', 'tuple[dsa.DSAPrivateKey, memoryview]')):
            '''Make DSA private key from data.'''
            (p, q, g, y) = ()
            data = self.get_public(data)
            (x, data) = _get_mpint(data)
            if (p, q, g, y) != pubfields:
                raise ValueError('Corrupt data: dsa field mismatch')
            parameter_numbers = dsa.DSAParameterNumbers(p, q, g)
            public_numbers = dsa.DSAPublicNumbers(y, parameter_numbers)
            self._validate(public_numbers)
            private_numbers = dsa.DSAPrivateNumbers(x, public_numbers)
            private_key = private_numbers.private_key()
            return (private_key, data)

        
        def encode_public(self = None, public_key = None, f_pub = None):
            '''Write DSA public key'''
            public_numbers = public_key.public_numbers()
            parameter_numbers = public_numbers.parameter_numbers
            self._validate(public_numbers)
            f_pub.put_mpint(parameter_numbers.p)
            f_pub.put_mpint(parameter_numbers.q)
            f_pub.put_mpint(parameter_numbers.g)
            f_pub.put_mpint(public_numbers.y)

        
        def encode_private(self = None, private_key = None, f_priv = None):
            '''Write DSA private key'''
            self.encode_public(private_key.public_key(), f_priv)
            f_priv.put_mpint(private_key.private_numbers().x)

        
        def _validate(self = None, public_numbers = None):
            parameter_numbers = public_numbers.parameter_numbers
            if parameter_numbers.p.bit_length() != 1024:
                raise ValueError('SSH supports only 1024 bit DSA keys')


    
    class _SSHFormatECDSA:
        '''Format for ECDSA keys.

    Public:
        str curve
        bytes point
    Private:
        str curve
        bytes point
        mpint secret
    '''
        
        def __init__(self = None, ssh_curve_name = None, curve = None):
            self.ssh_curve_name = ssh_curve_name
            self.curve = curve

        
        def get_public(self = None, data = None):
            '''ECDSA public fields'''
            (curve, data) = _get_sshstr(data)
            (point, data) = _get_sshstr(data)
            if curve != self.ssh_curve_name:
                raise ValueError('Curve name mismatch')
            if point[0] != 4:
                raise NotImplementedError('Need uncompressed point')
            return ((curve, point), data)

        
        def load_public(self = None, data = None):
            '''Make ECDSA public key from data.'''
            (_, point) = ()
            data = self.get_public(data)
            public_key = ec.EllipticCurvePublicKey.from_encoded_point(self.curve, point.tobytes())
            return (public_key, data)

        
        def load_private(self = None, data = None, pubfields = None, unsafe_skip_rsa_key_validation = ('data', 'memoryview', 'unsafe_skip_rsa_key_validation', 'bool', 'return', 'tuple[ec.EllipticCurvePrivateKey, memoryview]')):
            '''Make ECDSA private key from data.'''
            (curve_name, point) = ()
            data = self.get_public(data)
            (secret, data) = _get_mpint(data)
            if (curve_name, point) != pubfields:
                raise ValueError('Corrupt data: ecdsa field mismatch')
            private_key = ec.derive_private_key(secret, self.curve)
            return (private_key, data)

        
        def encode_public(self = None, public_key = None, f_pub = None):
            '''Write ECDSA public key'''
            point = public_key.public_bytes(Encoding.X962, PublicFormat.UncompressedPoint)
            f_pub.put_sshstr(self.ssh_curve_name)
            f_pub.put_sshstr(point)

        
        def encode_private(self = None, private_key = None, f_priv = None):
            '''Write ECDSA private key'''
            public_key = private_key.public_key()
            private_numbers = private_key.private_numbers()
            self.encode_public(public_key, f_priv)
            f_priv.put_mpint(private_numbers.private_value)


    
    class _SSHFormatEd25519:
        '''Format for Ed25519 keys.

    Public:
        bytes point
    Private:
        bytes point
        bytes secret_and_point
    '''
        
        def get_public(self = None, data = None):
            '''Ed25519 public fields'''
            (point, data) = _get_sshstr(data)
            return ((point,), data)

        
        def load_public(self = None, data = None):
            '''Make Ed25519 public key from data.'''
            (point,) = ()
            data = self.get_public(data)
            public_key = ed25519.Ed25519PublicKey.from_public_bytes(point.tobytes())
            return (public_key, data)

        
        def load_private(self = None, data = None, pubfields = None, unsafe_skip_rsa_key_validation = ('data', 'memoryview', 'unsafe_skip_rsa_key_validation', 'bool', 'return', 'tuple[ed25519.Ed25519PrivateKey, memoryview]')):
            '''Make Ed25519 private key from data.'''
            (point,) = ()
            data = self.get_public(data)
            (keypair, data) = _get_sshstr(data)
            secret = keypair[:32]
            point2 = keypair[32:]
            if point != point2 or (point,) != pubfields:
                raise ValueError('Corrupt data: ed25519 field mismatch')
            private_key = ed25519.Ed25519PrivateKey.from_private_bytes(secret)
            return (private_key, data)

        
        def encode_public(self = None, public_key = None, f_pub = None):
            '''Write Ed25519 public key'''
            raw_public_key = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
            f_pub.put_sshstr(raw_public_key)

        
        def encode_private(self = None, private_key = None, f_priv = None):
            '''Write Ed25519 private key'''
            public_key = private_key.public_key()
            raw_private_key = private_key.private_bytes(Encoding.Raw, PrivateFormat.Raw, NoEncryption())
            raw_public_key = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
            f_keypair = _FragList([
                raw_private_key,
                raw_public_key])
            self.encode_public(public_key, f_priv)
            f_priv.put_sshstr(f_keypair)


    
    def load_application(data = None):
        '''
    U2F application strings
    '''
        (application, data) = _get_sshstr(data)
        if not application.tobytes().startswith(b'ssh:'):
            raise ValueError(f'''U2F application string does not start with b\'ssh:\' ({application})''')
        return (application, data)

    
    class _SSHFormatSKEd25519:
        '''
    The format of a sk-ssh-ed25519@openssh.com public key is:

        string\t\t"sk-ssh-ed25519@openssh.com"
        string\t\tpublic key
        string\t\tapplication (user-specified, but typically "ssh:")
    '''
        
        def load_public(self = None, data = None):
            '''Make Ed25519 public key from data.'''
            (public_key, data) = _lookup_kformat(_SSH_ED25519).load_public(data)
            (_, data) = load_application(data)
            return (public_key, data)

        
        def get_public(self = None, data = None):
            raise UnsupportedAlgorithm('sk-ssh-ed25519 private keys cannot be loaded')


    
    class _SSHFormatSKECDSA:
        '''
    The format of a sk-ecdsa-sha2-nistp256@openssh.com public key is:

        string\t\t"sk-ecdsa-sha2-nistp256@openssh.com"
        string\t\tcurve name
        ec_point\tQ
        string\t\tapplication (user-specified, but typically "ssh:")
    '''
        
        def load_public(self = None, data = None):
            '''Make ECDSA public key from data.'''
            (public_key, data) = _lookup_kformat(_ECDSA_NISTP256).load_public(data)
            (_, data) = load_application(data)
            return (public_key, data)

        
        def get_public(self = None, data = None):
            raise UnsupportedAlgorithm('sk-ecdsa-sha2-nistp256 private keys cannot be loaded')


    _KEY_FORMATS = {
        _SK_SSH_ECDSA_NISTP256: _SSHFormatSKECDSA(),
        _SK_SSH_ED25519: _SSHFormatSKEd25519(),
        _ECDSA_NISTP521: _SSHFormatECDSA(b'nistp521', ec.SECP521R1()),
        _ECDSA_NISTP384: _SSHFormatECDSA(b'nistp384', ec.SECP384R1()),
        _ECDSA_NISTP256: _SSHFormatECDSA(b'nistp256', ec.SECP256R1()),
        _SSH_ED25519: _SSHFormatEd25519(),
        _SSH_DSA: _SSHFormatDSA(),
        _SSH_RSA: _SSHFormatRSA() }
    
    def _lookup_kformat(key_type = None):
        '''Return valid format or throw error'''
        if not isinstance(key_type, bytes):
            key_type = memoryview(key_type).tobytes()
        if key_type in _KEY_FORMATS:
            return _KEY_FORMATS[key_type]
        raise None(f'''Unsupported key type: {key_type!r}''')

    SSHPrivateKeyTypes = typing.Union[(ec.EllipticCurvePrivateKey, rsa.RSAPrivateKey, dsa.DSAPrivateKey, ed25519.Ed25519PrivateKey)]
    
    def load_ssh_private_key(data = None, password = None, backend = None, *, unsafe_skip_rsa_key_validation):
        '''Load private key from OpenSSH custom encoding.'''
        utils._check_byteslike('data', data)
    # WARNING: Decompyle incomplete

    
    def _serialize_ssh_private_key(private_key = None, password = None, encryption_algorithm = None):
        '''Serialize private key with OpenSSH custom encoding.'''
        utils._check_bytes('password', password)
        if isinstance(private_key, dsa.DSAPrivateKey):
            warnings.warn('SSH DSA key support is deprecated and will be removed in a future release', utils.DeprecatedIn40, stacklevel = 4)
        key_type = _get_ssh_key_type(private_key)
        kformat = _lookup_kformat(key_type)
        f_kdfoptions = _FragList()
    # WARNING: Decompyle incomplete

    SSHPublicKeyTypes = typing.Union[(ec.EllipticCurvePublicKey, rsa.RSAPublicKey, dsa.DSAPublicKey, ed25519.Ed25519PublicKey)]
    SSHCertPublicKeyTypes = typing.Union[(ec.EllipticCurvePublicKey, rsa.RSAPublicKey, ed25519.Ed25519PublicKey)]
    
    class SSHCertificateType(enum.Enum):
        USER = 1
        HOST = 2

    
    class SSHCertificate:
        
        def __init__(self, _nonce, _public_key, _serial, _cctype, _key_id, _valid_principals, _valid_after, _valid_before, _critical_options, _extensions, _sig_type, _sig_key, _inner_sig_type, _signature = None, _tbs_cert_body = None, _cert_key_type = None, _cert_body = ('_nonce', 'memoryview', '_public_key', 'SSHPublicKeyTypes', '_serial', 'int', '_cctype', 'int', '_key_id', 'memoryview', '_valid_principals', 'list[bytes]', '_valid_after', 'int', '_valid_before', 'int', '_critical_options', 'dict[bytes, bytes]', '_extensions', 'dict[bytes, bytes]', '_sig_type', 'memoryview', '_sig_key', 'memoryview', '_inner_sig_type', 'memoryview', '_signature', 'memoryview', '_tbs_cert_body', 'memoryview', '_cert_key_type', 'bytes', '_cert_body', 'memoryview')):
            self._nonce = _nonce
            self._public_key = _public_key
            self._serial = _serial
            
            try:
                self._type = SSHCertificateType(_cctype)
                self._key_id = _key_id
                self._valid_principals = _valid_principals
                self._valid_after = _valid_after
                self._valid_before = _valid_before
                self._critical_options = _critical_options
                self._extensions = _extensions
                self._sig_type = _sig_type
                self._sig_key = _sig_key
                self._inner_sig_type = _inner_sig_type
                self._signature = _signature
                self._cert_key_type = _cert_key_type
                self._cert_body = _cert_body
                self._tbs_cert_body = _tbs_cert_body
                return None
            except ValueError:
                raise ValueError('Invalid certificate type')


        nonce = (lambda self = None: bytes(self._nonce))()
        
        def public_key(self = None):
            return typing.cast(SSHCertPublicKeyTypes, self._public_key)

        serial = (lambda self = None: self._serial)()
        type = (lambda self = None: self._type)()
        key_id = (lambda self = None: bytes(self._key_id))()
        valid_principals = (lambda self = None: self._valid_principals)()
        valid_before = (lambda self = None: self._valid_before)()
        valid_after = (lambda self = None: self._valid_after)()
        critical_options = (lambda self = None: self._critical_options)()
        extensions = (lambda self = None: self._extensions)()
        
        def signature_key(self = None):
            sigformat = _lookup_kformat(self._sig_type)
            (signature_key, sigkey_rest) = sigformat.load_public(self._sig_key)
            _check_empty(sigkey_rest)
            return signature_key

        
        def public_bytes(self = None):
            return bytes(self._cert_key_type) + b' ' + binascii.b2a_base64(bytes(self._cert_body), newline = False)

        
        def verify_cert_signature(self = None):
            signature_key = self.signature_key()
            if isinstance(signature_key, ed25519.Ed25519PublicKey):
                signature_key.verify(bytes(self._signature), bytes(self._tbs_cert_body))
                return None
            if isinstance(signature_key, ec.EllipticCurvePublicKey):
                (r, data) = _get_mpint(self._signature)
                (s, data) = _get_mpint(data)
                _check_empty(data)
                computed_sig = asym_utils.encode_dss_signature(r, s)
                hash_alg = _get_ec_hash_alg(signature_key.curve)
                signature_key.verify(computed_sig, bytes(self._tbs_cert_body), ec.ECDSA(hash_alg))
                return None
        # WARNING: Decompyle incomplete


    
    def _get_ec_hash_alg(curve = None):
        if isinstance(curve, ec.SECP256R1):
            return hashes.SHA256()
        if None(curve, ec.SECP384R1):
            return hashes.SHA384()
    # WARNING: Decompyle incomplete

    
    def _load_ssh_public_identity(data = None, _legacy_dsa_allowed = None):
        utils._check_byteslike('data', data)
        m = _SSH_PUBKEY_RC.match(data)
        if not m:
            raise ValueError('Invalid line format')
        key_type = m.group(1)
        orig_key_type = m.group(1)
        key_body = m.group(2)
        with_cert = False
        if key_type.endswith(_CERT_SUFFIX):
            with_cert = True
            key_type = key_type[:-len(_CERT_SUFFIX)]
        if not key_type == _SSH_DSA and _legacy_dsa_allowed:
            raise UnsupportedAlgorithm("DSA keys aren't supported in SSH certificates")
        kformat = _lookup_kformat(key_type)
    # WARNING: Decompyle incomplete

    
    def load_ssh_public_identity(data = None):
        return _load_ssh_public_identity(data)

    
    def _parse_exts_opts(exts_opts = None):
        result = { }
        last_name = None
    # WARNING: Decompyle incomplete

    
    def ssh_key_fingerprint(key = None, hash_algorithm = None):
        if not isinstance(hash_algorithm, (hashes.MD5, hashes.SHA256)):
            raise TypeError('hash_algorithm must be either MD5 or SHA256')
        key_type = _get_ssh_key_type(key)
        kformat = _lookup_kformat(key_type)
        f_pub = _FragList()
        f_pub.put_sshstr(key_type)
        kformat.encode_public(key, f_pub)
        ssh_binary_data = f_pub.tobytes()
        hash_obj = hashes.Hash(hash_algorithm)
        hash_obj.update(ssh_binary_data)
        return hash_obj.finalize()

    
    def load_ssh_public_key(data = None, backend = None):
        cert_or_key = _load_ssh_public_identity(data, _legacy_dsa_allowed = True)
        if isinstance(cert_or_key, SSHCertificate):
            public_key = cert_or_key.public_key()
        else:
            public_key = cert_or_key
        if isinstance(public_key, dsa.DSAPublicKey):
            warnings.warn('SSH DSA keys are deprecated and will be removed in a future release.', utils.DeprecatedIn40, stacklevel = 2)
        return public_key

    
    def serialize_ssh_public_key(public_key = None):
        '''One-line public key format for OpenSSH'''
        if isinstance(public_key, dsa.DSAPublicKey):
            warnings.warn('SSH DSA key support is deprecated and will be removed in a future release', utils.DeprecatedIn40, stacklevel = 4)
        key_type = _get_ssh_key_type(public_key)
        kformat = _lookup_kformat(key_type)
        f_pub = _FragList()
        f_pub.put_sshstr(key_type)
        kformat.encode_public(public_key, f_pub)
        pub = binascii.b2a_base64(f_pub.tobytes()).strip()
        return b''.join([
            key_type,
            b' ',
            pub])

    SSHCertPrivateKeyTypes = typing.Union[(ec.EllipticCurvePrivateKey, rsa.RSAPrivateKey, ed25519.Ed25519PrivateKey)]
    _SSHKEY_CERT_MAX_PRINCIPALS = 256
    
    class SSHCertificateBuilder:
        
        def __init__(self, _public_key, _serial, _type, _key_id, _valid_principals, _valid_for_all_principals = None, _valid_before = None, _valid_after = None, _critical_options = (None, None, None, None, [], False, None, None, [], []), _extensions = ('_public_key', 'SSHCertPublicKeyTypes | None', '_serial', 'int | None', '_type', 'SSHCertificateType | None', '_key_id', 'bytes | None', '_valid_principals', 'list[bytes]', '_valid_for_all_principals', 'bool', '_valid_before', 'int | None', '_valid_after', 'int | None', '_critical_options', 'list[tuple[bytes, bytes]]', '_extensions', 'list[tuple[bytes, bytes]]')):
            self._public_key = _public_key
            self._serial = _serial
            self._type = _type
            self._key_id = _key_id
            self._valid_principals = _valid_principals
            self._valid_for_all_principals = _valid_for_all_principals
            self._valid_before = _valid_before
            self._valid_after = _valid_after
            self._critical_options = _critical_options
            self._extensions = _extensions

        
        def public_key(self = None, public_key = None):
            if not isinstance(public_key, (ec.EllipticCurvePublicKey, rsa.RSAPublicKey, ed25519.Ed25519PublicKey)):
                raise TypeError('Unsupported key type')
        # WARNING: Decompyle incomplete

        
        def serial(self = None, serial = None):
            if not isinstance(serial, int):
                raise TypeError('serial must be an integer')
            if not  <= 0, serial or 0, serial < 0x10000000000000000:
                raise ValueError('serial must be between 0 and 2**64')
            raise ValueError('serial must be between 0 and 2**64')
        # WARNING: Decompyle incomplete

        
        def type(self = None, type = None):
            if not isinstance(type, SSHCertificateType):
                raise TypeError('type must be an SSHCertificateType')
        # WARNING: Decompyle incomplete

        
        def key_id(self = None, key_id = None):
            if not isinstance(key_id, bytes):
                raise TypeError('key_id must be bytes')
        # WARNING: Decompyle incomplete

        
        def valid_principals(self = None, valid_principals = None):
            if self._valid_for_all_principals:
                raise ValueError("Principals can't be set because the cert is valid for all principals")
            if not (lambda .0: pass# WARNING: Decompyle incomplete
)(valid_principals()) or valid_principals:
                raise TypeError("principals must be a list of bytes and can't be empty")
            if self._valid_principals:
                raise ValueError('valid_principals already set')
            if len(valid_principals) > _SSHKEY_CERT_MAX_PRINCIPALS:
                raise ValueError('Reached or exceeded the maximum number of valid_principals')
            return SSHCertificateBuilder(_public_key = self._public_key, _serial = self._serial, _type = self._type, _key_id = self._key_id, _valid_principals = valid_principals, _valid_for_all_principals = self._valid_for_all_principals, _valid_before = self._valid_before, _valid_after = self._valid_after, _critical_options = self._critical_options, _extensions = self._extensions)

        
        def valid_for_all_principals(self):
            if self._valid_principals:
                raise ValueError("valid_principals already set, can't set valid_for_all_principals")
            if self._valid_for_all_principals:
                raise ValueError('valid_for_all_principals already set')
            return SSHCertificateBuilder(_public_key = self._public_key, _serial = self._serial, _type = self._type, _key_id = self._key_id, _valid_principals = self._valid_principals, _valid_for_all_principals = True, _valid_before = self._valid_before, _valid_after = self._valid_after, _critical_options = self._critical_options, _extensions = self._extensions)

        
        def valid_before(self = None, valid_before = None):
            if not isinstance(valid_before, (int, float)):
                raise TypeError('valid_before must be an int or float')
            valid_before = int(valid_before)
            if valid_before < 0 or valid_before >= 0x10000000000000000:
                raise ValueError('valid_before must [0, 2**64)')
        # WARNING: Decompyle incomplete

        
        def valid_after(self = None, valid_after = None):
            if not isinstance(valid_after, (int, float)):
                raise TypeError('valid_after must be an int or float')
            valid_after = int(valid_after)
            if valid_after < 0 or valid_after >= 0x10000000000000000:
                raise ValueError('valid_after must [0, 2**64)')
        # WARNING: Decompyle incomplete

        
        def add_critical_option(self = None, name = None, value = None):
            if not isinstance(name, bytes) or isinstance(value, bytes):
                raise TypeError('name and value must be bytes')
        # WARNING: Decompyle incomplete

        
        def add_extension(self = None, name = None, value = None):
            if not isinstance(name, bytes) or isinstance(value, bytes):
                raise TypeError('name and value must be bytes')
        # WARNING: Decompyle incomplete

        
        def sign(self = None, private_key = None):
            if not isinstance(private_key, (ec.EllipticCurvePrivateKey, rsa.RSAPrivateKey, ed25519.Ed25519PrivateKey)):
                raise TypeError('Unsupported private key type')
        # WARNING: Decompyle incomplete


    return None
except ImportError:
    _bcrypt_supported = False
    
    def _bcrypt_kdf(password = None, salt = None, desired_key_bytes = None, rounds = (False,), ignore_few_rounds = ('password', 'bytes', 'salt', 'bytes', 'desired_key_bytes', 'int', 'rounds', 'int', 'ignore_few_rounds', 'bool', 'return', 'bytes')):
        raise UnsupportedAlgorithm('Need bcrypt module')

    continue

