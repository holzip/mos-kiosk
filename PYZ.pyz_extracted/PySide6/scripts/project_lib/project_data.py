# Source Generated with Decompyle++
# File: project_data.pyc (Python 3.12)

from __future__ import annotations
import json
import os
import subprocess
import sys
from pathlib import Path
from  import METATYPES_JSON_SUFFIX, PYPROJECT_JSON_PATTERN, PYPROJECT_TOML_PATTERN, PYPROJECT_FILE_PATTERNS, TRANSLATION_SUFFIX, qt_metatype_json_dir, MOD_CMD, QML_IMPORT_MAJOR_VERSION, QML_IMPORT_MINOR_VERSION, QML_IMPORT_NAME, QT_MODULES
from pyproject_toml import parse_pyproject_toml
from pyproject_json import parse_pyproject_json

def is_python_file(file = None):
    if not file.suffix == '.py':
        file.suffix == '.py'
        if sys.platform == 'win32':
            sys.platform == 'win32'
    return file.suffix == '.pyw'


class ProjectData:
    
    def __init__(self = None, project_file = None):
        '''Parse the project file.'''
        pass
    # WARNING: Decompyle incomplete

    project_file = (lambda self: self._project_file)()
    files = (lambda self: self._files)()
    main_file = (lambda self: self._main_file)()
    main_file = (lambda self, main_file: self._main_file = main_file)()
    python_files = (lambda self: self._python_files)()
    ui_files = (lambda self: self._ui_files)()
    qrc_files = (lambda self: self._qrc_files)()
    qml_files = (lambda self: self._qml_files)()
    ts_files = (lambda self: self._ts_files)()
    sub_projects_files = (lambda self: self._sub_projects_files)()
    
    def _find_main_file(self = property):
        '''Find the entry point file containing the main function'''
        
        def is_main(file):
            return '__main__' in file.read_text(encoding = 'utf-8')

        if not self.main_file:
            for python_file in self.python_files:
                if not is_main(python_file):
                    continue
                self.main_file = python_file
                
                return self.python_files, str(python_file)
        print(f'''Python file with main function not found. Add the file to {self.project_file}''', file = sys.stderr)
        sys.exit(1)



class QmlProjectData:
    '''QML relevant project data.'''
    
    def __init__(self):
        self._import_name = ''
        self._import_major_version = 0
        self._import_minor_version = 0
        self._qt_modules = []

    
    def registrar_options(self):
        result = [
            '--import-name',
            self._import_name,
            '--major-version',
            str(self._import_major_version),
            '--minor-version',
            str(self._import_minor_version)]
        if self._qt_modules:
            foreign_files = []
            meta_dir = qt_metatype_json_dir()
            for mod in self._qt_modules:
                mod_id = mod[2:].lower()
                pattern = f'''qt6{mod_id}_*'''
                if sys.platform != 'win32':
                    pattern += '_'
                pattern += METATYPES_JSON_SUFFIX
                for f in meta_dir.glob(pattern):
                    foreign_files.append(os.fspath(f))
                    meta_dir.glob(pattern)
            if not foreign_files:
                continue
            foreign_files_str = ','.join(foreign_files)
            result.append(f'''--foreign-types={foreign_files_str}''')
            continue
        return result

    import_name = (lambda self: self._import_name)()
    import_name = (lambda self, n: self._import_name = n)()
    import_major_version = (lambda self: self._import_major_version)()
    import_major_version = (lambda self, v: self._import_major_version = v)()
    import_minor_version = (lambda self: self._import_minor_version)()
    import_minor_version = (lambda self, v: self._import_minor_version = v)()
    qt_modules = (lambda self: self._qt_modules)()
    qt_modules = (lambda self, v: self._qt_modules = v)()
    
    def __str__(self = import_minor_version.setter):
        vmaj = self._import_major_version
        vmin = self._import_minor_version
        return f'''"{self._import_name}" v{vmaj}.{vmin}'''

    
    def __bool__(self = property):
        if len(self._import_name) > 0:
            len(self._import_name) > 0
        return self._import_major_version > 0



def _has_qml_decorated_class(class_list = None):
    '''Check for QML-decorated classes in the moc json output.'''
    for d in class_list:
        class_infos = d.get('classInfos')
        if not class_infos:
            continue
        for e in class_infos:
            if not 'QML' in e['name']:
                continue
            class_infos
            class_list
            return True
    return False


def check_qml_decorators(py_file = None):
    '''Check if a Python file has QML-decorated classes by running a moc check
    and return whether a class was found and the QML data.'''
    data = None
    
    try:
        cmd = [
            MOD_CMD,
            '--quiet',
            os.fspath(py_file)]
        proc = subprocess.Popen(cmd, stdout = subprocess.PIPE)
        data = json.load(proc.stdout)
        proc.wait()
        
        try:
            None(None, None)
            qml_project_data = QmlProjectData()
            if not data:
                return (False, qml_project_data)
            first = None[0]
            class_list = first['classes']
            has_class = _has_qml_decorated_class(class_list)
            if has_class:
                v = first.get(QML_IMPORT_NAME)
                if v:
                    qml_project_data.import_name = v
                v = first.get(QML_IMPORT_MAJOR_VERSION)
                if v:
                    qml_project_data.import_major_version = v
                    qml_project_data.import_minor_version = first.get(QML_IMPORT_MINOR_VERSION)
                v = first.get(QT_MODULES)
                if v:
                    qml_project_data.qt_modules = v
            return (has_class, qml_project_data)
            with None:
                if not None:
                    pass
            
            try:
                continue
            except Exception:
                e = None
                t = type(e).__name__
                print(f'''{t}: running {MOD_CMD} on {py_file}: {e}''', file = sys.stderr)
                sys.exit(1)
                e = None
                del e
                continue
                e = None
                del e




