# Source Generated with Decompyle++
# File: panel.pyc (Python 3.12)

'''Диалоги административной панели: управление WiFi, информация о системе,
управление приложением (диагностика), аутентификация сервисного меню.
'''
import platform
import socket
import subprocess
import sys
from typing import Any, Optional
from PySide6.QtCore import QEvent, Qt, QThreadPool, QTimer, Signal, Slot
from PySide6.QtWidgets import QApplication, QDialogButtonBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QListWidget, QPushButton, QTabWidget, QTextEdit, QVBoxLayout, QWidget
from config.secrets import check_password
from config.state import state
from kiosk.dialog_security import kiosk_input_password
from kiosk.kiosk_frameless_dialog import KioskFramelessDialog, kiosk_frameless_alert, kiosk_frameless_confirm
from network.wifi_worker import AsyncWorker
from utils.logging_setup import logger
from utils.qt_typography import sans_font

def check_service_password(parent = None):
    '''Запросить и проверить пароль сервисного меню (SMC — Service Menu Code).

    Если kiosk_smc пустая строка — доступ разрешён без пароля.
    Возвращает True при правильном пароле или при пустом kiosk_smc.
    '''
    expected = getattr(state, 'KIOSK_SMC', '')
    if not expected:
        return True
    (password, ok) = kiosk_input_password(parent, 'Сервисное меню', 'Введите пароль:')
    if not ok:
        return False
    if not password or password.strip():
        kiosk_frameless_alert(parent, 'Сервисное меню', 'Пароль не введён.', level = 'warning')
        return False
    
    try:
        ok_pw = check_password(password, expected)
        if not ok_pw:
            kiosk_frameless_alert(parent, 'Сервисное меню', 'Неверный пароль.', level = 'warning')
            return False
        return True
    except Exception:
        e = None
        logger.exception('Ошибка проверки пароля сервисного меню: %s', e)
        kiosk_frameless_alert(parent, 'Сервисное меню', 'Ошибка проверки пароля.', level = 'critical')
        e = None
        del e
        return False
        e = None
        del e



class WiFiManagementDialog(KioskFramelessDialog):
    pass
# WARNING: Decompyle incomplete


class SystemInfoDialog(KioskFramelessDialog):
    pass
# WARNING: Decompyle incomplete


class AppManagementDialog(KioskFramelessDialog):
    pass
# WARNING: Decompyle incomplete

