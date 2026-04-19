# Source Generated with Decompyle++
# File: result.pyc (Python 3.12)

'''Test result object'''
import io
import sys
import traceback
from  import util
from functools import wraps
__unittest = True

def failfast(method):
    pass
# WARNING: Decompyle incomplete

STDOUT_LINE = '\nStdout:\n%s'
STDERR_LINE = '\nStderr:\n%s'

class TestResult(object):
    '''Holder for test result information.

    Test results are automatically managed by the TestCase and TestSuite
    classes, and do not need to be explicitly manipulated by writers of tests.

    Each instance holds the total number of tests run, and collections of
    failures and errors that occurred among those test runs. The collections
    contain tuples of (testcase, exceptioninfo), where exceptioninfo is the
    formatted traceback of the error that occurred.
    '''
    _previousTestClass = None
    _testRunEntered = False
    _moduleSetUpFailed = False
    
    def __init__(self, stream, descriptions, verbosity = (None, None, None)):
        self.failfast = False
        self.failures = []
        self.errors = []
        self.testsRun = 0
        self.skipped = []
        self.expectedFailures = []
        self.unexpectedSuccesses = []
        self.collectedDurations = []
        self.shouldStop = False
        self.buffer = False
        self.tb_locals = False
        self._stdout_buffer = None
        self._stderr_buffer = None
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        self._mirrorOutput = False

    
    def printErrors(self):
        '''Called by TestRunner after test run'''
        pass

    
    def startTest(self, test):
        '''Called when the given test is about to be run'''
        False = self, self.testsRun += 1, .testsRun
        self._setupStdout()

    
    def _setupStdout(self):
        pass
    # WARNING: Decompyle incomplete

    
    def startTestRun(self):
        '''Called once before any tests are executed.

        See startTest for a method called before each test.
        '''
        pass

    
    def stopTest(self, test):
        '''Called when the given test has been run'''
        self._restoreStdout()
        self._mirrorOutput = False

    
    def _restoreStdout(self):
        if self.buffer:
            if self._mirrorOutput:
                output = sys.stdout.getvalue()
                error = sys.stderr.getvalue()
                if output:
                    if not output.endswith('\n'):
                        output += '\n'
                    self._original_stdout.write(STDOUT_LINE % output)
                if error:
                    if not error.endswith('\n'):
                        error += '\n'
                    self._original_stderr.write(STDERR_LINE % error)
            sys.stdout = self._original_stdout
            sys.stderr = self._original_stderr
            self._stdout_buffer.seek(0)
            self._stdout_buffer.truncate()
            self._stderr_buffer.seek(0)
            self._stderr_buffer.truncate()
            return None

    
    def stopTestRun(self):
        '''Called once after all tests are executed.

        See stopTest for a method called after each test.
        '''
        pass

    addError = (lambda self, test, err: self.errors.append((test, self._exc_info_to_string(err, test)))self._mirrorOutput = True)()
    addFailure = (lambda self, test, err: self.failures.append((test, self._exc_info_to_string(err, test)))self._mirrorOutput = True)()
    
    def addSubTest(self, test, subtest, err):
        """Called at the end of a subtest.
        'err' is None if the subtest ended successfully, otherwise it's a
        tuple of values as returned by sys.exc_info().
        """
        pass
    # WARNING: Decompyle incomplete

    
    def addSuccess(self, test):
        '''Called when a test has completed successfully'''
        pass

    
    def addSkip(self, test, reason):
        '''Called when a test is skipped.'''
        self.skipped.append((test, reason))

    
    def addExpectedFailure(self, test, err):
        '''Called when an expected failure/error occurred.'''
        self.expectedFailures.append((test, self._exc_info_to_string(err, test)))

    addUnexpectedSuccess = (lambda self, test: self.unexpectedSuccesses.append(test))()
    
    def addDuration(self, test, elapsed):
        '''Called when a test finished to run, regardless of its outcome.
        *test* is the test case corresponding to the test method.
        *elapsed* is the time represented in seconds, and it includes the
        execution of cleanup functions.
        '''
        if hasattr(self, 'collectedDurations'):
            self.collectedDurations.append((str(test), elapsed))
            return None

    
    def wasSuccessful(self):
        '''Tells whether or not this result was a success.'''
        if None if  == len(self.failures), len(self.errors) else None, len(self.failures), len(self.errors) == 0:
            None if  == len(self.failures), len(self.errors) else None, len(self.failures), len(self.errors) == 0
            if not not hasattr(self, 'unexpectedSuccesses'):
                not hasattr(self, 'unexpectedSuccesses')
        return len(self.unexpectedSuccesses) == 0

    
    def stop(self):
        '''Indicates that the tests should be aborted.'''
        self.shouldStop = True

    
    def _exc_info_to_string(self, err, test):
        '''Converts a sys.exc_info()-style tuple of values into a string.'''
        (exctype, value, tb) = err
        tb = self._clean_tracebacks(exctype, value, tb, test)
        tb_e = traceback.TracebackException(exctype, value, tb, capture_locals = self.tb_locals, compact = True)
        msgLines = list(tb_e.format())
        if self.buffer:
            output = sys.stdout.getvalue()
            error = sys.stderr.getvalue()
            if output:
                if not output.endswith('\n'):
                    output += '\n'
                msgLines.append(STDOUT_LINE % output)
            if error:
                if not error.endswith('\n'):
                    error += '\n'
                msgLines.append(STDERR_LINE % error)
        return ''.join(msgLines)

    
    def _clean_tracebacks(self, exctype, value, tb, test):
        ret = None
        first = True
        excs = [
            (exctype, value, tb)]
        seen = {
            id(value)}
    # WARNING: Decompyle incomplete

    
    def _is_relevant_tb_level(self, tb):
        return '__unittest' in tb.tb_frame.f_globals

    
    def _remove_unittest_tb_frames(self, tb):
        '''Truncates usercode tb at the first unittest frame.

        If the first frame of the traceback is in user code,
        the prefix up to the first unittest frame is returned.
        If the first frame is already in the unittest module,
        the traceback is not modified.
        '''
        prev = None
        if not tb and self._is_relevant_tb_level(tb):
            prev = tb
            tb = tb.tb_next
            if not tb and self._is_relevant_tb_level(tb):
                continue
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '<%s run=%i errors=%i failures=%i>' % (util.strclass(self.__class__), self.testsRun, len(self.errors), len(self.failures))


