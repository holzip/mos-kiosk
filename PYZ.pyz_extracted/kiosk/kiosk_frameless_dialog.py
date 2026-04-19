# Source Generated with Decompyle++
# File: kiosk_frameless_dialog.pyc (Python 3.12)

'''Диалоги без рамки WM: KWin не показывает ПКМ по заголовку («Свернуть», «На весь экран» и т.д.).'''
from __future__ import annotations
from typing import Literal
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class KioskFramelessDialog(QDialog):
    pass
# WARNING: Decompyle incomplete


def kiosk_frameless_exit_confirm(parent = None, *, title, main_text, detail_text, yes_text, no_text):
    '''Подтверждение выхода из киоска. True — пользователь подтвердил.'''
    pass
# WARNING: Decompyle incomplete


def kiosk_frameless_alert(parent = None, title = None, text = None, *, level):
    '''Одна кнопка «OK» — предупреждение/ошибка в том же стиле, что пароль и выход.'''
    dlg = KioskFramelessDialog(parent, title = title, min_w = 400, min_h = 180)
    (sym, icolor) = {
        'info': ('ℹ', '#3498db'),
        'warning': ('⚠', '#f39c12'),
        'critical': ('⚠', '#e74c3c') }[level]
    dlg.kiosk_body.setStyleSheet('#kioskDlgBody { background: #2d2d2d; color: #ecf0f1; }QLabel { font-size: 14px; color: #ecf0f1; }QPushButton#kioskAlertOk { min-width: 120px; padding: 10px 20px; border-radius: 4px; border: none; font-size: 14px; background: #2980b9; color: #ffffff; }QPushButton#kioskAlertOk:hover { background: #3498db; color: #ffffff; }')
    row = QHBoxLayout()
    icon = QLabel(sym)
    icon.setStyleSheet(f'''font-size: 32px; color: {icolor};''')
    row.addWidget(icon)
    msg = QLabel(text)
    msg.setWordWrap(True)
    row.addWidget(msg, 1)
    dlg.content_layout.addLayout(row)
    btn_row = QHBoxLayout()
    btn_row.addStretch()
    btn_ok = QPushButton('OK')
    btn_ok.setObjectName('kioskAlertOk')
    btn_ok.clicked.connect(dlg.accept)
    btn_row.addWidget(btn_ok)
    dlg.content_layout.addLayout(btn_row)
    btn_ok.setDefault(True)
    btn_ok.setFocus()
    dlg.apply_no_context_menus()
    dlg.exec()


def kiosk_frameless_confirm(parent = None, *, title, message, yes_text, no_text, default_no):
    '''Диалог Да/Нет в стиле остальных безрамочных окон. True — подтверждение (yes).'''
    pass
# WARNING: Decompyle incomplete


def kiosk_frameless_password(parent = None, title = None, label_text = None):
    '''Ввод пароля без рамки WM. (пароль, ok).'''
    pass
# WARNING: Decompyle incomplete

