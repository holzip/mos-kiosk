# Source Generated with Decompyle++
# File: pyi_rth_pyside6.pyc (Python 3.12)


def _pyi_rthook():
    import os
    import sys
    is_macos_app_bundle = is_macos_app_bundle
    prepend_path_to_environment_variable = prepend_path_to_environment_variable
    import _pyi_rth_utils
    qt_rth_utils = qt
    import _pyi_rth_utils
    qt_rth_utils.ensure_single_qt_bindings_package('PySide6')
    if sys.platform.startswith('win'):
        pyqt_path = os.path.join(sys._MEIPASS, 'PySide6')
    else:
        pyqt_path = os.path.join(sys._MEIPASS, 'PySide6', 'Qt')
    os.environ['QT_PLUGIN_PATH'] = os.path.join(pyqt_path, 'plugins')
    if is_macos_app_bundle:
        pyqt_path_res = os.path.normpath(os.path.join(sys._MEIPASS, '..', 'Resources', os.path.relpath(pyqt_path, sys._MEIPASS)))
        os.environ['QML2_IMPORT_PATH'] = os.pathsep.join([
            os.path.join(pyqt_path_res, 'qml'),
            os.path.join(pyqt_path, 'qml')])
    else:
        os.environ['QML2_IMPORT_PATH'] = os.path.join(pyqt_path, 'qml')
    if sys.platform.startswith('win'):
        prepend_path_to_environment_variable(sys._MEIPASS, 'PATH')
    if not sys.platform == 'darwin' and is_macos_app_bundle:
        prepend_path_to_environment_variable(sys._MEIPASS, 'DYLD_LIBRARY_PATH')
    qt_rth_utils.create_embedded_qt_conf('PySide6', pyqt_path)

_pyi_rthook()
del _pyi_rthook
