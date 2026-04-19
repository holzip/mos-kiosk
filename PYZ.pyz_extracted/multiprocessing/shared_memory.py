# Source Generated with Decompyle++
# File: shared_memory.pyc (Python 3.12)

'''Provides shared memory for direct access across processes.

The API of this package is currently provisional. Refer to the
documentation for details.
'''
__all__ = [
    'SharedMemory',
    'ShareableList']
from functools import partial
import mmap
import os
import errno
import struct
import secrets
import types
if os.name == 'nt':
    import _winapi
    _USE_POSIX = False
else:
    import _posixshmem
    _USE_POSIX = True
from  import resource_tracker
_O_CREX = os.O_CREAT | os.O_EXCL
_SHM_SAFE_NAME_LENGTH = 14
if _USE_POSIX:
    _SHM_NAME_PREFIX = '/psm_'
else:
    _SHM_NAME_PREFIX = 'wnsm_'

def _make_filename():
    '''Create a random filename for the shared memory object.'''
    nbytes = (_SHM_SAFE_NAME_LENGTH - len(_SHM_NAME_PREFIX)) // 2
# WARNING: Decompyle incomplete


class SharedMemory:
    '''Creates a new shared memory block or attaches to an existing
    shared memory block.

    Every shared memory block is assigned a unique name.  This enables
    one process to create a shared memory block with a particular name
    so that a different process can attach to that same shared memory
    block using that same name.

    As a resource for sharing data across processes, shared memory blocks
    may outlive the original process that created them.  When one process
    no longer needs access to a shared memory block that might still be
    needed by other processes, the close() method should be called.
    When a shared memory block is no longer needed by any process, the
    unlink() method should be called to ensure proper cleanup.'''
    _name = None
    _fd = -1
    _mmap = None
    _buf = None
    _flags = os.O_RDWR
    _mode = 384
    _prepend_leading_slash = True if _USE_POSIX else False
    
    def __init__(self, name, create, size = (None, False, 0)):
        if not size >= 0:
            raise ValueError("'size' must be a positive integer")
        if create:
            self._flags = _O_CREX | os.O_RDWR
            if size == 0:
                raise ValueError("'size' must be a positive number different from zero")
    # WARNING: Decompyle incomplete

    
    def __del__(self):
        
        try:
            self.close()
            return None
        except OSError:
            return None


    
    def __reduce__(self):
        return (self.__class__, (self.name, False, self.size))

    
    def __repr__(self):
        return f'''{self.__class__.__name__}({self.name!r}, size={self.size})'''

    buf = (lambda self: self._buf)()
    name = (lambda self: reported_name = self._nameif _USE_POSIX and self._prepend_leading_slash and self._name.startswith('/'):
reported_name = self._name[1:]reported_name)()
    size = (lambda self: self._size)()
    
    def close(self):
        '''Closes access to the shared memory from this instance but does
        not destroy the shared memory block.'''
        pass
    # WARNING: Decompyle incomplete

    
    def unlink(self):
        '''Requests that the underlying shared memory block be destroyed.

        In order to ensure proper cleanup of resources, unlink should be
        called once (and only once) across all processes which have access
        to the shared memory block.'''
        if _USE_POSIX:
            if self._name:
                _posixshmem.shm_unlink(self._name)
                resource_tracker.unregister(self._name, 'shared_memory')
                return None
            return None


_encoding = 'utf8'

class ShareableList:
    '''Pattern for a mutable list-like object shareable via a shared
    memory block.  It differs from the built-in list type in that these
    lists can not change their overall length (i.e. no append, insert,
    etc.)

    Because values are packed into a memoryview as bytes, the struct
    packing format for any storable value must require no more than 8
    characters to describe its format.'''
    _types_mapping = {
        None.__class__: 'xxxxxx?x',
        bytes: '%ds',
        str: '%ds',
        bool: 'xxxxxxx?',
        float: 'd',
        int: 'q' }
    _alignment = 8
    _back_transforms_mapping = {
        0: (lambda value: value),
        1: (lambda value: value.rstrip(b'\x00').decode(_encoding)),
        2: (lambda value: value.rstrip(b'\x00')),
        3: (lambda _value: pass) }
    _extract_recreation_code = (lambda value: if not isinstance(value, (str, bytes, None.__class__)):
0if isinstance(value, str):
1if isinstance(value, bytes):
23)()
    
    def __init__(self = staticmethod, sequence = (None,), *, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_packing_format(self, position):
        '''Gets the packing format for a single value stored in the list.'''
        position = position if position >= 0 else position + self._list_len
        if position >= self._list_len or self._list_len < 0:
            raise IndexError('Requested position out of range.')
        v = struct.unpack_from('8s', self.shm.buf, self._offset_packing_formats + position * 8)[0]
        fmt = v.rstrip(b'\x00')
        fmt_as_str = fmt.decode(_encoding)
        return fmt_as_str

    
    def _get_back_transform(self, position):
        '''Gets the back transformation function for a single value.'''
        if position >= self._list_len or self._list_len < 0:
            raise IndexError('Requested position out of range.')
        transform_code = struct.unpack_from('b', self.shm.buf, self._offset_back_transform_codes + position)[0]
        transform_function = self._back_transforms_mapping[transform_code]
        return transform_function

    
    def _set_packing_format_and_transform(self, position, fmt_as_str, value):
        '''Sets the packing format and back transformation code for a
        single value in the list at the specified position.'''
        if position >= self._list_len or self._list_len < 0:
            raise IndexError('Requested position out of range.')
        struct.pack_into('8s', self.shm.buf, self._offset_packing_formats + position * 8, fmt_as_str.encode(_encoding))
        transform_code = self._extract_recreation_code(value)
        struct.pack_into('b', self.shm.buf, self._offset_back_transform_codes + position, transform_code)

    
    def __getitem__(self, position):
        position = position if position >= 0 else position + self._list_len
        
        try:
            offset = self._offset_data_start + self._allocated_offsets[position]
            (v,) = struct.unpack_from(self._get_packing_format(position), self.shm.buf, offset)
            back_transform = self._get_back_transform(position)
            v = back_transform(v)
            return v
        except IndexError:
            raise IndexError('index out of range')


    
    def __setitem__(self, position, value):
        position = position if position >= 0 else position + self._list_len
        
        try:
            item_offset = self._allocated_offsets[position]
            offset = self._offset_data_start + item_offset
            current_format = self._get_packing_format(position)
            if not isinstance(value, (str, bytes)):
                new_format = self._types_mapping[type(value)]
                encoded_value = value
            else:
                allocated_length = self._allocated_offsets[position + 1] - item_offset
                encoded_value = value.encode(_encoding) if isinstance(value, str) else value
                if len(encoded_value) > allocated_length:
                    raise ValueError('bytes/str item exceeds available storage')
                if current_format[-1] == 's':
                    new_format = current_format
                else:
                    new_format = self._types_mapping[str] % (allocated_length,)
            self._set_packing_format_and_transform(position, new_format, value)
            struct.pack_into(new_format, self.shm.buf, offset, encoded_value)
            return None
        except IndexError:
            raise IndexError('assignment index out of range')


    
    def __reduce__(self):
        return (partial(self.__class__, name = self.shm.name), ())

    
    def __len__(self):
        return struct.unpack_from('q', self.shm.buf, 0)[0]

    
    def __repr__(self):
        return f'''{self.__class__.__name__}({list(self)}, name={self.shm.name!r})'''

    format = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _format_size_metainfo = (lambda self: 'q' * (self._list_len + 1))()
    _format_packing_metainfo = (lambda self: '8s' * self._list_len)()
    _format_back_transform_codes = (lambda self: 'b' * self._list_len)()
    _offset_data_start = (lambda self: (self._list_len + 2) * 8)()
    _offset_packing_formats = (lambda self: self._offset_data_start + self._allocated_offsets[-1])()
    _offset_back_transform_codes = (lambda self: self._offset_packing_formats + self._list_len * 8)()
    
    def count(self, value):
        '''L.count(value) -> integer -- return number of occurrences of value.'''
        pass
    # WARNING: Decompyle incomplete

    
    def index(self, value):
        '''L.index(value) -> integer -- return first index of value.
        Raises ValueError if the value is not present.'''
        for position, entry in enumerate(self):
            if not value == entry:
                continue
            
            return enumerate(self), position
        raise ValueError(f'''{value!r} not in this container''')

    __class_getitem__ = classmethod(types.GenericAlias)

