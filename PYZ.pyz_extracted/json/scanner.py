# Source Generated with Decompyle++
# File: scanner.pyc (Python 3.12)

'''JSON token scanner
'''
import re

try:
    from _json import make_scanner as c_make_scanner
    __all__ = [
        'make_scanner']
    NUMBER_RE = re.compile('(-?(?:0|[1-9][0-9]*))(\\.[0-9]+)?([eE][-+]?[0-9]+)?', re.VERBOSE | re.MULTILINE | re.DOTALL)
    
    def py_make_scanner(context):
        pass
    # WARNING: Decompyle incomplete

    if not c_make_scanner:
        c_make_scanner
    make_scanner = py_make_scanner
    return None
except ImportError:
    c_make_scanner = None
    continue

