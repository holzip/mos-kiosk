# Source Generated with Decompyle++
# File: utils.pyc (Python 3.12)

'''Miscellaneous utilities.'''
__all__ = [
    'collapse_rfc2231_value',
    'decode_params',
    'decode_rfc2231',
    'encode_rfc2231',
    'formataddr',
    'formatdate',
    'format_datetime',
    'getaddresses',
    'make_msgid',
    'mktime_tz',
    'parseaddr',
    'parsedate',
    'parsedate_tz',
    'parsedate_to_datetime',
    'unquote']
import os
import re
import time
import random
import socket
import datetime
import urllib.parse as urllib
from email._parseaddr import quote
from email._parseaddr import AddressList as _AddressList
from email._parseaddr import mktime_tz
from email._parseaddr import parsedate, parsedate_tz, _parsedate_tz
from email.charset import Charset
COMMASPACE = ', '
EMPTYSTRING = ''
UEMPTYSTRING = ''
CRLF = '\r\n'
TICK = "'"
specialsre = re.compile('[][\\\\()<>@,:;".]')
escapesre = re.compile('[\\\\"]')

def _has_surrogates(s):
    '''Return True if s may contain surrogate-escaped binary data.'''
    
    try:
        s.encode()
        return False
    except UnicodeEncodeError:
        return True



def _sanitize(string):
    original_bytes = string.encode('utf-8', 'surrogateescape')
    return original_bytes.decode('utf-8', 'replace')


def formataddr(pair, charset = ('utf-8',)):
    """The inverse of parseaddr(), this takes a 2-tuple of the form
    (realname, email_address) and returns the string value suitable
    for an RFC 2822 From, To or Cc header.

    If the first element of pair is false, then the second element is
    returned unmodified.

    The optional charset is the character set that is used to encode
    realname in case realname is not ASCII safe.  Can be an instance of str or
    a Charset-like object which has a header_encode method.  Default is
    'utf-8'.
    """
    (name, address) = pair
    address.encode('ascii')
    if name:
        
        try:
            name.encode('ascii')
            quotes = ''
            if specialsre.search(name):
                quotes = '"'
            name = escapesre.sub('\\\\\\g<0>', name)
            return f'''{quotes!s}{name!s}{quotes!s} <{address!s}>'''
            return address
        except UnicodeEncodeError:
            if isinstance(charset, str):
                charset = Charset(charset)
            encoded_name = charset.header_encode(name)
            return 



def _iter_escaped_chars(addr):
    pass
# WARNING: Decompyle incomplete


def _strip_quoted_realnames(addr):
    '''Strip real names between quotes.'''
    if '"' not in addr:
        return addr
    start = None
    open_pos = None
    result = []
# WARNING: Decompyle incomplete

supports_strict_parsing = True

def getaddresses(fieldvalues = None, *, strict):
    """Return a list of (REALNAME, EMAIL) or ('','') for each fieldvalue.

    When parsing fails for a fieldvalue, a 2-tuple of ('', '') is returned in
    its place.

    If strict is true, use a strict parser which rejects malformed inputs.
    """
    if not strict:
        all = (lambda .0: pass# WARNING: Decompyle incomplete
)(fieldvalues())
        a = _AddressList(all)
        return a.addresslist
# WARNING: Decompyle incomplete


def _check_parenthesis(addr):
    addr = _strip_quoted_realnames(addr)
    opens = 0
    for pos, ch in _iter_escaped_chars(addr):
        if ch == '(':
            opens += 1
            continue
        if not ch == ')':
            continue
        opens -= 1
        if not opens < 0:
            continue
        _iter_escaped_chars(addr)
        return False
    return opens == 0


def _pre_parse_validation(email_header_fields):
    accepted_values = []
    for v in email_header_fields:
        if not _check_parenthesis(v):
            v = "('', '')"
        accepted_values.append(v)
    return accepted_values


def _post_parse_validation(parsed_email_header_tuples):
    accepted_values = []
    for v in parsed_email_header_tuples:
        if '[' in v[1]:
            v = ('', '')
        accepted_values.append(v)
    return accepted_values


def _format_timetuple_and_zone(timetuple, zone):
    return '%s, %02d %s %04d %02d:%02d:%02d %s' % ([
        'Mon',
        'Tue',
        'Wed',
        'Thu',
        'Fri',
        'Sat',
        'Sun'][timetuple[6]], timetuple[2], [
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
        'Dec'][timetuple[1] - 1], timetuple[0], timetuple[3], timetuple[4], timetuple[5], zone)


def formatdate(timeval, localtime, usegmt = (None, False, False)):
    '''Returns a date string as specified by RFC 2822, e.g.:

    Fri, 09 Nov 2001 01:08:47 -0000

    Optional timeval if given is a floating-point time value as accepted by
    gmtime() and localtime(), otherwise the current time is used.

    Optional localtime is a flag that when True, interprets timeval, and
    returns a date relative to the local timezone instead of UTC, properly
    taking daylight savings time into account.

    Optional argument usegmt means that the timezone is written out as
    an ascii string, not numeric one (so "GMT" instead of "+0000"). This
    is needed for HTTP, and is only used when localtime==False.
    '''
    pass
# WARNING: Decompyle incomplete


def format_datetime(dt, usegmt = (False,)):
    """Turn a datetime into a date string as specified in RFC 2822.

    If usegmt is True, dt must be an aware datetime with an offset of zero.  In
    this case 'GMT' will be rendered instead of the normal +0000 required by
    RFC2822.  This is to support HTTP headers involving date stamps.
    """
    now = dt.timetuple()
# WARNING: Decompyle incomplete


def make_msgid(idstring, domain = (None, None)):
    """Returns a string suitable for RFC 2822 compliant Message-ID, e.g:

    <142480216486.20800.16526388040877946887@nightshade.la.mastaler.com>

    Optional idstring if given is a string used to strengthen the
    uniqueness of the message id.  Optional domain if given provides the
    portion of the message id after the '@'.  It defaults to the locally
    defined hostname.
    """
    timeval = int(time.time() * 100)
    pid = os.getpid()
    randint = random.getrandbits(64)
# WARNING: Decompyle incomplete


def parsedate_to_datetime(data):
    parsed_date_tz = _parsedate_tz(data)
# WARNING: Decompyle incomplete


def parseaddr(addr = None, *, strict):
    """
    Parse addr into its constituent realname and email address parts.

    Return a tuple of realname and email address, unless the parse fails, in
    which case return a 2-tuple of ('', '').

    If strict is True, use a strict parser which rejects malformed inputs.
    """
    if not strict:
        addrs = _AddressList(addr).addresslist
        if not addrs:
            return ('', '')
        return addrs[0]
    if None(addr, list):
        addr = addr[0]
    if not isinstance(addr, str):
        return ('', '')
    addr = _pre_parse_validation([
        addr])[0]
    addrs = _post_parse_validation(_AddressList(addr).addresslist)
    if addrs or len(addrs) > 1:
        return ('', '')
    return addrs[0]


def unquote(str):
