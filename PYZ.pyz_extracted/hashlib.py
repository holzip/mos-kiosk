# Source Generated with Decompyle++
# File: hashlib.pyc (Python 3.12)

'''hashlib module - A common interface to many hash functions.

new(name, data=b\'\', **kwargs) - returns a new hash object implementing the
                                given hash function; initializing the hash
                                using the given binary data.

Named constructor functions are also available, these are faster
than using new(name):

md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(),
sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.

More algorithms may be available on your platform but the above are guaranteed
to exist.  See the algorithms_guaranteed and algorithms_available attributes
to find out what algorithm names can be passed to new().

NOTE: If you want the adler32 or crc32 hash functions they are available in
the zlib module.

Choose your hash function wisely.  Some have known collision weaknesses.
sha384 and sha512 will be slow on 32 bit platforms.

Hash objects have these methods:
 - update(data): Update the hash object with the bytes in data. Repeated calls
                 are equivalent to a single call with the concatenation of all
                 the arguments.
 - digest():     Return the digest of the bytes passed to the update() method
                 so far as a bytes object.
 - hexdigest():  Like digest() except the digest is returned as a string
                 of double length, containing only hexadecimal digits.
 - copy():       Return a copy (clone) of the hash object. This can be used to
                 efficiently compute the digests of datas that share a common
                 initial substring.

For example, to obtain the digest of the byte string \'Nobody inspects the
spammish repetition\':

    >>> import hashlib
    >>> m = hashlib.md5()
    >>> m.update(b"Nobody inspects")
    >>> m.update(b" the spammish repetition")
    >>> m.digest()
    b\'\\xbbd\\x9c\\x83\\xdd\\x1e\\xa5\\xc9\\xd9\\xde\\xc9\\xa1\\x8d\\xf0\\xff\\xe9\'

More condensed:

    >>> hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
    \'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2\'

'''
__always_supported = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'blake2s', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'shake_128', 'shake_256')
algorithms_guaranteed = set(__always_supported)
algorithms_available = set(__always_supported)
__all__ = __always_supported + ('new', 'algorithms_guaranteed', 'algorithms_available', 'file_digest')
__builtin_constructor_cache = { }
__block_openssl_constructor = {
    'blake2b',
    'blake2s'}

def __get_builtin_constructor(name):
    cache = __builtin_constructor_cache
    constructor = cache.get(name)
# WARNING: Decompyle incomplete


def __get_openssl_constructor(name):
    if name in __block_openssl_constructor:
        return __get_builtin_constructor(name)
    
    try:
        f = getattr(_hashlib, 'openssl_' + name)
        f(usedforsecurity = False)
        return f
    except (AttributeError, ValueError):
        return 



def __py_new(name, data = (b'',), **kwargs):
    """new(name, data=b'', **kwargs) - Return a new hashing object using the
    named algorithm; optionally initialized with data (which must be
    a bytes-like object).
    """
    pass
# WARNING: Decompyle incomplete


def __hash_new(name, data = (b'',), **kwargs):
    """new(name, data=b'') - Return a new hashing object using the named algorithm;
    optionally initialized with data (which must be a bytes-like object).
    """
    pass
# WARNING: Decompyle incomplete


try:
    import _hashlib
    new = __hash_new
    __get_hash = __get_openssl_constructor
    algorithms_available = algorithms_available.union(_hashlib.openssl_md_meth_names)
    
    try:
        from _hashlib import pbkdf2_hmac
        __all__ += ('pbkdf2_hmac',)
        
        try:
            from _hashlib import scrypt
            
            def file_digest(fileobj = None, digest = {
                '_bufsize': 262144 }, *, _bufsize):
                """Hash the contents of a file-like object. Returns a digest object.

    *fileobj* must be a file-like object opened for reading in binary mode.
    It accepts file objects from open(), io.BytesIO(), and SocketIO objects.
    The function may bypass Python's I/O and use the file descriptor *fileno*
    directly.

    *digest* must either be a hash algorithm name as a *str*, a hash
    constructor, or a callable that returns a hash object.
    """
                if isinstance(digest, str):
                    digestobj = new(digest)
                else:
                    digestobj = digest()
                if hasattr(fileobj, 'getbuffer'):
                    digestobj.update(fileobj.getbuffer())
                    return digestobj
                if not None(fileobj, 'readinto') and hasattr(fileobj, 'readable') or fileobj.readable():
                    raise ValueError(f'''\'{fileobj!r}\' is not a file-like object in binary reading mode.''')
                buf = bytearray(_bufsize)
                view = memoryview(buf)
                size = fileobj.readinto(buf)
                if size == 0:
                    return digestobj
                None.update(view[:size])
                continue

            for __func_name in __always_supported:
                globals()[__func_name] = __get_hash(__func_name)
            del __always_supported
            del __func_name
            del __get_hash
            del __py_new
            del __hash_new
            del __get_openssl_constructor
            return None
            except ImportError:
                _hashlib = None
                new = __py_new
                __get_hash = __get_builtin_constructor
                continue
            except ImportError:
                continue
        except ImportError:
            continue
            except ValueError:
                import logging
                logging.exception('code for hash %s was not found.', __func_name)
                continue



