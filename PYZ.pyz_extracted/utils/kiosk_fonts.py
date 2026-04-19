# Source Generated with Decompyle++
# File: kiosk_fonts.pyc (Python 3.12)

'''Локальные шрифты: каталог <корень>/fonts.

Поиск каталога (первый существующий):
  - MOSTECH_KIOSK_DIR/fonts
  - родитель сценария при запуске *.py (python mt_kiosk.py → тот же корень, что и mt_kiosk)
  - /opt/.../app/… → fonts рядом с app
  - KIOSK_v3/fonts (рядом с utils/)
  - родитель KIOSK_v3 (например KIOSK_v2/fonts в монорепо)
  - текущий каталог ./fonts
  - рядом с бинарником (если это не системный python из /usr/bin и т.п.)

Поддерживаются .ttf, .otf, .ttc.

На веб-страницах с явным font-family в CSS настройки WebEngine задают только «дефолтные»
семейства (generic); сайт может по-прежнему тянуть указанные им шрифты с системы/CDN.
'''
from __future__ import annotations
import os
import sys
from pathlib import Path
from typing import List, Optional
__all__ = [
    'resolve_kiosk_fonts_directory',
    'font_directory_candidates',
    'load_kiosk_bundle_fonts',
    'get_kiosk_bundle_font_families',
    'apply_kiosk_fonts_to_qapplication',
    'apply_kiosk_fonts_to_profile',
    'WEBENGINE_PREFERRED_SANS_FAMILY',
    'WEBENGINE_PREFERRED_SERIF_FAMILY']
WEBENGINE_PREFERRED_SANS_FAMILY = 'Arial'
WEBENGINE_PREFERRED_SERIF_FAMILY = 'Arial'
_LOADED_FAMILIES: 'List[str]' = []
_FONT_SCAN_DONE: 'bool' = False

def font_directory_candidates():
    '''Упорядоченный список возможных каталогов .../fonts (как есть, без проверки is_dir).'''
    pass
# WARNING: Decompyle incomplete


def resolve_kiosk_fonts_directory():
    '''Первый существующий каталог fonts из кандидатов.'''
    for cand in font_directory_candidates():
        if not cand.is_dir():
            continue
        
        return font_directory_candidates(), cand


def load_kiosk_bundle_fonts():
    '''Зарегистрировать шрифты из каталога fonts; вернуть список имён семейств.'''
    global _FONT_SCAN_DONE
    if _FONT_SCAN_DONE:
        return list(_LOADED_FAMILIES)
    _FONT_SCAN_DONE = None
    QFontDatabase = QFontDatabase
    import PySide6.QtGui
    logger = logger
    import utils.logging_setup
    fonts_dir = resolve_kiosk_fonts_directory()
    if not fonts_dir:
        c = font_directory_candidates()
        if not os.environ.get('MOSTECH_KIOSK_DIR'):
            os.environ.get('MOSTECH_KIOSK_DIR')
        if c:
            '<корень проекта>'(None, ' | '.join, (lambda .0: pass# WARNING: Decompyle incomplete
)(c()))
            return []
        None(logger.info, 'Локальные шрифты: каталог fonts не найден (остаются системные). Ожидается, например, %s/fonts с .ttf/.otf. Проверены пути: %s', '<корень проекта>')
        return []
    paths = None
    
    try:
        for p in sorted(fonts_dir.iterdir()):
            if not p.is_file():
                continue
            if p.suffix.lower() not in ('.ttf', '.otf', '.ttc'):
                continue
            paths.append(p)
        if not paths:
            logger.info('Локальные шрифты: в %s нет файлов .ttf/.otf/.ttc — остаются системные', fonts_dir)
            return []
        seen = None()
        for fp in paths:
            fid = QFontDatabase.addApplicationFont(str(fp))
            if fid < 0:
                logger.warning('Шрифт не загружен (отклонён Qt): %s', fp)
                continue
            for fam in QFontDatabase.applicationFontFamilies(fid):
                if not fam:
                    fam
                nm = ''.strip()
                if not nm:
                    continue
                if not nm not in seen:
                    continue
                seen.add(nm)
                _LOADED_FAMILIES.append(nm)
        if _LOADED_FAMILIES:
            logger.info('Загружены локальные шрифты из %s: %s', fonts_dir, ', '.join(_LOADED_FAMILIES[:8]) + '…' if len(_LOADED_FAMILIES) > 8 else '')
        return list(_LOADED_FAMILIES)
    except OSError:
        e = None
        logger.warning('Не удалось прочитать %s: %s', fonts_dir, e)
        del e
        return None
        None = 
        del e
        except Exception:
            e = None, []
            logger.warning('Ошибка загрузки шрифта %s: %s', fp, e)
            e = None
            del e
            continue
            e = None
            del e



def get_kiosk_bundle_font_families():
    '''Семейства после однократного сканирования каталога fonts.'''
    return load_kiosk_bundle_fonts()


def apply_kiosk_fonts_to_qapplication(app = None):
    '''Поставить основной шрифт окружения Qt по первому загруженному семейству.'''
    families = get_kiosk_bundle_font_families()
    if not families:
        return None
    QFont = QFont
    import PySide6.QtGui
    logger = logger
    import utils.logging_setup
    f = QFont(families[0])
    app.setFont(f)
    logger.info('QApplication: шрифт интерфейса → %s', families[0])


def apply_kiosk_fonts_to_profile(profile = None):
    '''Настроить семейства WebEngine: бандл из ``fonts/``, затем generic sans/serif (см. константы выше).'''
    QWebEngineSettings = QWebEngineSettings
    import PySide6.QtWebEngineCore
    logger = logger
    import utils.logging_setup
    settings = profile.settings()
    ff = QWebEngineSettings.FontFamily
    families = get_kiosk_bundle_font_families()
    if families:
        primary = families[0]
        settings.setFontFamily(ff.StandardFont, primary)
        settings.setFontFamily(ff.SansSerifFont, primary)
        mono = (lambda .0: pass# WARNING: Decompyle incomplete
)(families(), None)
        if mono:
            settings.setFontFamily(ff.FixedFont, mono)
        logger.info('WebEngine: бандл Standard/SansSerif → %s (страницы с явным font-family в CSS могут игнорировать)', primary)
    if not WEBENGINE_PREFERRED_SANS_FAMILY:
        WEBENGINE_PREFERRED_SANS_FAMILY
    sans = ''.strip()
    if not WEBENGINE_PREFERRED_SERIF_FAMILY:
        WEBENGINE_PREFERRED_SERIF_FAMILY
    serif = ''.strip()
    if sans:
        settings.setFontFamily(ff.StandardFont, sans)
        settings.setFontFamily(ff.SansSerifFont, sans)
    if serif:
        settings.setFontFamily(ff.SerifFont, serif)
    if sans or serif:
        if not sans:
            sans
        if not serif:
            serif
        logger.info('WebEngine: generic → sans-serif=%s, serif=%s', '(не задано)', '(не задано)')
        return None

