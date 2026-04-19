# Source Generated with Decompyle++
# File: page_load.pyc (Python 3.12)

'''
Логика загрузки страницы: таймаут, повторные попытки, индикатор времени (как в mostech-kiosk_150).
Параметры берутся из config.state. Обработчики loadStarted/loadFinished и таймер подключаются в окне.
'''
from config.state import state
from kiosk.load_finished_spurious import document_urls_match_for_same_navigation, should_ignore_load_finished_false_as_spurious

def get_page_load_timeout_ms():
    '''Таймаут загрузки страницы, мс (из конфига page_load_timeout_seconds).'''
    sec = getattr(state, 'PAGE_LOAD_TIMEOUT_SECONDS', 10)
    return int(sec * 1000)


def get_page_load_retry_delay_ms():
    '''Задержка между проверкой результата и следующей попыткой, мс.'''
    sec = getattr(state, 'PAGE_LOAD_RETRY_DELAY_SECONDS', 2)
    return int(sec * 1000)


def get_page_load_max_retries():
    '''Максимальное число повторных попыток загрузки при «Страница недоступна».'''
    return getattr(state, 'PAGE_LOAD_MAX_RETRIES', 3)


def show_page_load_time():
    '''Показывать ли индикатор времени загрузки в углу и в tooltip кнопки «Техподдержка».'''
    return getattr(state, 'SHOW_PAGE_LOAD_TIME', True)


def should_retry_page_load(retry_count = None):
    '''Есть ли ещё попытки загрузки (retry_count < max_retries).'''
    return retry_count < get_page_load_max_retries()

__all__ = [
    'document_urls_match_for_same_navigation',
    'get_page_load_max_retries',
    'get_page_load_retry_delay_ms',
    'get_page_load_timeout_ms',
    'should_ignore_load_finished_false_as_spurious',
    'should_retry_page_load',
    'show_page_load_time']
