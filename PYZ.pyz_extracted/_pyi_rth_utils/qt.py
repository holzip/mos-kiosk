# Source Generated with Decompyle++
# File: qt.pyc (Python 3.12)

import os
import importlib
import atexit
_registered_qt_bindings = None

def ensure_single_qt_bindings_package(qt_bindings):
    pass
# WARNING: Decompyle incomplete

_QT_CONF_FILENAME = ':/qt/etc/qt.conf'
_QT_CONF_RESOURCE_NAME = b'\x00\x02\x00\x00\x07\x84\x00q\x00t\x00\x03\x00\x00l\xa3\x00e\x00t\x00c\x00\x07\x08t\xa6\xa6\x00q\x00t\x00.\x00c\x00o\x00n\x00f'
_QT_CONF_RESOURCE_STRUCT = b'\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\n\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'

def create_embedded_qt_conf(qt_bindings, prefix_path):
    
    try:
        QtCore = importlib.import_module(qt_bindings + '.QtCore')
        if QtCore.QFile.exists(_QT_CONF_FILENAME):
            return None
        if os.sep == '\\':
            prefix_path = prefix_path.replace(os.sep, '/')
        qt_conf = f'''[Paths]\nPrefix = {prefix_path}\n'''
        if os.name == 'nt' and qt_bindings in frozenset({'PySide2', 'PySide6'}):
            qt_conf += f'''LibraryExecutables = {prefix_path}'''
        if qt_bindings in frozenset({'PyQt5', 'PySide2'}):
            qt_conf = qt_conf.encode('latin1')
        else:
            qt_conf = qt_conf.encode('utf-8')
        qt_conf_size = len(qt_conf)
        qt_resource_data = qt_conf_size.to_bytes(4, 'big') + qt_conf
        succeeded = QtCore.qRegisterResourceData(1, _QT_CONF_RESOURCE_STRUCT, _QT_CONF_RESOURCE_NAME, qt_resource_data)
        if not succeeded:
            return None
        atexit.register(QtCore.qUnregisterResourceData, 1, _QT_CONF_RESOURCE_STRUCT, _QT_CONF_RESOURCE_NAME, qt_resource_data)
        return None
    except ImportError:
        return None


