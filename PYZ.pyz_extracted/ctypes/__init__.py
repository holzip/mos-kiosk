# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

'''create and manipulate C data types in Python'''
import os as _os
import sys as _sys
import types as _types
__version__ = '1.1.0'
from _ctypes import Union, Structure, Array
from _ctypes import _Pointer
from _ctypes import CFuncPtr as _CFuncPtr
from _ctypes import __version__ as _ctypes_version
from _ctypes import RTLD_LOCAL, RTLD_GLOBAL
from _ctypes import ArgumentError
from _ctypes import SIZEOF_TIME_T
from struct import calcsize as _calcsize
if __version__ != _ctypes_version:
    raise Exception('Version number mismatch', __version__, _ctypes_version)
if _os.name == 'nt':
    from _ctypes import FormatError
DEFAULT_MODE = RTLD_LOCAL
if _os.name == 'posix' and _sys.platform == 'darwin' and int(_os.uname().release.split('.')[0]) < 8:
    DEFAULT_MODE = RTLD_GLOBAL
from _ctypes import FUNCFLAG_CDECL as _FUNCFLAG_CDECL, FUNCFLAG_PYTHONAPI as _FUNCFLAG_PYTHONAPI, FUNCFLAG_USE_ERRNO as _FUNCFLAG_USE_ERRNO, FUNCFLAG_USE_LASTERROR as _FUNCFLAG_USE_LASTERROR

def create_string_buffer(init, size = (None,)):
    '''create_string_buffer(aBytes) -> character array
    create_string_buffer(anInteger) -> character array
    create_string_buffer(aBytes, anInteger) -> character array
    '''
    pass
# WARNING: Decompyle incomplete

c_buffer = create_string_buffer
_c_functype_cache = { }

def CFUNCTYPE(restype, *argtypes, **kw):
    '''CFUNCTYPE(restype, *argtypes,
                 use_errno=False, use_last_error=False) -> function prototype.

    restype: the result type
    argtypes: a sequence specifying the argument types

    The function prototype can be called in different ways to create a
    callable object:

    prototype(integer address) -> foreign function
    prototype(callable) -> create and return a C callable function from callable
    prototype(integer index, method name[, paramflags]) -> foreign function calling a COM method
    prototype((ordinal number, dll object)[, paramflags]) -> foreign function exported by ordinal
    prototype((function name, dll object)[, paramflags]) -> foreign function exported by name
    '''
    pass
# WARNING: Decompyle incomplete

if _os.name == 'nt':
    from _ctypes import LoadLibrary as _dlopen
    from _ctypes import FUNCFLAG_STDCALL as _FUNCFLAG_STDCALL
    _win_functype_cache = { }
    
    def WINFUNCTYPE(restype, *argtypes, **kw):
        pass
    # WARNING: Decompyle incomplete

    if WINFUNCTYPE.__doc__:
        WINFUNCTYPE.__doc__ = CFUNCTYPE.__doc__.replace('CFUNCTYPE', 'WINFUNCTYPE')
    elif _os.name == 'posix':
        from _ctypes import dlopen as _dlopen
from _ctypes import sizeof, byref, addressof, alignment, resize
from _ctypes import get_errno, set_errno
from _ctypes import _SimpleCData

def _check_size(typ, typecode = (None,)):
    calcsize = calcsize
    import struct
# WARNING: Decompyle incomplete


class py_object(_SimpleCData):
    pass
# WARNING: Decompyle incomplete

_check_size(py_object, 'P')

class c_short(_SimpleCData):
    _type_ = 'h'

_check_size(c_short)

class c_ushort(_SimpleCData):
    _type_ = 'H'

_check_size(c_ushort)

class c_long(_SimpleCData):
    _type_ = 'l'

_check_size(c_long)

class c_ulong(_SimpleCData):
    _type_ = 'L'

_check_size(c_ulong)

class c_float(_SimpleCData):
    _type_ = 'f'

_check_size(c_float)

class c_double(_SimpleCData):
    _type_ = 'd'

_check_size(c_double)

class c_longdouble(_SimpleCData):
    _type_ = 'g'

if sizeof(c_longdouble) == sizeof(c_double):
    c_longdouble = c_double

class c_ubyte(_SimpleCData):
    _type_ = 'B'

c_ubyte.__ctype_le__ = c_ubyte
c_ubyte.__ctype_be__ = c_ubyte
_check_size(c_ubyte)

class c_byte(_SimpleCData):
    _type_ = 'b'

c_byte.__ctype_le__ = c_byte
c_byte.__ctype_be__ = c_byte
_check_size(c_byte)

class c_char(_SimpleCData):
    _type_ = 'c'

c_char.__ctype_le__ = c_char
c_char.__ctype_be__ = c_char
_check_size(c_char)

class c_char_p(_SimpleCData):
    _type_ = 'z'
    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({c_void_p.from_buffer(self).value!s})'''


_check_size(c_char_p, 'P')

class c_void_p(_SimpleCData):
    _type_ = 'P'

c_voidp = c_void_p
_check_size(c_void_p)

class c_bool(_SimpleCData):
    _type_ = '?'

from _ctypes import POINTER, pointer, _pointer_type_cache

class c_wchar_p(_SimpleCData):
    _type_ = 'Z'
    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({c_void_p.from_buffer(self).value!s})'''



class c_wchar(_SimpleCData):
    _type_ = 'u'


def _reset_cache():
    _pointer_type_cache.clear()
    _c_functype_cache.clear()
    if _os.name == 'nt':
        _win_functype_cache.clear()
    POINTER(c_wchar).from_param = c_wchar_p.from_param
    POINTER(c_char).from_param = c_char_p.from_param
    _pointer_type_cache[None] = c_void_p


def create_unicode_buffer(init, size = (None,)):
    '''create_unicode_buffer(aString) -> character array
    create_unicode_buffer(anInteger) -> character array
    create_unicode_buffer(aString, anInteger) -> character array
    '''
    pass
# WARNING: Decompyle incomplete


def SetPointerType(pointer, cls):
    pass
# WARNING: Decompyle incomplete


def ARRAY(typ, len):
    return typ * len


class CDLL(object):
    """An instance of this class represents a loaded dll/shared
    library, exporting functions using the standard C calling
    convention (named 'cdecl' on Windows).

    The exported functions can be accessed as attributes, or by
    indexing with the function name.  Examples:

    <obj>.qsort -> callable object
    <obj>['qsort'] -> callable object

    Calling the functions releases the Python GIL during the call and
    reacquires it afterwards.
    """
    _func_flags_ = _FUNCFLAG_CDECL
    _func_restype_ = c_int
    _name = '<uninitialized>'
    _handle = 0
    _FuncPtr = None
    
    def __init__(self, name, mode, handle, use_errno, use_last_error, winmode = (DEFAULT_MODE, None, False, False, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return "<%s '%s', handle %x at %#x>" % (self.__class__.__name__, self._name, self._handle & _sys.maxsize * 2 + 1, id(self) & _sys.maxsize * 2 + 1)

    
    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            raise AttributeError(name)
        func = self.__getitem__(name)
        setattr(self, name, func)
        return func

    
    def __getitem__(self, name_or_ordinal):
        func = self._FuncPtr((name_or_ordinal, self))
        if not isinstance(name_or_ordinal, int):
            func.__name__ = name_or_ordinal
        return func



class PyDLL(CDLL):
    '''This class represents the Python library itself.  It allows
    accessing Python API functions.  The GIL is not released, and
    Python exceptions are handled correctly.
    '''
    _func_flags_ = _FUNCFLAG_CDECL | _FUNCFLAG_PYTHONAPI

if _os.name == 'nt':
    
    class WinDLL(CDLL):
        '''This class represents a dll exporting functions using the
        Windows stdcall calling convention.
        '''
        _func_flags_ = _FUNCFLAG_STDCALL

    from _ctypes import _check_HRESULT, _SimpleCData
    
    class HRESULT(_SimpleCData):
        _type_ = 'l'
        _check_retval_ = _check_HRESULT

    
    class OleDLL(CDLL):
        '''This class represents a dll exporting functions using the
        Windows stdcall calling convention, and returning HRESULT.
        HRESULT error values are automatically raised as OSError
        exceptions.
        '''
        _func_flags_ = _FUNCFLAG_STDCALL
        _func_restype_ = HRESULT


class LibraryLoader(object):
    
    def __init__(self, dlltype):
        self._dlltype = dlltype

    
    def __getattr__(self, name):
        if name[0] == '_':
            raise AttributeError(name)
        
        try:
            dll = self._dlltype(name)
            setattr(self, name, dll)
            return dll
        except OSError:
            raise AttributeError(name)


    
    def __getitem__(self, name):
        return getattr(self, name)

    
    def LoadLibrary(self, name):
        return self._dlltype(name)

    __class_getitem__ = classmethod(_types.GenericAlias)

cdll = LibraryLoader(CDLL)
pydll = LibraryLoader(PyDLL)
if _os.name == 'nt':
    pythonapi = PyDLL('python dll', None, _sys.dllhandle)
elif _sys.platform == 'cygwin':
    pythonapi = PyDLL('libpython%d.%d.dll' % _sys.version_info[:2])
else:
    pythonapi = PyDLL(None)
if _os.name == 'nt':
    windll = LibraryLoader(WinDLL)
    oledll = LibraryLoader(OleDLL)
    GetLastError = windll.kernel32.GetLastError
    from _ctypes import get_last_error, set_last_error
    
    def WinError(code, descr = (None, None)):
        pass
    # WARNING: Decompyle incomplete

if sizeof(c_uint) == sizeof(c_void_p):
    c_size_t = c_uint
    c_ssize_t = c_int
elif sizeof(c_ulong) == sizeof(c_void_p):
    c_size_t = c_ulong
    c_ssize_t = c_long
elif sizeof(c_ulonglong) == sizeof(c_void_p):
    c_size_t = c_ulonglong
    c_ssize_t = c_longlong
from _ctypes import _memmove_addr, _memset_addr, _string_at_addr, _cast_addr
memmove = CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_size_t)(_memmove_addr)
memset = CFUNCTYPE(c_void_p, c_void_p, c_int, c_size_t)(_memset_addr)

def PYFUNCTYPE(restype, *argtypes):
    pass
# WARNING: Decompyle incomplete

_cast = PYFUNCTYPE(py_object, c_void_p, py_object, py_object)(_cast_addr)

def cast(obj, typ):
    return _cast(obj, obj, typ)

_string_at = PYFUNCTYPE(py_object, c_void_p, c_int)(_string_at_addr)

def string_at(ptr, size = (-1,)):
    '''string_at(ptr[, size]) -> string

    Return the byte string at void *ptr.'''
    return _string_at(ptr, size)


try:
    from _ctypes import _wstring_at_addr
    _wstring_at = PYFUNCTYPE(py_object, c_void_p, c_int)(_wstring_at_addr)
    
    def wstring_at(ptr, size = (-1,)):
        '''wstring_at(ptr[, size]) -> string

        Return the wide-character string at void *ptr.'''
        return _wstring_at(ptr, size)

    if _os.name == 'nt':
        
        def DllGetClassObject(rclsid, riid, ppv):
            
            try:
                ccom = __import__('comtypes.server.inprocserver', globals(), locals(), [
                    '*'])
                return ccom.DllGetClassObject(rclsid, riid, ppv)
            except ImportError:
                return -2147221231


        
        def DllCanUnloadNow():
            
            try:
                ccom = __import__('comtypes.server.inprocserver', globals(), locals(), [
                    '*'])
                return ccom.DllCanUnloadNow()
            except ImportError:
                return 0


    from ctypes._endian import BigEndianStructure, LittleEndianStructure
    from ctypes._endian import BigEndianUnion, LittleEndianUnion
    c_int8 = c_byte
    c_uint8 = c_ubyte
    for kind in (c_short, c_int, c_long, c_longlong):
        if sizeof(kind) == 2:
            c_int16 = kind
            continue
        if sizeof(kind) == 4:
            c_int32 = kind
            continue
        if not sizeof(kind) == 8:
            continue
        c_int64 = kind
    for kind in (c_ushort, c_uint, c_ulong, c_ulonglong):
        if sizeof(kind) == 2:
            c_uint16 = kind
            continue
        if sizeof(kind) == 4:
            c_uint32 = kind
            continue
        if not sizeof(kind) == 8:
            continue
        c_uint64 = kind
    del kind
    if SIZEOF_TIME_T == 8:
        c_time_t = c_int64
    elif SIZEOF_TIME_T == 4:
        c_time_t = c_int32
    else:
        raise SystemError(f'''Unexpected sizeof(time_t): SIZEOF_TIME_T={SIZEOF_TIME_T!r}''')
    _reset_cache()
    return None
except ImportError:
    continue

