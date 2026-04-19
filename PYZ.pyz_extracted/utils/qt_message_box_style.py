# Source Generated with Decompyle++
# File: qt_message_box_style.pyc (Python 3.12)

'''Явные цвета QMessageBox (без раскраски текста от системной темы Qt/KDE).'''
from __future__ import annotations
KIOSK_QMESSAGEBOX_STYLESHEET = 'QMessageBox { background-color: #2d2d2d; }QMessageBox QLabel { color: #ecf0f1; background-color: transparent; font-size: 14px; }QMessageBox QPushButton { min-width: 88px; padding: 8px 14px; font-size: 14px; background-color: #34495e; color: #ecf0f1; border: 1px solid #4a6278; border-radius: 4px;}QMessageBox QPushButton:hover { background-color: #4a6278; color: #ffffff; }QMessageBox QPushButton:pressed { background-color: #2c3e50; }QMessageBox QPushButton:default { background-color: #2980b9; color: #ffffff; border: 1px solid #3498db;}QMessageBox QPushButton:default:hover { background-color: #3498db; color: #ffffff; }QMessageBox QTextEdit, QMessageBox QPlainTextEdit { background-color: #1a1a1a; color: #ecf0f1; border: 1px solid #555; font-size: 13px;}'

def apply_kiosk_qmessagebox_style(mb = None):
    mb.setStyleSheet(KIOSK_QMESSAGEBOX_STYLESHEET)

