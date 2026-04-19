# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

'''Прослойка совместимости PySide6 ↔ PyQt6.

Позволяет коду проекта использовать импорты PySide6,
при этом на системах где PySide6 недоступен (но есть PyQt6)
автоматически подставляется PyQt6.

Использование:
    Вместо  ``from PySide6.QtWidgets import ...``
    пишем   ``from qt_compat.QtWidgets import ...``

    Или (рекомендуемый вариант): при запуске mt_kiosk.py
    автоматически подставляется фейковый модуль PySide6,
    и существующий код не нужно менять.

Порядок приоритета:
    1. PySide6 (если установлен — используем как есть)
    2. PyQt6  (используем через shim, подменяя Signal/Slot/etc.)
'''
import importlib
import sys
QT_BINDING: str = ''

try:
    import PySide6
    QT_BINDING = 'PySide6'
    
    def _install_pyside6_shim():
        '''Установить фейковый PySide6 модуль, перенаправляющий в PyQt6.

    После вызова ``from PySide6.QtWidgets import ...`` будет работать
    даже если PySide6 не установлен — импорт прозрачно уходит в PyQt6.
    '''
        if QT_BINDING == 'PySide6':
            return None
        _shim = _shim
        import qt_compat
        _shim.install()

    return None
except ImportError:
    import PyQt6
    QT_BINDING = 'PyQt6'
except ImportError:
    raise ImportError('Ни PySide6 ни PyQt6 не установлены.\nУстановите один из них:\n  pip install PySide6\n  # или (ROSA/Fedora):\n  sudo dnf install python3-qt6-webengine python3-qt6-widgets')

continue
