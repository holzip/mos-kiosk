# Source Generated with Decompyle++
# File: _sitebuiltins.pyc (Python 3.12)

'''
The objects used by the site module to add custom builtins.
'''
import sys

class Quitter(object):
    
    def __init__(self, name, eof):
        self.name = name
        self.eof = eof

    
    def __repr__(self):
        return f'''Use {self.name!s}() or {self.eof!s} to exit'''

    
    def __call__(self, code = (None,)):
        
        try:
            sys.stdin.close()
            raise SystemExit(code)
        except:
            raise SystemExit(code)




class _Printer(object):
    '''interactive prompt objects for printing the license text, a list of
    contributors and the copyright notice.'''
    MAXLINES = 23
    
    def __init__(self, name, data, files, dirs = ((), ())):
        import os
        self._Printer__name = name
        self._Printer__data = data
        self._Printer__lines = None
    # WARNING: Decompyle incomplete

    
    def _Printer__setup(self):
        if self._Printer__lines:
            return None
        data = None
        for filename in self._Printer__filenames:
            fp = open(filename, encoding = 'utf-8')
            data = fp.read()
            None(None, None)
            self._Printer__filenames
        if not data:
            data = self._Printer__data
        self._Printer__lines = data.split('\n')
        self._Printer__linecnt = len(self._Printer__lines)
        return None
        with None:
            if not None:
                pass
        continue
        except OSError:
            continue

    
    def __repr__(self):
        self._Printer__setup()
        if len(self._Printer__lines) <= self.MAXLINES:
            return '\n'.join(self._Printer__lines)
        return None % (self._Printer__name,) * 2

    
    def __call__(self):
        self._Printer__setup()
        prompt = 'Hit Return for more, or q (and Return) to quit: '
        lineno = 0
    # WARNING: Decompyle incomplete



class _Helper(object):
    """Define the builtin 'help'.

    This is a wrapper around pydoc.help that provides a helpful message
    when 'help' is typed at the Python interactive prompt.

    Calling help() at the Python prompt starts an interactive help session.
    Calling help(thing) prints help for the python object 'thing'.
    """
    
    def __repr__(self):
        return 'Type help() for interactive help, or help(object) for help about object.'

    
    def __call__(self, *args, **kwds):
        import pydoc
    # WARNING: Decompyle incomplete


