# Source Generated with Decompyle++
# File: main.pyc (Python 3.12)

'''Unittest main program'''
import sys
import argparse
import os
import warnings
from  import loader, runner
from signals import installHandler
__unittest = True
_NO_TESTS_EXITCODE = 5
MAIN_EXAMPLES = 'Examples:\n  %(prog)s test_module               - run tests from test_module\n  %(prog)s module.TestClass          - run tests from module.TestClass\n  %(prog)s module.Class.test_method  - run specified test method\n  %(prog)s path/to/test_file.py      - run tests from test_file.py\n'
MODULE_EXAMPLES = "Examples:\n  %(prog)s                           - run default set of tests\n  %(prog)s MyTestSuite               - run suite 'MyTestSuite'\n  %(prog)s MyTestCase.testSomething  - run MyTestCase.testSomething\n  %(prog)s MyTestCase                - run all 'test*' test methods\n                                       in MyTestCase\n"

def _convert_name(name):
    if os.path.isfile(name) and name.lower().endswith('.py'):
        if os.path.isabs(name):
            rel_path = os.path.relpath(name, os.getcwd())
            if os.path.isabs(rel_path) or rel_path.startswith(os.pardir):
                return name
            name = None
        return os.path.normpath(name)[:-3].replace('\\', '.').replace('/', '.')


def _convert_names(names):
    pass
# WARNING: Decompyle incomplete


def _convert_select_pattern(pattern):
    if '*' not in pattern:
        pattern = '*%s*' % pattern
    return pattern


class TestProgram(object):
    '''A command-line program that runs a set of tests; this is primarily
       for making test modules conveniently executable.
    '''
    module = None
    verbosity = 1
    failfast = None
    catchbreak = None
    buffer = None
    progName = None
    warnings = None
    testNamePatterns = None
    _discovery_parser = None
    
    def __init__(self, module, defaultTest, argv, testRunner, testLoader, exit, verbosity, failfast, catchbreak = None, buffer = ('__main__', None, None, None, loader.defaultTestLoader, True, 1, None, None, None, None), warnings = {
        'tb_locals': False,
        'durations': None }, *, tb_locals, durations):
        if isinstance(module, str):
            self.module = __import__(module)
            for part in module.split('.')[1:]:
                self.module = getattr(self.module, part)
        else:
            self.module = module
    # WARNING: Decompyle incomplete

    
    def usageExit(self, msg = (None,)):
        warnings.warn('TestProgram.usageExit() is deprecated and will be removed in Python 3.13', DeprecationWarning)
        if msg:
            print(msg)
    # WARNING: Decompyle incomplete

    
    def _print_help(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def parseArgs(self, argv):
        self._initArgParsers()
    # WARNING: Decompyle incomplete

    
    def createTests(self, from_discovery, Loader = (False, None)):
        if self.testNamePatterns:
            self.testLoader.testNamePatterns = self.testNamePatterns
    # WARNING: Decompyle incomplete

    
    def _initArgParsers(self):
        parent_parser = self._getParentArgParser()
        self._main_parser = self._getMainArgParser(parent_parser)
        self._discovery_parser = self._getDiscoveryArgParser(parent_parser)

    
    def _getParentArgParser(self):
        parser = argparse.ArgumentParser(add_help = False)
        parser.add_argument('-v', '--verbose', dest = 'verbosity', action = 'store_const', const = 2, help = 'Verbose output')
        parser.add_argument('-q', '--quiet', dest = 'verbosity', action = 'store_const', const = 0, help = 'Quiet output')
        parser.add_argument('--locals', dest = 'tb_locals', action = 'store_true', help = 'Show local variables in tracebacks')
        parser.add_argument('--durations', dest = 'durations', type = int, default = None, metavar = 'N', help = 'Show the N slowest test cases (N=0 for all)')
    # WARNING: Decompyle incomplete

    
    def _getMainArgParser(self, parent):
        parser = argparse.ArgumentParser(parents = [
            parent])
        parser.prog = self.progName
        parser.print_help = self._print_help
        parser.add_argument('tests', nargs = '*', help = 'a list of any number of test modules, classes and test methods.')
        return parser

    
    def _getDiscoveryArgParser(self, parent):
        parser = argparse.ArgumentParser(parents = [
            parent])
        parser.prog = '%s discover' % self.progName
        parser.epilog = 'For test discovery all test modules must be importable from the top level directory of the project.'
        parser.add_argument('-s', '--start-directory', dest = 'start', help = "Directory to start discovery ('.' default)")
        parser.add_argument('-p', '--pattern', dest = 'pattern', help = "Pattern to match tests ('test*.py' default)")
        parser.add_argument('-t', '--top-level-directory', dest = 'top', help = 'Top level directory of project (defaults to start directory)')
        for arg in ('start', 'pattern', 'top'):
            parser.add_argument(arg, nargs = '?', default = argparse.SUPPRESS, help = argparse.SUPPRESS)
        return parser

    
    def _do_discovery(self, argv, Loader = (None,)):
        self.start = '.'
        self.pattern = 'test*.py'
        self.top = None
    # WARNING: Decompyle incomplete

    
    def runTests(self):
        if self.catchbreak:
            installHandler()
    # WARNING: Decompyle incomplete


main = TestProgram
