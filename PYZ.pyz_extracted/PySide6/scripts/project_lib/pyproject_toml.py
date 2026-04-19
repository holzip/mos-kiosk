# Source Generated with Decompyle++
# File: pyproject_toml.pyc (Python 3.12)

from __future__ import annotations
import sys
if sys.version_info >= (3, 11):
    import tomllib
from pathlib import Path
from  import PYPROJECT_JSON_PATTERN
from pyproject_parse_result import PyProjectParseResult
from pyproject_json import parse_pyproject_json

def _parse_toml_content(content = None):
    '''
    Parse TOML content for project name and files list only.
    '''
    result = {
        'project': { },
        'tool': {
            'pyside6-project': { } } }
    current_section = None
# WARNING: Decompyle incomplete


def _write_toml_content(data = None):
    '''
    Write minimal TOML content with project and tool.pyside6-project sections.
    '''
    lines = []
    if 'project' in data and data['project']:
        lines.append('[project]')
        for key, value in sorted(data['project'].items()):
            if not isinstance(value, str):
                continue
            lines.append(f'''{key} = "{value}"''')
# WARNING: Decompyle incomplete


def parse_pyproject_toml(pyproject_toml_file = None):
    '''
    Parse a pyproject.toml file and return a PyProjectParseResult object.
    '''
    result = PyProjectParseResult()
    
    try:
        content = pyproject_toml_file.read_text(encoding = 'utf-8')
        if sys.version_info >= (3, 11):
            root_table = tomllib.loads(content)
            print('Using tomllib for parsing TOML content')
        else:
            root_table = _parse_toml_content(content)
        pyside_table = root_table.get('tool', { }).get('pyside6-project', { })
        if not pyside_table:
            result.errors.append('Missing [tool.pyside6-project] table')
            return result
        files = None.get('files', [])
        if not isinstance(files, list):
            result.errors.append('Missing or invalid files list')
            return result
        for file in None:
            if not isinstance(file, str):
                result.errors.append(f'''Invalid file: {file}''')
                
                return None, result
            if not file_path.is_absolute():
                (pyproject_toml_file.parent / file).resolve() = None(file)
            result.files.append(file_path)
        return result
    except Exception:
        e = None
        result.errors.append(str(e))
        del e
        return None
        None = 
        del e



def write_pyproject_toml(pyproject_file = None, project_name = None, project_files = None):
    '''
    Create or update a pyproject.toml file with the specified content.
    '''
    data = {
        'project': {
            'name': project_name },
        'tool': {
            'pyside6-project': {
                'files': sorted(project_files) } } }
    
    try:
        content = _write_toml_content(data)
        pyproject_file.write_text(content, encoding = 'utf-8')
        return None
    except Exception:
        e = None
        raise ValueError(f'''Error writing TOML file: {str(e)}''')
        e = None
        del e



def migrate_pyproject(pyproject_file = None):
    '''
    Migrate a project *.pyproject JSON file to the new pyproject.toml format.

    The containing subprojects are migrated recursively.

    :return: 0 if successful, 1 if an error occurred.
    '''
    pass
# WARNING: Decompyle incomplete

