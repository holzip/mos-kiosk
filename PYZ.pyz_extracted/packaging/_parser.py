# Source Generated with Decompyle++
# File: _parser.pyc (Python 3.12)

'''Handwritten parser of dependency specifiers.

The docstring for each __parse_* function contains EBNF-inspired grammar representing
the implementation.
'''
from __future__ import annotations
import ast
from typing import List, Literal, NamedTuple, Sequence, Tuple, Union
from _tokenizer import DEFAULT_RULES, Tokenizer

class Node:
    __slots__ = ('value',)
    
    def __init__(self = None, value = None):
        self.value = value

    
    def __str__(self = None):
        return self.value

    
    def __repr__(self = None):
        return f'''<{self.__class__.__name__}({self.value!r})>'''

    
    def serialize(self = None):
        raise NotImplementedError



class Variable(Node):
    __slots__ = ()
    
    def serialize(self = None):
        return str(self)



class Value(Node):
    __slots__ = ()
    
    def serialize(self = None):
        return f'''"{self}"'''



class Op(Node):
    __slots__ = ()
    
    def serialize(self = None):
        return str(self)


MarkerLogical = Literal[('and', 'or')]
MarkerVar = Union[(Variable, Value)]
MarkerItem = Tuple[(MarkerVar, Op, MarkerVar)]
MarkerAtom = Union[(MarkerItem, Sequence['MarkerAtom'])]
MarkerList = List[Union[('MarkerList', MarkerAtom, MarkerLogical)]]

class ParsedRequirement(NamedTuple):
    marker: 'MarkerList | None' = 'ParsedRequirement'


def parse_requirement(source = None):
    return _parse_requirement(Tokenizer(source, rules = DEFAULT_RULES))


def _parse_requirement(tokenizer = None):
    '''
    requirement = WS? IDENTIFIER WS? extras WS? requirement_details
    '''
    tokenizer.consume('WS')
    name_token = tokenizer.expect('IDENTIFIER', expected = 'package name at the start of dependency specifier')
    name = name_token.text
    tokenizer.consume('WS')
    extras = _parse_extras(tokenizer)
    tokenizer.consume('WS')
    (url, specifier, marker) = _parse_requirement_details(tokenizer)
    tokenizer.expect('END', expected = 'end of dependency specifier')
    return ParsedRequirement(name, url, extras, specifier, marker)


def _parse_requirement_details(tokenizer = None):
    '''
    requirement_details = AT URL (WS requirement_marker?)?
                        | specifier WS? (requirement_marker)?
    '''
    specifier = ''
    url = ''
    marker = None
    if tokenizer.check('AT'):
        tokenizer.read()
        tokenizer.consume('WS')
        url_start = tokenizer.position
        url = tokenizer.expect('URL', expected = 'URL after @').text
        if tokenizer.check('END', peek = True):
            return (url, specifier, marker)
        None.expect('WS', expected = 'whitespace after URL')
        if tokenizer.check('END', peek = True):
            return (url, specifier, marker)
        marker = None(tokenizer, span_start = url_start, expected = 'semicolon (after URL and whitespace)')
    else:
        specifier_start = tokenizer.position
        specifier = _parse_specifier(tokenizer)
        tokenizer.consume('WS')
        if tokenizer.check('END', peek = True):
            return (url, specifier, marker)
        marker = None(tokenizer, span_start = specifier_start, expected = 'comma (within version specifier), semicolon (after version specifier)' if specifier else 'semicolon (after name with no version specifier)')
    return (url, specifier, marker)


def _parse_requirement_marker(tokenizer = None, *, span_start, expected):
    '''
    requirement_marker = SEMICOLON marker WS?
    '''
    if not tokenizer.check('SEMICOLON'):
        tokenizer.raise_syntax_error(f'''Expected {expected} or end''', span_start = span_start, span_end = None)
    tokenizer.read()
    marker = _parse_marker(tokenizer)
    tokenizer.consume('WS')
    return marker


def _parse_extras(tokenizer = None):
    '''
    extras = (LEFT_BRACKET wsp* extras_list? wsp* RIGHT_BRACKET)?
    '''
    if not tokenizer.check('LEFT_BRACKET', peek = True):
        return []
    None.enclosing_tokens('LEFT_BRACKET', 'RIGHT_BRACKET', around = 'extras')
    tokenizer.consume('WS')
    extras = _parse_extras_list(tokenizer)
    tokenizer.consume('WS')
    None(None, None)
    return extras
    with None:
        if not None:
            pass
# WARNING: Decompyle incomplete


def _parse_extras_list(tokenizer = None):
    """
    extras_list = identifier (wsp* ',' wsp* identifier)*
    """
    extras = []
    if not tokenizer.check('IDENTIFIER'):
        return extras
    None.append(tokenizer.read().text)
    tokenizer.consume('WS')
    if tokenizer.check('IDENTIFIER', peek = True):
        tokenizer.raise_syntax_error('Expected comma between extra names')
    elif not tokenizer.check('COMMA'):
        return extras
    tokenizer.read()
    tokenizer.consume('WS')
    extra_token = tokenizer.expect('IDENTIFIER', expected = 'extra name after comma')
    extras.append(extra_token.text)
    continue


def _parse_specifier(tokenizer = None):
    '''
    specifier = LEFT_PARENTHESIS WS? version_many WS? RIGHT_PARENTHESIS
              | WS? version_many WS?
    '''
    tokenizer.enclosing_tokens('LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS', around = 'version specifier')
    tokenizer.consume('WS')
    parsed_specifiers = _parse_version_many(tokenizer)
    tokenizer.consume('WS')
    None(None, None)
    return parsed_specifiers
    with None:
        if not None:
            pass
# WARNING: Decompyle incomplete


def _parse_version_many(tokenizer = None):
    '''
    version_many = (SPECIFIER (WS? COMMA WS? SPECIFIER)*)?
    '''
    parsed_specifiers = ''
    if tokenizer.check('SPECIFIER'):
        span_start = tokenizer.position
        parsed_specifiers += tokenizer.read().text
        if tokenizer.check('VERSION_PREFIX_TRAIL', peek = True):
            tokenizer.raise_syntax_error('.* suffix can only be used with `==` or `!=` operators', span_start = span_start, span_end = tokenizer.position + 1)
        if tokenizer.check('VERSION_LOCAL_LABEL_TRAIL', peek = True):
            tokenizer.raise_syntax_error('Local version label can only be used with `==` or `!=` operators', span_start = span_start, span_end = tokenizer.position)
        tokenizer.consume('WS')
        if not tokenizer.check('COMMA'):
            return parsed_specifiers
        None += tokenizer.read().text
        tokenizer.consume('WS')
        if tokenizer.check('SPECIFIER'):
            continue
    return parsed_specifiers


def parse_marker(source = None):
    return _parse_full_marker(Tokenizer(source, rules = DEFAULT_RULES))


def _parse_full_marker(tokenizer = None):
    retval = _parse_marker(tokenizer)
    tokenizer.expect('END', expected = 'end of marker expression')
    return retval


def _parse_marker(tokenizer = None):
    '''
    marker = marker_atom (BOOLOP marker_atom)+
    '''
    expression = [
        _parse_marker_atom(tokenizer)]
    if tokenizer.check('BOOLOP'):
        token = tokenizer.read()
        expr_right = _parse_marker_atom(tokenizer)
        expression.extend((token.text, expr_right))
        if tokenizer.check('BOOLOP'):
            continue
    return expression


def _parse_marker_atom(tokenizer = None):
    '''
    marker_atom = WS? LEFT_PARENTHESIS WS? marker WS? RIGHT_PARENTHESIS WS?
                | WS? marker_item WS?
    '''
    tokenizer.consume('WS')
    if tokenizer.check('LEFT_PARENTHESIS', peek = True):
        tokenizer.enclosing_tokens('LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS', around = 'marker expression')
        tokenizer.consume('WS')
        marker = _parse_marker(tokenizer)
        tokenizer.consume('WS')
        None(None, None)
    else:
        marker = _parse_marker_item(tokenizer)
    tokenizer.consume('WS')
# WARNING: Decompyle incomplete


def _parse_marker_item(tokenizer = None):
    '''
    marker_item = WS? marker_var WS? marker_op WS? marker_var WS?
    '''
    tokenizer.consume('WS')
    marker_var_left = _parse_marker_var(tokenizer)
    tokenizer.consume('WS')
    marker_op = _parse_marker_op(tokenizer)
    tokenizer.consume('WS')
    marker_var_right = _parse_marker_var(tokenizer)
    tokenizer.consume('WS')
    return (marker_var_left, marker_op, marker_var_right)


def _parse_marker_var(tokenizer = None):
    '''
    marker_var = VARIABLE | QUOTED_STRING
    '''
    if tokenizer.check('VARIABLE'):
        return process_env_var(tokenizer.read().text.replace('.', '_'))
    if None.check('QUOTED_STRING'):
        return process_python_str(tokenizer.read().text)
    None.raise_syntax_error(message = 'Expected a marker variable or quoted string')


def process_env_var(env_var = None):
    if env_var in ('platform_python_implementation', 'python_implementation'):
        return Variable('platform_python_implementation')
    return None(env_var)


def process_python_str(python_str = None):
    value = ast.literal_eval(python_str)
    return Value(str(value))


def _parse_marker_op(tokenizer = None):
    '''
    marker_op = IN | NOT IN | OP
    '''
    if tokenizer.check('IN'):
        tokenizer.read()
        return Op('in')
    if None.check('NOT'):
        tokenizer.read()
        tokenizer.expect('WS', expected = "whitespace after 'not'")
        tokenizer.expect('IN', expected = "'in' after 'not'")
        return Op('not in')
    if None.check('OP'):
        return Op(tokenizer.read().text)
    return None.raise_syntax_error('Expected marker operator, one of <=, <, !=, ==, >=, >, ~=, ===, in, not in')

