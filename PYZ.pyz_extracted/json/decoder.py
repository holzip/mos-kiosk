# Source Generated with Decompyle++
# File: decoder.pyc (Python 3.12)

'''Implementation of JSONDecoder
'''
import re
from json import scanner

try:
    from _json import scanstring as c_scanstring
    __all__ = [
        'JSONDecoder',
        'JSONDecodeError']
    FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
    NaN = float('nan')
    PosInf = float('inf')
    NegInf = float('-inf')
    
    class JSONDecodeError(ValueError):
        '''Subclass of ValueError with the following additional properties:

    msg: The unformatted error message
    doc: The JSON document being parsed
    pos: The start index of doc where parsing failed
    lineno: The line corresponding to pos
    colno: The column corresponding to pos

    '''
        
        def __init__(self, msg, doc, pos):
            lineno = doc.count('\n', 0, pos) + 1
            colno = pos - doc.rfind('\n', 0, pos)
            errmsg = '%s: line %d column %d (char %d)' % (msg, lineno, colno, pos)
            ValueError.__init__(self, errmsg)
            self.msg = msg
            self.doc = doc
            self.pos = pos
            self.lineno = lineno
            self.colno = colno

        
        def __reduce__(self):
            return (self.__class__, (self.msg, self.doc, self.pos))


    _CONSTANTS = {
        '-Infinity': NegInf,
        'Infinity': PosInf,
        'NaN': NaN }
    HEXDIGITS = re.compile('[0-9A-Fa-f]{4}', FLAGS)
    STRINGCHUNK = re.compile('(.*?)(["\\\\\\x00-\\x1f])', FLAGS)
    BACKSLASH = {
        '"': '"',
        '\\': '\\',
        '/': '/',
        'b': '\x08',
        'f': '\x0c',
        'n': '\n',
        'r': '\r',
        't': '\t' }
    
    def _decode_uXXXX(s, pos, _m = (HEXDIGITS.match,)):
        esc = _m(s, pos + 1)
    # WARNING: Decompyle incomplete

    
    def py_scanstring(s, end, strict, _b, _m = (True, BACKSLASH, STRINGCHUNK.match)):
        '''Scan the string s for a JSON string. End is the index of the
    character in s after the quote that started the JSON string.
    Unescapes all valid JSON string escape sequences and raises ValueError
    on attempt to decode an invalid string. If strict is False then literal
    control characters are allowed in the string.

    Returns a tuple of the decoded string and the index of the character in s
    after the end quote.'''
        chunks = []
        _append = chunks.append
        begin = end - 1
        chunk = _m(s, end)
    # WARNING: Decompyle incomplete

    if not c_scanstring:
        c_scanstring
    scanstring = py_scanstring
    WHITESPACE = re.compile('[ \\t\\n\\r]*', FLAGS)
    WHITESPACE_STR = ' \t\n\r'
    
    def JSONObject(s_and_end, strict, scan_once, object_hook, object_pairs_hook, memo, _w, _ws = (None, WHITESPACE.match, WHITESPACE_STR)):
        (s, end) = s_and_end
        pairs = []
        pairs_append = pairs.append
    # WARNING: Decompyle incomplete

    
    def JSONArray(s_and_end, scan_once, _w, _ws = (WHITESPACE.match, WHITESPACE_STR)):
        (s, end) = s_and_end
        values = []
        nextchar = s[end:end + 1]
        if nextchar in _ws:
            end = _w(s, end + 1).end()
            nextchar = s[end:end + 1]
        if nextchar == ']':
            return (values, end + 1)
        _append = None.append
        
        try:
            (value, end) = scan_once(s, end)
            _append(value)
            nextchar = s[end:end + 1]
            if nextchar in _ws:
                end = _w(s, end + 1).end()
                nextchar = s[end:end + 1]
            end += 1
            if nextchar == ']':
                return (values, end)
            if None != ',':
                raise JSONDecodeError("Expecting ',' delimiter", s, end - 1)
            
            try:
                if s[end] in _ws:
                    end += 1
                    if s[end] in _ws:
                        end = _w(s, end + 1).end()
                continue
                except StopIteration:
                    err = None
                    raise JSONDecodeError('Expecting value', s, err.value), None
                    err = None
                    del err
            except IndexError:
                continue



    
    class JSONDecoder(object):
        '''Simple JSON <https://json.org> decoder

    Performs the following translations in decoding by default:

    +---------------+-------------------+
    | JSON          | Python            |
    +===============+===================+
    | object        | dict              |
    +---------------+-------------------+
    | array         | list              |
    +---------------+-------------------+
    | string        | str               |
    +---------------+-------------------+
    | number (int)  | int               |
    +---------------+-------------------+
    | number (real) | float             |
    +---------------+-------------------+
    | true          | True              |
    +---------------+-------------------+
    | false         | False             |
    +---------------+-------------------+
    | null          | None              |
    +---------------+-------------------+

    It also understands ``NaN``, ``Infinity``, and ``-Infinity`` as
    their corresponding ``float`` values, which is outside the JSON spec.

    '''
        
        def __init__(self = None, *, object_hook, parse_float, parse_int, parse_constant, strict, object_pairs_hook):
            """``object_hook``, if specified, will be called with the result
        of every JSON object decoded and its return value will be used in
        place of the given ``dict``.  This can be used to provide custom
        deserializations (e.g. to support JSON-RPC class hinting).

        ``object_pairs_hook``, if specified will be called with the result of
        every JSON object decoded with an ordered list of pairs.  The return
        value of ``object_pairs_hook`` will be used instead of the ``dict``.
        This feature can be used to implement custom decoders.
        If ``object_hook`` is also defined, the ``object_pairs_hook`` takes
        priority.

        ``parse_float``, if specified, will be called with the string
        of every JSON float to be decoded. By default this is equivalent to
        float(num_str). This can be used to use another datatype or parser
        for JSON floats (e.g. decimal.Decimal).

        ``parse_int``, if specified, will be called with the string
        of every JSON int to be decoded. By default this is equivalent to
        int(num_str). This can be used to use another datatype or parser
        for JSON integers (e.g. float).

        ``parse_constant``, if specified, will be called with one of the
        following strings: -Infinity, Infinity, NaN.
        This can be used to raise an exception if invalid JSON numbers
        are encountered.

        If ``strict`` is false (true is the default), then control
        characters will be allowed inside strings.  Control characters in
        this context are those with character codes in the 0-31 range,
        including ``'\\t'`` (tab), ``'\\n'``, ``'\\r'`` and ``'\\0'``.
        """
            self.object_hook = object_hook
            if not parse_float:
                parse_float
            self.parse_float = float
            if not parse_int:
                parse_int
            self.parse_int = int
            if not parse_constant:
                parse_constant
            self.parse_constant = _CONSTANTS.__getitem__
            self.strict = strict
            self.object_pairs_hook = object_pairs_hook
            self.parse_object = JSONObject
            self.parse_array = JSONArray
            self.parse_string = scanstring
            self.memo = { }
            self.scan_once = scanner.make_scanner(self)

        
        def decode(self, s, _w = (WHITESPACE.match,)):
            '''Return the Python representation of ``s`` (a ``str`` instance
        containing a JSON document).

        '''
            (obj, end) = self.raw_decode(s, idx = _w(s, 0).end())
            end = _w(s, end).end()
            if end != len(s):
                raise JSONDecodeError('Extra data', s, end)
            return obj

        
        def raw_decode(self, s, idx = (0,)):
            '''Decode a JSON document from ``s`` (a ``str`` beginning with
        a JSON document) and return a 2-tuple of the Python
        representation and the index in ``s`` where the document ended.

        This can be used to decode a JSON document from a string that may
        have extraneous data at the end.

        '''
            
            try:
                (obj, end) = self.scan_once(s, idx)
                return (obj, end)
            except StopIteration:
                err = None
                raise JSONDecodeError('Expecting value', s, err.value), None
                err = None
                del err



    return None
except ImportError:
    c_scanstring = None
    continue

