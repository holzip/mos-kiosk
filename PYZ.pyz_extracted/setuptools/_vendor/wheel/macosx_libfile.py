# Source Generated with Decompyle++
# File: macosx_libfile.pyc (Python 3.12)

'''
This module contains function to analyse dynamic library
headers to extract system information

Currently only for MacOSX

Library file on macosx system starts with Mach-O or Fat field.
This can be distinguish by first 32 bites and it is called magic number.
Proper value of magic number is with suffix _MAGIC. Suffix _CIGAM means
reversed bytes order.
Both fields can occur in two types: 32 and 64 bytes.

FAT field inform that this library contains few version of library
(typically for different types version). It contains
information where Mach-O headers starts.

Each section started with Mach-O header contains one library
(So if file starts with this field it contains only one version).

After filed Mach-O there are section fields.
Each of them starts with two fields:
cmd - magic number for this command
cmdsize - total size occupied by this section information.

In this case only sections LC_VERSION_MIN_MACOSX (for macosx 10.13 and earlier)
and LC_BUILD_VERSION (for macosx 10.14 and newer) are interesting,
because them contains information about minimal system version.

Important remarks:
- For fat files this implementation looks for maximum number version.
  It not check if it is 32 or 64 and do not compare it with currently built package.
  So it is possible to false report higher version that needed.
- All structures signatures are taken form macosx header files.
- I think that binary format will be more stable than `otool` output.
  and if apple introduce some changes both implementation will need to be updated.
- The system compile will set the deployment target no lower than
  11.0 for arm64 builds. For "Universal 2" builds use the x86_64 deployment
  target when the arm64 target is 11.0.
'''
from __future__ import annotations
import ctypes
import os
import sys
FAT_MAGIC = 0xCAFEBABE
FAT_CIGAM = 0xBEBAFECA
FAT_MAGIC_64 = 0xCAFEBABF
FAT_CIGAM_64 = 0xBFBAFECA
MH_MAGIC = 0xFEEDFACE
MH_CIGAM = 0xCEFAEDFE
MH_MAGIC_64 = 0xFEEDFACF
MH_CIGAM_64 = 0xCFFAEDFE
LC_VERSION_MIN_MACOSX = 36
LC_BUILD_VERSION = 50
CPU_TYPE_ARM64 = 16777228
mach_header_fields = [
    ('magic', ctypes.c_uint32),
    ('cputype', ctypes.c_int),
    ('cpusubtype', ctypes.c_int),
    ('filetype', ctypes.c_uint32),
    ('ncmds', ctypes.c_uint32),
    ('sizeofcmds', ctypes.c_uint32),
    ('flags', ctypes.c_uint32)]
mach_header_fields_64 = mach_header_fields + [
    ('reserved', ctypes.c_uint32)]
fat_header_fields = [
    ('magic', ctypes.c_uint32),
    ('nfat_arch', ctypes.c_uint32)]
fat_arch_fields = [
    ('cputype', ctypes.c_int),
    ('cpusubtype', ctypes.c_int),
    ('offset', ctypes.c_uint32),
    ('size', ctypes.c_uint32),
    ('align', ctypes.c_uint32)]
fat_arch_64_fields = [
    ('cputype', ctypes.c_int),
    ('cpusubtype', ctypes.c_int),
    ('offset', ctypes.c_uint64),
    ('size', ctypes.c_uint64),
    ('align', ctypes.c_uint32),
    ('reserved', ctypes.c_uint32)]
segment_base_fields = [
    ('cmd', ctypes.c_uint32),
    ('cmdsize', ctypes.c_uint32)]
segment_command_fields = [
    ('cmd', ctypes.c_uint32),
    ('cmdsize', ctypes.c_uint32),
    ('segname', ctypes.c_char * 16),
    ('vmaddr', ctypes.c_uint32),
    ('vmsize', ctypes.c_uint32),
    ('fileoff', ctypes.c_uint32),
    ('filesize', ctypes.c_uint32),
    ('maxprot', ctypes.c_int),
    ('initprot', ctypes.c_int),
    ('nsects', ctypes.c_uint32),
    ('flags', ctypes.c_uint32)]
segment_command_fields_64 = [
    ('cmd', ctypes.c_uint32),
    ('cmdsize', ctypes.c_uint32),
    ('segname', ctypes.c_char * 16),
    ('vmaddr', ctypes.c_uint64),
    ('vmsize', ctypes.c_uint64),
    ('fileoff', ctypes.c_uint64),
    ('filesize', ctypes.c_uint64),
    ('maxprot', ctypes.c_int),
    ('initprot', ctypes.c_int),
    ('nsects', ctypes.c_uint32),
    ('flags', ctypes.c_uint32)]
version_min_command_fields = segment_base_fields + [
    ('version', ctypes.c_uint32),
    ('sdk', ctypes.c_uint32)]
build_version_command_fields = segment_base_fields + [
    ('platform', ctypes.c_uint32),
    ('minos', ctypes.c_uint32),
    ('sdk', ctypes.c_uint32),
    ('ntools', ctypes.c_uint32)]

def swap32(x):
    return x << 24 & 0xFF000000 | x << 8 & 16711680 | x >> 8 & 65280 | x >> 24 & 255


def get_base_class_and_magic_number(lib_file, seek = (None,)):
    pass
# WARNING: Decompyle incomplete


def read_data(struct_class, lib_file):
    return struct_class.from_buffer_copy(lib_file.read(ctypes.sizeof(struct_class)))


def extract_macosx_min_system_version(path_to_lib):
    lib_file = open(path_to_lib, 'rb')
    (BaseClass, magic_number) = get_base_class_and_magic_number(lib_file, 0)
    if magic_number not in (FAT_MAGIC, FAT_MAGIC_64, MH_MAGIC, MH_MAGIC_64):
        None(None, None)
        return None
# WARNING: Decompyle incomplete


def read_mach_header(lib_file, seek = (None,)):
    '''
    This function parses a Mach-O header and extracts
    information about the minimal macOS version.

    :param lib_file: reference to opened library file with pointer
    '''
    (base_class, magic_number) = get_base_class_and_magic_number(lib_file, seek)
    arch = '32' if magic_number == MH_MAGIC else '64'
    
    class SegmentBase(base_class):
        _fields_ = segment_base_fields

    mach_header = read_data(MachHeader, lib_file)
    for _i in range(mach_header.ncmds):
        pos = lib_file.tell()
        segment_base = read_data(SegmentBase, lib_file)
        lib_file.seek(pos)
        if segment_base.cmd == LC_VERSION_MIN_MACOSX:
            
            class VersionMinCommand(base_class):
                _fields_ = version_min_command_fields

            version_info = read_data(VersionMinCommand, lib_file)
            
            return None, parse_version(version_info.version)
        if range(mach_header.ncmds).cmd == LC_BUILD_VERSION:
            
            class read_data(VersionBuild, lib_file)(base_class):
                _fields_ = build_version_command_fields

            
            return None, parse_version(version_info.minos)
        None if arch == '32' else None.seek(pos + segment_base.cmdsize)


def parse_version(version):
    x = (version & 0xFFFF0000) >> 16
    y = (version & 65280) >> 8
    z = version & 255
    return (x, y, z)


def calculate_macosx_platform_tag(archive_root, platform_tag):
    '''
    Calculate proper macosx platform tag basing on files which are included to wheel

    Example platform tag `macosx-10.14-x86_64`
    '''
    (prefix, base_version, suffix) = platform_tag.split('-')
    base_version = (lambda .0: pass# WARNING: Decompyle incomplete
)(base_version.split('.')())
    base_version = base_version[:2]
    if base_version[0] > 10:
        base_version = (base_version[0], 0)
# WARNING: Decompyle incomplete

