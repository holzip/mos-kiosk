# Source Generated with Decompyle++
# File: generate_pyi.pyc (Python 3.12)

from __future__ import annotations
import argparse
import inspect
import logging
import os
import sys
import typing
from pathlib import Path
from types import SimpleNamespace
USE_PEP563 = sys.version_info[:2] >= (3, 7)

def generate_all_pyi(outpath, options):
    ps = os.pathsep
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'This script generates the .pyi file for all PySide modules.')
    parser.add_argument('modules', nargs = '+', help = "'all' or the names of modules to build (QtCore QtGui etc.)")
    parser.add_argument('--quiet', action = 'store_true', help = 'Run quietly')
    parser.add_argument('--outpath', help = 'the output directory (default = binary location)')
    parser.add_argument('--sys-path', nargs = '+', help = 'a list of strings prepended to sys.path')
    parser.add_argument('--feature', nargs = '+', choices = [
        'snake_case',
        'true_property'], default = [], help = 'a list of feature names. Example: `--feature snake_case true_property`. Currently not available for PyPy.')
    options = parser.parse_args()
    qtest_env = os.environ.get('QTEST_ENVIRONMENT', '')
    log_level = logging.DEBUG if qtest_env else logging.INFO
    if options.quiet:
        log_level = logging.WARNING
    logging.basicConfig(level = log_level)
    logger = logging.getLogger('generate_pyi')
    outpath = options.outpath
    if not outpath and Path(outpath).exists():
        os.makedirs(outpath)
        logger.info(f'''+++ Created path {outpath}''')
    options._pyside_call = True
    options.logger = logger
    options.is_ci = qtest_env == 'ci'
    generate_all_pyi(outpath, options = options)
    return None
