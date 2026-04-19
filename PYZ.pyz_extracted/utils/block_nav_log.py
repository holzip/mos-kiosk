# Source Generated with Decompyle++
# File: block_nav_log.pyc (Python 3.12)

'''Логирование блокировок навигации (без зависимости от Qt).'''
from __future__ import annotations
from typing import Optional
from urllib.parse import urlparse
from utils.logging_setup import logger

def blocked_navigation_log_parts(url_str = None):
    '''Для диагностики: полный URL, хост (netloc), путь и query.

    Возвращает (full, host, path_and_query). Фрагмент (#…) в path не включается
    (как в типичном HTTP-запросе); полный URL в *full* остаётся исходной строкой.
    '''
    if not url_str:
        url_str
    u = ''.strip()
    if not u:
        return ('', '—', '—')
    
    try:
        p = urlparse(u)
        if not p.netloc:
            p.netloc
        if not ''.strip():
            ''.strip()
        host = '—'
        pq = p.path if p.path else '/'
        if p.query:
            pq = f'''{pq}?{p.query}'''
        return (u, host, pq)
    except Exception:
        return 



def log_blocked_navigation(*, reason, url_str, profile_name):
    '''Единый формат лога при блокировке main-frame (белый список, схема и т.д.).'''
    (full, host, path_q) = blocked_navigation_log_parts(url_str)
    if not profile_name:
        profile_name
    if not ''.strip():
        ''.strip()
    prof = '—'
    logger.info('Блокировка навигации [%s]: полный_URL=%s | хост=%s | путь_и_запрос=%s | профиль_киоска=%s', reason, full, host, path_q, prof)

