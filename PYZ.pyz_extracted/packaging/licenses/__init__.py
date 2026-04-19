# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

from __future__ import annotations
import re
from typing import NewType, cast
from _spdx import EXCEPTIONS, LICENSES
__all__ = [
    'InvalidLicenseExpression',
    'NormalizedLicenseExpression',
    'canonicalize_license_expression']
license_ref_allowed = re.compile('^[A-Za-z0-9.-]*$')
NormalizedLicenseExpression = NewType('NormalizedLicenseExpression', str)

class InvalidLicenseExpression(ValueError):
    '''Raised when a license-expression string is invalid

    >>> canonicalize_license_expression("invalid")
    Traceback (most recent call last):
        ...
    packaging.licenses.InvalidLicenseExpression: Invalid license expression: \'invalid\'
    '''
    pass


def canonicalize_license_expression(raw_license_expression = None):
    if not raw_license_expression:
        message = f'''Invalid license expression: {raw_license_expression!r}'''
        raise InvalidLicenseExpression(message)
    license_expression = raw_license_expression.replace('(', ' ( ').replace(')', ' ) ')
    licenseref_prefix = 'LicenseRef-'
# WARNING: Decompyle incomplete

