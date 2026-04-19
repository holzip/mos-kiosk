# Source Generated with Decompyle++
# File: kiosk_session.pyc (Python 3.12)

'''Единая точка входа для X-Session-Key и X-Session-Client.

Все обновления ключа идут через :class:`KioskSessionContext`.
Интерцептор и диагностика читают только отсюда — одна строка ключа на все запросы.
'''
from __future__ import annotations
from typing import Optional
from PySide6.QtCore import QObject, Signal
from network.session_protocol import normalize_session_key_for_md5

class KioskSessionContext(QObject):
    pass
# WARNING: Decompyle incomplete

