# Source Generated with Decompyle++
# File: utils.pyc (Python 3.12)

from __future__ import annotations
from cryptography.hazmat.bindings._rust import asn1
from cryptography.hazmat.primitives import hashes
decode_dss_signature = asn1.decode_dss_signature
encode_dss_signature = asn1.encode_dss_signature

class Prehashed:
    
    def __init__(self = None, algorithm = None):
        if not isinstance(algorithm, hashes.HashAlgorithm):
            raise TypeError('Expected instance of HashAlgorithm.')
        self._algorithm = algorithm
        self._digest_size = algorithm.digest_size

    digest_size = (lambda self = None: self._digest_size)()

