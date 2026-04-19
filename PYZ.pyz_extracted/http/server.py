# Source Generated with Decompyle++
# File: server.pyc (Python 3.12)

"""HTTP server classes.

Note: BaseHTTPRequestHandler doesn't implement any HTTP request; see
SimpleHTTPRequestHandler for simple implementations of GET, HEAD and POST,
and CGIHTTPRequestHandler for CGI scripts.

It does, however, optionally implement HTTP/1.1 persistent connections,
as of version 0.3.

Notes on CGIHTTPRequestHandler
------------------------------

This class implements GET and POST requests to cgi-bin scripts.

If the os.fork() function is not present (e.g. on Windows),
subprocess.Popen() is used as a fallback, with slightly altered semantics.

In all cases, the implementation is intentionally naive -- all
requests are executed synchronously.

SECURITY WARNING: DON'T USE THIS CODE UNLESS YOU ARE INSIDE A FIREWALL
-- it may execute arbitrary Python code or external programs.

Note that status code 200 is sent prior to execution of a CGI script, so
scripts cannot send other status codes such as 302 (redirect).

XXX To do:

- log requests even later (to capture byte count)
- log user-agent header and other interesting goodies
- send error log to separate file
"""
__version__ = '0.6'
__all__ = [
    'HTTPServer',
    'ThreadingHTTPServer',
    'BaseHTTPRequestHandler',
    'SimpleHTTPRequestHandler',
    'CGIHTTPRequestHandler']
import copy
import datetime
import email.utils as email
import html
import http.client as http
import io
import itertools
import mimetypes
import os
import posixpath
import select
import shutil
import socket
import socketserver
import sys
import time
import urllib.parse as urllib
from http import HTTPStatus
DEFAULT_ERROR_MESSAGE = '<!DOCTYPE HTML>\n<html lang="en">\n    <head>\n        <meta charset="utf-8">\n        <title>Error response</title>\n    </head>\n    <body>\n        <h1>Error response</h1>\n        <p>Error code: %(code)d</p>\n        <p>Message: %(message)s.</p>\n        <p>Error code explanation: %(code)s - %(explain)s.</p>\n    </body>\n</html>\n'
DEFAULT_ERROR_CONTENT_TYPE = 'text/html;charset=utf-8'

class HTTPServer(socketserver.TCPServer):
    allow_reuse_address = 1
    
    def server_bind(self):
        '''Override server_bind to store the server name.'''
        socketserver.TCPServer.server_bind(self)
        (host, port) = self.server_address[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port



class ThreadingHTTPServer(HTTPServer, socketserver.ThreadingMixIn):
    daemon_threads = True


class BaseHTTPRequestHandler(socketserver.StreamRequestHandler):
    __module__ = __name__
    __qualname__ = 'BaseHTTPRequestHandler'
    __doc__ = 'HTTP request handler base class.\n\n    The following explanation of HTTP serves to guide you through the\n    code as well as to expose any misunderstandings I may have about\n    HTTP (so you don\'t need to read the code to figure out I\'m wrong\n    :-).\n\n    HTTP (HyperText Transfer Protocol) is an extensible protocol on\n    top of a reliable stream transport (e.g. TCP/IP).  The protocol\n    recognizes three parts to a request:\n\n    1. One line identifying the request type and path\n    2. An optional set of RFC-822-style headers\n    3. An optional data part\n\n    The headers and data are separated by a blank line.\n\n    The first line of the request has the form\n\n    <command> <path> <version>\n\n    where <command> is a (case-sensitive) keyword such as GET or POST,\n    <path> is a string containing path information for the request,\n    and <version> should be the string "HTTP/1.0" or "HTTP/1.1".\n    <path> is encoded using the URL encoding scheme (using %xx to signify\n    the ASCII character with hex code xx).\n\n    The specification specifies that lines are separated by CRLF but\n    for compatibility with the widest range of clients recommends\n    servers also handle LF.  Similarly, whitespace in the request line\n    is treated sensibly (allowing multiple spaces between components\n    and allowing trailing whitespace).\n\n    Similarly, for output, lines ought to be separated by CRLF pairs\n    but most clients grok LF characters just fine.\n\n    If the first line of the request has the form\n\n    <command> <path>\n\n    (i.e. <version> is left out) then this is assumed to be an HTTP\n    0.9 request; this form has no optional headers and data part and\n    the reply consists of just the data.\n\n    The reply form of the HTTP 1.x protocol again has three parts:\n\n    1. One line giving the response code\n    2. An optional set of RFC-822-style headers\n    3. The data\n\n    Again, the headers and data are separated by a blank line.\n\n    The response code line has the form\n\n    <version> <responsecode> <responsestring>\n\n    where <version> is the protocol version ("HTTP/1.0" or "HTTP/1.1"),\n    <responsecode> is a 3-digit response code indicating success or\n    failure of the request, and <responsestring> is an optional\n    human-readable string explaining what the response code means.\n\n    This server parses the request and the headers, and then calls a\n    function specific to the request type (<command>).  Specifically,\n    a request SPAM will be handled by a method do_SPAM().  If no\n    such method exists the server sends an error response to the\n    client.  If it exists, it is called with no arguments:\n\n    do_SPAM()\n\n    Note that the request name is case sensitive (i.e. SPAM and spam\n    are different requests).\n\n    The various request details are stored in instance variables:\n\n    - client_address is the client IP address in the form (host,\n    port);\n\n    - command, path and version are the broken-down request line;\n\n    - headers is an instance of email.message.Message (or a derived\n    class) containing the header information;\n\n    - rfile is a file object open for reading positioned at the\n    start of the optional input data part;\n\n    - wfile is a file object open for writing.\n\n    IT IS IMPORTANT TO ADHERE TO THE PROTOCOL FOR WRITING!\n\n    The first thing to be written must be the response line.  Then\n    follow 0 or more header lines, then a blank line, and then the\n    actual data (if any).  The meaning of the header lines depends on\n    the command executed by the server; in most cases, when data is\n    returned, there should be at least one header line of the form\n\n    Content-type: <type>/<subtype>\n\n    where <type> and <subtype> should be registered MIME types,\n    e.g. "text/html" or "text/plain".\n\n    '
    sys_version = 'Python/' + sys.version.split()[0]
    server_version = 'BaseHTTP/' + __version__
    error_message_format = DEFAULT_ERROR_MESSAGE
    error_content_type = DEFAULT_ERROR_CONTENT_TYPE
    default_request_version = 'HTTP/0.9'
    
    def parse_request(self):
        '''Parse a request (internal).

        The request should be stored in self.raw_requestline; the results
        are in self.command, self.path, self.request_version and
        self.headers.

        Return True for success, False for failure; on failure, any relevant
        error response has already been sent back.

        '''
        self.command = None
        self.request_version = self.default_request_version
        version = self.default_request_version
        self.close_connection = True
        requestline = str(self.raw_requestline, 'iso-8859-1')
        requestline = requestline.rstrip('\r\n')
        self.requestline = requestline
        words = requestline.split()
        if len(words) == 0:
            return False
        if len(words) >= 3:
            version = words[-1]
            
            try:
                if not version.startswith('HTTP/'):
                    raise ValueError
                base_version_number = version.split('/', 1)[1]
                version_number = base_version_number.split('.')
                if len(version_number) != 2:
                    raise ValueError
                if (lambda .0: pass# WARNING: Decompyle incomplete
)(version_number()):
                    raise ValueError('non digit in http version')
                if (lambda .0: pass# WARNING: Decompyle incomplete
)(version_number()):
                    raise ValueError('unreasonable length http version')
                version_number = (int(version_number[0]), int(version_number[1]))
                if version_number >= (1, 1) and self.protocol_version >= 'HTTP/1.1':
                    self.close_connection = False
                if version_number >= (2, 0):
                    self.send_error(HTTPStatus.HTTP_VERSION_NOT_SUPPORTED, 'Invalid HTTP version (%s)' % base_version_number)
                    return False
                self.request_version = version
                self.send_error(HTTPStatus.BAD_REQUEST, 'Bad request syntax (%r)' % requestline)
                return False
                (command, path) = words[:2]
                if len(words) == 2:
                    self.close_connection = True
                    if command != 'GET':
                        self.send_error(HTTPStatus.BAD_REQUEST, 'Bad HTTP/0.9 request type (%r)' % command)
                        return False
                self.command, self.path = command, path
                if self.path.startswith('//'):
                    self.path = '/' + self.path.lstrip('/')
                
                try:
                    self.headers = http.client.parse_headers(self.rfile, _class = self.MessageClass)
                    conntype = self.headers.get('Connection', '')
                    if conntype.lower() == 'close':
                        self.close_connection = True
                    elif conntype.lower() == 'keep-alive' and self.protocol_version >= 'HTTP/1.1':
                        self.close_connection = False
                    expect = self.headers.get('Expect', '')
                    if not expect.lower() == '100-continue' and self.protocol_version >= 'HTTP/1.1' and self.request_version >= 'HTTP/1.1' and self.handle_expect_100():
                        return False
                    return True
                    except (ValueError, IndexError):
                        self.send_error(HTTPStatus.BAD_REQUEST, 'Bad request version (%r)' % version)
                        return False
                except http.client.LineTooLong:
                    err = None
                    self.send_error(HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE, 'Line too long', str(err))
                    err = None
                    del err
                    return False
                    err = None
                    del err
                    except http.client.HTTPException:
                        err = None
                        self.send_error(HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE, 'Too many headers', str(err))
                        err = None
                        del err
                        return False
                        err = None
                        del err



    
    def handle_expect_100(self):
        '''Decide what to do with an "Expect: 100-continue" header.

        If the client is expecting a 100 Continue response, we must
        respond with either a 100 Continue or a final response before
        waiting for the request body. The default is to always respond
        with a 100 Continue. You can behave differently (for example,
        reject unauthorized requests) by overriding this method.

        This method should either return True (possibly after sending
        a 100 Continue response) or send an error response and return
        False.

        '''
        self.send_response_only(HTTPStatus.CONTINUE)
        self.end_headers()
        return True

    
    def handle_one_request(self):
        """Handle a single HTTP request.

        You normally don't need to override this method; see the class
        __doc__ string for information on how to handle specific HTTP
        commands such as GET and POST.

        """
        
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
                return None
                
                try:
                    if not self.raw_requestline:
                        self.close_connection = True
                        return None
                        
                        try:
                            if not self.parse_request():
                                return None
                                
                                try:
                                    mname = 'do_' + self.command
                                    if not hasattr(self, mname):
                                        self.send_error(HTTPStatus.NOT_IMPLEMENTED, 'Unsupported method (%r)' % self.command)
                                        return None
                                        
                                        try:
                                            method = getattr(self, mname)
                                            method()
                                            self.wfile.flush()
                                            return None
                                        except TimeoutError:
                                            e = None
                                            self.log_error('Request timed out: %r', e)
                                            self.close_connection = True
                                            e = None
                                            del e
                                            return None
                                            e = None
                                            del e






    
    def handle(self):
        '''Handle multiple requests if necessary.'''
        self.close_connection = True
        self.handle_one_request()
        if not self.close_connection:
            self.handle_one_request()
            if not self.close_connection:
                continue
            return None

    
    def send_error(self, code, message, explain = (None, None)):
        '''Send and log an error reply.

        Arguments are
        * code:    an HTTP error code
                   3 digits
        * message: a simple optional 1 line reason phrase.
                   *( HTAB / SP / VCHAR / %x80-FF )
                   defaults to short entry matching the response code
        * explain: a detailed message defaults to the long entry
                   matching the response code.

        This sends an error response (so it must be called before any
        output has been generated), logs the error, and finally sends
        a piece of HTML explaining the error to the user.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def send_response(self, code, message = (None,)):
        '''Add the response header to the headers buffer and log the
        response code.

        Also send two standard headers with the server software
        version and the current date.

        '''
        self.log_request(code)
        self.send_response_only(code, message)
        self.send_header('Server', self.version_string())
        self.send_header('Date', self.date_time_string())

    
    def send_response_only(self, code, message = (None,)):
        '''Send the response header only.'''
        pass
    # WARNING: Decompyle incomplete

    
    def send_header(self, keyword, value):
        '''Send a MIME header to the headers buffer.'''
        if self.request_version != 'HTTP/0.9':
            if not hasattr(self, '_headers_buffer'):
                self._headers_buffer = []
            self._headers_buffer.append(f'''{keyword!s}: {value!s}\r\n'''.encode('latin-1', 'strict'))
        if keyword.lower() == 'connection':
            if value.lower() == 'close':
                self.close_connection = True
                return None
            if value.lower() == 'keep-alive':
                self.close_connection = False
                return None
            return None

    
    def end_headers(self):
        '''Send the blank line ending the MIME headers.'''
        if self.request_version != 'HTTP/0.9':
            self._headers_buffer.append(b'\r\n')
            self.flush_headers()
            return None

    
    def flush_headers(self):
        if hasattr(self, '_headers_buffer'):
            self.wfile.write(b''.join(self._headers_buffer))
            self._headers_buffer = []
            return None

    
    def log_request(self, code, size = ('-', '-')):
        '''Log an accepted request.

        This is called by send_response().

        '''
        if isinstance(code, HTTPStatus):
            code = code.value
        self.log_message('"%s" %s %s', self.requestline, str(code), str(size))

    
    def log_error(self, format, *args):
        '''Log an error.

        This is called when a request cannot be fulfilled.  By
        default it passes the message on to log_message().

        Arguments are the same as for log_message().

        XXX This should go to the separate error log.

        '''
        pass
    # WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    pass
# WARNING: Decompyle incomplete


def _url_collapse_path(path):
    """
    Given a URL path, remove extra '/'s and '.' path elements and collapse
    any '..' references and returns a collapsed path.

    Implements something akin to RFC-2396 5.2 step 6 to parse relative paths.
    The utility of this function is limited to is_cgi method and helps
    preventing some security attacks.

    Returns: The reconstituted URL, which will always start with a '/'.

    Raises: IndexError if too many '..' occur within the path.

    """
    (path, _, query) = path.partition('?')
    path = urllib.parse.unquote(path)
    path_parts = path.split('/')
    head_parts = []
    for part in path_parts[:-1]:
        if part == '..':
            head_parts.pop()
            continue
        if not part:
            continue
        if not part != '.':
            continue
        head_parts.append(part)
    if path_parts:
        tail_part = path_parts.pop()
        if tail_part:
            if tail_part == '..':
                head_parts.pop()
                tail_part = ''
            elif tail_part == '.':
                tail_part = ''
            else:
                tail_part = ''
    if query:
        tail_part = '?'.join((tail_part, query))
    splitpath = ('/' + '/'.join(head_parts), tail_part)
    collapsed_path = '/'.join(splitpath)
    return collapsed_path

nobody = None

def nobody_uid():
    """Internal routine to get nobody's uid"""
    global nobody, nobody
    if nobody:
        return nobody
    
    try:
        import pwd
        
        try:
            nobody = pwd.getpwnam('nobody')[2]
            return nobody
            except ImportError:
                return -1
        except KeyError:
            nobody = max + (lambda .0: pass# WARNING: Decompyle incomplete
)(pwd.getpwall()())
            return nobody




def executable(path):
    '''Test for executable file.'''
    return os.access(path, os.X_OK)


class CGIHTTPRequestHandler(SimpleHTTPRequestHandler):
    '''Complete HTTP server with GET, HEAD and POST commands.

    GET and HEAD also support running CGI scripts.

    The POST command is *only* implemented for CGI scripts.

    '''
    have_fork = hasattr(os, 'fork')
    rbufsize = 0
    
    def do_POST(self):
        '''Serve a POST request.

        This is only implemented for CGI scripts.

        '''
        if self.is_cgi():
            self.run_cgi()
            return None
        self.send_error(HTTPStatus.NOT_IMPLEMENTED, 'Can only POST to CGI scripts')

    
    def send_head(self):
        '''Version of send_head that support CGI scripts'''
        if self.is_cgi():
            return self.run_cgi()
        return None.send_head(self)

    
    def is_cgi(self):
        """Test whether self.path corresponds to a CGI script.

        Returns True and updates the cgi_info attribute to the tuple
        (dir, rest) if self.path requires running a CGI script.
        Returns False otherwise.

        If any exception is raised, the caller should assume that
        self.path was rejected as invalid and act accordingly.

        The default implementation tests whether the normalized url
        path begins with one of the strings in self.cgi_directories
        (and the next character is a '/' or the end of the string).

        """
        collapsed_path = _url_collapse_path(self.path)
        dir_sep = collapsed_path.find('/', 1)
        if dir_sep > 0 and collapsed_path[:dir_sep] not in self.cgi_directories:
            dir_sep = collapsed_path.find('/', dir_sep + 1)
            if dir_sep > 0 and collapsed_path[:dir_sep] not in self.cgi_directories:
                continue
        if dir_sep > 0:
            tail = collapsed_path[dir_sep + 1:]
            head = collapsed_path[:dir_sep]
            self.cgi_info = (head, tail)
            return True
        return False

    cgi_directories = [
        '/cgi-bin',
        '/htbin']
    
    def is_executable(self, path):
        '''Test whether argument path is an executable file.'''
        return executable(path)

    
    def is_python(self, path):
        '''Test whether argument path is a Python script.'''
        (head, tail) = os.path.splitext(path)
        return tail.lower() in ('.py', '.pyw')

    
    def run_cgi(self):
        '''Execute a CGI script.'''
        (dir, rest) = self.cgi_info
        path = dir + '/' + rest
        i = path.find('/', len(dir) + 1)
        if i >= 0:
            nextdir = path[:i]
            nextrest = path[i + 1:]
            scriptdir = self.translate_path(nextdir)
            if os.path.isdir(scriptdir):
                rest = nextrest
                dir = nextdir
                i = path.find('/', len(dir) + 1)
            
        elif i >= 0:
            continue
        (rest, _, query) = rest.partition('?')
        i = rest.find('/')
        if i >= 0:
            rest = rest[i:]
            script = rest[:i]
        else:
            rest = ''
            script = rest
        scriptname = dir + '/' + script
        scriptfile = self.translate_path(scriptname)
        if not os.path.exists(scriptfile):
            self.send_error(HTTPStatus.NOT_FOUND, 'No such CGI script (%r)' % scriptname)
            return None
        if not os.path.isfile(scriptfile):
            self.send_error(HTTPStatus.FORBIDDEN, 'CGI script is not a plain file (%r)' % scriptname)
            return None
        ispy = self.is_python(scriptname)
        if not (self.have_fork or ispy) and self.is_executable(scriptfile):
            self.send_error(HTTPStatus.FORBIDDEN, 'CGI script is not executable (%r)' % scriptname)
            return None
        env = copy.deepcopy(os.environ)
        env['SERVER_SOFTWARE'] = self.version_string()
        env['SERVER_NAME'] = self.server.server_name
        env['GATEWAY_INTERFACE'] = 'CGI/1.1'
        env['SERVER_PROTOCOL'] = self.protocol_version
        env['SERVER_PORT'] = str(self.server.server_port)
        env['REQUEST_METHOD'] = self.command
        uqrest = urllib.parse.unquote(rest)
        env['PATH_INFO'] = uqrest
        env['PATH_TRANSLATED'] = self.translate_path(uqrest)
        env['SCRIPT_NAME'] = scriptname
        env['QUERY_STRING'] = query
        env['REMOTE_ADDR'] = self.client_address[0]
        authorization = self.headers.get('authorization')
    # WARNING: Decompyle incomplete



def _get_best_family(*address):
    pass
# WARNING: Decompyle incomplete


def test(HandlerClass, ServerClass, protocol, port, bind = (BaseHTTPRequestHandler, ThreadingHTTPServer, 'HTTP/1.0', 8000, None)):
    '''Test the HTTP request handler class.

    This runs an HTTP server on port 8000 (or the port argument).

    '''
    (ServerClass.address_family, addr) = _get_best_family(bind, port)
    HandlerClass.protocol_version = protocol
    httpd = ServerClass(addr, HandlerClass)
    (host, port) = httpd.socket.getsockname()[:2]
    url_host = f'''[{host}]''' if ':' in host else host
    print(f'''Serving HTTP on {host} port {port} (http://{url_host}:{port}/) ...''')
    httpd.serve_forever()
    None(None, None)
    return None
    except KeyboardInterrupt:
        print('\nKeyboard interrupt received, exiting.')
        sys.exit(0)
        continue
    with None:
        if not None:
            pass

if __name__ == '__main__':
    import argparse
    import contextlib
    parser = argparse.ArgumentParser()
    parser.add_argument('--cgi', action = 'store_true', help = 'run as CGI server')
    parser.add_argument('-b', '--bind', metavar = 'ADDRESS', help = 'bind to this address (default: all interfaces)')
    parser.add_argument('-d', '--directory', default = os.getcwd(), help = 'serve this directory (default: current directory)')
    parser.add_argument('-p', '--protocol', metavar = 'VERSION', default = 'HTTP/1.0', help = 'conform to this HTTP version (default: %(default)s)')
    parser.add_argument('port', default = 8000, type = int, nargs = '?', help = 'bind to this port (default: %(default)s)')
    args = parser.parse_args()
    
    class DualStackServer(ThreadingHTTPServer):
        pass
    # WARNING: Decompyle incomplete

    test(HandlerClass = handler_class, ServerClass = DualStackServer, port = args.port, bind = args.bind, protocol = args.protocol)
    return None
