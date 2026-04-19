# Source Generated with Decompyle++
# File: _compression.pyc (Python 3.12)

'''Internal classes used by the gzip, lzma and bz2 modules'''
import io
import sys
BUFFER_SIZE = io.DEFAULT_BUFFER_SIZE

class BaseStream(io.BufferedIOBase):
    '''Mode-checking helper functions.'''
    
    def _check_not_closed(self):
        if self.closed:
            raise ValueError('I/O operation on closed file')

    
    def _check_can_read(self):
        if not self.readable():
            raise io.UnsupportedOperation('File not open for reading')

    
    def _check_can_write(self):
        if not self.writable():
            raise io.UnsupportedOperation('File not open for writing')

    
    def _check_can_seek(self):
        if not self.readable():
            raise io.UnsupportedOperation('Seeking is only supported on files open for reading')
        if not self.seekable():
            raise io.UnsupportedOperation('The underlying file object does not support seeking')



class DecompressReader(io.RawIOBase):
    pass
# WARNING: Decompyle incomplete

