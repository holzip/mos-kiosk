# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

import os
import sys
from pathlib import Path
from types import ModuleType
__pre_all__ = [
    'QtCore',
    'QtGui',
    'QtWidgets',
    'QtPrintSupport',
    'QtSql',
    'QtNetwork',
    'QtTest',
    'QtConcurrent',
    'QtDBus',
    'QtDesigner',
    'QtXml',
    'QtHelp',
    'QtMultimedia',
    'QtMultimediaWidgets',
    'QtOpenGL',
    'QtOpenGLWidgets',
    'QtPdf',
    'QtPdfWidgets',
    'QtPositioning',
    'QtLocation',
    'QtNetworkAuth',
    'QtNfc',
    'QtQml',
    'QtQuick',
    'QtQuick3D',
    'QtQuickControls2',
    'QtQuickTest',
    'QtQuickWidgets',
    'QtRemoteObjects',
    'QtScxml',
    'QtSensors',
    'QtSerialPort',
    'QtSerialBus',
    'QtStateMachine',
    'QtTextToSpeech',
    'QtCharts',
    'QtSpatialAudio',
    'QtSvg',
    'QtSvgWidgets',
    'QtDataVisualization',
    'QtGraphs',
    'QtGraphsWidgets',
    'QtBluetooth',
    'QtUiTools',
    'QtWebChannel',
    'QtWebEngineCore',
    'QtWebEngineWidgets',
    'QtWebEngineQuick',
    'QtWebSockets',
    'QtHttpServer',
    'QtWebView',
    'Qt3DCore',
    'Qt3DRender',
    'Qt3DInput',
    'Qt3DLogic',
    'Qt3DAnimation',
    'Qt3DExtras']
__version__ = '6.9.3'
__version_info__ = (6, 9, 3, '', '')
SKIP_MYPY_TEST = bool('')

def _additional_dll_directories(package_dir):
    root = Path(package_dir).parent
    if root.suffix == '.zip':
        return []
    shiboken6 = None / 'shiboken6'
    if shiboken6.is_dir():
        return [
            shiboken6]
    shiboken6 = None(root).parent / 'shiboken6' / 'libshiboken'
    if not shiboken6.is_dir():
        raise ImportError(str(shiboken6) + ' does not exist')
    result = [
        shiboken6,
        root / 'libpyside']
    libpysideqml = root / 'libpysideqml'
    if libpysideqml.is_dir():
        result.append(libpysideqml)
    for path in os.environ.get('PATH').split(';'):
        if not path:
            continue
        if not (Path(path) / 'qmake.exe').exists():
            continue
        result.append(path)
        os.environ.get('PATH').split(';')
        return result
    return result


def _setupQtDirectories():
    global Shiboken
    pyside_package_dir = Path(__file__).parent.resolve()
    if sys.platform == 'win32':
        for dir in _additional_dll_directories(pyside_package_dir):
            os.add_dll_directory(os.fspath(dir))
    
    try:
        Shiboken = Shiboken
        import shiboken6
        if sys.platform == 'win32':
            os.environ['PATH'] = os.fspath(pyside_package_dir) + os.pathsep + os.environ['PATH']
            openssl_dir = pyside_package_dir / 'openssl'
            if openssl_dir.exists():
                path = os.environ['PATH']
                
                try:
                    os.environ['PATH'] = os.fspath(openssl_dir) + os.pathsep + path
                    
                    try:
                        QtNetwork = QtNetwork
                        import 
                        
                        try:
                            QtNetwork.QSslSocket.supportsSsl()
                            os.environ['PATH'] = path
                            return None
                            return None
                            return None
                            except Exception:
                                e = None
                                paths = ', '.join(sys.path)
                                print(f'''PySide6/__init__.py: Unable to import Shiboken from {paths}: {e}''', file = sys.stderr)
                                raise 
                                e = None
                                del e
                            except ImportError:
                                
                                try:
                                    continue
                                    
                                    try:
                                        pass
                                    except:
                                        os.environ['PATH'] = path








def _find_all_qt_modules():
    unordered = set()
    pattern = 'Qt*.pyd' if sys.platform == 'win32' else 'Qt*.so'
    for module in Path(__file__).resolve().parent.glob(pattern):
        name = module.name[:module.name.find('.')]
        if name.endswith('_d'):
            name = name[:-2]
        unordered.add(name)
    ordered_part = __pre_all__
    result = []
    for name in ordered_part:
        if not name in unordered:
            continue
        result.append(name)
        unordered.remove(name)
    result.extend(unordered)
    return result


def __getattr__(name = None):
    global __all__
    if name == '__all__':
        __all__ = _find_all_qt_modules()
        return __all__
    raise None(f'''module \'{__name__}\' has no attribute \'{name}\' :)''')


class ModuleDict(dict):
    
    def __missing__(self, key):
        if key == '__all__':
            self[key] = __all__ if '__all__' in globals() else __getattr__('__all__')
            return __all__
        raise None(f'''dict of module \'{__name__}\' has no key \'{key}\' :)''')



class SubModule(ModuleType):
    pass

_setupQtDirectories()
Shiboken.replaceModuleDict(sys.modules['PySide6'], SubModule, ModuleDict(globals()))
