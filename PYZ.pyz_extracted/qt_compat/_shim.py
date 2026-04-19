# Source Generated with Decompyle++
# File: _shim.pyc (Python 3.12)

'''Шим PySide6 → PyQt6: создаёт фейковый пакет PySide6 в sys.modules.

После install() все ``from PySide6.QtXxx import ...`` прозрачно
идут через PyQt6, с трансляцией:
  - PySide6.QtCore.Signal  → PyQt6.QtCore.pyqtSignal
  - PySide6.QtCore.Slot    → PyQt6.QtCore.pyqtSlot
  - PySide6.QtCore.Property → PyQt6.QtCore.pyqtProperty

Остальные классы и функции одинаковы в PySide6 и PyQt6.
'''
import importlib
import sys
import types
_SUBMODULE_MAP = {
    'PySide6.QtCore': 'PyQt6.QtCore',
    'PySide6.QtGui': 'PyQt6.QtGui',
    'PySide6.QtWidgets': 'PyQt6.QtWidgets',
    'PySide6.QtNetwork': 'PyQt6.QtNetwork',
    'PySide6.QtWebEngineCore': 'PyQt6.QtWebEngineCore',
    'PySide6.QtWebEngineWidgets': 'PyQt6.QtWebEngineWidgets',
    'PySide6.QtWebChannel': 'PyQt6.QtWebChannel',
    'PySide6.QtPrintSupport': 'PyQt6.QtPrintSupport' }

def _make_qtcore_shim():
    '''Создать модуль-обёртку для QtCore с трансляцией Signal/Slot.'''
    real = importlib.import_module('PyQt6.QtCore')
    shim = types.ModuleType('PySide6.QtCore')
    shim.__dict__.update(real.__dict__)
    shim.Signal = real.pyqtSignal
    shim.Slot = real.pyqtSlot
    shim.Property = real.pyqtProperty
    return shim


def _make_submodule_shim(pyside_name = None, pyqt_name = None):
    '''Создать модуль-обёртку для произвольного подмодуля.'''
    real = importlib.import_module(pyqt_name)
    shim = types.ModuleType(pyside_name)
    shim.__dict__.update(real.__dict__)
    return shim


def _make_webenginewidgets_shim():
    '''Шим для QtWebEngineWidgets — дополнительные маппинги.'''
    real = importlib.import_module('PyQt6.QtWebEngineWidgets')
    shim = types.ModuleType('PySide6.QtWebEngineWidgets')
    shim.__dict__.update(real.__dict__)
    
    try:
        QWebEngineProfile = QWebEngineProfile
        QWebEngineSettings = QWebEngineSettings
        QWebEnginePage = QWebEnginePage
        import PyQt6.QtWebEngineCore
        if not hasattr(shim, 'QWebEngineProfile'):
            shim.QWebEngineProfile = QWebEngineProfile
        if not hasattr(shim, 'QWebEngineSettings'):
            shim.QWebEngineSettings = QWebEngineSettings
        if not hasattr(shim, 'QWebEnginePage'):
            shim.QWebEnginePage = QWebEnginePage
        return shim
    except ImportError:
        return shim



def install():
    '''Установить фейковый PySide6 пакет в sys.modules.'''
    if 'PySide6' in sys.modules:
        return None
    fake_pyside6 = types.ModuleType('PySide6')
    fake_pyside6.__path__ = []
    fake_pyside6.__version__ = 'shim-over-PyQt6'
    sys.modules['PySide6'] = fake_pyside6
    qtcore_shim = _make_qtcore_shim()
    sys.modules['PySide6.QtCore'] = qtcore_shim
    fake_pyside6.QtCore = qtcore_shim
    
    try:
        we_shim = _make_webenginewidgets_shim()
        sys.modules['PySide6.QtWebEngineWidgets'] = we_shim
        fake_pyside6.QtWebEngineWidgets = we_shim
        for pyside_name, pyqt_name in _SUBMODULE_MAP.items():
            if pyside_name in sys.modules:
                continue
            shim = _make_submodule_shim(pyside_name, pyqt_name)
            sys.modules[pyside_name] = shim
            attr_name = pyside_name.split('.')[-1]
            setattr(fake_pyside6, attr_name, shim)
        return None
    except ImportError:
        continue
        except ImportError:
            continue


