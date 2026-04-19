# Source Generated with Decompyle++
# File: loader.pyc (Python 3.12)

'''Loading unittests.'''
import os
import re
import sys
import traceback
import types
import functools
from fnmatch import fnmatch, fnmatchcase
from  import case, suite, util
__unittest = True
VALID_MODULE_NAME = re.compile('[_a-z]\\w*\\.py$', re.IGNORECASE)

class _FailedTest(case.TestCase):
    pass
# WARNING: Decompyle incomplete


def _make_failed_import_test(name, suiteClass):
    message = f'''Failed to import test module: {name!s}\n{traceback.format_exc()!s}'''
    return _make_failed_test(name, ImportError(message), suiteClass, message)


def _make_failed_load_tests(name, exception, suiteClass):
    message = f'''Failed to call load_tests:\n{traceback.format_exc()!s}'''
    return _make_failed_test(name, exception, suiteClass, message)


def _make_failed_test(methodname, exception, suiteClass, message):
    test = _FailedTest(methodname, exception)
    return (suiteClass((test,)), message)


def _make_skipped_test(methodname, exception, suiteClass):
    testSkipped = (lambda self: pass)()
    attrs = {
        methodname: testSkipped }
    TestClass = type('ModuleSkipped', (case.TestCase,), attrs)
    return suiteClass((TestClass(methodname),))


def _splitext(path):
    return os.path.splitext(path)[0]


class TestLoader(object):
    pass
# WARNING: Decompyle incomplete

defaultTestLoader = TestLoader()

def _makeLoader(prefix, sortUsing, suiteClass, testNamePatterns = (None, None)):
    loader = TestLoader()
    loader.sortTestMethodsUsing = sortUsing
    loader.testMethodPrefix = prefix
    loader.testNamePatterns = testNamePatterns
    if suiteClass:
        loader.suiteClass = suiteClass
    return loader


def getTestCaseNames(testCaseClass, prefix, sortUsing, testNamePatterns = (util.three_way_cmp, None)):
    import warnings
    warnings.warn('unittest.getTestCaseNames() is deprecated and will be removed in Python 3.13. Please use unittest.TestLoader.getTestCaseNames() instead.', DeprecationWarning, stacklevel = 2)
    return _makeLoader(prefix, sortUsing, testNamePatterns = testNamePatterns).getTestCaseNames(testCaseClass)


def makeSuite(testCaseClass, prefix, sortUsing, suiteClass = ('test', util.three_way_cmp, suite.TestSuite)):
    import warnings
    warnings.warn('unittest.makeSuite() is deprecated and will be removed in Python 3.13. Please use unittest.TestLoader.loadTestsFromTestCase() instead.', DeprecationWarning, stacklevel = 2)
    return _makeLoader(prefix, sortUsing, suiteClass).loadTestsFromTestCase(testCaseClass)


def findTestCases(module, prefix, sortUsing, suiteClass = ('test', util.three_way_cmp, suite.TestSuite)):
    import warnings
    warnings.warn('unittest.findTestCases() is deprecated and will be removed in Python 3.13. Please use unittest.TestLoader.loadTestsFromModule() instead.', DeprecationWarning, stacklevel = 2)
    return _makeLoader(prefix, sortUsing, suiteClass).loadTestsFromModule(module)

