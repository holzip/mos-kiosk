# Source Generated with Decompyle++
# File: cookiejar.pyc (Python 3.12)

__doc__ = "HTTP cookie handling for web clients.\n\nThis module has (now fairly distant) origins in Gisle Aas' Perl module\nHTTP::Cookies, from the libwww-perl library.\n\nDocstrings, comments and debug strings in this code refer to the\nattributes of the HTTP cookie system as cookie-attributes, to distinguish\nthem clearly from Python attributes.\n\nClass diagram (note that BSDDBCookieJar and the MSIE* classes are not\ndistributed with the Python standard library, but are available from\nhttp://wwwsearch.sf.net/):\n\n                        CookieJar____\n                        /     \\      \\\n            FileCookieJar      \\      \\\n             /    |   \\         \\      \\\n MozillaCookieJar | LWPCookieJar \\      \\\n                  |               |      \\\n                  |   ---MSIEBase |       \\\n                  |  /      |     |        \\\n                  | /   MSIEDBCookieJar BSDDBCookieJar\n                  |/\n               MSIECookieJar\n\n"
__all__ = [
    'Cookie',
    'CookieJar',
    'CookiePolicy',
    'DefaultCookiePolicy',
    'FileCookieJar',
    'LWPCookieJar',
    'LoadError',
    'MozillaCookieJar']
import os
import copy
import datetime
import re
import time
import urllib.parse as urllib
import urllib.request as urllib
import threading as _threading
import http.client as http
from calendar import timegm
debug = False
logger = None

def _debug(*args):
    global logger
    if not debug:
        return None
    if not logger:
        import logging
        logger = logging.getLogger('http.cookiejar')
# WARNING: Decompyle incomplete

HTTPONLY_ATTR = 'HTTPOnly'
HTTPONLY_PREFIX = '#HttpOnly_'
DEFAULT_HTTP_PORT = str(http.client.HTTP_PORT)
NETSCAPE_MAGIC_RGX = re.compile('#( Netscape)? HTTP Cookie File')
MISSING_FILENAME_TEXT = 'a filename was not supplied (nor was the CookieJar instance initialised with one)'
NETSCAPE_HEADER_TEXT = '# Netscape HTTP Cookie File\n# http://curl.haxx.se/rfc/cookie_spec.html\n# This is a generated file!  Do not edit.\n\n'

def _warn_unhandled_exception():
    import io
    import warnings
    import traceback
    f = io.StringIO()
    traceback.print_exc(None, f)
    msg = f.getvalue()
    warnings.warn('http.cookiejar bug!\n%s' % msg, stacklevel = 2)

EPOCH_YEAR = 1970

def _timegm(tt):
    (year, month, mday, hour, min, sec) = tt[:6]
    if year >= EPOCH_YEAR:
        if  <= 1, month or 1, month <= 12:
            pass
        else:
            return None
        if  <= 1, mday or 1, mday <= 31:
            pass
        else:
            return None
        if  <= 0, hour or 0, hour <= 24:
            pass
        else:
            return None
        if  <= 0, min or 0, min <= 59:
            pass
        else:
            return None
        if  <= 0, sec or 0, sec <= 61:
            return timegm(tt)
        return None

DAYS = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun']
MONTHS = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec']
# WARNING: Decompyle incomplete
