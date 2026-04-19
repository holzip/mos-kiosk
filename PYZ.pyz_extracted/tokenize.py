# Source Generated with Decompyle++
# File: tokenize.pyc (Python 3.12)

__doc__ = 'Tokenization help for Python programs.\n\ntokenize(readline) is a generator that breaks a stream of bytes into\nPython tokens.  It decodes the bytes according to PEP-0263 for\ndetermining source file encoding.\n\nIt accepts a readline-like method which is called repeatedly to get the\nnext line of input (or b"" for EOF).  It generates 5-tuples with these\nmembers:\n\n    the token type (see token.py)\n    the token (a string)\n    the starting (row, column) indices of the token (a 2-tuple of ints)\n    the ending (row, column) indices of the token (a 2-tuple of ints)\n    the original line (string)\n\nIt is designed to match the working of the Python tokenizer exactly, except\nthat it produces COMMENT tokens for comments and gives type OP for all\noperators.  Additionally, all token lists start with an ENCODING token\nwhich tells you which encoding was used to decode the bytes stream.\n'
__author__ = 'Ka-Ping Yee <ping@lfw.org>'
__credits__ = 'GvR, ESR, Tim Peters, Thomas Wouters, Fred Drake, Skip Montanaro, Raymond Hettinger, Trent Nelson, Michael Foord'
from builtins import open as _builtin_open
from codecs import lookup, BOM_UTF8
import collections
import functools
from io import TextIOWrapper
import itertools as _itertools
import re
import sys
# WARNING: Decompyle incomplete
