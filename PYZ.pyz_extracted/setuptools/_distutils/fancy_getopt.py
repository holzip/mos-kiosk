# Source Generated with Decompyle++
# File: fancy_getopt.pyc (Python 3.12)

__doc__ = 'distutils.fancy_getopt\n\nWrapper around the standard getopt module that provides the following\nadditional features:\n  * short and long options are tied together\n  * options have help strings, so fancy_getopt could potentially\n    create a complete usage summary\n  * options set attributes of a passed-in object\n'
from __future__ import annotations
import getopt
import re
import string
import sys
from collections.abc import Sequence
from typing import Any
from errors import DistutilsArgError, DistutilsGetoptError
longopt_pat = '[a-zA-Z](?:[a-zA-Z0-9-]*)'
longopt_re = re.compile(f'''^{longopt_pat}$''')
neg_alias_re = re.compile(f'''^({longopt_pat})=!({longopt_pat})$''')
longopt_xlate = str.maketrans('-', '_')

class FancyGetopt:
    '''Wrapper around the standard \'getopt()\' module that provides some
    handy extra functionality:
      * short and long options are tied together
      * options have help strings, and help text can be assembled
        from them
      * options set attributes of a passed-in object
      * boolean options can have "negative aliases" -- eg. if
        --quiet is the "negative alias" of --verbose, then "--quiet"
        on the command line sets \'verbose\' to false
    '''
    
    def __init__(self, option_table = (None,)):
        self.option_table = option_table
        self.option_index = { }
        if self.option_table:
            self._build_index()
        self.alias = { }
        self.negative_alias = { }
        self.short_opts = []
        self.long_opts = []
        self.short2long = { }
        self.attr_name = { }
        self.takes_arg = { }
        self.option_order = []

    
    def _build_index(self):
        self.option_index.clear()
        for option in self.option_table:
            self.option_index[option[0]] = option

    
    def set_option_table(self, option_table):
        self.option_table = option_table
        self._build_index()

    
    def add_option(self, long_option, short_option, help_string = (None, None)):
        if long_option in self.option_index:
            raise DistutilsGetoptError(f'''option conflict: already an option \'{long_option}\'''')
        option = (long_option, short_option, help_string)
        self.option_table.append(option)
        self.option_index[long_option] = option

    
    def has_option(self, long_option):
        """Return true if the option table for this parser has an
        option with long name 'long_option'."""
        return long_option in self.option_index

    
    def get_attr_name(self, long_option):
        """Translate long option name 'long_option' to the form it
        has as an attribute of some object: ie., translate hyphens
        to underscores."""
        return long_option.translate(longopt_xlate)

    
    def _check_alias_dict(self, aliases, what):
        pass
    # WARNING: Decompyle incomplete

    
    def set_aliases(self, alias):
        '''Set the aliases for this option parser.'''
        self._check_alias_dict(alias, 'alias')
        self.alias = alias

    
    def set_negative_aliases(self, negative_alias):
        """Set the negative aliases for this option parser.
        'negative_alias' should be a dictionary mapping option names to
        option names, both the key and value must already be defined
        in the option table."""
        self._check_alias_dict(negative_alias, 'negative alias')
        self.negative_alias = negative_alias

    
    def _grok_option_table(self):
        """Populate the various data structures that keep tabs on the
        option table.  Called by 'getopt()' before it can do anything
        worthwhile.
        """
        self.long_opts = []
        self.short_opts = []
        self.short2long.clear()
        self.repeat = { }
    # WARNING: Decompyle incomplete

    
    def getopt(self = None, args = None, object = None):
        """Parse command-line options in args. Store as attributes on object.

        If 'args' is None or not supplied, uses 'sys.argv[1:]'.  If
        'object' is None or not supplied, creates a new OptionDummy
        object, stores option values there, and returns a tuple (args,
        object).  If 'object' is supplied, it is modified in place and
        'getopt()' just returns 'args'; in both cases, the returned
        'args' is a modified copy of the passed-in 'args' list, which
        is left untouched.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def get_option_order(self):
        """Returns the list of (option, value) tuples processed by the
        previous run of 'getopt()'.  Raises RuntimeError if
        'getopt()' hasn't been called yet.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def generate_help(self, header = (None,)):
        '''Generate help text (a list of strings, one per suggested line of
        output) from the option table for this FancyGetopt object.
        '''
        max_opt = 0
    # WARNING: Decompyle incomplete

    
    def print_help(self, header, file = (None, None)):
        pass
    # WARNING: Decompyle incomplete



def fancy_getopt(options = None, negative_opt = None, object = None, args = ('args', 'Sequence[str] | None')):
    parser = FancyGetopt(options)
    parser.set_negative_aliases(negative_opt)
    return parser.getopt(args, object)

# WARNING: Decompyle incomplete
