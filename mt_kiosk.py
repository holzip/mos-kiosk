# Source Generated with Decompyle++
# File: mt_kiosk.pyc (Python 3.12)

'''Точка входа: Мостех Киоск v3, PySide6/Qt6 WebEngine.'''
import sys
import os
import time
import traceback
_project_root = os.path.dirname(os.path.abspath(__file__))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)
if not getattr(sys, 'frozen', False):
    os.environ.setdefault('MOSTECH_KIOSK_DIR', _project_root)
if not getattr(sys, 'frozen', False) and os.environ.get('QTWEBENGINE_LOCALES_PATH'):
    if not getattr(sys, '_MEIPASS', None):
        getattr(sys, '_MEIPASS', None)
    _bundle_base = os.path.dirname(os.path.abspath(sys.executable))
    for _loc in (os.path.join(_bundle_base, 'PySide6', 'Qt', 'translations', 'qtwebengine_locales'), os.path.join(_bundle_base, 'PySide6', 'Qt', 'translations')):
        if not os.path.isdir(_loc):
            continue
        os.environ['QTWEBENGINE_LOCALES_PATH'] = _loc
        (os.path.join(_bundle_base, 'PySide6', 'Qt', 'translations', 'qtwebengine_locales'), os.path.join(_bundle_base, 'PySide6', 'Qt', 'translations'))
from qt_compat import QT_BINDING, _install_pyside6_shim
_install_pyside6_shim()
logger = None

try:
    from utils.logging_setup import logger, log_file_path as _log_file
    
    def _show_fatal_error(title = None, message = None):
        '''Показать критическую ошибку: GUI-диалог если возможно, иначе stderr.'''
        if logger:
            logger.critical('%s: %s', title, message)
    # WARNING: Decompyle incomplete

    
    def _apply_dns_flags(dns_server = None):
        '''Настроить DNS для Chromium/Qt WebEngine через переменную среды.

    Вызывается после загрузки конфига, но до создания первого QWebEngineView.
    Поддерживаемые форматы browser_dns_server:
      - https://...  → DNS-over-HTTPS через --dns-over-https-templates
      - IP-адрес     → отключает async DNS; для полного эффекта требуется
                       настройка /etc/resolv.conf или systemd-resolved
    '''
        if not dns_server:
            return None
        existing = os.environ.get('QTWEBENGINE_CHROMIUM_FLAGS', '')
        if dns_server.startswith('https://'):
            extra = f'''--dns-over-https-templates={dns_server} --enable-features=DnsOverHttps'''
            logger.info('DNS: DoH → %s', dns_server)
        else:
            extra = '--disable-features=AsyncDns'
            logger.info('DNS: plain IP %s — применён --disable-features=AsyncDns. Для надёжного эффекта настройте /etc/resolv.conf или systemd-resolved.', dns_server)
        os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = (existing + ' ' + extra).strip()
        logger.debug('QTWEBENGINE_CHROMIUM_FLAGS = %s', os.environ['QTWEBENGINE_CHROMIUM_FLAGS'])

    _PID_PATH = os.path.join(os.path.expanduser('~'), '.mostech-kiosk.pid')
    _LOCK_PATH = os.path.join(os.path.expanduser('~'), '.mostech-kiosk.lock')
    _KIOSK_INSTANCE_LOCK_FD = None
    
    def _release_instance_lock():
        pass
    # WARNING: Decompyle incomplete

    
    def _cleanup_pid_file():
        pass
    # WARNING: Decompyle incomplete

    
    def _check_single_instance_pid_fallback():
        '''Резерв без flock (Windows / ошибка открытия lock).'''
        my_pid = os.getpid()
    # WARNING: Decompyle incomplete

    
    def _try_acquire_single_instance():
        '''Один экземпляр на UID (flock). Повторный запуск — тихий exit 0.'''
        global _KIOSK_INSTANCE_LOCK_FD
        pass
    # WARNING: Decompyle incomplete

    
    def main():
        '''Главная функция. Возвращает код возврата процесса.'''
        pass
    # WARNING: Decompyle incomplete

    if __name__ == '__main__':
        
        try:
            sys.exit(main())
            return None
            return None
            except Exception:
                _init_err = None
                print(f'''[mostech-kiosk] ОШИБКА инициализации логирования: {_init_err}''', file = sys.stderr)
                traceback.print_exc(file = sys.stderr)
                _log_file = None
                import logging
                logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')
                logger = logging.getLogger('KioskApp')
                _init_err = None
                del _init_err
                continue
                _init_err = None
                del _init_err
        except Exception:
            e = None
            if logger:
                logger.critical('Необработанное исключение: %s', e, exc_info = True)
            _show_fatal_error('Мостех Киоск — критическая ошибка', f'''Произошла непредвиденная ошибка:\n{e}\n\nОбратитесь в техподдержку.''')
            sys.exit(1)
            e = None
            del e
            return None
            e = None
            del e


