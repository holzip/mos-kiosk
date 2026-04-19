# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

import sys
from distutils.command.bdist import bdist
if 'egg' not in bdist.format_commands:
    
    try:
        bdist.format_commands['egg'] = ('bdist_egg', 'Python .egg file')
        del bdist
        del sys
        return None
        del bdist
        del sys
        return None
    except TypeError:
        bdist.format_command['egg'] = ('bdist_egg', 'Python .egg file')
        bdist.format_commands.append('egg')
        del bdist
        del sys
        return None

