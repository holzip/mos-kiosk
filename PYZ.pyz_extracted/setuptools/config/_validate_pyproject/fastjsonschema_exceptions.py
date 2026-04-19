# Source Generated with Decompyle++
# File: fastjsonschema_exceptions.pyc (Python 3.12)

import re
SPLIT_RE = re.compile('[\\.\\[\\]]+')

class JsonSchemaException(ValueError):
    '''
    Base exception of ``fastjsonschema`` library.
    '''
    pass


class JsonSchemaValueException(JsonSchemaException):
    pass
# WARNING: Decompyle incomplete


class JsonSchemaDefinitionException(JsonSchemaException):
    '''
    Exception raised by generator of validation function.
    '''
    pass

