# Source Generated with Decompyle++
# File: pyimod03_ctypes.pyc (Python 3.12)

'''
Hooks to make ctypes.CDLL, .PyDLL, etc. look in sys._MEIPASS first.
'''
import sys

def install():
    '''
    Install the hooks.

    This must be done from a function as opposed to at module-level, because when the module is imported/executed,
    the import machinery is not completely set up yet.
    '''
    pass
# WARNING: Decompyle incomplete

if sys.platform.startswith('darwin'):
    
    try:
        from ctypes.macholib import dyld
        dyld.DEFAULT_LIBRARY_FALLBACK.insert(0, sys._MEIPASS)
        return None
        return None
    except ImportError:
        return None

