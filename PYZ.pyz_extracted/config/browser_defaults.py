# Source Generated with Decompyle++
# File: browser_defaults.pyc (Python 3.12)

'''Значения по умолчанию для браузера без зависимости от Qt.

Версия Chromium в User-Agent должна совпадать с базой Upstream Chromium в
используемом Qt WebEngine. Целевая сборка: PySide6 6.9.x (Qt 6.9.3 →
Chromium 130.0.6723.192). Таблица версий:
https://wiki.qt.io/QtWebEngine/ChromiumVersions

При смене PySide6/Qt обновите CHROMIUM_VERSION_STRING по вики (или
``qWebEngineChromiumVersion()`` на АРМ).
'''
CHROMIUM_VERSION_STRING = '130.0.6723.192'
DEFAULT_BROWSER_USER_AGENT = f'''KIOSK; Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{CHROMIUM_VERSION_STRING} Safari/537.36'''
