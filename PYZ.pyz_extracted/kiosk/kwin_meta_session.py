# Source Generated with Decompyle++
# File: kwin_meta_session.pyc (Python 3.12)

'''
Отключение одиночного Meta (Win) в KWin только на время сессии киоска.

Перед показом окна киоска — отключение; при выходе — восстановление из бэкапа.
Ранее дублировалось в build/kwin-meta-key.sh (не входит в RPM).

На не-Linux / без Plasma / без kwriteconfig5 — no-op.
'''
from __future__ import annotations
import os
import shutil
import subprocess
import sys
from pathlib import Path

def _is_linux():
    return sys.platform.startswith('linux')


def _kwinrc_path():
    return Path.home() / '.config' / 'kwinrc'


def _session_backup_path():
    d = Path.home() / '.cache' / 'mostech-kiosk'
    d.mkdir(parents = True, exist_ok = True)
    return d / 'kwin-meta-session.bak'


def _read_meta_line(kwinrc = None):
    if not kwinrc.is_file():
        return '__MISSING__'
    in_section = False
    
    try:
        for line in kwinrc.read_text(encoding = 'utf-8', errors = 'replace').splitlines():
            s = line.strip()
            if s.startswith('[') and s.endswith(']'):
                in_section = s.lower() == '[modifieronlyshortcuts]'
                continue
            if not in_section:
                continue
                
                try:
                    if not s.startswith('Meta='):
                        continue
                        
                        try:
                            if '=' in line:
                                
                                return kwinrc.read_text(encoding = 'utf-8', errors = 'replace').splitlines(), line.split('=', 1)[1].strip()
                            
                            return None, kwinrc.read_text(encoding = 'utf-8', errors = 'replace').splitlines()
                            
                            try:
                                return '__MISSING__'
                            except OSError:
                                return '__MISSING__'






def _plasma_session():
    if not os.environ.get('XDG_SESSION_DESKTOP'):
        os.environ.get('XDG_SESSION_DESKTOP')
    desk = ''.lower()
    if 'plasma' in desk or desk == 'kde':
        return True
    if not os.environ.get('KDE_FULL_SESSION'):
        os.environ.get('KDE_FULL_SESSION')
    if ''.lower() == 'true':
        return True
    return False


def resolve_should_disable_kwin_meta(config_value = None):
    '''
    None / отсутствует ключ — только в сессии Plasma/KDE и при наличии kwriteconfig5.
    True — на любом Linux с kwriteconfig5.
    False — никогда.
    '''
    if not _is_linux() or shutil.which('kwriteconfig5'):
        return False
    if config_value is False:
        return False
    if config_value is True:
        return True
    return _plasma_session()


def _kwin_reconfigure():
    uid = os.getuid()
    bus_sock = Path(f'''/run/user/{uid}/bus''')
    env = os.environ.copy()
    if 'DBUS_SESSION_BUS_ADDRESS' not in env and bus_sock.is_socket():
        env['DBUS_SESSION_BUS_ADDRESS'] = f'''unix:path={bus_sock}'''
    if 'DISPLAY' not in env:
        env['DISPLAY'] = os.environ.get('DISPLAY', ':0')
    for cmd in ('qdbus6', 'qdbus'):
        if not shutil.which(cmd):
            continue
        r = subprocess.run([
            cmd,
            'org.kde.KWin',
            '/KWin',
            'reconfigure'], env = env, capture_output = True, timeout = 8)
        if r.returncode == 0:
            ('qdbus6', 'qdbus')
            return None
    continue
    return None
    except (OSError, subprocess.TimeoutExpired):
        continue


class KwinMetaSession:
    
    def __init__(self = None, log = None):
        self._log = log
        self._active = False

    
    def disable(self = None):
        kwinrc = _kwinrc_path()
        kwinrc.parent.mkdir(parents = True, exist_ok = True)
        prev = _read_meta_line(kwinrc)
        
        try:
            _session_backup_path().write_text(prev + '\n', encoding = 'utf-8')
            
            try:
                subprocess.run([
                    'kwriteconfig5',
                    '--file',
                    str(kwinrc),
                    '--group',
                    'ModifierOnlyShortcuts',
                    '--key',
                    'Meta',
                    ''], check = False, timeout = 15, capture_output = True)
                _kwin_reconfigure()
                self._active = True
                self._log.info('KWin: Meta отключён на время сессии киоска')
                return None
                except OSError:
                    e = None
                    self._log.warning('kwin-meta: бэкап: %s', e)
                    e = None
                    del e
                    return None
                    e = None
                    del e
            except (OSError, subprocess.TimeoutExpired):
                e = None
                self._log.warning('kwin-meta: kwriteconfig5: %s', e)
                e = None
                del e
                return None
                e = None
                del e



    
    def restore(self = None):
        if not self._active:
            return None
        self._active = False
        kwinrc = _kwinrc_path()
        bp = _session_backup_path()
        
        try:
            if not bp.is_file():
                subprocess.run([
                    'kwriteconfig5',
                    '--file',
                    str(kwinrc),
                    '--group',
                    'ModifierOnlyShortcuts',
                    '--key',
                    'Meta',
                    '--delete'], capture_output = True, timeout = 15)
            else:
                text = bp.read_text(encoding = 'utf-8')
                if not text.splitlines():
                    text.splitlines()
                prev = [
                    ''][0].strip()
                if prev == '__MISSING__':
                    subprocess.run([
                        'kwriteconfig5',
                        '--file',
                        str(kwinrc),
                        '--group',
                        'ModifierOnlyShortcuts',
                        '--key',
                        'Meta',
                        '--delete'], capture_output = True, timeout = 15)
                else:
                    subprocess.run([
                        'kwriteconfig5',
                        '--file',
                        str(kwinrc),
                        '--group',
                        'ModifierOnlyShortcuts',
                        '--key',
                        'Meta',
                        prev], capture_output = True, timeout = 15)
            
            try:
                if bp.is_file():
                    bp.unlink()
                _kwin_reconfigure()
                self._log.info('KWin: Meta восстановлен после выхода из киоска')
                return None
                except OSError:
                    e = None
                    self._log.warning('kwin-meta: восстановление: %s', e)
                    
                    try:
                        e = None
                        del e
                        continue
                        e = None
                        del e
                        
                        try:
                            except OSError:
                                continue
                        except OSError:
                            pass






