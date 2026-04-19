# Source Generated with Decompyle++
# File: qt_typography.pyc (Python 3.12)

'''Типографика в Qt / WebEngine (требует PySide6).'''
from __future__ import annotations
from typing import Optional
from PySide6.QtGui import QFont
from utils.typography import HTML_SANS_FONT_FAMILY
__all__ = [
    'HTML_SANS_FONT_FAMILY',
    'sans_font',
    'webengine_sans_family_name']

def sans_font(point_size = None):
    '''Шрифт Qt с подсказкой SansSerif (семейство подставит платформа).'''
    f = QFont()
    f.setStyleHint(QFont.StyleHint.SansSerif)
# WARNING: Decompyle incomplete


def webengine_sans_family_name():
    '''Имя семейства для QWebEngineSettings.*Font; иначе общий generic CSS.'''
    if not sans_font().family():
        sans_font().family()
    if not ''.strip():
        ''.strip()
    return 'sans-serif'

