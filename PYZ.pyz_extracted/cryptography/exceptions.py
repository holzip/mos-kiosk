# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.12)

from __future__ import annotations
import typing
from cryptography.hazmat.bindings._rust import exceptions as rust_exceptions
if typing.TYPE_CHECKING:
    from cryptography.hazmat.bindings._rust import openssl as rust_openssl
_Reasons = rust_exceptions._Reasons

class UnsupportedAlgorithm(Exception):
    pass
# WARNING: Decompyle incomplete


class AlreadyFinalized(Exception):
    pass


class AlreadyUpdated(Exception):
    pass


class NotYetFinalized(Exception):
    pass


class InvalidTag(Exception):
    pass


class InvalidSignature(Exception):
    pass


class InternalError(Exception):
    pass
# WARNING: Decompyle incomplete


class InvalidKey(Exception):
    pass

