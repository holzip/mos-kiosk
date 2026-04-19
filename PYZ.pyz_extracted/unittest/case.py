# Source Generated with Decompyle++
# File: case.pyc (Python 3.12)

'''Test case implementation'''
import sys
import functools
import difflib
import pprint
import re
import warnings
import collections
import contextlib
import traceback
import time
import types
from  import result
from util import strclass, safe_repr, _count_diff_all_purpose, _count_diff_hashable, _common_shorten_repr
__unittest = True
_subtest_msg_sentinel = object()
DIFF_OMITTED = '\nDiff is %s characters long. Set self.maxDiff to None to see it.'

class SkipTest(Exception):
    '''
    Raise this exception in a test to skip it.

    Usually you can use TestCase.skipTest() or one of the skipping decorators
    instead of raising this directly.
    '''
    pass


class _ShouldStop(Exception):
    '''
    The test should stop.
    '''
    pass


class _UnexpectedSuccess(Exception):
    """
    The test was supposed to fail, but it didn't!
    """
    pass


class _Outcome(object):
    
    def __init__(self, result = (None,)):
        self.expecting_failure = False
        self.result = result
        self.result_supports_subtests = hasattr(result, 'addSubTest')
        self.success = True
        self.expectedFailure = None

    testPartExecutor = (lambda self, test_case, subTest = (False,): pass# WARNING: Decompyle incomplete
)()


def _addSkip(result, test_case, reason):
    addSkip = getattr(result, 'addSkip', None)
# WARNING: Decompyle incomplete


def _addError(result, test, exc_info):
    pass
# WARNING: Decompyle incomplete


def _id(obj):
    return obj


def _enter_context(cm, addcleanup):
    cls = type(cm)
    
    try:
        enter = cls.__enter__
        exit = cls.__exit__
        result = enter(cm)
        addcleanup(exit, cm, None, None, None)
        return result
    except AttributeError:
        raise TypeError(f'''\'{cls.__module__}.{cls.__qualname__}\' object does not support the context manager protocol'''), None


_module_cleanups = []

def addModuleCleanup(function, *args, **kwargs):
    '''Same as addCleanup, except the cleanup items are called even if
    setUpModule fails (unlike tearDownModule).'''
    _module_cleanups.append((function, args, kwargs))


def enterModuleContext(cm):
    '''Same as enterContext, but module-wide.'''
    return _enter_context(cm, addModuleCleanup)


def doModuleCleanups():
    '''Execute all module cleanup functions. Normally called for you after
    tearDownModule.'''
    exceptions = []
# WARNING: Decompyle incomplete


def skip(reason):
    '''
    Unconditionally skip a test.
    '''
    pass
# WARNING: Decompyle incomplete


def skipIf(condition, reason):
    '''
    Skip a test if the condition is true.
    '''
    if condition:
        return skip(reason)


def skipUnless(condition, reason):
    '''
    Skip a test unless the condition is true.
    '''
    if not condition:
        return skip(reason)


def expectedFailure(test_item):
    test_item.__unittest_expecting_failure__ = True
    return test_item


def _is_subtype(expected, basetype):
    pass
# WARNING: Decompyle incomplete


class _BaseTestCaseContext:
    
    def __init__(self, test_case):
        self.test_case = test_case

    
    def _raiseFailure(self, standardMsg):
        msg = self.test_case._formatMessage(self.msg, standardMsg)
        raise self.test_case.failureException(msg)



class _AssertRaisesBaseContext(_BaseTestCaseContext):
    
    def __init__(self, expected, test_case, expected_regex = (None,)):
        _BaseTestCaseContext.__init__(self, test_case)
        self.expected = expected
        self.test_case = test_case
    # WARNING: Decompyle incomplete

    
    def handle(self, name, args, kwargs):
        """
        If args is empty, assertRaises/Warns is being used as a
        context manager, so check for a 'msg' kwarg and return self.
        If args is not empty, call a callable passing positional and keyword
        arguments.
        """
        pass
    # WARNING: Decompyle incomplete



class _AssertRaisesContext(_AssertRaisesBaseContext):
    '''A context manager used to implement TestCase.assertRaises* methods.'''
    _base_type = BaseException
    _base_type_str = 'an exception type or tuple of exception types'
    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_value, tb):
        pass
    # WARNING: Decompyle incomplete

    __class_getitem__ = classmethod(types.GenericAlias)


class _AssertWarnsContext(_AssertRaisesBaseContext):
    '''A context manager used to implement TestCase.assertWarns* methods.'''
    _base_type = Warning
    _base_type_str = 'a warning type or tuple of warning types'
    
    def __enter__(self):
        for v in list(sys.modules.values()):
            if not getattr(v, '__warningregistry__', None):
                continue
            v.__warningregistry__ = { }
        self.warnings_manager = warnings.catch_warnings(record = True)
        self.warnings = self.warnings_manager.__enter__()
        warnings.simplefilter('always', self.expected)
        return self

    
    def __exit__(self, exc_type, exc_value, tb):
        self.warnings_manager.__exit__(exc_type, exc_value, tb)
    # WARNING: Decompyle incomplete



class _OrderedChainMap(collections.ChainMap):
    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete



class TestCase(object):
    pass
# WARNING: Decompyle incomplete


class FunctionTestCase(TestCase):
    pass
# WARNING: Decompyle incomplete


class _SubTest(TestCase):
    pass
# WARNING: Decompyle incomplete

