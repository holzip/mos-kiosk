# Source Generated with Decompyle++
# File: errors.pyc (Python 3.12)


class Error(Exception):
    '''Some compile/link operation failed.'''
    pass


class PreprocessError(Error):
    '''Failure to preprocess one or more C/C++ files.'''
    pass


class CompileError(Error):
    '''Failure to compile one or more C/C++ source files.'''
    pass


class LibError(Error):
    '''Failure to create a static library from one or more C/C++ object
    files.'''
    pass


class LinkError(Error):
    '''Failure to link one or more C/C++ object files into an executable
    or shared library file.'''
    pass


class UnknownFileType(Error):
    '''Attempt to process an unknown file type.'''
    pass

