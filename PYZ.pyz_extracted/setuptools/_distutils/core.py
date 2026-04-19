# Source Generated with Decompyle++
# File: core.pyc (Python 3.12)

"""distutils.core

The only module that needs to be imported to use the Distutils; provides
the 'setup' function (which is to be called from the setup script).  Also
indirectly provides the Distribution and Command classes, although they are
really defined in distutils.dist and distutils.cmd.
"""
from __future__ import annotations
import os
import sys
import tokenize
from collections.abc import Iterable
from cmd import Command
from debug import DEBUG
from dist import Distribution
from errors import CCompilerError, DistutilsArgError, DistutilsError, DistutilsSetupError
from extension import Extension
__all__ = [
    'Distribution',
    'Command',
    'Extension',
    'setup']
USAGE = 'usage: %(script)s [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]\n   or: %(script)s --help [cmd1 cmd2 ...]\n   or: %(script)s --help-commands\n   or: %(script)s cmd --help\n'

def gen_usage(script_name):
    script = os.path.basename(script_name)
    return USAGE % locals()

_setup_stop_after = None
_setup_distribution = None
setup_keywords = ('distclass', 'script_name', 'script_args', 'options', 'name', 'version', 'author', 'author_email', 'maintainer', 'maintainer_email', 'url', 'license', 'description', 'long_description', 'keywords', 'platforms', 'classifiers', 'download_url', 'requires', 'provides', 'obsoletes')
extension_keywords = ('name', 'sources', 'include_dirs', 'define_macros', 'undef_macros', 'library_dirs', 'libraries', 'runtime_library_dirs', 'extra_objects', 'extra_compile_args', 'extra_link_args', 'swig_opts', 'export_symbols', 'depends', 'language')

def setup(**attrs):
    """The gateway to the Distutils: do everything your setup script needs
    to do, in a highly flexible and user-driven way.  Briefly: create a
    Distribution instance; find and parse config files; parse the command
    line; run each Distutils command found there, customized by the options
    supplied to 'setup()' (as keyword arguments), in config files, and on
    the command line.

    The Distribution instance might be an instance of a class supplied via
    the 'distclass' keyword argument to 'setup'; if no such class is
    supplied, then the Distribution class (in dist.py) is instantiated.
    All other arguments to 'setup' (except for 'cmdclass') are used to set
    attributes of the Distribution instance.

    The 'cmdclass' argument, if supplied, is a dictionary mapping command
    names to command classes.  Each command encountered on the command line
    will be turned into a command class, which is in turn instantiated; any
    class found in 'cmdclass' is used in place of the default, which is
    (for command 'foo_bar') class 'foo_bar' in module
    'distutils.command.foo_bar'.  The command class must provide a
    'user_options' attribute which is a list of option specifiers for
    'distutils.fancy_getopt'.  Any command-line options between the current
    and the next command are used to set attributes of the current command
    object.

    When the entire command-line has been successfully parsed, calls the
    'run()' method on each command object in turn.  This method will be
    driven entirely by the Distribution object (which each command object
    has a reference to, thanks to its constructor), and the
    command-specific options that became attributes of each command
    object.
    """
    global _setup_distribution
    klass = attrs.get('distclass')
    if klass:
        attrs.pop('distclass')
    else:
        klass = Distribution
    if 'script_name' not in attrs:
        attrs['script_name'] = os.path.basename(sys.argv[0])
    if 'script_args' not in attrs:
        attrs['script_args'] = sys.argv[1:]
    
    try:
        _setup_distribution = klass(attrs)
        dist = klass(attrs)
        if _setup_stop_after == 'init':
            return dist
        None.parse_config_files()
        if DEBUG:
            print('options (after parsing config files):')
            dist.dump_option_dicts()
        if _setup_stop_after == 'config':
            return dist
        
        try:
            ok = dist.parse_command_line()
            if DEBUG:
                print('options (after parsing command line):')
                dist.dump_option_dicts()
            if _setup_stop_after == 'commandline':
                return dist
            if None:
                return run_commands(dist)
            return None
            except DistutilsSetupError:
                msg = None
                if 'name' not in attrs:
                    raise SystemExit(f'''error in setup command: {msg}''')
                raise SystemExit('error in {} setup command: {}'.format(attrs['name'], msg))
                msg = None
                del msg
        except DistutilsArgError:
            msg = None
            raise SystemExit(gen_usage(dist.script_name) + f'''\nerror: {msg}''')
            msg = None
            del msg




def run_commands(dist):
    '''Given a Distribution object run all the commands,
    raising ``SystemExit`` errors in the case of failure.

    This function assumes that either ``sys.argv`` or ``dist.script_args``
    is already set accordingly.
    '''
    
    try:
        dist.run_commands()
        return dist
    except KeyboardInterrupt:
        raise SystemExit('interrupted')
        except OSError:
            exc = None
            if DEBUG:
                sys.stderr.write(f'''error: {exc}\n''')
                raise 
            raise SystemExit(f'''error: {exc}''')
            exc = None
            del exc
        except (DistutilsError, CCompilerError):
            msg = None
            if DEBUG:
                raise 
            raise SystemExit('error: ' + str(msg))
            msg = None
            del msg



def run_setup(script_name = None, script_args = None, stop_after = None):
    """Run a setup script in a somewhat controlled environment, and
    return the Distribution instance that drives things.  This is useful
    if you need to find out the distribution meta-data (passed as
    keyword args from 'script' to 'setup()', or the contents of the
    config files or command-line.

    'script_name' is a file that will be read and run with 'exec()';
    'sys.argv[0]' will be replaced with 'script' for the duration of the
    call.  'script_args' is a list of strings; if supplied,
    'sys.argv[1:]' will be replaced by 'script_args' for the duration of
    the call.

    'stop_after' tells 'setup()' when to stop processing; possible
    values:
      init
        stop after the Distribution instance has been created and
        populated with the keyword arguments to 'setup()'
      config
        stop after config files have been parsed (and their data
        stored in the Distribution instance)
      commandline
        stop after the command-line ('sys.argv[1:]' or 'script_args')
        have been parsed (and the data stored in the Distribution)
      run [default]
        stop after all commands have been run (the same as if 'setup()'
        had been called in the usual way

    Returns the Distribution instance, which provides all information
    used to drive the Distutils.
    """
    global _setup_stop_after
    if stop_after not in ('init', 'config', 'commandline', 'run'):
        raise ValueError(f'''invalid value for \'stop_after\': {stop_after!r}''')
    _setup_stop_after = stop_after
    save_argv = sys.argv.copy()
    g = {
        '__file__': script_name,
        '__name__': '__main__' }
# WARNING: Decompyle incomplete

