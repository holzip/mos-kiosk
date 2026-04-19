# Source Generated with Decompyle++
# File: requirements.pyc (Python 3.12)

from typing import Any, Iterator, Optional, Set
from _parser import parse_requirement as _parse_requirement
from _tokenizer import ParserSyntaxError
from markers import Marker, _normalize_extra_values
from specifiers import SpecifierSet
from utils import canonicalize_name

class InvalidRequirement(ValueError):
    '''
    An invalid requirement was found, users should refer to PEP 508.
    '''
    pass


class Requirement:
    '''Parse a requirement.

    Parse a given requirement string into its parts, such as name, specifier,
    URL, and extras. Raises InvalidRequirement on a badly-formed requirement
    string.
    '''
    
    def __init__(self = None, requirement_string = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _iter_parts(self = None, name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        return ''.join(self._iter_parts(self.name))

    
    def __repr__(self = None):
        return f'''<Requirement(\'{self}\')>'''

    
    def __hash__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self = None, other = None):
        if not isinstance(other, Requirement):
            return NotImplemented
        if None(self.name) == canonicalize_name(other.name):
            None(self.name) == canonicalize_name(other.name)
            if self.extras == other.extras:
                self.extras == other.extras
                if self.specifier == other.specifier:
                    self.specifier == other.specifier
                    if self.url == other.url:
                        self.url == other.url
        return self.marker == other.marker


