# Source Generated with Decompyle++
# File: unicode_utils.pyc (Python 3.12)

import sys
import unicodedata
from configparser import RawConfigParser
from compat import py39
from warnings import SetuptoolsDeprecationWarning

def decompose(path):
    if isinstance(path, str):
        return unicodedata.normalize('NFD', path)
    
    try:
        path = path.decode('utf-8')
        path = unicodedata.normalize('NFD', path)
        path = path.encode('utf-8')
        return path
    except UnicodeError:
        return path



def filesys_decode(path):
    '''
    Ensure that the given path is decoded,
    ``None`` when no expected encoding works
    '''
    if isinstance(path, str):
        return path
    if not None.getfilesystemencoding():
        None.getfilesystemencoding()
    fs_enc = 'utf-8'
    candidates = (fs_enc, 'utf-8')
    for enc in candidates:
        
        return candidates, path.decode(enc)
    return None
    except UnicodeDecodeError:
        continue


def try_encode(string, enc):
    '''turn unicode encoding into a functional routine'''
    
    try:
        return string.encode(enc)
    except UnicodeEncodeError:
        return None



def _read_utf8_with_fallback(file = None, fallback_encoding = None):
    '''
    First try to read the file with UTF-8, if there is an error fallback to a
    different encoding ("locale" by default). Returns the content of the file.
    Also useful when reading files that might have been produced by an older version of
    setuptools.
    '''
    
    try:
        f = open(file, 'r', encoding = 'utf-8')
        
        try:
            None(None, None)
            return 
            with None:
                if not None, f.read():
                    pass
            
            try:
                return None
                
                try:
                    pass
                except UnicodeDecodeError:
                    _Utf8EncodingNeeded.emit(file = file, fallback_encoding = fallback_encoding)
                    None(None, None)
                    return 
                    with None:
                        if not open(file, 'r', encoding = fallback_encoding), f.read(), :
                            pass
                    return None






def _cfg_read_utf8_with_fallback(cfg = None, file = None, fallback_encoding = None):
    '''Same idea as :func:`_read_utf8_with_fallback`, but for the
    :meth:`RawConfigParser.read` method.

    This method may call ``cfg.clear()``.
    '''
    
    try:
        cfg.read(file, encoding = 'utf-8')
        return None
    except UnicodeDecodeError:
        _Utf8EncodingNeeded.emit(file = file, fallback_encoding = fallback_encoding)
        cfg.clear()
        cfg.read(file, encoding = fallback_encoding)
        return None



class _Utf8EncodingNeeded(SetuptoolsDeprecationWarning):
    _SUMMARY = '\n    `encoding="utf-8"` fails with {file!r}, trying `encoding={fallback_encoding!r}`.\n    '
    _DETAILS = '\n    Fallback behavior for UTF-8 is considered **deprecated** and future versions of\n    `setuptools` may not implement it.\n\n    Please encode {file!r} with "utf-8" to ensure future builds will succeed.\n\n    If this file was produced by `setuptools` itself, cleaning up the cached files\n    and re-building/re-installing the package with a newer version of `setuptools`\n    (e.g. by updating `build-system.requires` in its `pyproject.toml`)\n    might solve the problem.\n    '

