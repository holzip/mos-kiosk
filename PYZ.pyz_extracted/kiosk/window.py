# Source Generated with Decompyle++
# File: window.pyc (Python 3.12)

__doc__ = 'Главное окно киоска: WebEngine, панель управления, сервисное меню.'
import getpass
import os
import shutil
import stat
import subprocess
import threading
import time
import urllib.parse as urllib
from typing import Optional
from PySide6.QtCore import QObject, QUrl, Qt, QTimer, QThreadPool, Signal, Slot, QEvent
from PySide6.QtGui import QAction, QCursor, QFontMetrics, QKeySequence, QShortcut
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QVBoxLayout, QHBoxLayout, QApplication, QPushButton, QLabel, QComboBox, QFrame, QLineEdit, QDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
# WARNING: Decompyle incomplete
