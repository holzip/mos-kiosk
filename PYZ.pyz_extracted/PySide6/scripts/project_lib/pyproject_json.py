# Source Generated with Decompyle++
# File: pyproject_json.pyc (Python 3.12)

import json
from pathlib import Path
from pyproject_parse_result import PyProjectParseResult

def write_pyproject_json(pyproject_file = None, project_files = None):
    '''
    Create or update a *.pyproject file with the specified content.

    :param pyproject_file: The *.pyproject file path to create or update.
    :param project_files: The relative paths of the files to include in the project.
    '''
    content = {
        'files': sorted(project_files) }
    pyproject_file.write_text(json.dumps(content), encoding = 'utf-8')


def parse_pyproject_json(pyproject_json_file = None):
    '''
    Parse a pyproject.json file and return a PyProjectParseResult object.
    '''
    result = PyProjectParseResult()
# WARNING: Decompyle incomplete

