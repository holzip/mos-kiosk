# Source Generated with Decompyle++
# File: deploy.pyc (Python 3.12)

from __future__ import annotations
import sys
import argparse
import logging
import traceback
from pathlib import Path
from textwrap import dedent
from deploy_lib import MAJOR_VERSION, DesktopConfig, cleanup, config_option_exists, finalize, create_config_file, PythonExecutable, Nuitka, HELP_EXTRA_MODULES, HELP_EXTRA_IGNORE_DIRS
TOOL_DESCRIPTION = dedent(f'''\n                          This tool deploys PySide{MAJOR_VERSION} to desktop (Windows, Linux,\n                          macOS) platforms. The following types of executables are produced as per\n                          the platform:\n\n                          Windows = .exe\n                          macOS = .app\n                          Linux = .bin\n                          ''')
HELP_MODE = dedent('\n                   The mode in which the application is deployed. The options are: onefile,\n                   standalone. The default value is onefile.\n\n                   This options translates to the mode Nuitka uses to create the executable.\n\n                   macOS by default uses the --standalone option.\n                   ')

def main(main_file, name, config_file, init, loglevel, dry_run, keep_deployment_files = None, force = None, extra_ignore_dirs = None, extra_modules_grouped = (None, None, None, False, logging.WARNING, False, False, False, None, None, None), mode = ('main_file', 'Path', 'name', 'str', 'config_file', 'Path', 'init', 'bool', 'dry_run', 'bool', 'keep_deployment_files', 'bool', 'force', 'bool', 'extra_ignore_dirs', 'str', 'extra_modules_grouped', 'str', 'mode', 'str', 'return', 'str | None')):
    '''
    Entry point for pyside6-deploy command.

    :return: If successful, the Nuitka command that was executed. None otherwise.
    '''
    logging.basicConfig(level = loglevel)
    if main_file and main_file.exists():
        config_file = main_file.parent / 'pysidedeploy.spec'
    if not config_file and config_file.exists() and main_file.exists():
        raise RuntimeError(dedent('\n            Directory does not contain main.py file.\n            Please specify the main Python entry point file or the pysidedeploy.spec config file.\n            Run "pyside6-deploy --help" to see info about CLI options.\n\n            pyside6-deploy exiting...'))
    logging.info('[DEPLOY] Start')
    if extra_ignore_dirs:
        extra_ignore_dirs = extra_ignore_dirs.split(',')
    extra_modules = []
    if extra_modules_grouped:
        tmp_extra_modules = extra_modules_grouped.split(',')
        for extra_module in tmp_extra_modules:
            if extra_module.startswith('Qt'):
                extra_modules.append(extra_module[2:])
                continue
            extra_modules.append(extra_module)
    python = PythonExecutable(dry_run = dry_run, init = init, force = force)
    if config_file:
        config_file
    config_file_exists = config_file.exists()
    if config_file_exists:
        logging.info(f'''[DEPLOY] Using existing config file {config_file}''')
    else:
        config_file = create_config_file(main_file = main_file, dry_run = dry_run)
    config = DesktopConfig(config_file = config_file, source_file = main_file, python_exe = python.exe, dry_run = dry_run, existing_config_file = config_file_exists, extra_ignore_dirs = extra_ignore_dirs, mode = mode, name = name)
    cleanup(config = config)
    python.install_dependencies(config = config, packages = 'packages')
    add_arg = ' --static-libpython=no'
    if python.is_pyenv_python() and add_arg not in config.extra_args:
        pass
    if not dry_run:
        config.update_config()
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = TOOL_DESCRIPTION)
    parser.add_argument('-c', '--config-file', type = (lambda p: Path(p).absolute()), default = Path.cwd() / 'pysidedeploy.spec', help = 'Path to the .spec config file')
    parser.add_argument(type = (lambda p: Path(p).absolute()), help = 'Path to main python file', nargs = '?', dest = 'main_file', default = None if config_option_exists() else Path.cwd() / 'main.py')
    parser.add_argument('--init', action = 'store_true', help = "Create pysidedeploy.spec file, if it doesn't already exists")
    parser.add_argument('-v', '--verbose', help = 'Run in verbose mode', action = 'store_const', dest = 'loglevel', const = logging.INFO)
    parser.add_argument('--dry-run', action = 'store_true', help = 'Show the commands to be run')
    parser.add_argument('--keep-deployment-files', action = 'store_true', help = 'Keep the generated deployment files generated')
    parser.add_argument('-f', '--force', action = 'store_true', help = 'Force all input prompts')
    parser.add_argument('--name', type = str, help = 'Application name')
    parser.add_argument('--extra-ignore-dirs', type = str, help = HELP_EXTRA_IGNORE_DIRS)
    parser.add_argument('--extra-modules', type = str, help = HELP_EXTRA_MODULES)
    parser.add_argument('--mode', choices = [
        'onefile',
        'standalone'], default = 'onefile', help = HELP_MODE)
    args = parser.parse_args()
    main(args.main_file, args.name, args.config_file, args.init, args.loglevel, args.dry_run, args.keep_deployment_files, args.force, args.extra_ignore_dirs, args.extra_modules, args.mode)
    return None
