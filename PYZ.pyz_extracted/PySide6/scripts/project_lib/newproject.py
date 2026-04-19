# Source Generated with Decompyle++
# File: newproject.pyc (Python 3.12)

from __future__ import annotations
import os
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from pyproject_toml import write_pyproject_toml
from pyproject_json import write_pyproject_json
_WIDGET_MAIN = "if __name__ == '__main__':\n    app = QApplication(sys.argv)\n    window = MainWindow()\n    window.show()\n    sys.exit(app.exec())\n"
_WIDGET_IMPORTS = 'import sys\nfrom PySide6.QtWidgets import QApplication, QMainWindow\n'
_WIDGET_CLASS_DEFINITION = 'class MainWindow(QMainWindow):\n    def __init__(self):\n        super().__init__()\n'
_WIDGET_SETUP_UI_CODE = '        self._ui = Ui_MainWindow()\n        self._ui.setupUi(self)\n'
_MAINWINDOW_FORM = '<?xml version="1.0" encoding="UTF-8"?>\n<ui version="4.0">\n <class>MainWindow</class>\n <widget class="QMainWindow" name="MainWindow">\n  <property name="geometry">\n   <rect>\n    <x>0</x>\n    <y>0</y>\n    <width>800</width>\n    <height>600</height>\n   </rect>\n  </property>\n  <property name="windowTitle">\n   <string>MainWindow</string>\n  </property>\n  <widget class="QWidget" name="centralwidget"/>\n  <widget class="QMenuBar" name="menubar">\n   <property name="geometry">\n    <rect>\n     <x>0</x>\n     <y>0</y>\n     <width>800</width>\n     <height>22</height>\n    </rect>\n   </property>\n  </widget>\n  <widget class="QStatusBar" name="statusbar"/>\n </widget>\n</ui>\n'
_QUICK_FORM = 'import QtQuick\nimport QtQuick.Controls\n\nApplicationWindow {\n    id: window\n    width: 1024\n    height: 600\n    visible: true\n}\n'
_QUICK_MAIN = 'import sys\nfrom pathlib import Path\n\nfrom PySide6.QtGui import QGuiApplication\nfrom PySide6.QtCore import QUrl\nfrom PySide6.QtQml import QQmlApplicationEngine\n\n\nif __name__ == "__main__":\n    app = QGuiApplication()\n    engine = QQmlApplicationEngine()\n    qml_file = Path(__file__).parent / \'main.qml\'\n    engine.load(QUrl.fromLocalFile(qml_file))\n    if not engine.rootObjects():\n        sys.exit(-1)\n    exit_code = app.exec()\n    del engine\n    sys.exit(exit_code)\n'
NewProjectFiles = list[tuple[(str, str)]]
NewProjectType = <NODE:12>()

def _write_project(directory = None, files = None, legacy_pyproject = dataclass(frozen = True)):
    '''
    Create the project files in the specified directory.

    :param directory: The directory to create the project in.
    :param files: The files that belong to the project to create.
    '''
    file_names = []
    for file_name, contents in files:
        (directory / file_name).write_text(contents)
        print(f'''Wrote {directory.name}{os.sep}{file_name}.''')
        file_names.append(file_name)
    if legacy_pyproject:
        pyproject_file = directory / f'''{directory.name}.pyproject'''
        write_pyproject_json(pyproject_file, file_names)
    else:
        pyproject_file = directory / 'pyproject.toml'
        write_pyproject_toml(pyproject_file, directory.name, file_names)
    print(f'''Wrote {pyproject_file}.''')


def _widget_project():
    '''Create a (form-less) widgets project.'''
    main_py = _WIDGET_IMPORTS + '\n\n' + _WIDGET_CLASS_DEFINITION + '\n\n' + _WIDGET_MAIN
    return [
        ('main.py', main_py)]


def _ui_form_project():
    '''Create a Qt Designer .ui form based widgets project.'''
    main_py = _WIDGET_IMPORTS + '\nfrom ui_mainwindow import Ui_MainWindow\n\n\n' + _WIDGET_CLASS_DEFINITION + _WIDGET_SETUP_UI_CODE + '\n\n' + _WIDGET_MAIN
    return [
        ('main.py', main_py),
        ('mainwindow.ui', _MAINWINDOW_FORM)]


def _qml_project():
    '''Create a QML project.'''
    return [
        ('main.py', _QUICK_MAIN),
        ('main.qml', _QUICK_FORM)]


class NewProjectTypes(Enum):
    QUICK = NewProjectType('new-quick', 'Create a new Qt Quick project', _qml_project())
    WIDGET_FORM = NewProjectType('new-ui', 'Create a new Qt Widgets Form project', _ui_form_project())
    WIDGET = NewProjectType('new-widget', 'Create a new Qt Widgets project', _widget_project())
    find_by_command = (lambda command = None: pass# WARNING: Decompyle incomplete
)()


def new_project(project_dir = None, project_type = None, legacy_pyproject = None):
    '''
    Create a new project at the specified project_dir directory.

    :param project_dir: The directory path to create the project. If existing, must be empty.
    :param project_type: The Qt type of project to create (Qt Widgets, Qt Quick, etc.)

    :return: 0 if the project was created successfully, otherwise 1.
    '''
    if any(project_dir.iterdir()):
        print(f'''Can not create project at {project_dir}: directory is not empty.''', file = sys.stderr)
        return 1
    project_dir.mkdir(parents = True, exist_ok = True)
    
    try:
        _write_project(project_dir, project_type.files, legacy_pyproject)
        if project_type == NewProjectTypes.WIDGET_FORM:
            print(f'''Run "pyside6-project build {project_dir}" to build the project''')
        print(f'''Run "pyside6-project run {project_dir / 'main.py'}" to run the project''')
        return 0
    except Exception:
        e = None
        print(f'''Error creating project file: {str(e)}''', file = sys.stderr)
        e = None
        del e
        return 1
        e = None
        del e


