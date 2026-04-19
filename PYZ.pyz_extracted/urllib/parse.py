# Source Generated with Decompyle++
# File: parse.pyc (Python 3.12)

'''Parse (absolute and relative) URLs.

urlparse module is based upon the following RFC specifications.

RFC 3986 (STD66): "Uniform Resource Identifiers" by T. Berners-Lee, R. Fielding
and L.  Masinter, January 2005.

RFC 2732 : "Format for Literal IPv6 Addresses in URL\'s by R.Hinden, B.Carpenter
and L.Masinter, December 1999.

RFC 2396:  "Uniform Resource Identifiers (URI)": Generic Syntax by T.
Berners-Lee, R. Fielding, and L. Masinter, August 1998.

RFC 2368: "The mailto URL scheme", by P.Hoffman , L Masinter, J. Zawinski, July 1998.

RFC 1808: "Relative Uniform Resource Locators", by R. Fielding, UC Irvine, June
1995.

RFC 1738: "Uniform Resource Locators (URL)" by T. Berners-Lee, L. Masinter, M.
McCahill, December 1994

RFC 3986 is considered the current standard and any future changes to
urlparse module should conform with it.  The urlparse module is
currently not entirely compliant with this RFC due to defacto
scenarios for parsing, and for backward compatibility purposes, some
parsing quirks from older RFCs are retained. The testcases in
test_urlparse.py provides a good indicator of parsing behavior.

The WHATWG URL Parser spec should also be considered.  We are not compliant with
it either due to existing user code API behavior expectations (Hyrum\'s Law).
It serves as a useful guide when making changes.
'''
from collections import namedtuple
import functools
import math
import re
import types
import warnings
import ipaddress
__all__ = [
    'urlparse',
    'urlunparse',
    'urljoin',
    'urldefrag',
    'urlsplit',
    'urlunsplit',
    'urlencode',
    'parse_qs',
    'parse_qsl',
    'quote',
    'quote_plus',
    'quote_from_bytes',
    'unquote',
    'unquote_plus',
    'unquote_to_bytes',
    'DefragResult',
    'ParseResult',
    'SplitResult',
    'DefragResultBytes',
    'ParseResultBytes',
    'SplitResultBytes']
uses_relative = [
    '',
    'ftp',
    'http',
    'gopher',
    'nntp',
    'imap',
    'wais',
    'file',
    'https',
    'shttp',
    'mms',
    'prospero',
    'rtsp',
    'rtsps',
    'rtspu',
    'sftp',
    'svn',
    'svn+ssh',
    'ws',
    'wss']
uses_netloc = [
    '',
    'ftp',
    'http',
    'gopher',
    'nntp',
    'telnet',
    'imap',
    'wais',
    'file',
    'mms',
    'https',
    'shttp',
    'snews',
    'prospero',
    'rtsp',
    'rtsps',
    'rtspu',
    'rsync',
    'svn',
    'svn+ssh',
    'sftp',
    'nfs',
    'git',
    'git+ssh',
    'ws',
    'wss',
    'itms-services']
uses_params = [
    '',
    'ftp',
    'hdl',
    'prospero',
    'http',
    'imap',
    'https',
    'shttp',
    'rtsp',
    'rtsps',
    'rtspu',
    'sip',
    'sips',
    'mms',
    'sftp',
    'tel']
non_hierarchical = [
    'gopher',
    'hdl',
    'mailto',
    'news',
    'telnet',
    'wais',
    'imap',
    'snews',
    'sip',
    'sips']
uses_query = [
    '',
    'http',
    'wais',
    'imap',
    'https',
    'shttp',
    'mms',
    'gopher',
    'rtsp',
    'rtsps',
    'rtspu',
    'sip',
    'sips']
uses_fragment = [
    '',
    'ftp',
    'hdl',
    'http',
    'gopher',
    'news',
    'nntp',
    'wais',
    'https',
    'shttp',
    'snews',
    'file',
    'prospero']
scheme_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-.'
_WHATWG_C0_CONTROL_OR_SPACE = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f '
_UNSAFE_URL_BYTES_TO_REMOVE = [
    '\t',
    '\r',
    '\n']

def clear_cache():
    '''Clear internal performance caches. Undocumented; some tests want it.'''
    urlsplit.cache_clear()
    _byte_quoter_factory.cache_clear()

_implicit_encoding = 'ascii'
_implicit_errors = 'strict'

def _noop(obj):
    return obj


def _encode_result(obj, encoding, errors = (_implicit_encoding, _implicit_errors)):
    return obj.encode(encoding, errors)


def _decode_args(args, encoding, errors = (_implicit_encoding, _implicit_errors)):
    pass
# WARNING: Decompyle incomplete


def _coerce_args(*args):
    str_input = isinstance(args[0], str)
    for arg in args[1:]:
        if not arg:
            continue
        if not isinstance(arg, str) != str_input:
            continue
        raise TypeError('Cannot mix str and non-str arguments')
    if str_input:
        return args + (_noop,)
    return None(args) + (_encode_result,)


class _ResultMixinStr(object):
    '''Standard approach to encoding parsed results from str to bytes'''
    __slots__ = ()
    
    def encode(self, encoding, errors = ('ascii', 'strict')):
        pass
    # WARNING: Decompyle incomplete



class _ResultMixinBytes(object):
    '''Standard approach to decoding parsed results from bytes to str'''
    __slots__ = ()
    
    def decode(self, encoding, errors = ('ascii', 'strict')):
        pass
    # WARNING: Decompyle incomplete



class _NetlocResultMixinBase(object):
    '''Shared methods for the parsed result objects containing a netloc element'''
    __slots__ = ()
    username = (lambda self: self._userinfo[0])()
    password = (lambda self: self._userinfo[1])()
    hostname = (lambda self: hostname = self._hostinfo[0]if not hostname:
Noneseparator = '%' if isinstance(hostname, str) else b'%'(hostname, percent, zone) = hostname.partition(separator)hostname.lower() + percent + zone)()
    port = (lambda self: port = self._hostinfo[1]# WARNING: Decompyle incomplete
)()
    __class_getitem__ = classmethod(types.GenericAlias)


class _NetlocResultMixinStr(_ResultMixinStr, _NetlocResultMixinBase):
    __slots__ = ()
    _userinfo = (lambda self: netloc = self.netloc(userinfo, have_info, hostinfo) = netloc.rpartition('@')if have_info:
(username, have_password, password) = userinfo.partition(':')if not have_password:
password = None(username, password)username = Nonepassword = None(username, password))()
    _hostinfo = (lambda self: netloc = self.netloc(_, _, hostinfo) = netloc.rpartition('@')(_, have_open_br, bracketed) = hostinfo.partition('[')if have_open_br:
(hostname, _, port) = bracketed.partition(']')(_, _, port) = port.partition(':')else:
(hostname, _, port) = hostinfo.partition(':')if not port:
port = None(hostname, port))()


class _NetlocResultMixinBytes(_ResultMixinBytes, _NetlocResultMixinBase):
    __slots__ = ()
    _userinfo = (lambda self: netloc = self.netloc(userinfo, have_info, hostinfo) = netloc.rpartition(b'@')if have_info:
(username, have_password, password) = userinfo.partition(b':')if not have_password:
password = None(username, password)username = Nonepassword = None(username, password))()
    _hostinfo = (lambda self: netloc = self.netloc(_, _, hostinfo) = netloc.rpartition(b'@')(_, have_open_br, bracketed) = hostinfo.partition(b'[')if have_open_br:
(hostname, _, port) = bracketed.partition(b']')(_, _, port) = port.partition(b':')else:
(hostname, _, port) = hostinfo.partition(b':')if not port:
port = None(hostname, port))()

_DefragResultBase = namedtuple('DefragResult', 'url fragment')
_SplitResultBase = namedtuple('SplitResult', 'scheme netloc path query fragment')
_ParseResultBase = namedtuple('ParseResult', 'scheme netloc path params query fragment')
_DefragResultBase.__doc__ = '\nDefragResult(url, fragment)\n\nA 2-tuple that contains the url without fragment identifier and the fragment\nidentifier as a separate argument.\n'
_DefragResultBase.url.__doc__ = 'The URL with no fragment identifier.'
_DefragResultBase.fragment.__doc__ = '\nFragment identifier separated from URL, that allows indirect identification of a\nsecondary resource by reference to a primary resource and additional identifying\ninformation.\n'
_SplitResultBase.__doc__ = '\nSplitResult(scheme, netloc, path, query, fragment)\n\nA 5-tuple that contains the different components of a URL. Similar to\nParseResult, but does not split params.\n'
_SplitResultBase.scheme.__doc__ = 'Specifies URL scheme for the request.'
_SplitResultBase.netloc.__doc__ = '\nNetwork location where the request is made to.\n'
_SplitResultBase.path.__doc__ = '\nThe hierarchical path, such as the path to a file to download.\n'
_SplitResultBase.query.__doc__ = "\nThe query component, that contains non-hierarchical data, that along with data\nin path component, identifies a resource in the scope of URI's scheme and\nnetwork location.\n"
_SplitResultBase.fragment.__doc__ = '\nFragment identifier, that allows indirect identification of a secondary resource\nby reference to a primary resource and additional identifying information.\n'
_ParseResultBase.__doc__ = '\nParseResult(scheme, netloc, path, params, query, fragment)\n\nA 6-tuple that contains components of a parsed URL.\n'
_ParseResultBase.scheme.__doc__ = _SplitResultBase.scheme.__doc__
_ParseResultBase.netloc.__doc__ = _SplitResultBase.netloc.__doc__
_ParseResultBase.path.__doc__ = _SplitResultBase.path.__doc__
_ParseResultBase.params.__doc__ = '\nParameters for last path element used to dereference the URI in order to provide\naccess to perform some operation on the resource.\n'
_ParseResultBase.query.__doc__ = _SplitResultBase.query.__doc__
_ParseResultBase.fragment.__doc__ = _SplitResultBase.fragment.__doc__
ResultBase = _NetlocResultMixinStr

class DefragResult(_ResultMixinStr, _DefragResultBase):
    __slots__ = ()
    
    def geturl(self):
        if self.fragment:
            return self.url + '#' + self.fragment
        return None.url



class SplitResult(_NetlocResultMixinStr, _SplitResultBase):
    __slots__ = ()
    
    def geturl(self):
        return urlunsplit(self)



class ParseResult(_NetlocResultMixinStr, _ParseResultBase):
    __slots__ = ()
    
    def geturl(self):
        return urlunparse(self)



class DefragResultBytes(_ResultMixinBytes, _DefragResultBase):
    __slots__ = ()
    
    def geturl(self):
        if self.fragment:
            return self.url + b'#' + self.fragment
        return None.url



class SplitResultBytes(_NetlocResultMixinBytes, _SplitResultBase):
    __slots__ = ()
    
    def geturl(self):
        return urlunsplit(self)



class ParseResultBytes(_NetlocResultMixinBytes, _ParseResultBase):
    __slots__ = ()
    
    def geturl(self):
        return urlunparse(self)



def _fix_result_transcoding():
    _result_pairs = ((DefragResult, DefragResultBytes), (SplitResult, SplitResultBytes), (ParseResult, ParseResultBytes))
    for _decoded, _encoded in _result_pairs:
        _decoded._encoded_counterpart = _encoded
        _encoded._decoded_counterpart = _decoded

_fix_result_transcoding()
del _fix_result_transcoding

def urlparse(url, scheme, allow_fragments = ('', True)):
    '''Parse a URL into 6 components:
    <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    The result is a named 6-tuple with fields corresponding to the
    above. It is either a ParseResult or ParseResultBytes object,
    depending on the type of the url parameter.

    The username, password, hostname, and port sub-components of netloc
    can also be accessed as attributes of the returned object.

    The scheme argument provides the default value of the scheme
    component when no scheme is found in url.

    If allow_fragments is False, no attempt is made to separate the
    fragment component from the previous component, which can be either
    path or query.

    Note that % escapes are not expanded.
    '''
    (url, scheme, _coerce_result) = _coerce_args(url, scheme)
    splitresult = urlsplit(url, scheme, allow_fragments)
    (scheme, netloc, url, query, fragment) = splitresult
    if scheme in uses_params and ';' in url:
        (url, params) = _splitparams(url)
    else:
        params = ''
    result = ParseResult(scheme, netloc, url, params, query, fragment)
    return _coerce_result(result)


def _splitparams(url):
