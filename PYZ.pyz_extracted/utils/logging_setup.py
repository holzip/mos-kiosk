# Source Generated with Decompyle++
# File: logging_setup.pyc (Python 3.12)

'''Логирование киоска.

Уровни сообщений
-----------------
INFO  — события, понятные пользователю / администратору:
        «Конфиг загружен», «Начало сессии», «Обмен данными», «Сеть недоступна».
        Технические детали (ключи, MAC-адреса, URL-запросы) на INFO не выводятся.

DEBUG — полная техническая картина для разработчика:
        значения ключей, источники идентификатора, сетевые запросы и ответы.
        Включается через переменную среды: KIOSK_LOG_LEVEL=DEBUG

Путь к лог-файлу (автоопределение, можно переопределить KIOSK_LOG_DIR):
  1. $KIOSK_LOG_DIR            — явное задание
  2. /var/log/mostech-kiosk/   — системная установка (если доступна запись)
  3. ~/.local/share/mostech-kiosk/logs/  — пользовательская установка
  4. /tmp                      — fallback
'''
from __future__ import annotations
import logging
import os
import time
from typing import Iterable, Tuple

def _get_log_dir():
    '''Автоматически выбирает каталог для лога.'''
    env_dir = os.environ.get('KIOSK_LOG_DIR', '').strip()
    if env_dir:
        
        try:
            os.makedirs(env_dir, exist_ok = True)
            return env_dir
            system_log = '/var/log/mostech-kiosk'
            
            try:
                os.makedirs(system_log, exist_ok = True)
                _probe = os.path.join(system_log, '.write_probe')
                f = open(_probe, 'w')
                f.write('')
                
                try:
                    None(None, None)
                    os.unlink(_probe)
                    return system_log
                    except OSError:
                        continue
                    with None:
                        if not None:
                            pass
                    
                    try:
                        continue
                    except (OSError, PermissionError):
                        pass

                    user_log = os.path.join(os.environ.get('HOME', os.path.expanduser('~')), '.local', 'share', 'mostech-kiosk', 'logs')
                    
                    try:
                        os.makedirs(user_log, exist_ok = True)
                        return user_log
                    except OSError:
                        return '/tmp'






def _build_log_path(log_dir = None):
    """Формирует имя файла лога: mostech-kiosk_YYYY-MM-DD.log.

    Ежедневная ротация: один файл на день, дозапись (mode='a').
    Старые файлы не удаляются автоматически — убирает администратор или logrotate.
    """
    date_str = time.strftime('%Y-%m-%d')
    return os.path.join(log_dir, f'''mostech-kiosk_{date_str}.log''')


def _configure_logging_with_fallback(log_dirs = None, *, level, fmt, datefmt):
    '''Пытается настроить логирование по списку каталогов; при ошибке берет следующий.'''
    last_error = None
    for log_dir in log_dirs:
        log_path = _build_log_path(log_dir)
        logging.basicConfig(filename = log_path, filemode = 'a', level = level, format = fmt, datefmt = datefmt, encoding = 'utf-8')
        
        return log_dirs, log_path
# WARNING: Decompyle incomplete


def _setup_logging():
    primary_dir = _get_log_dir()
    user_fallback = os.path.join(os.environ.get('HOME', os.path.expanduser('~')), '.local', 'share', 'mostech-kiosk', 'logs')
    
    try:
        os.makedirs(user_fallback, exist_ok = True)
        level_name = os.environ.get('KIOSK_LOG_LEVEL', 'INFO').upper()
        level = getattr(logging, level_name, logging.INFO)
        fmt = '%(asctime)s  %(levelname)-7s  %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        candidates = [
            primary_dir]
        if user_fallback not in candidates:
            candidates.append(user_fallback)
        if '/tmp' not in candidates:
            candidates.append('/tmp')
        log_path = _configure_logging_with_fallback(candidates, level = level, fmt = fmt, datefmt = datefmt)
        _logger = logging.getLogger('KioskApp')
        _logger.info('============================================================')
        _logger.info('Запуск Мостех Киоск')
        _logger.info('Лог-файл: %s', log_path)
        if level == logging.DEBUG:
            _logger.debug('Режим отладки активен (KIOSK_LOG_LEVEL=DEBUG)')
        return (log_path, _logger)
    except OSError:
        continue


(log_file_path, logger) = _setup_logging()
