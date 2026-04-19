# Source Generated with Decompyle++
# File: _cipheralgorithm.pyc (Python 3.12)

from __future__ import annotations
import abc
from cryptography import utils

def CipherAlgorithm():
    '''CipherAlgorithm'''
    name = (lambda self = None: pass)()()
    key_sizes = (lambda self = None: pass)()()
    key_size = (lambda self = None: pass)()()

CipherAlgorithm = <NODE:27>(CipherAlgorithm, 'CipherAlgorithm', metaclass = abc.ABCMeta)

class BlockCipherAlgorithm(CipherAlgorithm):
    key: 'utils.Buffer' = 'BlockCipherAlgorithm'
    block_size = (lambda self = None: pass)()()


def _verify_key_size(algorithm = None, key = None):
    utils._check_byteslike('key', key)
    if len(key) * 8 not in algorithm.key_sizes:
        raise ValueError(f'''Invalid key size ({len(key) * 8}) for {algorithm.name}.''')
    return key

