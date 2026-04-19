# Source Generated with Decompyle++
# File: _elffile.pyc (Python 3.12)

'''
ELF file parser.

This provides a class ``ELFFile`` that parses an ELF executable in a similar
interface to ``ZipFile``. Only the read interface is implemented.

Based on: https://gist.github.com/lyssdod/f51579ae8d93c8657a5564aefc2ffbca
ELF header: https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.eheader.html
'''
from __future__ import annotations
import enum
import os
import struct
from typing import IO

class ELFInvalid(ValueError):
    pass


class EIClass(enum.IntEnum):
    C32 = 1
    C64 = 2


class EIData(enum.IntEnum):
    Lsb = 1
    Msb = 2


class EMachine(enum.IntEnum):
    I386 = 3
    S390 = 22
    Arm = 40
    X8664 = 62
    AArc64 = 183


class ELFFile:
    '''
    Representation of an ELF executable.
    '''
    
    def __init__(self = None, f = None):
        self._f = f
        
        try:
            ident = self._read('16B')
            magic = bytes(ident[:4])
            if magic != b'\x7fELF':
                raise ELFInvalid(f'''invalid magic: {magic!r}''')
            self.capacity = ident[4]
            self.encoding = ident[5]
            
            try:
                (e_fmt, self._p_fmt, self._p_idx) = {
                    (1, 1): ('<HHIIIIIHHH', '<IIIIIIII', (0, 1, 4)),
                    (1, 2): ('>HHIIIIIHHH', '>IIIIIIII', (0, 1, 4)),
                    (2, 1): ('<HHIQQQIHHH', '<IIQQQQQQ', (0, 2, 5)),
                    (2, 2): ('>HHIQQQIHHH', '>IIQQQQQQ', (0, 2, 5)) }[(self.capacity, self.encoding)]
                
                try:
                    (_, self.machine, _, _, self._e_phoff, _, self.flags, _, self._e_phentsize, self._e_phnum) = self._read(e_fmt)
                    return None
                    except struct.error:
                        e = None
                        raise ELFInvalid('unable to parse identification'), e
                        e = None
                        del e
                    except KeyError:
                        e = None
                        raise ELFInvalid(f'''unrecognized capacity ({self.capacity}) or encoding ({self.encoding})'''), e
                        e = None
                        del e
                except struct.error:
                    e = None
                    raise ELFInvalid('unable to parse machine and section information'), e
                    e = None
                    del e




    
    def _read(self = None, fmt = None):
        return struct.unpack(fmt, self._f.read(struct.calcsize(fmt)))

    interpreter = (lambda self = None: for index in range(self._e_phnum):
self._f.seek(self._e_phoff + self._e_phentsize * index)data = self._read(self._p_fmt)if data[self._p_idx[0]] != 3:
continueself._f.seek(data[self._p_idx[1]])range(self._e_phnum), os.fsdecode(self._f.read(data[self._p_idx[2]])).strip('\x00')Noneexcept struct.error:
continue)()

