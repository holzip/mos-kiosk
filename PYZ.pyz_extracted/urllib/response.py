# Source Generated with Decompyle++
# File: response.pyc (Python 3.12)

'''Response classes used by urllib.

The base class, addbase, defines a minimal file-like interface,
including read() and readline().  The typical response object is an
addinfourl instance, which defines an info() method that returns
headers and a geturl() method that returns the url.
'''
import tempfile
__all__ = [
    'addbase',
    'addclosehook',
    'addinfo',
    'addinfourl']

class addbase(tempfile._TemporaryFileWrapper):
    pass
# WARNING: Decompyle incomplete


class addclosehook(addbase):
    pass
# WARNING: Decompyle incomplete


class addinfo(addbase):
    pass
# WARNING: Decompyle incomplete


class addinfourl(addinfo):
    pass
# WARNING: Decompyle incomplete

