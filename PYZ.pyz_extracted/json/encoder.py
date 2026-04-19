# Source Generated with Decompyle++
# File: encoder.pyc (Python 3.12)

'''Implementation of JSONEncoder
'''
import re

try:
    from _json import encode_basestring_ascii as c_encode_basestring_ascii
    
    try:
        from _json import encode_basestring as c_encode_basestring
        
        try:
            from _json import make_encoder as c_make_encoder
            ESCAPE = re.compile('[\\x00-\\x1f\\\\"\\b\\f\\n\\r\\t]')
            ESCAPE_ASCII = re.compile('([\\\\"]|[^\\ -~])')
            HAS_UTF8 = re.compile(b'[\x80-\xff]')
            ESCAPE_DCT = {
                '\\': '\\\\',
                '"': '\\"',
                '\x08': '\\b',
                '\x0c': '\\f',
                '\n': '\\n',
                '\r': '\\r',
                '\t': '\\t' }
            for i in range(32):
                ESCAPE_DCT.setdefault(chr(i), '\\u{0:04x}'.format(i))
            del i
            INFINITY = float('inf')
            
            def py_encode_basestring(s):
                '''Return a JSON representation of a Python string

    '''
                
                def replace(match):
                    return ESCAPE_DCT[match.group(0)]

                return '"' + ESCAPE.sub(replace, s) + '"'

            if not c_encode_basestring:
                c_encode_basestring
            encode_basestring = py_encode_basestring
            
            def py_encode_basestring_ascii(s):
                '''Return an ASCII-only JSON representation of a Python string

    '''
                
                def replace(match):
                    s = match.group(0)
                    
                    try:
                        return ESCAPE_DCT[s]
                    except KeyError:
                        n = ord(s)
                        if n < 65536:
                            return 
                        None -= 65536
                        s2 = 56320 | n & 1023
                        return 


                return '"' + ESCAPE_ASCII.sub(replace, s) + '"'

            if not c_encode_basestring_ascii:
                c_encode_basestring_ascii
            encode_basestring_ascii = py_encode_basestring_ascii
            
            class JSONEncoder(object):
                '''Extensible JSON <https://json.org> encoder for Python data structures.

    Supports the following objects and types by default:

    +-------------------+---------------+
    | Python            | JSON          |
    +===================+===============+
    | dict              | object        |
    +-------------------+---------------+
    | list, tuple       | array         |
    +-------------------+---------------+
    | str               | string        |
    +-------------------+---------------+
    | int, float        | number        |
    +-------------------+---------------+
    | True              | true          |
    +-------------------+---------------+
    | False             | false         |
    +-------------------+---------------+
    | None              | null          |
    +-------------------+---------------+

    To extend this to recognize other objects, subclass and implement a
    ``.default()`` method with another method that returns a serializable
    object for ``o`` if possible, otherwise it should call the superclass
    implementation (to raise ``TypeError``).

    '''
                item_separator = ', '
                key_separator = ': '
                
                def __init__(self = None, *, skipkeys, ensure_ascii, check_circular, allow_nan, sort_keys, indent, separators, default):
                    """Constructor for JSONEncoder, with sensible defaults.

        If skipkeys is false, then it is a TypeError to attempt
        encoding of keys that are not str, int, float, bool or None.
        If skipkeys is True, such items are simply skipped.

        If ensure_ascii is true, the output is guaranteed to be str
        objects with all incoming non-ASCII characters escaped.  If
        ensure_ascii is false, the output can contain non-ASCII characters.

        If check_circular is true, then lists, dicts, and custom encoded
        objects will be checked for circular references during encoding to
        prevent an infinite recursion (which would cause an RecursionError).
        Otherwise, no such check takes place.

        If allow_nan is true, then NaN, Infinity, and -Infinity will be
        encoded as such.  This behavior is not JSON specification compliant,
        but is consistent with most JavaScript based encoders and decoders.
        Otherwise, it will be a ValueError to encode such floats.

        If sort_keys is true, then the output of dictionaries will be
        sorted by key; this is useful for regression tests to ensure
        that JSON serializations can be compared on a day-to-day basis.

        If indent is a non-negative integer, then JSON array
        elements and object members will be pretty-printed with that
        indent level.  An indent level of 0 will only insert newlines.
        None is the most compact representation.

        If specified, separators should be an (item_separator, key_separator)
        tuple.  The default is (', ', ': ') if *indent* is ``None`` and
        (',', ': ') otherwise.  To get the most compact JSON representation,
        you should specify (',', ':') to eliminate whitespace.

        If specified, default is a function that gets called for objects
        that can't otherwise be serialized.  It should return a JSON encodable
        version of the object or raise a ``TypeError``.

        """
                    self.skipkeys = skipkeys
                    self.ensure_ascii = ensure_ascii
                    self.check_circular = check_circular
                    self.allow_nan = allow_nan
                    self.sort_keys = sort_keys
                    self.indent = indent
                # WARNING: Decompyle incomplete

                
                def default(self, o):
                    '''Implement this method in a subclass such that it returns
        a serializable object for ``o``, or calls the base implementation
        (to raise a ``TypeError``).

        For example, to support arbitrary iterators, you could
        implement default like this::

            def default(self, o):
                try:
                    iterable = iter(o)
                except TypeError:
                    pass
                else:
                    return list(iterable)
                # Let the base class default method raise the TypeError
                return super().default(o)

        '''
                    raise TypeError(f'''Object of type {o.__class__.__name__} is not JSON serializable''')

                
                def encode(self, o):
                    '''Return a JSON string representation of a Python data structure.

        >>> from json.encoder import JSONEncoder
        >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
        \'{"foo": ["bar", "baz"]}\'

        '''
                    if isinstance(o, str):
                        if self.ensure_ascii:
                            return encode_basestring_ascii(o)
                        return None(o)
                    chunks = None.iterencode(o, _one_shot = True)
                    if not isinstance(chunks, (list, tuple)):
                        chunks = list(chunks)
                    return ''.join(chunks)

                
                def iterencode(self, o, _one_shot = (False,)):
                    '''Encode the given object and yield each string
        representation as available.

        For example::

            for chunk in JSONEncoder().iterencode(bigobject):
                mysocket.write(chunk)

        '''
                    if self.check_circular:
                        markers = { }
                    else:
                        markers = None
                    if self.ensure_ascii:
                        _encoder = encode_basestring_ascii
                    else:
                        _encoder = encode_basestring
                    
                    def floatstr(o, allow_nan, _repr, _inf, _neginf = (self.allow_nan, float.__repr__, INFINITY, -INFINITY)):
                        if o != o:
                            text = 'NaN'
                        elif o == _inf:
                            text = 'Infinity'
                        elif o == _neginf:
                            text = '-Infinity'
                        else:
                            return _repr(o)
                        if not None:
                            raise ValueError('Out of range float values are not JSON compliant: ' + repr(o))
                        return text

                # WARNING: Decompyle incomplete


            
            def _make_iterencode(markers, _default, _encoder, _indent, _floatstr, _key_separator, _item_separator, _sort_keys, _skipkeys, _one_shot, ValueError, dict, float, id, int, isinstance, list, str, tuple, _intstr = (ValueError, dict, float, id, int, isinstance, list, str, tuple, int.__repr__)):
                pass
            # WARNING: Decompyle incomplete

            return None
            except ImportError:
                c_encode_basestring_ascii = None
                continue
            except ImportError:
                c_encode_basestring = None
                continue
        except ImportError:
            c_make_encoder = None
            continue



