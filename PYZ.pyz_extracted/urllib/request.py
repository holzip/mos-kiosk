# Source Generated with Decompyle++
# File: request.pyc (Python 3.12)

'''An extensible library for opening URLs using a variety of protocols

The simplest way to use this module is to call the urlopen function,
which accepts a string containing a URL or a Request object (described
below).  It opens the URL and returns the results as file-like
object; the returned object has some extra methods described below.

The OpenerDirector manages a collection of Handler objects that do
all the actual work.  Each Handler implements a particular protocol or
option.  The OpenerDirector is a composite object that invokes the
Handlers needed to open the requested URL.  For example, the
HTTPHandler performs HTTP GET and POST requests and deals with
non-error returns.  The HTTPRedirectHandler automatically deals with
HTTP 301, 302, 303, 307, and 308 redirect errors, and the
HTTPDigestAuthHandler deals with digest authentication.

urlopen(url, data=None) -- Basic usage is the same as original
urllib.  pass the url and optionally data to post to an HTTP URL, and
get a file-like object back.  One difference is that you can also pass
a Request instance instead of URL.  Raises a URLError (subclass of
OSError); for HTTP errors, raises an HTTPError, which can also be
treated as a valid response.

build_opener -- Function that creates a new OpenerDirector instance.
Will install the default handlers.  Accepts one or more Handlers as
arguments, either instances or Handler classes that it will
instantiate.  If one of the argument is a subclass of the default
handler, the argument will be installed instead of the default.

install_opener -- Installs a new opener as the default opener.

objects of interest:

OpenerDirector -- Sets up the User Agent as the Python-urllib client and manages
the Handler classes, while dealing with requests and responses.

Request -- An object that encapsulates the state of a request.  The
state can be as simple as the URL.  It can also include extra HTTP
headers, e.g. a User-Agent.

BaseHandler --

internals:
BaseHandler and parent
_call_chain conventions

Example usage:

import urllib.request

# set up authentication info
authinfo = urllib.request.HTTPBasicAuthHandler()
authinfo.add_password(realm=\'PDQ Application\',
                      uri=\'https://mahler:8092/site-updates.py\',
                      user=\'klem\',
                      passwd=\'geheim$parole\')

proxy_support = urllib.request.ProxyHandler({"http" : "http://ahad-haam:3128"})

# build a new opener that adds authentication and caching FTP handlers
opener = urllib.request.build_opener(proxy_support, authinfo,
                                     urllib.request.CacheFTPHandler)

# install it
urllib.request.install_opener(opener)

f = urllib.request.urlopen(\'https://www.python.org/\')
'''
import base64
import bisect
import email
import hashlib
import http.client as http
import io
import os
import re
import socket
import string
import sys
import time
import tempfile
import contextlib
import warnings
from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib.parse import urlparse, urlsplit, urljoin, unwrap, quote, unquote, _splittype, _splithost, _splitport, _splituser, _splitpasswd, _splitattr, _splitquery, _splitvalue, _splittag, _to_bytes, unquote_to_bytes, urlunparse
from urllib.response import addinfourl, addclosehook

try:
    import ssl
    _have_ssl = True
    __all__ = [
        'Request',
        'OpenerDirector',
        'BaseHandler',
        'HTTPDefaultErrorHandler',
        'HTTPRedirectHandler',
        'HTTPCookieProcessor',
        'ProxyHandler',
        'HTTPPasswordMgr',
        'HTTPPasswordMgrWithDefaultRealm',
        'HTTPPasswordMgrWithPriorAuth',
        'AbstractBasicAuthHandler',
        'HTTPBasicAuthHandler',
        'ProxyBasicAuthHandler',
        'AbstractDigestAuthHandler',
        'HTTPDigestAuthHandler',
        'ProxyDigestAuthHandler',
        'HTTPHandler',
        'FileHandler',
        'FTPHandler',
        'CacheFTPHandler',
        'DataHandler',
        'UnknownHandler',
        'HTTPErrorProcessor',
        'urlopen',
        'install_opener',
        'build_opener',
        'pathname2url',
        'url2pathname',
        'getproxies',
        'urlretrieve',
        'urlcleanup',
        'URLopener',
        'FancyURLopener']
    __version__ = '%d.%d' % sys.version_info[:2]
    _opener = None
    
    def urlopen(url = None, data = (None, socket._GLOBAL_DEFAULT_TIMEOUT), timeout = {
        'cafile': None,
        'capath': None,
        'cadefault': False,
        'context': None }, *, cafile, capath, cadefault, context):
        '''Open the URL url, which can be either a string or a Request object.

    *data* must be an object specifying additional data to be sent to
    the server, or None if no such data is needed.  See Request for
    details.

    urllib.request module uses HTTP/1.1 and includes a "Connection:close"
    header in its HTTP requests.

    The optional *timeout* parameter specifies a timeout in seconds for
    blocking operations like the connection attempt (if not specified, the
    global default timeout setting will be used). This only works for HTTP,
    HTTPS and FTP connections.

    If *context* is specified, it must be a ssl.SSLContext instance describing
    the various SSL options. See HTTPSConnection for more details.

    The optional *cafile* and *capath* parameters specify a set of trusted CA
    certificates for HTTPS requests. cafile should point to a single file
    containing a bundle of CA certificates, whereas capath should point to a
    directory of hashed certificate files. More information can be found in
    ssl.SSLContext.load_verify_locations().

    The *cadefault* parameter is ignored.


    This function always returns an object which can work as a
    context manager and has the properties url, headers, and status.
    See urllib.response.addinfourl for more detail on these properties.

    For HTTP and HTTPS URLs, this function returns a http.client.HTTPResponse
    object slightly modified. In addition to the three new methods above, the
    msg attribute contains the same information as the reason attribute ---
    the reason phrase returned by the server --- instead of the response
    headers as it is specified in the documentation for HTTPResponse.

    For FTP, file, and data URLs and requests explicitly handled by legacy
    URLopener and FancyURLopener classes, this function returns a
    urllib.response.addinfourl object.

    Note that None may be returned if no handler handles the request (though
    the default installed global OpenerDirector uses UnknownHandler to ensure
    this never happens).

    In addition, if proxy settings are detected (for example, when a *_proxy
    environment variable like http_proxy is set), ProxyHandler is default
    installed and makes sure the requests are handled through the proxy.

    '''
        pass
    # WARNING: Decompyle incomplete

    
    def install_opener(opener):
        global _opener
        _opener = opener

    _url_tempfiles = []
    
    def urlretrieve(url, filename, reporthook, data = (None, None, None)):
        '''
    Retrieve a URL into a temporary location on disk.

    Requires a URL argument. If a filename is passed, it is used as
    the temporary file location. The reporthook argument should be
    a callable that accepts a block number, a read size, and the
    total file size of the URL target. The data argument should be
    valid URL encoded data.

    If a filename is passed and the URL points to a local resource,
    the result is a copy from local file to new file.

    Returns a tuple containing the path to the newly created
    data file as well as the resulting HTTPMessage object.
    '''
        (url_type, path) = _splittype(url)
        fp = contextlib.closing(urlopen(url, data))
        headers = fp.info()
        if not url_type == 'file' and filename:
            None(None, None)
            return 
        if None:
            pass
        else:
            tempfile.NamedTemporaryFile(delete = False) = open(filename, 'wb')
            filename = tfp.name
            _url_tempfiles.append(filename)
        tfp
        result = (filename, headers)
        bs = 8192
        size = -1
        read = 0
        blocknum = 0
        if 'content-length' in headers:
            size = int(headers['Content-Length'])
        if reporthook:
            reporthook(blocknum, bs, size)
        block = fp.read(bs)
        if fp.read(bs):
            read += len(block)
            tfp.write(block)
            blocknum += 1
            if reporthook:
                reporthook(blocknum, bs, size)
            block = fp.read(bs)
            if fp.read(bs):
                continue
        None(None, None)
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def urlcleanup():
        '''Clean up temporary files from urlretrieve calls.'''
        global _opener
        for temp_file in _url_tempfiles:
            os.unlink(temp_file)
        del _url_tempfiles[:]
        if _opener:
            _opener = None
            return None
        return None
        except OSError:
            continue

    _cut_port_re = re.compile(':\\d+$', re.ASCII)
    
    def request_host(request):
        '''Return request-host, as defined by RFC 2965.

    Variation from RFC: returned value is lowercased, for convenient
    comparison.

    '''
        url = request.full_url
        host = urlparse(url)[1]
        if host == '':
            host = request.get_header('Host', '')
        host = _cut_port_re.sub('', host, 1)
        return host.lower()

    
    class Request:
        
        def __init__(self, url, data, headers, origin_req_host, unverifiable, method = (None, { }, None, False, None)):
            self.full_url = url
            self.headers = { }
            self.unredirected_hdrs = { }
            self._data = None
            self.data = data
            self._tunnel_host = None
            for key, value in headers.items():
                self.add_header(key, value)
        # WARNING: Decompyle incomplete

        full_url = (lambda self: if self.fragment:
'{}#{}'.format(self._full_url, self.fragment)None._full_url)()
        full_url = (lambda self, url: self._full_url = unwrap(url)(self._full_url, self.fragment) = _splittag(self._full_url)self._parse())()
        full_url = (lambda self: self._full_url = Noneself.fragment = Noneself.selector = '')()
        data = (lambda self: self._data)()
        data = (lambda self, data: if data != self._data:
self._data = dataif self.has_header('Content-length'):
self.remove_header('Content-length')NoneNone)()
        data = (lambda self: self.data = None)()
        
        def _parse(self):
            (self.type, rest) = _splittype(self._full_url)
        # WARNING: Decompyle incomplete

        
        def get_method(self):
            '''Return a string indicating the HTTP request method.'''
            pass
        # WARNING: Decompyle incomplete

        
        def get_full_url(self):
            return self.full_url

        
        def set_proxy(self, host, type):
            if not self.type == 'https' and self._tunnel_host:
                self._tunnel_host = self.host
                self.host = host
                return None
            self.type = type
            self.selector = self.full_url
            self.host = host

        
        def has_proxy(self):
            return self.selector == self.full_url

        
        def add_header(self, key, val):
            self.headers[key.capitalize()] = val

        
        def add_unredirected_header(self, key, val):
            self.unredirected_hdrs[key.capitalize()] = val

        
        def has_header(self, header_name):
            if not header_name in self.headers:
                header_name in self.headers
            return header_name in self.unredirected_hdrs

        
        def get_header(self, header_name, default = (None,)):
            return self.headers.get(header_name, self.unredirected_hdrs.get(header_name, default))

        
        def remove_header(self, header_name):
            self.headers.pop(header_name, None)
            self.unredirected_hdrs.pop(header_name, None)

        
        def header_items(self):
            pass
        # WARNING: Decompyle incomplete


    
    class OpenerDirector:
        
        def __init__(self):
            client_version = 'Python-urllib/%s' % __version__
            self.addheaders = [
                ('User-agent', client_version)]
            self.handlers = []
            self.handle_open = { }
            self.handle_error = { }
            self.process_response = { }
            self.process_request = { }

        
        def add_handler(self, handler):
            if not hasattr(handler, 'add_parent'):
                raise TypeError('expected BaseHandler instance, got %r' % type(handler))
            added = False
            for meth in dir(handler):
                if meth in ('redirect_request', 'do_open', 'proxy_open'):
                    continue
                i = meth.find('_')
                protocol = meth[:i]
                condition = meth[i + 1:]
                if condition.startswith('error'):
                    j = condition.find('_') + i + 1
                    kind = meth[j + 1:]
                    kind = int(kind)
                    lookup = self.handle_error.get(protocol, { })
                    self.handle_error[protocol] = lookup
                elif condition == 'open':
                    kind = protocol
                    lookup = self.handle_open
                elif condition == 'response':
                    kind = protocol
                    lookup = self.process_response
                elif condition == 'request':
                    kind = protocol
                    lookup = self.process_request
                
                handlers = lookup.setdefault(kind, [])
                added = True
            if added:
                bisect.insort(self.handlers, handler)
                handler.add_parent(self)
                return None
            return None
            except ValueError:
                continue

        
        def close(self):
            pass

        
        def _call_chain(self, chain, kind, meth_name, *args):
            handlers = chain.get(kind, ())
        # WARNING: Decompyle incomplete

        
        def open(self, fullurl, data, timeout = (None, socket._GLOBAL_DEFAULT_TIMEOUT)):
            if isinstance(fullurl, str):
                req = Request(fullurl, data)
        # WARNING: Decompyle incomplete

        
        def _open(self, req, data = (None,)):
            result = self._call_chain(self.handle_open, 'default', 'default_open', req)
            if result:
                return result
            protocol = None.type
            result = self._call_chain(self.handle_open, protocol, protocol + '_open', req)
            if result:
                return result
            return None._call_chain(self.handle_open, 'unknown', 'unknown_open', req)

        
        def error(self, proto, *args):
            if proto in ('http', 'https'):
                dict = self.handle_error['http']
                proto = args[2]
                meth_name = 'http_error_%s' % proto
                http_err = 1
                orig_args = args
            else:
                dict = self.handle_error
                meth_name = proto + '_error'
                http_err = 0
            args = (dict, proto, meth_name) + args
        # WARNING: Decompyle incomplete


    
    def build_opener(*handlers):
        '''Create an opener object from a list of handlers.

    The opener will use several default handlers, including support
    for HTTP, FTP and when applicable HTTPS.

    If any of the handlers passed as arguments are subclasses of the
    default handlers, the default handlers will not be used.
    '''
        opener = OpenerDirector()
        default_classes = [
            ProxyHandler,
            UnknownHandler,
            HTTPHandler,
            HTTPDefaultErrorHandler,
            HTTPRedirectHandler,
            FTPHandler,
            FileHandler,
            HTTPErrorProcessor,
            DataHandler]
        if hasattr(http.client, 'HTTPSConnection'):
            default_classes.append(HTTPSHandler)
        skip = set()
        for klass in default_classes:
            for check in handlers:
                if isinstance(check, type):
                    if not issubclass(check, klass):
                        continue
                    skip.add(klass)
                    continue
                if not isinstance(check, klass):
                    continue
                skip.add(klass)
        for klass in skip:
            default_classes.remove(klass)
        for klass in default_classes:
            opener.add_handler(klass())
        for h in handlers:
            if isinstance(h, type):
                h = h()
            opener.add_handler(h)
        return opener

    
    class BaseHandler:
        handler_order = 500
        
        def add_parent(self, parent):
            self.parent = parent

        
        def close(self):
            pass

        
        def __lt__(self, other):
            if not hasattr(other, 'handler_order'):
                return True
            return self.handler_order < other.handler_order


    
    class HTTPErrorProcessor(BaseHandler):
        '''Process HTTP error responses.'''
        handler_order = 1000
        
        def http_response(self, request, response):
            hdrs = response.info()
            msg = response.msg
            code = response.code
            if not  <= 200, code or 200, code < 300:
                pass
            
            return response

        https_response = http_response

    
    class HTTPDefaultErrorHandler(BaseHandler):
        
        def http_error_default(self, req, fp, code, msg, hdrs):
            raise HTTPError(req.full_url, code, msg, hdrs, fp)


    
    class HTTPRedirectHandler(BaseHandler):
        max_repeats = 4
        max_redirections = 10
        
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            """Return a Request or None in response to a redirect.

        This is called by the http_error_30x methods when a
        redirection response is received.  If a redirection should
        take place, return a new Request to allow http_error_30x to
        perform the redirect.  Otherwise, raise HTTPError if no-one
        else should try to handle this url.  Return None if you can't
        but another Handler might.
        """
            m = req.get_method()
            if not code in (301, 302, 303, 307, 308) or m in ('GET', 'HEAD'):
                if not code in (301, 302, 303) or m == 'POST':
                    raise HTTPError(req.full_url, code, msg, headers, fp)
            newurl = newurl.replace(' ', '%20')
            CONTENT_HEADERS = ('content-length', 'content-type')
        # WARNING: Decompyle incomplete

        
        def http_error_302(self, req, fp, code, msg, headers):
            if 'location' in headers:
                newurl = headers['location']
            elif 'uri' in headers:
                newurl = headers['uri']
            else:
                return None
            urlparts = urlparse(newurl)
            if urlparts.scheme not in ('http', 'https', 'ftp', ''):
                raise HTTPError(newurl, code, f'''{msg!s} - Redirection to url \'{newurl!s}\' is not allowed''', headers, fp)
            if urlparts.path and urlparts.netloc:
                urlparts = list(urlparts)
                urlparts[2] = '/'
            newurl = urlunparse(urlparts)
            newurl = quote(newurl, encoding = 'iso-8859-1', safe = string.punctuation)
            newurl = urljoin(req.full_url, newurl)
            new = self.redirect_request(req, fp, code, msg, headers, newurl)
        # WARNING: Decompyle incomplete

        http_error_301 = http_error_302
        http_error_303 = http_error_302
        http_error_307 = http_error_302
        http_error_308 = http_error_302
        inf_msg = 'The HTTP server returned a redirect error that would lead to an infinite loop.\nThe last 30x error message was:\n'

    
    def _parse_proxy(proxy):
        '''Return (scheme, user, password, host/port) given a URL or an authority.

    If a URL is supplied, it must have an authority (host:port) component.
    According to RFC 3986, having an authority component means the URL must
    have two slashes after the scheme.
    '''
        (scheme, r_scheme) = _splittype(proxy)
        if not r_scheme.startswith('/'):
            scheme = None
            authority = proxy
        elif not r_scheme.startswith('//'):
            raise ValueError('proxy URL with no authority: %r' % proxy)
        if '@' in r_scheme:
            host_separator = r_scheme.find('@')
            end = r_scheme.find('/', host_separator)
        else:
            end = r_scheme.find('/', 2)
        if end == -1:
            end = None
        authority = r_scheme[2:end]
        (userinfo, hostport) = _splituser(authority)
    # WARNING: Decompyle incomplete

    
    class ProxyHandler(BaseHandler):
        handler_order = 100
        
        def __init__(self, proxies = (None,)):
            pass
        # WARNING: Decompyle incomplete

        
        def proxy_open(self, req, proxy, type):
            orig_type = req.type
            (proxy_type, user, password, hostport) = _parse_proxy(proxy)
        # WARNING: Decompyle incomplete


    
    class HTTPPasswordMgr:
        
        def __init__(self):
            self.passwd = { }

        
        def add_password(self, realm, uri, user, passwd):
            pass
        # WARNING: Decompyle incomplete

        
        def find_user_password(self, realm, authuri):
            domains = self.passwd.get(realm, { })
            for default_port in (True, False):
                reduced_authuri = self.reduce_uri(authuri, default_port)
                for uris, authinfo in domains.items():
                    for uri in uris:
                        if not self.is_suburi(uri, reduced_authuri):
                            continue
                        
                        
                        
                        return (True, False), domains.items(), uris, authinfo
            return (None, None)

        
        def reduce_uri(self, uri, default_port = (True,)):
            '''Accept authority or URI and extract only the authority and path.'''
            parts = urlsplit(uri)
            if parts[1]:
                scheme = parts[0]
                authority = parts[1]
                if not parts[2]:
                    parts[2]
                path = '/'
            else:
                scheme = None
                authority = uri
                path = '/'
            (host, port) = _splitport(authority)
        # WARNING: Decompyle incomplete

        
        def is_suburi(self, base, test):
            '''Check if test is below base in a URI tree

        Both args must be URIs in reduced form.
        '''
            if base == test:
                return True
            if base[0] != test[0]:
                return False
            prefix = base[1]
            if prefix[-1:] != '/':
                prefix += '/'
            return test[1].startswith(prefix)


    
    class HTTPPasswordMgrWithDefaultRealm(HTTPPasswordMgr):
        
        def find_user_password(self, realm, authuri):
            (user, password) = HTTPPasswordMgr.find_user_password(self, realm, authuri)
        # WARNING: Decompyle incomplete


    
    class HTTPPasswordMgrWithPriorAuth(HTTPPasswordMgrWithDefaultRealm):
        pass
    # WARNING: Decompyle incomplete

    
    class AbstractBasicAuthHandler:
        rx = re.compile('(?:^|,)[ \t]*([^ \t,]+)[ \t]+realm=(["\']?)([^"\']*)\\2', re.I)
        
        def __init__(self, password_mgr = (None,)):
            pass
        # WARNING: Decompyle incomplete

        
        def _parse_realm(self, header):
            pass
        # WARNING: Decompyle incomplete

        
        def http_error_auth_reqed(self, authreq, host, req, headers):
            headers = headers.get_all(authreq)
            if not headers:
                return None
            unsupported = None
        # WARNING: Decompyle incomplete

        
        def retry_http_basic_auth(self, host, req, realm):
            (user, pw) = self.passwd.find_user_password(realm, host)
        # WARNING: Decompyle incomplete

        
        def http_request(self, req):
            if not hasattr(self.passwd, 'is_authenticated') or self.passwd.is_authenticated(req.full_url):
                return req
            if not None.has_header('Authorization'):
                (user, passwd) = self.passwd.find_user_password(None, req.full_url)
                credentials = '{0}:{1}'.format(user, passwd).encode()
                auth_str = base64.standard_b64encode(credentials).decode()
                req.add_unredirected_header('Authorization', 'Basic {}'.format(auth_str.strip()))
            return req

        
        def http_response(self, req, response):
            if hasattr(self.passwd, 'is_authenticated'):
                if  <= 200, response.code or 200, response.code < 300:
                    pass
                
            else:
                self.passwd.update_authenticated(req.full_url, True)
                return response
            None.passwd.update_authenticated(req.full_url, False)
            return response

        https_request = http_request
        https_response = http_response

    
    class HTTPBasicAuthHandler(BaseHandler, AbstractBasicAuthHandler):
        auth_header = 'Authorization'
        
        def http_error_401(self, req, fp, code, msg, headers):
            url = req.full_url
            response = self.http_error_auth_reqed('www-authenticate', url, req, headers)
            return response


    
    class ProxyBasicAuthHandler(BaseHandler, AbstractBasicAuthHandler):
        auth_header = 'Proxy-authorization'
        
        def http_error_407(self, req, fp, code, msg, headers):
            authority = req.host
            response = self.http_error_auth_reqed('proxy-authenticate', authority, req, headers)
            return response


    _randombytes = os.urandom
    
    class AbstractDigestAuthHandler:
        
        def __init__(self, passwd = (None,)):
            pass
        # WARNING: Decompyle incomplete

        
        def reset_retry_count(self):
            self.retried = 0

        
        def http_error_auth_reqed(self, auth_header, host, req, headers):
            authreq = headers.get(auth_header, None)
            if self.retried > 5:
                raise HTTPError(req.full_url, 401, 'digest auth failed', headers, None)
            if authreq:
                authreq.split()[0] = self, self.retried += 1, .retried
                if scheme.lower() == 'digest':
                    return self.retry_http_digest_auth(req, authreq)
                if None.lower() != 'basic':
                    raise ValueError("AbstractDigestAuthHandler does not support the following scheme: '%s'" % scheme)
                return None

        
        def retry_http_digest_auth(self, req, auth):
            (token, challenge) = auth.split(' ', 1)
            chal = parse_keqv_list(filter(None, parse_http_list(challenge)))
            auth = self.get_authorization(req, chal)
            if auth:
                auth_val = 'Digest %s' % auth
                if req.headers.get(self.auth_header, None) == auth_val:
                    return None
                req.add_unredirected_header(self.auth_header, auth_val)
                resp = self.parent.open(req, timeout = req.timeout)
                return resp

        
        def get_cnonce(self, nonce):
            s = f'''{self.nonce_count!s}:{nonce!s}:{time.ctime()!s}:'''
            b = s.encode('ascii') + _randombytes(8)
            dig = hashlib.sha1(b).hexdigest()
            return dig[:16]

        
        def get_authorization(self, req, chal):
            pass
        # WARNING: Decompyle incomplete

        
        def get_algorithm_impls(self, algorithm):
            pass
        # WARNING: Decompyle incomplete

        
        def get_entity_digest(self, data, chal):
            pass


    
    class HTTPDigestAuthHandler(AbstractDigestAuthHandler, BaseHandler):
        '''An authentication protocol defined by RFC 2069

    Digest authentication improves on basic authentication because it
    does not transmit passwords in the clear.
    '''
        auth_header = 'Authorization'
        handler_order = 490
        
        def http_error_401(self, req, fp, code, msg, headers):
            host = urlparse(req.full_url)[1]
            retry = self.http_error_auth_reqed('www-authenticate', host, req, headers)
            self.reset_retry_count()
            return retry


    
    class ProxyDigestAuthHandler(AbstractDigestAuthHandler, BaseHandler):
        auth_header = 'Proxy-Authorization'
        handler_order = 490
        
        def http_error_407(self, req, fp, code, msg, headers):
            host = req.host
            retry = self.http_error_auth_reqed('proxy-authenticate', host, req, headers)
            self.reset_retry_count()
            return retry


    
    class AbstractHTTPHandler(BaseHandler):
        
        def __init__(self, debuglevel = (None,)):
            pass
        # WARNING: Decompyle incomplete

        
        def set_http_debuglevel(self, level):
            self._debuglevel = level

        
        def _get_content_length(self, request):
            return http.client.HTTPConnection._get_content_length(request.data, request.get_method())

        
        def do_request_(self, request):
            host = request.host
            if not host:
                raise URLError('no host given')
        # WARNING: Decompyle incomplete

        
        def do_open(self, http_class, req, **http_conn_args):
            '''Return an HTTPResponse object for the request, using http_class.

        http_class must implement the HTTPConnection API from http.client.
        '''
            host = req.host
            if not host:
                raise URLError('no host given')
        # WARNING: Decompyle incomplete


    
    class HTTPHandler(AbstractHTTPHandler):
        
        def http_open(self, req):
            return self.do_open(http.client.HTTPConnection, req)

        http_request = AbstractHTTPHandler.do_request_

    if hasattr(http.client, 'HTTPSConnection'):
        
        class HTTPSHandler(AbstractHTTPHandler):
            
            def __init__(self, debuglevel, context, check_hostname = (None, None, None)):
                pass
            # WARNING: Decompyle incomplete

            
            def https_open(self, req):
                return self.do_open(http.client.HTTPSConnection, req, context = self._context)

            https_request = AbstractHTTPHandler.do_request_

        __all__.append('HTTPSHandler')
    
    class HTTPCookieProcessor(BaseHandler):
        
        def __init__(self, cookiejar = (None,)):
            import http.cookiejar as http
        # WARNING: Decompyle incomplete

        
        def http_request(self, request):
            self.cookiejar.add_cookie_header(request)
            return request

        
        def http_response(self, request, response):
            self.cookiejar.extract_cookies(response, request)
            return response

        https_request = http_request
        https_response = http_response

    
    class UnknownHandler(BaseHandler):
        
        def unknown_open(self, req):
            type = req.type
            raise URLError('unknown url type: %s' % type)


    
    def parse_keqv_list(l):
        '''Parse list of key=value strings where keys are not duplicated.'''
        parsed = { }
        for elt in l:
            (k, v) = elt.split('=', 1)
            if v[0] == '"' and v[-1] == '"':
                v = v[1:-1]
            parsed[k] = v
        return parsed

    
    def parse_http_list(s):
        '''Parse lists as described by RFC 2068 Section 2.

    In particular, parse comma-separated lists where the elements of
    the list may include quoted-strings.  A quoted-string could
    contain a comma.  A non-quoted string could have quotes in the
    middle.  Neither commas nor quotes count if they are escaped.
    Only double-quotes count, not single-quotes.
    '''
        res = []
        part = ''
        escape = False
        quote = False
        for cur in s:
            if escape:
                part += cur
                escape = False
                continue
            if quote:
                if cur == '\\':
                    escape = True
                    continue
                if cur == '"':
                    quote = False
                part += cur
                continue
            if cur == ',':
                res.append(part)
                part = ''
                continue
            if cur == '"':
                quote = True
            part += cur
        if part:
            res.append(part)
    # WARNING: Decompyle incomplete

    
    class FileHandler(BaseHandler):
        
        def file_open(self, req):
            url = req.selector
            if url[:2] == '//' and url[2:3] != '/' and req.host and req.host != 'localhost':
                if req.host not in self.get_names():
                    raise URLError('file:// scheme is supported only on localhost')
                return None
            return self.open_local_file(req)

        names = None
        
        def get_names(self):
            pass
        # WARNING: Decompyle incomplete

        
        def open_local_file(self, req):
            import email.utils as email
            import mimetypes
            host = req.host
            filename = req.selector
            localfile = url2pathname(filename)
        # WARNING: Decompyle incomplete


    
    def _safe_gethostbyname(host):
        
        try:
            return socket.gethostbyname(host)
        except socket.gaierror:
            return None


    
    class FTPHandler(BaseHandler):
        
        def ftp_open(self, req):
            import ftplib
            import mimetypes
            host = req.host
            if not host:
                raise URLError('ftp error: no host given')
            (host, port) = _splitport(host)
        # WARNING: Decompyle incomplete

        
        def connect_ftp(self, user, passwd, host, port, dirs, timeout):
            return ftpwrapper(user, passwd, host, port, dirs, timeout, persistent = False)


    
    class CacheFTPHandler(FTPHandler):
        
        def __init__(self):
            self.cache = { }
            self.timeout = { }
            self.soonest = 0
            self.delay = 60
            self.max_conns = 16

        
        def setTimeout(self, t):
            self.delay = t

        
        def setMaxConns(self, m):
            self.max_conns = m

        
        def connect_ftp(self, user, passwd, host, port, dirs, timeout):
            key = (user, host, port, '/'.join(dirs), timeout)
            if key in self.cache:
                self.timeout[key] = time.time() + self.delay
            else:
                self.cache[key] = ftpwrapper(user, passwd, host, port, dirs, timeout)
                self.timeout[key] = time.time() + self.delay
            self.check_cache()
            return self.cache[key]

        
        def check_cache(self):
            t = time.time()
            if self.soonest <= t:
                for k, v in list(self.timeout.items()):
                    if not v < t:
                        continue
                    self.cache[k].close()
                    del self.cache[k]
                    del self.timeout[k]
            self.soonest = min(list(self.timeout.values()))
            if len(self.cache) == self.max_conns:
                for k, v in list(self.timeout.items()):
                    if not v == self.soonest:
                        continue
                    del self.cache[k]
                    del self.timeout[k]
                    list(self.timeout.items())
                self.soonest = min(list(self.timeout.values()))
                return None

        
        def clear_cache(self):
            for conn in self.cache.values():
                conn.close()
            self.cache.clear()
            self.timeout.clear()


    
    class DataHandler(BaseHandler):
        
        def data_open(self, req):
            url = req.full_url
            (scheme, data) = url.split(':', 1)
            (mediatype, data) = data.split(',', 1)
            data = unquote_to_bytes(data)
            if mediatype.endswith(';base64'):
                data = base64.decodebytes(data)
                mediatype = mediatype[:-7]
            if not mediatype:
                mediatype = 'text/plain;charset=US-ASCII'
            headers = email.message_from_string('Content-type: %s\nContent-length: %d\n' % (mediatype, len(data)))
            return addinfourl(io.BytesIO(data), headers, url)


    MAXFTPCACHE = 10
    ftpcache = { }
    
    class URLopener:
        """Class to open URLs.
    This is a class rather than just a subroutine because we may need
    more than one set of global protocol-specific options.
    Note -- this is a base class for those who don't want the
    automatic handling of errors type 302 (relocated) and 401
    (authorization needed)."""
        __tempfiles = None
        version = 'Python-urllib/%s' % __version__
        
        def __init__(self, proxies = (None,), **x509):
            msg = '%(class)s style of invoking requests is deprecated. Use newer urlopen functions/methods' % {
                'class': self.__class__.__name__ }
            warnings.warn(msg, DeprecationWarning, stacklevel = 3)
        # WARNING: Decompyle incomplete

        
        def __del__(self):
            self.close()

        
        def close(self):
            self.cleanup()

        
        def cleanup(self):
            if self.__tempfiles:
                for file in self.__tempfiles:
                    self._URLopener__unlink(file)
                del self.__tempfiles[:]
            if self.tempcache:
                self.tempcache.clear()
                return None
            return None
            except OSError:
                continue

        
        def addheader(self, *args):
            """Add a header to be used by the HTTP interface only
        e.g. u.addheader('Accept', 'sound/basic')"""
            self.addheaders.append(args)

        
        def open(self, fullurl, data = (None,)):
            """Use URLopener().open(file) instead of open(file, 'r')."""
            fullurl = unwrap(_to_bytes(fullurl))
            fullurl = quote(fullurl, safe = "%/:=&?~#+!$,;'@()*[]|")
            if self.tempcache and fullurl in self.tempcache:
                (filename, headers) = self.tempcache[fullurl]
                fp = open(filename, 'rb')
                return addinfourl(fp, headers, fullurl)
            (urltype, url) = None(fullurl)
            if not urltype:
                urltype = 'file'
            if urltype in self.proxies:
                proxy = self.proxies[urltype]
                (urltype, proxyhost) = _splittype(proxy)
                (host, selector) = _splithost(proxyhost)
                url = (host, fullurl)
            else:
                proxy = None
            name = 'open_' + urltype
            self.type = urltype
            name = name.replace('-', '_')
            if hasattr(self, name) or name == 'open_local_file':
                if proxy:
                    return self.open_unknown_proxy(proxy, fullurl, data)
                return None.open_unknown(fullurl, data)
        # WARNING: Decompyle incomplete

        
        def open_unknown(self, fullurl, data = (None,)):
            '''Overridable interface to open unknown URL type.'''
            (type, url) = _splittype(fullurl)
            raise OSError('url error', 'unknown url type', type)

        
        def open_unknown_proxy(self, proxy, fullurl, data = (None,)):
            '''Overridable interface to open unknown URL type.'''
            (type, url) = _splittype(fullurl)
            raise OSError('url error', 'invalid proxy for %s' % type, proxy)

        
        def retrieve(self, url, filename, reporthook, data = (None, None, None)):
            '''retrieve(url) returns (filename, headers) for a local object
        or (tempfilename, headers) for a remote object.'''
            url = unwrap(_to_bytes(url))
            if self.tempcache and url in self.tempcache:
                return self.tempcache[url]
            (type, url1) = None(url)
        # WARNING: Decompyle incomplete

        
        def _open_generic_http(self, connection_factory, url, data):
            '''Make an HTTP connection using connection_class.

        This is an internal method that should be called from
        open_http() or open_https().

        Arguments:
        - connection_factory should take a host name and return an
          HTTPConnection instance.
        - url is the url to retrieval or a host, relative-path pair.
        - data is payload for a POST request or None.
        '''
            user_passwd = None
            proxy_passwd = None
            if isinstance(url, str):
                (host, selector) = _splithost(url)
                if host:
                    (user_passwd, host) = _splituser(host)
                    host = unquote(host)
                realhost = host
            else:
                (host, selector) = url
                (proxy_passwd, host) = _splituser(host)
                (urltype, rest) = _splittype(selector)
                url = rest
                user_passwd = None
                if urltype.lower() != 'http':
                    realhost = None
                else:
                    (realhost, rest) = _splithost(rest)
                    if realhost:
                        (user_passwd, realhost) = _splituser(realhost)
                    if user_passwd:
                        selector = f'''{urltype!s}://{realhost!s}{rest!s}'''
                    if proxy_bypass(realhost):
                        host = realhost
            if not host:
                raise OSError('http error', 'no host given')
            if proxy_passwd:
                proxy_passwd = unquote(proxy_passwd)
                proxy_auth = base64.b64encode(proxy_passwd.encode()).decode('ascii')
            else:
                proxy_auth = None
            if user_passwd:
                user_passwd = unquote(user_passwd)
                auth = base64.b64encode(user_passwd.encode()).decode('ascii')
            else:
                auth = None
            http_conn = connection_factory(host)
            headers = { }
            if proxy_auth:
                headers['Proxy-Authorization'] = 'Basic %s' % proxy_auth
            if auth:
                headers['Authorization'] = 'Basic %s' % auth
            if realhost:
                headers['Host'] = realhost
            headers['Connection'] = 'close'
            for header, value in self.addheaders:
                headers[header] = value
        # WARNING: Decompyle incomplete

        
        def open_http(self, url, data = (None,)):
            '''Use HTTP protocol.'''
            return self._open_generic_http(http.client.HTTPConnection, url, data)

        
        def http_error(self, url, fp, errcode, errmsg, headers, data = (None,)):
            '''Handle http errors.

        Derived class can override this, or provide specific handlers
        named http_error_DDD where DDD is the 3-digit error code.'''
            name = 'http_error_%d' % errcode
        # WARNING: Decompyle incomplete

        
        def http_error_default(self, url, fp, errcode, errmsg, headers):
            '''Default error handler: close the connection and raise OSError.'''
            fp.close()
            raise HTTPError(url, errcode, errmsg, headers, None)

        if _have_ssl:
            
            def _https_connection(self, host):
                pass
            # WARNING: Decompyle incomplete

            
            def open_https(self, url, data = (None,)):
                '''Use HTTPS protocol.'''
                return self._open_generic_http(self._https_connection, url, data)

        
        def open_file(self, url):
            '''Use local file or FTP depending on form of URL.'''
            if not isinstance(url, str):
                raise URLError('file error: proxy support for file protocol currently not implemented')
            if url[:2] == '//' and url[2:3] != '/' and url[2:12].lower() != 'localhost/':
                raise ValueError('file:// scheme is supported only on localhost')
            return self.open_local_file(url)

        
        def open_local_file(self, url):
            '''Use local file.'''
            import email.utils as email
            import mimetypes
            (host, file) = _splithost(url)
            localname = url2pathname(file)
            
            try:
                stats = os.stat(localname)
                size = stats.st_size
                modified = email.utils.formatdate(stats.st_mtime, usegmt = True)
                mtype = mimetypes.guess_type(url)[0]
                if not mtype:
                    mtype
                headers = email.message_from_string('Content-Type: %s\nContent-Length: %d\nLast-modified: %s\n' % ('text/plain', size, modified))
                if not host:
                    urlfile = file
                    if file[:1] == '/':
                        urlfile = 'file://' + file
                    return addinfourl(open(localname, 'rb'), headers, urlfile)
                (host, port) = None(host)
                if port and socket.gethostbyname(host) in (localhost(),) + thishost():
                    urlfile = file
                    if file[:1] == '/':
                        urlfile = 'file://' + file
                    elif file[:2] == './':
                        raise ValueError('local file url may start with / or file:. Unknown url of type: %s' % url)
                    return addinfourl(open(localname, 'rb'), headers, urlfile)
                raise None('local file error: not on local host')
            except OSError:
                e = None
                raise URLError(e.strerror, e.filename)
                e = None
                del e


        
        def open_ftp(self, url):
            '''Use FTP protocol.'''
            if not isinstance(url, str):
                raise URLError('ftp error: proxy support for ftp protocol currently not implemented')
            import mimetypes
            (host, path) = _splithost(url)
            if not host:
                raise URLError('ftp error: no host given')
            (host, port) = _splitport(host)
            (user, host) = _splituser(host)
            if user:
                (user, passwd) = _splitpasswd(user)
            else:
                passwd = None
            host = unquote(host)
            if not user:
                user
            user = unquote('')
            if not passwd:
                passwd
            passwd = unquote('')
            host = socket.gethostbyname(host)
            if not port:
                import ftplib
                port = ftplib.FTP_PORT
            else:
                port = int(port)
            (path, attrs) = _splitattr(path)
            path = unquote(path)
            dirs = path.split('/')
            file = dirs[-1]
            dirs = dirs[:-1]
            if not dirs and dirs[0]:
                dirs = dirs[1:]
            if not dirs and dirs[0]:
                dirs[0] = '/'
            key = (user, host, port, '/'.join(dirs))
            if len(self.ftpcache) > MAXFTPCACHE:
                for k in list(self.ftpcache):
                    if not k != key:
                        continue
                    v = self.ftpcache[k]
                    del self.ftpcache[k]
                    v.close()
        # WARNING: Decompyle incomplete

        
        def open_data(self, url, data = (None,)):
            '''Use "data" URL.'''
            if not isinstance(url, str):
                raise URLError('data error: proxy support for data protocol currently not implemented')
            
            try:
                (type, data) = url.split(',', 1)
                if not type:
                    type = 'text/plain;charset=US-ASCII'
                semi = type.rfind(';')
                if semi >= 0 and '=' not in type[semi:]:
                    encoding = type[semi + 1:]
                    type = type[:semi]
                else:
                    encoding = ''
                msg = []
                msg.append('Date: %s' % time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(time.time())))
                msg.append('Content-type: %s' % type)
                if encoding == 'base64':
                    data = base64.decodebytes(data.encode('ascii')).decode('latin-1')
                else:
                    data = unquote(data)
                msg.append('Content-Length: %d' % len(data))
                msg.append('')
                msg.append(data)
                msg = '\n'.join(msg)
                headers = email.message_from_string(msg)
                f = io.StringIO(msg)
                return addinfourl(f, headers, url)
            except ValueError:
                raise OSError('data error', 'bad data URL')



    
    class FancyURLopener(URLopener):
        '''Derived class with handlers for errors we can handle (perhaps).'''
        
        def __init__(self, *args, **kwargs):
            pass
        # WARNING: Decompyle incomplete

        
        def http_error_default(self, url, fp, errcode, errmsg, headers):
            """Default error handling -- don't raise an exception."""
            return addinfourl(fp, headers, 'http:' + url, errcode)

        
        def http_error_302(self, url, fp, errcode, errmsg, headers, data = (None,)):
            '''Error 302 -- relocated (temporarily).'''
            
            try:
                if self.maxtries and self.tries >= self.maxtries:
                    self.tries = 0
                    return meth(url, fp, 500, 'Internal Server Error: Redirect Recursion', headers)
                result = self, self.tries += 1, .tries.redirect_internal(url, fp, errcode, errmsg, headers, data)
                self.tries = 0
                return result
            except:
                self.tries = 0


        
        def redirect_internal(self, url, fp, errcode, errmsg, headers, data):
            if 'location' in headers:
                newurl = headers['location']
            elif 'uri' in headers:
                newurl = headers['uri']
            else:
                return None
            fp.close()
            newurl = urljoin(self.type + ':' + url, newurl)
            urlparts = urlparse(newurl)
            if urlparts.scheme not in ('http', 'https', 'ftp', ''):
                raise HTTPError(newurl, errcode, errmsg + " Redirection to url '%s' is not allowed." % newurl, headers, fp)
            return self.open(newurl)

        
        def http_error_301(self, url, fp, errcode, errmsg, headers, data = (None,)):
            '''Error 301 -- also relocated (permanently).'''
            return self.http_error_302(url, fp, errcode, errmsg, headers, data)

        
        def http_error_303(self, url, fp, errcode, errmsg, headers, data = (None,)):
            '''Error 303 -- also relocated (essentially identical to 302).'''
            return self.http_error_302(url, fp, errcode, errmsg, headers, data)

        
        def http_error_307(self, url, fp, errcode, errmsg, headers, data = (None,)):
            '''Error 307 -- relocated, but turn POST into error.'''
            pass
        # WARNING: Decompyle incomplete

        
        def http_error_308(self, url, fp, errcode, errmsg, headers, data = (None,)):
            '''Error 308 -- relocated, but turn POST into error.'''
            pass
        # WARNING: Decompyle incomplete

        
        def http_error_401(self, url, fp, errcode, errmsg, headers, data, retry = (None, False)):
            '''Error 401 -- authentication required.
        This function supports Basic authentication only.'''
            if 'www-authenticate' not in headers:
                URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
            stuff = headers['www-authenticate']
            match = re.match('[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
            if not match:
                URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
            (scheme, realm) = match.groups()
            if scheme.lower() != 'basic':
                URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
            if not retry:
                URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
            name = 'retry_' + self.type + '_basic_auth'
        # WARNING: Decompyle incomplete

        
        def http_error_407(self, url, fp, errcode, errmsg, headers, data, retry = (None, False)):
            '''Error 407 -- proxy authentication required.
        This function supports Basic authentication only.'''
            if 'proxy-authenticate' not in headers:
                URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
            stuff = headers['proxy-authenticate']
            match = re.match('[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
            if not match:
                URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
            (scheme, realm) = match.groups()
            if scheme.lower() != 'basic':
                URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
            if not retry:
                URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
            name = 'retry_proxy_' + self.type + '_basic_auth'
        # WARNING: Decompyle incomplete

        
        def retry_proxy_http_basic_auth(self, url, realm, data = (None,)):
            (host, selector) = _splithost(url)
            newurl = 'http://' + host + selector
            proxy = self.proxies['http']
            (urltype, proxyhost) = _splittype(proxy)
            (proxyhost, proxyselector) = _splithost(proxyhost)
            i = proxyhost.find('@') + 1
            proxyhost = proxyhost[i:]
            (user, passwd) = self.get_user_passwd(proxyhost, realm, i)
            if not user and passwd:
                return None
            proxyhost = f'''{quote(user, safe = '')!s}:{quote(passwd, safe = '')!s}@{proxyhost!s}'''
            self.proxies['http'] = 'http://' + proxyhost + proxyselector
        # WARNING: Decompyle incomplete

        
        def retry_proxy_https_basic_auth(self, url, realm, data = (None,)):
            (host, selector) = _splithost(url)
            newurl = 'https://' + host + selector
            proxy = self.proxies['https']
            (urltype, proxyhost) = _splittype(proxy)
            (proxyhost, proxyselector) = _splithost(proxyhost)
            i = proxyhost.find('@') + 1
            proxyhost = proxyhost[i:]
            (user, passwd) = self.get_user_passwd(proxyhost, realm, i)
            if not user and passwd:
                return None
            proxyhost = f'''{quote(user, safe = '')!s}:{quote(passwd, safe = '')!s}@{proxyhost!s}'''
            self.proxies['https'] = 'https://' + proxyhost + proxyselector
        # WARNING: Decompyle incomplete

        
        def retry_http_basic_auth(self, url, realm, data = (None,)):
            (host, selector) = _splithost(url)
            i = host.find('@') + 1
            host = host[i:]
            (user, passwd) = self.get_user_passwd(host, realm, i)
            if not user and passwd:
                return None
            host = f'''{quote(user, safe = '')!s}:{quote(passwd, safe = '')!s}@{host!s}'''
            newurl = 'http://' + host + selector
        # WARNING: Decompyle incomplete

        
        def retry_https_basic_auth(self, url, realm, data = (None,)):
            (host, selector) = _splithost(url)
            i = host.find('@') + 1
            host = host[i:]
            (user, passwd) = self.get_user_passwd(host, realm, i)
            if not user and passwd:
                return None
            host = f'''{quote(user, safe = '')!s}:{quote(passwd, safe = '')!s}@{host!s}'''
            newurl = 'https://' + host + selector
        # WARNING: Decompyle incomplete

        
        def get_user_passwd(self, host, realm, clear_cache = (0,)):
            key = realm + '@' + host.lower()
            if key in self.auth_cache:
                if clear_cache:
                    del self.auth_cache[key]
                else:
                    return self.auth_cache[key]
                (user, passwd) = None.prompt_user_passwd(host, realm)
                if user or passwd:
                    self.auth_cache[key] = (user, passwd)
            return (user, passwd)

        
        def prompt_user_passwd(self, host, realm):
            '''Override this in a GUI environment!'''
            import getpass
            
            try:
                user = input(f'''Enter username for {realm!s} at {host!s}: ''')
                passwd = getpass.getpass(f'''Enter password for {user!s} in {realm!s} at {host!s}: ''')
                return (user, passwd)
            except KeyboardInterrupt:
                print()
                return (None, None)



    _localhost = None
    
    def localhost():
        """Return the IP address of the magic hostname 'localhost'."""
        pass
    # WARNING: Decompyle incomplete

    _thishost = None
    
    def thishost():
        '''Return the IP addresses of the current host.'''
        pass
    # WARNING: Decompyle incomplete

    _ftperrors = None
    
    def ftperrors():
        '''Return the set of errors raised by the FTP class.'''
        pass
    # WARNING: Decompyle incomplete

    _noheaders = None
    
    def noheaders():
        '''Return an empty email Message object.'''
        pass
    # WARNING: Decompyle incomplete

    
    class ftpwrapper:
        '''Class used by open_ftp() for cache of open FTP connections.'''
        
        def __init__(self, user, passwd, host, port, dirs, timeout, persistent = (None, True)):
            self.user = user
            self.passwd = passwd
            self.host = host
            self.port = port
            self.dirs = dirs
            self.timeout = timeout
            self.refcount = 0
            self.keepalive = persistent
            
            try:
                self.init()
                return None
            except:
                self.close()
                raise 


        
        def init(self):
            import ftplib
            self.busy = 0
            self.ftp = ftplib.FTP()
            self.ftp.connect(self.host, self.port, self.timeout)
            self.ftp.login(self.user, self.passwd)
            _target = '/'.join(self.dirs)
            self.ftp.cwd(_target)

        
        def retrfile(self, file, type):
            import ftplib
            self.endtransfer()
            if type in ('d', 'D'):
                cmd = 'TYPE A'
                isdir = 1
            else:
                cmd = 'TYPE ' + type
                isdir = 0
        # WARNING: Decompyle incomplete

        
        def endtransfer(self):
            if not self.busy:
                return None
            self.busy = 0
            
            try:
                self.ftp.voidresp()
                return None
            except ftperrors():
                return None


        
        def close(self):
            self.keepalive = False
            if self.refcount <= 0:
                self.real_close()
                return None

        
        def file_close(self):
            self.endtransfer()
            if self.refcount <= 0:
                if not self.keepalive:
                    self.real_close()
                    return None
                return None

        
        def real_close(self):
            self.endtransfer()
            
            try:
                self.ftp.close()
                return None
            except ftperrors():
                return None



    
    def getproxies_environment():
        '''Return a dictionary of scheme -> proxy server URL mappings.

    Scan the environment for variables named <scheme>_proxy;
    this seems to be the standard convention.  If you need a
    different way, you can pass a proxies dictionary to the
    [Fancy]URLopener constructor.
    '''
        proxies = { }
        environment = []
        for name in os.environ.keys():
            if not len(name) > 5:
                continue
            if not name[-6] == '_':
                continue
            if not name[-5:].lower() == 'proxy':
                continue
            value = os.environ[name]
            proxy_name = name[:-6].lower()
            environment.append((name, value, proxy_name))
            if not value:
                continue
            proxies[proxy_name] = value
        if 'REQUEST_METHOD' in os.environ:
            proxies.pop('http', None)
        for name, value, proxy_name in environment:
            if not name[-6:] == '_proxy':
                continue
            if value:
                proxies[proxy_name] = value
                continue
            proxies.pop(proxy_name, None)
        return proxies

    
    def proxy_bypass_environment(host, proxies = (None,)):
        """Test if proxies should not be used for a particular host.

    Checks the proxy dict for the value of no_proxy, which should
    be a list of comma separated DNS suffixes, or '*' for all hosts.

    """
        pass
    # WARNING: Decompyle incomplete

    
    def _proxy_bypass_macosx_sysconf(host, proxy_settings):
        """
    Return True iff this host shouldn't be accessed using a proxy

    This function uses the MacOSX framework SystemConfiguration
    to fetch the proxy information.

    proxy_settings come from _scproxy._get_proxy_settings or get mocked ie:
    { 'exclude_simple': bool,
      'exceptions': ['foo.bar', '*.bar.com', '127.0.0.1', '10.1', '10.0/16']
    }
    """
        fnmatch = fnmatch
        import fnmatch
        AddressValueError = AddressValueError
        IPv4Address = IPv4Address
        import ipaddress
        (hostonly, port) = _splitport(host)
        
        def ip2num(ipAddr):
            parts = ipAddr.split('.')
            parts = list(map(int, parts))
            if len(parts) != 4:
                parts = parts + [
                    0,
                    0,
                    0,
                    0][:4]
            return parts[0] << 24 | parts[1] << 16 | parts[2] << 8 | parts[3]

        if '.' not in host and proxy_settings['exclude_simple']:
            return True
        hostIP = None
    # WARNING: Decompyle incomplete

    
    def _proxy_bypass_winreg_override(host, override):
        '''Return True if the host should bypass the proxy server.

    The proxy override list is obtained from the Windows
    Internet settings proxy override registry value.

    An example of a proxy override value is:
    "www.example.com;*.example.net; 192.168.0.1"
    '''
        fnmatch = fnmatch
        import fnmatch
        (host, _) = _splitport(host)
        proxy_override = override.split(';')
        for test in proxy_override:
            test = test.strip()
            if test == '<local>':
                if not '.' not in host:
                    continue
                proxy_override
                return True
            if not fnmatch(host, test):
                continue
            return True
        return False

    if sys.platform == 'darwin':
        from _scproxy import _get_proxy_settings, _get_proxies
        
        def proxy_bypass_macosx_sysconf(host):
            proxy_settings = _get_proxy_settings()
            return _proxy_bypass_macosx_sysconf(host, proxy_settings)

        
        def getproxies_macosx_sysconf():
            '''Return a dictionary of scheme -> proxy server URL mappings.

        This function uses the MacOSX framework SystemConfiguration
        to fetch the proxy information.
        '''
            return _get_proxies()

        
        def proxy_bypass(host):
            '''Return True, if host should be bypassed.

        Checks proxy settings gathered from the environment, if specified,
        or from the MacOSX framework SystemConfiguration.

        '''
            proxies = getproxies_environment()
            if proxies:
                return proxy_bypass_environment(host, proxies)
            return None(host)

        
        def getproxies():
            if not getproxies_environment():
                getproxies_environment()
            return getproxies_macosx_sysconf()

        return None
    if os.name == 'nt':
        
        def getproxies_registry():
            '''Return a dictionary of scheme -> proxy server URL mappings.

        Win32 uses the registry to store proxies.

        '''
            proxies = { }
            
            try:
                import winreg
                
                try:
                    internetSettings = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings')
                    proxyEnable = winreg.QueryValueEx(internetSettings, 'ProxyEnable')[0]
                    if proxyEnable:
                        proxyServer = str(winreg.QueryValueEx(internetSettings, 'ProxyServer')[0])
                        if '=' not in proxyServer and ';' not in proxyServer:
                            proxyServer = 'http={0};https={0};ftp={0}'.format(proxyServer)
                        for p in proxyServer.split(';'):
                            (protocol, address) = p.split('=', 1)
                            if not re.match('(?:[^/:]+)://', address):
                                if protocol in ('http', 'https', 'ftp'):
                                    address = 'http://' + address
                                elif protocol == 'socks':
                                    address = 'socks://' + address
                            proxies[protocol] = address
                        if proxies.get('socks'):
                            address = re.sub('^socks://', 'socks4://', proxies['socks'])
                            if not proxies.get('http'):
                                proxies.get('http')
                            proxies['http'] = address
                            if not proxies.get('https'):
                                proxies.get('https')
                            proxies['https'] = address
                    internetSettings.Close()
                    return proxies
                    except ImportError:
                        return 
                except (OSError, ValueError, TypeError):
                    return proxies



        
        def getproxies():
            '''Return a dictionary of scheme -> proxy server URL mappings.

        Returns settings gathered from the environment, if specified,
        or the registry.

        '''
            if not getproxies_environment():
                getproxies_environment()
            return getproxies_registry()

        
        def proxy_bypass_registry(host):
            
            try:
                import winreg
                
                try:
                    internetSettings = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings')
                    proxyEnable = winreg.QueryValueEx(internetSettings, 'ProxyEnable')[0]
                    proxyOverride = str(winreg.QueryValueEx(internetSettings, 'ProxyOverride')[0])
                    if not proxyEnable or proxyOverride:
                        return False
                    return _proxy_bypass_winreg_override(host, proxyOverride)
                    except ImportError:
                        return False
                except OSError:
                    return False



        
        def proxy_bypass(host):
            '''Return True, if host should be bypassed.

        Checks proxy settings gathered from the environment, if specified,
        or the registry.

        '''
            proxies = getproxies_environment()
            if proxies:
                return proxy_bypass_environment(host, proxies)
            return None(host)

        return None
    getproxies = getproxies_environment
    proxy_bypass = proxy_bypass_environment
    return None
except ImportError:
    _have_ssl = False
    continue

