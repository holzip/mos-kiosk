# Source Generated with Decompyle++
# File: error_reporting.pyc (Python 3.12)

import io
import json
import logging
import os
import re
import typing
from contextlib import contextmanager
from textwrap import indent, wrap
from typing import Any, Dict, Generator, Iterator, List, Optional, Sequence, Union
from fastjsonschema_exceptions import JsonSchemaValueException
if typing.TYPE_CHECKING:
    import sys
    if sys.version_info < (3, 11):
        from typing_extensions import Self
    else:
        from typing import Self
_logger = logging.getLogger(__name__)
_MESSAGE_REPLACEMENTS = {
    'must be named by propertyName definition': 'keys must be named by',
    'one of contains definition': 'at least one item that matches',
    ' same as const definition:': '',
    'only specified items': 'only items matching the definition' }
_SKIP_DETAILS = ('must not be empty', 'is always invalid', 'must not be there')
_NEED_DETAILS = {
    'not',
    'allOf',
    'anyOf',
    'items',
    'oneOf',
    'contains',
    'propertyNames'}
_CAMEL_CASE_SPLITTER = re.compile('\\W+|([A-Z][^A-Z\\W]*)')
_IDENTIFIER = re.compile('^[\\w_]+$', re.I)
_TOML_JARGON = {
    'object': 'table',
    'property': 'key',
    'properties': 'keys',
    'property names': 'keys' }
_FORMATS_HELP = '\nFor more details about `format` see\nhttps://validate-pyproject.readthedocs.io/en/latest/api/validate_pyproject.formats.html\n'

class ValidationError(JsonSchemaValueException):
    '''Report violations of a given JSON schema.

    This class extends :exc:`~fastjsonschema.JsonSchemaValueException`
    by adding the following properties:

    - ``summary``: an improved version of the ``JsonSchemaValueException`` error message
      with only the necessary information)

    - ``details``: more contextual information about the error like the failing schema
      itself and the value that violates the schema.

    Depending on the level of the verbosity of the ``logging`` configuration
    the exception message will be only ``summary`` (default) or a combination of
    ``summary`` and ``details`` (when the logging level is set to :obj:`logging.DEBUG`).
    '''
    summary = ''
    details = ''
    _original_message = ''
    _from_jsonschema = (lambda cls = None, ex = None: formatter = _ErrorFormatting(ex)obj = cls(str(formatter), ex.value, formatter.name, ex.definition, ex.rule)debug_code = os.getenv('JSONSCHEMA_DEBUG_CODE_GENERATION', 'false').lower()if debug_code != 'false':
obj.__cause__, obj.__traceback__ = ex.__cause__, ex.__traceback__obj._original_message = ex.messageobj.summary = formatter.summaryobj.details = formatter.detailsobj)()

detailed_errors = (lambda : pass# WARNING: Decompyle incomplete
)()

class _ErrorFormatting:
    
    def __init__(self = None, ex = None):
        self.ex = ex
        self.name = f'''`{self._simplify_name(ex.name)}`'''
        self._original_message = self.ex.message.replace(ex.name, self.name)
        self._summary = ''
        self._details = ''

    
    def __str__(self = None):
        if _logger.getEffectiveLevel() <= logging.DEBUG and self.details:
            return f'''{self.summary}\n\n{self.details}'''
        return None.summary

    summary = (lambda self = None: if not self._summary:
self._summary = self._expand_summary()self._summary)()
    details = (lambda self = None: if not self._details:
self._details = self._expand_details()self._details)()
    _simplify_name = (lambda name = None: x = len('data.')if name.startswith('data.'):
name[x:])()
    
    def _expand_summary(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _expand_details(self = None):
        optional = []
        if not self.ex.definition:
            self.ex.definition
        definition = { }
        desc_lines = definition.pop('$$description', [])
        if not definition.pop('description', None):
            definition.pop('description', None)
        desc = ' '.join(desc_lines)
        if desc:
            description = '\n'.join(wrap(desc, width = 80, initial_indent = '    ', subsequent_indent = '    ', break_long_words = False))
            optional.append(f'''DESCRIPTION:\n{description}''')
        schema = json.dumps(definition, indent = 4)
        value = json.dumps(self.ex.value, indent = 4)
        defaults = [
            f'''GIVEN VALUE:\n{indent(value, '    ')}''',
            f'''OFFENDING RULE: {self.ex.rule!r}''',
            f'''DEFINITION:\n{indent(schema, '    ')}''']
        msg = '\n\n'.join(optional + defaults)
        epilog = f'''\n{_FORMATS_HELP}''' if 'format' in msg.lower() else ''
        return msg + epilog



class _SummaryWriter:
    _IGNORE = frozenset(('description', 'default', 'title', 'examples'))
    
    def __init__(self = None, jargon = None):
        if not jargon:
            jargon
        self.jargon = { }
        self._terms = {
            'anyOf': 'at least one of the following',
            'oneOf': 'exactly one of the following',
            'allOf': 'all of the following',
            'not': '(*NOT* the following)',
            'prefixItems': f'''{self._jargon('items')} (in order)''',
            'items': 'items',
            'contains': 'contains at least one of',
            'propertyNames': f'''non-predefined acceptable {self._jargon('property names')}''',
            'patternProperties': f'''{self._jargon('properties')} named via pattern''',
            'const': 'predefined value',
            'enum': 'one of' }
        self._guess_inline_defs = [
            'enum',
            'const',
            'maxLength',
            'minLength',
            'pattern',
            'format',
            'minimum',
            'maximum',
            'exclusiveMinimum',
            'exclusiveMaximum',
            'multipleOf']

    
    def _jargon(self = None, term = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self = None, schema = None, prefix = None, *, _path):
        if isinstance(schema, list):
            return self._handle_list(schema, prefix, _path)
        filtered = None._filter_unecessary(schema, _path)
        simple = self._handle_simple_dict(filtered, _path)
        if simple:
            return f'''{prefix}{simple}'''
        child_prefix = None._child_prefix(prefix, '  ')
        item_prefix = self._child_prefix(prefix, '- ')
        indent = len(prefix) * ' '
        buffer = io.StringIO()
        for key, value in enumerate(filtered.items()):
            child_path = None[key]
            line_prefix = prefix if i == 0 else indent
            buffer.write(f'''{line_prefix}{self._label(child_path)}:''')
            if isinstance(value, dict):
                filtered = self._filter_unecessary(value, child_path)
                simple = self._handle_simple_dict(filtered, child_path)
                buffer.write(f''' {simple}''' if simple else f'''\n{self(value, child_prefix, _path = child_path)}''')
                continue
            if isinstance(value, list):
                if key != 'type' or self._is_property(child_path):
                    children = self._handle_list(value, item_prefix, child_path)
                    sep = ' ' if children.startswith('[') else '\n'
                    buffer.write(f'''{sep}{children}''')
                    continue
            buffer.write(f''' {self._value(value, child_path)}\n''')
        None(None, None)
        return 
        with None:
            if not None, buffer.getvalue():
                pass

    
    def _is_unecessary(self = None, path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _filter_unecessary(self = None, schema = None, path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_simple_dict(self = None, value = None, path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_list(self = None, schemas = None, prefix = None, path = ('', ())):
        pass
    # WARNING: Decompyle incomplete

    
    def _is_property(self = None, path = None):
        '''Check if the given path can correspond to an arbitrarily named property'''
        counter = 0
        for key in path[-2::-1]:
            if key not in frozenset({'properties', 'patternProperties'}):
                path[-2::-1]
            else:
                counter += 1
        return counter % 2 == 1

    
    def _label(self = None, path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _value(self = None, value = None, path = None):
        if not path[-1] == 'type' and self._is_property(path):
            type_ = self._jargon(value)
            if isinstance(type_, list):
                return f'''[{', '.join(type_)}]'''
            return None
        return None(value)

    
    def _inline_attrs(self = None, schema = None, path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _child_prefix(self = None, parent_prefix = None, child_prefix = None):
        return len(parent_prefix) * ' ' + child_prefix



def _separate_terms(word = None):
    '''
    >>> _separate_terms("FooBar-foo")
    [\'foo\', \'bar\', \'foo\']
    '''
    pass
# WARNING: Decompyle incomplete

