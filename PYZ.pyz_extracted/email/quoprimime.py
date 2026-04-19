# Source Generated with Decompyle++
# File: quoprimime.pyc (Python 3.12)

__doc__ = "Quoted-printable content transfer encoding per RFCs 2045-2047.\n\nThis module handles the content transfer encoding method defined in RFC 2045\nto encode US ASCII-like 8-bit data called `quoted-printable'.  It is used to\nsafely encode text that is in a character set similar to the 7-bit US ASCII\ncharacter set, but that includes some 8-bit characters that are normally not\nallowed in email bodies or headers.\n\nQuoted-printable is very space-inefficient for encoding binary files; use the\nemail.base64mime module for that instead.\n\nThis module provides an interface to encode and decode both headers and bodies\nwith quoted-printable encoding.\n\nRFC 2045 defines a method for including character set information in an\n`encoded-word' in a header.  This method is commonly used for 8-bit real names\nin To:/From:/Cc: etc. fields, as well as Subject: lines.\n\nThis module does not do the line wrapping or end-of-line character\nconversion necessary for proper internationalized headers; it only\ndoes dumb encoding and decoding.  To deal with the various line\nwrapping issues, use the email.header module.\n"
__all__ = [
    'body_decode',
    'body_encode',
    'body_length',
    'decode',
    'decodestring',
    'header_decode',
    'header_encode',
    'header_length',
    'quote',
    'unquote']
import re
from string import ascii_letters, digits, hexdigits
CRLF = '\r\n'
NL = '\n'
EMPTYSTRING = ''
# WARNING: Decompyle incomplete
