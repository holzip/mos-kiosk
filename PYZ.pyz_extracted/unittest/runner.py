# Source Generated with Decompyle++
# File: runner.pyc (Python 3.12)

'''Running tests'''
import sys
import time
import warnings
from  import result
from case import _SubTest
from signals import registerResult
__unittest = True

class _WritelnDecorator(object):
    """Used to decorate file-like objects with a handy 'writeln' method"""
    
    def __init__(self, stream):
        self.stream = stream

    
    def __getattr__(self, attr):
        if attr in ('stream', '__getstate__'):
            raise AttributeError(attr)
        return getattr(self.stream, attr)

    
    def writeln(self, arg = (None,)):
        if arg:
            self.write(arg)
        self.write('\n')



class TextTestResult(result.TestResult):
    pass
# WARNING: Decompyle incomplete


class TextTestRunner(object):
    '''A test runner class that displays results in textual form.

    It prints out the names of tests as they are run, errors as they
    occur, and a summary of the results at the end of the test run.
    '''
    resultclass = TextTestResult
    
    def __init__(self, stream, descriptions, verbosity, failfast, buffer = None, resultclass = (None, True, 1, False, False, None, None), warnings = {
        'tb_locals': False,
        'durations': None }, *, tb_locals, durations):
        '''Construct a TextTestRunner.

        Subclasses should accept **kwargs to ensure compatibility as the
        interface changes.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _makeResult(self):
        
        try:
            return self.resultclass(self.stream, self.descriptions, self.verbosity, durations = self.durations)
        except TypeError:
            return 


    
    def _printDurations(self, result):
        if not result.collectedDurations:
            return None
        ls = sorted(result.collectedDurations, key = (lambda x: x[1]), reverse = True)
        if self.durations > 0:
            ls = ls[:self.durations]
        self.stream.writeln('Slowest test durations')
        if hasattr(result, 'separator2'):
            self.stream.writeln(result.separator2)
        hidden = False
        for test, elapsed in ls:
            if self.verbosity < 2 and elapsed < 0.001:
                hidden = True
                continue
            self.stream.writeln(f'''{'%.3fs' % elapsed!s:10} {test!s}''')
        if hidden:
            self.stream.writeln('\n(durations < 0.001s were hidden; use -v to show these durations)')
            return None
        self.stream.writeln('')

    
    def run(self, test):
        '''Run the given test case or test suite.'''
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        result.tb_locals = self.tb_locals
        warnings.catch_warnings()
        if self.warnings:
            warnings.simplefilter(self.warnings)
        startTime = time.perf_counter()
        startTestRun = getattr(result, 'startTestRun', None)
    # WARNING: Decompyle incomplete


