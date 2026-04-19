# Source Generated with Decompyle++
# File: session_protocol.pyc (Python 3.12)

__doc__ = 'Единая формула X-Session-Client для киоска и бэкенда.\n\nСервер должен проверять так же:\n  ожидаемый_client = md5( UTF-8( trim(X-Session-Key) + kiosk_ss ) ).hexdigest()\n\n- Пробелы по краям ключа из заголовка отбрасываются (как при разборе HTTP).\n- ``kiosk_ss`` — строка из конфига как есть (без обрезки), чтобы совпадать с сервером.\n'
from __future__ import annotations
import hashlib
X_SESSION_CLIENT_PLACEHOLDER = '0'
_SESSION_KEY_CYRILLIC_HEX_LOOKALIKES = 'авсдеАВСДЕ'
_SESSION_KEY_ASCII_HEX_REPLACEMENT = 'abcdeABCDE'
# WARNING: Decompyle incomplete
