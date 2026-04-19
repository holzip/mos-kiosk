# Source Generated with Decompyle++
# File: padding.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography import utils
from cryptography.hazmat.bindings._rust import ANSIX923PaddingContext, ANSIX923UnpaddingContext, PKCS7PaddingContext, PKCS7UnpaddingContext

def PaddingContext():
    '''PaddingContext'''
    update = (lambda self = None, data = None: pass)()
    finalize = (lambda self = None: pass)()

PaddingContext = <NODE:27>(PaddingContext, 'PaddingContext', metaclass = abc.ABCMeta)

def _byte_padding_check(block_size = None):
    if not  <= 0, block_size or 0, block_size <= 2040:
        raise ValueError('block_size must be in range(0, 2041).')
    raise ValueError('block_size must be in range(0, 2041).')
    if block_size % 8 != 0:
        raise ValueError('block_size must be a multiple of 8.')


class PKCS7:
    
    def __init__(self = None, block_size = None):
        _byte_padding_check(block_size)
        self.block_size = block_size

    
    def padder(self = None):
        return PKCS7PaddingContext(self.block_size)

    
    def unpadder(self = None):
        return PKCS7UnpaddingContext(self.block_size)


PaddingContext.register(PKCS7PaddingContext)
PaddingContext.register(PKCS7UnpaddingContext)

class ANSIX923:
    
    def __init__(self = None, block_size = None):
        _byte_padding_check(block_size)
        self.block_size = block_size

    
    def padder(self = None):
        return ANSIX923PaddingContext(self.block_size)

    
    def unpadder(self = None):
        return ANSIX923UnpaddingContext(self.block_size)


PaddingContext.register(ANSIX923PaddingContext)
PaddingContext.register(ANSIX923UnpaddingContext)
