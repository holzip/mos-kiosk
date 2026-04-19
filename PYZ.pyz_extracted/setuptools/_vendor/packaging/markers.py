# Source Generated with Decompyle++
# File: markers.pyc (Python 3.12)

from __future__ import annotations
import operator
import os
import platform
import sys
from typing import Any, Callable, TypedDict, cast
from _parser import MarkerAtom, MarkerList, Op, Value, Variable
from _parser import parse_marker as _parse_marker
from _tokenizer import ParserSyntaxError
from specifiers import InvalidSpecifier, Specifier
from utils import canonicalize_name
__all__ = [
    'InvalidMarker',
    'Marker',
    'UndefinedComparison',
    'UndefinedEnvironmentName',
    'default_environment']
Operator = Callable[([
    str,
    str], bool)]

class InvalidMarker(ValueError):
    '''
    An invalid marker was found, users should refer to PEP 508.
    '''
    pass


class UndefinedComparison(ValueError):
    """
    An invalid operation was attempted on a value that doesn't support it.
    """
    pass


class UndefinedEnvironmentName(ValueError):
    '''
    A name was attempted to be used that does not exist inside of the
    environment.
    '''
    pass


class Environment(TypedDict):
    sys_platform: 'str' = 'Environment'


def _normalize_extra_values(results = None):
    '''
    Normalize extra values.
    '''
    if isinstance(results[0], tuple):
        (lhs, op, rhs) = results[0]
        if isinstance(lhs, Variable) and lhs.value == 'extra':
            normalized_extra = canonicalize_name(rhs.value)
            rhs = Value(normalized_extra)
        elif isinstance(rhs, Variable) and rhs.value == 'extra':
            normalized_extra = canonicalize_name(lhs.value)
            lhs = Value(normalized_extra)
        results[0] = (lhs, op, rhs)
    return results


def _format_marker(marker = None, first = None):
    pass
# WARNING: Decompyle incomplete

_operators: 'dict[str, Operator]' = {
    'in': (lambda lhs, rhs: lhs in rhs),
    'not in': (lambda lhs, rhs: lhs not in rhs),
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt }

def _eval_op(lhs = None, op = None, rhs = None):
    
    try:
        spec = Specifier(''.join([
            op.serialize(),
            rhs]))
        return spec.contains(lhs, prereleases = True)
    except InvalidSpecifier:
        pass

    oper = _operators.get(op.serialize())
# WARNING: Decompyle incomplete


def _normalize(*, key, *values):
    if key == 'extra':
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(values())


def _evaluate_markers(markers = None, environment = None):
    groups = [
        []]
# WARNING: Decompyle incomplete


def format_full_version(info = None):
    version = f'''{info.major}.{info.minor}.{info.micro}'''
    kind = info.releaselevel
    if kind != 'final':
        version += kind[0] + str(info.serial)
    return version


def default_environment():
    iver = format_full_version(sys.implementation.version)
    implementation_name = sys.implementation.name
    return {
        'implementation_name': implementation_name,
        'implementation_version': iver,
        'os_name': os.name,
        'platform_machine': platform.machine(),
        'platform_release': platform.release(),
        'platform_system': platform.system(),
        'platform_version': platform.version(),
        'python_full_version': platform.python_version(),
        'platform_python_implementation': platform.python_implementation(),
        'python_version': '.'.join(platform.python_version_tuple()[:2]),
        'sys_platform': sys.platform }


class Marker:
    
    def __init__(self = None, marker = None):
        
        try:
            self._markers = _normalize_extra_values(_parse_marker(marker))
            return None
        except ParserSyntaxError:
            e = None
            raise InvalidMarker(str(e)), e
            e = None
            del e


    
    def __str__(self = None):
        return _format_marker(self._markers)

    
    def __repr__(self = None):
        return f'''<Marker(\'{self}\')>'''

    
    def __hash__(self = None):
        return hash((self.__class__.__name__, str(self)))

    
    def __eq__(self = None, other = None):
        if not isinstance(other, Marker):
            return NotImplemented
        return None(self) == str(other)

    
    def evaluate(self = None, environment = None):
        '''Evaluate a marker.

        Return the boolean from evaluating the given marker against the
        environment. environment is an optional argument to override all or
        part of the determined environment.

        The environment is determined from the current Python process.
        '''
        current_environment = cast('dict[str, str]', default_environment())
        current_environment['extra'] = ''
    # WARNING: Decompyle incomplete



def _repair_python_full_version(env = None):
    '''
    Work around platform.python_version() returning something that is not PEP 440
    compliant for non-tagged Python builds.
    '''
    if env['python_full_version'].endswith('+'):
        pass
    return env

