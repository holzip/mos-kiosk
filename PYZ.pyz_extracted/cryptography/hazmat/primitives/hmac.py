# Source Generated with Decompyle++
# File: hmac.pyc (Python 3.12)

from __future__ import annotations
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.primitives import hashes
__all__ = [
    'HMAC']
HMAC = rust_openssl.hmac.HMAC
hashes.HashContext.register(HMAC)
