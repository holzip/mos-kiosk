# Source Generated with Decompyle++
# File: py38.pyc (Python 3.12)

import sys
if sys.version_info < (3, 9):
    
    def removesuffix(self, suffix):
        if suffix and self.endswith(suffix):
            return self[:-len(suffix)]
        return None[:]

    
    def removeprefix(self, prefix):
        if self.startswith(prefix):
            return self[len(prefix):]
        return None[:]

    return None

def removesuffix(self, suffix):
    return self.removesuffix(suffix)


def removeprefix(self, prefix):
    return self.removeprefix(prefix)

