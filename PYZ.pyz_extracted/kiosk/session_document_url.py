# Source Generated with Decompyle++
# File: session_document_url.pyc (Python 3.12)

'''Сравнение URL для сохранения сессии при навигации только по query/fragment.'''
from __future__ import annotations
from PySide6.QtCore import QUrl

def qurl_same_http_document_locator(cur = None, new = None):
    '''Тот же логический HTTP-документ: scheme, host, port, path; query и fragment не сравниваем.

    Нужно для ссылок вида ``<a href="?">refresh</a>`` — в Qt это новая навигация, не ``NavigationTypeReload``.
    '''
    if not cur.isValid() or new.isValid():
        return False
    if not cur.scheme():
        cur.scheme()
    sch = ''.lower()
    if sch not in ('http', 'https'):
        return False
    if not new.scheme():
        new.scheme()
    if ''.lower() != sch:
        return False
    if not cur.host():
        cur.host()
    if not new.host():
        new.host()
    if ''.lower() != ''.lower():
        return False
    
    def _effective_port(u = None):
        p = u.port()
        if p >= 0:
            return p
        if not None.scheme():
            None.scheme()
        s = ''.lower()
        if s == 'https':
            return 443

    if _effective_port(cur) != _effective_port(new):
        return False
    
    def _path_key(u = None):
        if not u.path():
            u.path()
        p = ''
        if p == '':
            p = '/'
        if not p.rstrip('/'):
            p.rstrip('/')
        return '/'

    return _path_key(cur) == _path_key(new)

