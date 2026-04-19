# Source Generated with Decompyle++
# File: utils.pyc (Python 3.12)

from __future__ import annotations
import subprocess
import sys

ElementTree
from pathlib import Path
import xml.etree.ElementTree, etree
from  import QTPATHS_CMD, PYPROJECT_JSON_PATTERN, PYPROJECT_TOML_PATTERN, PYPROJECT_FILE_PATTERNS, ClOptions
from pyproject_toml import parse_pyproject_toml
from pyproject_json import parse_pyproject_json

def run_command(command = None, cwd = None, ignore_fail = None):
    '''
    Run a command using a subprocess.
    If dry run is enabled, the command will be printed to stdout instead of being executed.

    :param command: The command to run including the arguments
    :param cwd: The working directory to run the command in
    :param ignore_fail: If True, the current process will not exit if the command fails

    :return: The exit code of the command
    '''
    cloptions = ClOptions()
    if cloptions.quiet or cloptions.dry_run:
        print(' '.join(command))
    if cloptions.dry_run:
        return 0
    ex = subprocess.call(command, cwd = cwd)
    if not ex != 0 and ignore_fail:
        sys.exit(ex)
    return ex


def qrc_file_requires_rebuild(resources_file_path = None, compiled_resources_path = None):
    '''Returns whether a compiled qrc file needs to be rebuilt based on the files that references'''
    pass
# WARNING: Decompyle incomplete


def requires_rebuild(sources = None, artifact = None):
    '''Returns whether artifact needs to be rebuilt depending on sources'''
    if not artifact.is_file():
        return True
    artifact_mod_time = artifact.stat().st_mtime
    for source in sources:
        if source.stat().st_mtime > artifact_mod_time:
            sources
            return True
        if not source.suffix == '.qrc':
            continue
        if not qrc_file_requires_rebuild(source, artifact):
            continue
        return True
    return False


def _remove_path_recursion(path = None):
    '''Recursion to remove a file or directory.'''
    if path.is_file():
        path.unlink()
        return None
    if path.is_dir():
        for item in path.iterdir():
            _remove_path_recursion(item)
        path.rmdir()
        return None


def remove_path(path = None):
    '''Remove path (file or directory) observing opt_dry_run.'''
    cloptions = ClOptions()
    if not path.exists():
        return None
    if not cloptions.quiet:
        print(f'''Removing {path.name}...''')
    if cloptions.dry_run:
        return None
    _remove_path_recursion(path)


def package_dir():
    '''Return the PySide6 root.'''
    return Path(__file__).resolve().parents[2]

_qtpaths_info: 'dict[str, str]' = { }

def qtpaths():
    '''Run qtpaths and return a dict of values.'''
    if not _qtpaths_info:
        output = subprocess.check_output([
            QTPATHS_CMD,
            '--query'])
        for line in output.decode('utf-8').split('\n'):
            tokens = line.strip().split(':', maxsplit = 1)
            if not len(tokens) == 2:
                continue
            _qtpaths_info[tokens[0]] = tokens[1]
    return _qtpaths_info

_qt_metatype_json_dir: 'Path | None' = None

def qt_metatype_json_dir():
    '''Return the location of the Qt QML metatype files.'''
    global _qt_metatype_json_dir, _qt_metatype_json_dir
    if not _qt_metatype_json_dir:
        qt_dir = package_dir()
        if sys.platform != 'win32':
            qt_dir /= 'Qt'
        metatypes_dir = qt_dir / 'metatypes'
        if metatypes_dir.is_dir():
            _qt_metatype_json_dir = metatypes_dir
            return _qt_metatype_json_dir
        None(f'''Falling back to {QTPATHS_CMD} to determine metatypes directory.''', file = sys.stderr)
        _qt_metatype_json_dir = Path(qtpaths()['QT_INSTALL_ARCHDATA']) / 'metatypes'
    return _qt_metatype_json_dir


def resolve_valid_project_file(project_path_input = None, project_file_patterns = None):
    '''
    Find a valid project file given a preferred project file name and a list of project file name
    patterns for a fallback search.

    If the provided file name is a valid project file, return it. Otherwise, search for a known
    project file in the current working directory with the given patterns.

    Raises a ValueError if no project file is found, multiple project files are found in the same
    directory or the provided path is not a valid project file or folder.

    :param project_path_input: The command-line argument specifying a project file or folder path.
    :param project_file_patterns: The list of project file patterns to search for.

    :return: The resolved project file path
    '''
    if project_path_input:
        project_file = Path(project_path_input).resolve()
        if Path(project_path_input).resolve().is_file():
            if project_file.match(PYPROJECT_TOML_PATTERN):
                if bool(parse_pyproject_toml(project_file).errors):
                    raise ValueError(f'''Invalid project file: {project_file}''')
                return project_file
            if None.match(PYPROJECT_JSON_PATTERN):
                pyproject_json_result = parse_pyproject_json(project_file)
                errors = (lambda .0: pass# WARNING: Decompyle incomplete
)(pyproject_json_result.errors())
                if (lambda .0: pass# WARNING: Decompyle incomplete
)(pyproject_json_result.errors()):
                    raise ValueError(f'''Invalid project file: {project_file}\n{errors}''')
                return project_file
            raise None(f'''Unknown project file: {project_file}''')
    project_folder = Path.cwd()
    if project_path_input:
        if not Path(project_path_input).resolve().is_dir():
            raise ValueError(f'''Invalid project path: {project_path_input}''')
        project_folder = Path(project_path_input).resolve()
    for pattern in project_file_patterns:
        matches = list(project_folder.glob(pattern))
        if not list(project_folder.glob(pattern)):
            continue
        if len(matches) > 1:
            matched_files = (lambda .0: pass# WARNING: Decompyle incomplete
)(matches())
            raise ValueError(f'''Multiple project files found:\n{matched_files}''')
        project_file = matches[0]
        if pattern == PYPROJECT_TOML_PATTERN:
            if parse_pyproject_toml(project_file).errors:
                continue
            
            return project_file_patterns, project_file
        if project_file_patterns == PYPROJECT_JSON_PATTERN:
            (lambda .0: pass# WARNING: Decompyle incomplete
)(pyproject_json_result.errors()) = (lambda .0: pass# WARNING: Decompyle incomplete
)(pyproject_json_result.errors())
            if '\n'.join:
                raise ValueError(f'''Invalid project file: {project_file}\n{errors}''')
        
        return None, project_file
    raise ValueError('No project file found in the current directory')

