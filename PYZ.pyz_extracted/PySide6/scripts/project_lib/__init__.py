# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

from __future__ import annotations
from dataclasses import dataclass
QTPATHS_CMD = 'qtpaths6'
MOD_CMD = 'pyside6-metaobjectdump'
PYPROJECT_TOML_PATTERN = 'pyproject.toml'
PYPROJECT_JSON_PATTERN = '*.pyproject'
PYPROJECT_FILE_PATTERNS = [
    PYPROJECT_TOML_PATTERN,
    PYPROJECT_JSON_PATTERN]
QMLDIR_FILE = 'qmldir'
QML_IMPORT_NAME = 'QML_IMPORT_NAME'
QML_IMPORT_MAJOR_VERSION = 'QML_IMPORT_MAJOR_VERSION'
QML_IMPORT_MINOR_VERSION = 'QML_IMPORT_MINOR_VERSION'
QT_MODULES = 'QT_MODULES'
METATYPES_JSON_SUFFIX = 'metatypes.json'
TRANSLATION_SUFFIX = '.ts'
SHADER_SUFFIXES = ('.vert', '.frag')

class Singleton(type):
    pass
# WARNING: Decompyle incomplete


def ClOptions():
    '''ClOptions'''
    qml_module: 'bool' = '\n    Dataclass to store the cl options that needs to be passed as arguments.\n    '

ClOptions = <NODE:27>(ClOptions, 'ClOptions', metaclass = Singleton)()
from utils import run_command, requires_rebuild, remove_path, package_dir, qtpaths, qt_metatype_json_dir, resolve_valid_project_file
from project_data import is_python_file, ProjectData, QmlProjectData, check_qml_decorators
from newproject import new_project, NewProjectTypes
from design_studio_project import DesignStudioProject
from pyproject_toml import parse_pyproject_toml, write_pyproject_toml, migrate_pyproject
from pyproject_json import parse_pyproject_json
