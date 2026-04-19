# Source Generated with Decompyle++
# File: dialog_security.pyc (Python 3.12)

'''Модальные окна киоска: нельзя свернуть через ПКМ по заголовку и нет контекстных меню.

CustomizeWindowHint + только заголовок и «Закрыть» — без системного меню декорации WM,
где часто есть «Свернуть». Плюс NoContextMenu на окне и дочерних виджетах.
'''
from __future__ import annotations
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QWidget
from utils.qt_message_box_style import apply_kiosk_qmessagebox_style
_KIOSK_MODAL_FLAGS = Qt.WindowType.Dialog | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowStaysOnTopHint

def harden_kiosk_modal(w = None):
    '''Вызвать перед exec() для QDialog / QMessageBox / QInputDialog.'''
    w.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
    w.setWindowFlags(_KIOSK_MODAL_FLAGS)
    for ch in w.findChildren(QWidget):
        ch.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
    if isinstance(w, QMessageBox):
        apply_kiosk_qmessagebox_style(w)
        return None


def kiosk_question(parent = None, title = None, text = None, default_button = None, *, yes_text, no_text):
    mb = QMessageBox(parent)
    mb.setIcon(QMessageBox.Icon.Question)
    mb.setWindowTitle(title)
    mb.setText(text)
    mb.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    yb = mb.button(QMessageBox.StandardButton.Yes)
    nb = mb.button(QMessageBox.StandardButton.No)
# WARNING: Decompyle incomplete


def kiosk_information(parent = None, title = None, text = None):
    mb = QMessageBox(parent)
    mb.setIcon(QMessageBox.Icon.Information)
    mb.setWindowTitle(title)
    mb.setText(text)
    mb.setStandardButtons(QMessageBox.StandardButton.Ok)
    harden_kiosk_modal(mb)
    mb.exec()


def kiosk_warning(parent = None, title = None, text = None):
    mb = QMessageBox(parent)
    mb.setIcon(QMessageBox.Icon.Warning)
    mb.setWindowTitle(title)
    mb.setText(text)
    mb.setStandardButtons(QMessageBox.StandardButton.Ok)
    harden_kiosk_modal(mb)
    mb.exec()


def kiosk_critical(parent = None, title = None, text = None):
    mb = QMessageBox(parent)
    mb.setIcon(QMessageBox.Icon.Critical)
    mb.setWindowTitle(title)
    mb.setText(text)
    mb.setStandardButtons(QMessageBox.StandardButton.Ok)
    harden_kiosk_modal(mb)
    mb.exec()


def kiosk_input_password(parent = None, title = None, label = None):
    kiosk_frameless_password = kiosk_frameless_password
    import kiosk.kiosk_frameless_dialog
    return kiosk_frameless_password(parent, title, label)

