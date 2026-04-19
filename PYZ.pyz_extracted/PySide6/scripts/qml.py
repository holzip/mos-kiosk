# Source Generated with Decompyle++
# File: qml.pyc (Python 3.12)

from __future__ import annotations
import argparse
import importlib.util as importlib
import logging
import sys
import os
from pathlib import Path
from pprint import pprint
from PySide6.QtCore import QCoreApplication, Qt, QLibraryInfo, QUrl, SignalInstance
from PySide6.QtGui import QGuiApplication, QSurfaceFormat
from PySide6.QtQml import QQmlApplicationEngine, QQmlComponent
from PySide6.QtQuick import QQuickView, QQuickItem
from PySide6.QtWidgets import QApplication

def import_qml_modules(qml_parent_path = None, module_paths = None):
    '''
    Import all the python modules in the qml_parent_path. This way all the classes
    containing the @QmlElement/@QmlNamedElement are also imported

        Parameters:
                qml_parent_path (Path): Parent directory of the qml file
                module_paths (int): user give import paths obtained through cli
    '''
    search_dir_paths = []
    search_file_paths = []
    if not module_paths:
        search_dir_paths.append(qml_parent_path)
    else:
        for module_path in module_paths:
            if module_path.is_dir():
                search_dir_paths.append(module_path)
                continue
            if not module_path.exists():
                continue
            if not module_path.suffix == '.py':
                continue
            search_file_paths.append(module_path)
    
    def import_module(import_module_paths = None):
        """Import the modules in 'import_module_paths'"""
        for module_path in import_module_paths:
            module_name = module_path.name[:-3]
            _spec = importlib.util.spec_from_file_location(f'''{module_name}''', module_path)
            _module = importlib.util.module_from_spec(_spec)
            _spec.loader.exec_module(module = _module)

    modules_to_import = set()
    for search_path in search_dir_paths:
        possible_modules = list(search_path.glob('**/*.py'))
        for possible_module in possible_modules:
            if not possible_module.is_file():
                continue
            if not possible_module.name != '__init__.py':
                continue
            module_parent = str(possible_module.parent)
            if module_parent not in sys.path:
                sys.path.append(module_parent)
            modules_to_import.add(possible_module)
    for search_path in search_file_paths:
        sys.path.append(str(search_path.parent))
        modules_to_import.add(search_path)
    import_module(import_module_paths = modules_to_import)


def print_configurations():
    return 'Built-in configurations \n\t default \n\t resizeToItem'

# WARNING: Decompyle incomplete
