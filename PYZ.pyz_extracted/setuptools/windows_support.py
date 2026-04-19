# Source Generated with Decompyle++
# File: windows_support.pyc (Python 3.12)

import platform

def windows_only(func):
    if platform.system() != 'Windows':
        return (lambda : pass)

hide_file = (lambda path = None: import ctypesimport ctypes.wintypes as ctypesSetFileAttributes = ctypes.windll.kernel32.SetFileAttributesWSetFileAttributes.argtypes = (ctypes.wintypes.LPWSTR, ctypes.wintypes.DWORD)SetFileAttributes.restype = ctypes.wintypes.BOOLFILE_ATTRIBUTE_HIDDEN = 2ret = SetFileAttributes(path, FILE_ATTRIBUTE_HIDDEN)if not ret:
raise ctypes.WinError())()
