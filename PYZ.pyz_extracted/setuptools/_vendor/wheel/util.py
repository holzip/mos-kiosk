# Source Generated with Decompyle++
# File: util.pyc (Python 3.12)

from __future__ import annotations
import base64
import logging
log = logging.getLogger('wheel')

try:
    __import__('setuptools.logging')
    
    def urlsafe_b64encode(data = None):
        '''urlsafe_b64encode without padding'''
        return base64.urlsafe_b64encode(data).rstrip(b'=')

    
    def urlsafe_b64decode(data = None):
        '''urlsafe_b64decode without padding'''
        pad = b'=' * (4 - (len(data) & 3))
        return base64.urlsafe_b64decode(data + pad)

    return None
except ImportError:
    from  import _setuptools_logging
    _setuptools_logging.configure()
    continue

