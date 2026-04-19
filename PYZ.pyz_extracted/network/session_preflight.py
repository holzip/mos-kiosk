# Source Generated with Decompyle++
# File: session_preflight.pyc (Python 3.12)

'''Опциональный preflight до первого запроса WebEngine: curl -L, только куки.

Куки из цепочки ответов попадают в ``QWebEngineCookieStore``. Значение ``X-Session-Key``
из ответа curl **не** записывается в ``KioskSessionContext`` — ключ задаёт только WebEngine
(``responseHeaders`` после загрузки). Включение: ``session_key_preflight: true`` в конфиге.
'''
from __future__ import annotations
import os
import re
import shutil
import subprocess
import tempfile
from typing import Any, List, Optional, Tuple
from utils.logging_setup import logger
_SESSION_KEY_RE = re.compile('^x-session-key:\\s*(.+)\\s*$', re.I)

def _parse_last_response_headers(path = None):
    '''Из файла заголовков последнего ответа — X-Session-Key.'''
    key = None
    
    try:
        f = open(path, 'r', encoding = 'utf-8', errors = 'replace')
        for line in f:
            m = _SESSION_KEY_RE.match(line.strip())
            if not m:
                continue
            key = m.group(1).strip()
        
        try:
            None(None, None)
            return (key, { })
            with None:
                if not None:
                    pass
            
            try:
                continue
            except OSError:
                e = None
                logger.warning('session_preflight: чтение заголовков: %s', e)
                e = None
                del e
                return (key, { })
                e = None
                del e





def _parse_netscape_cookie_file(path = None):
    '''Строки Netscape → dict для QNetworkCookie на стороне Qt.'''
    out = []
    
    try:
        f = open(path, 'r', encoding = 'utf-8', errors = 'replace')
        for raw in f:
            line = raw.strip()
            if not (line or line.startswith('#')) and line.startswith('#HttpOnly_'):
                continue
            http_only = line.startswith('#HttpOnly_')
            if http_only:
                line = line[len('#HttpOnly_'):]
            parts = line.split('\t')
            if len(parts) < 7:
                continue
            (domain, _flag, cpath, secure, exp, name, value) = (parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], '\t'.join(parts[6:]))
            exp_i = int(exp) if exp.isdigit() else 0
            if not cpath.strip():
                cpath.strip()
            out.append({
                'domain': domain.strip(),
                'path': '/',
                'name': name.strip(),
                'value': value,
                'secure': secure.upper() == 'TRUE',
                'http_only': http_only,
                'expiration': exp_i })
        
        try:
            None(None, None)
            return out
            except ValueError:
                exp_i = 0
                continue
            with None:
                if not None:
                    pass
            
            try:
                return out
                
                try:
                    pass
                except OSError:
                    e = None
                    logger.warning('session_preflight: cookies file: %s', e)
                    e = None
                    del e
                    return out
                    e = None
                    del e






def run_session_preflight(start_url = None, user_agent = None, *, timeout_sec):
    '''
    curl -L по start_url: финальный URL, X-Session-Key с последнего ответа, куки.

    Returns:
        (session_key, url_effective, cookie_dicts)
    '''
    if not start_url.startswith(('http://', 'https://')):
        return (None, None, [])
    if not None.which('curl'):
        logger.warning('session_preflight: curl не найден')
        return (None, None, [])
    if not None:
        pass
    if not ''.strip():
        ''.strip()
    ua = 'MostechKiosk/3.0'
    d = tempfile.mkdtemp(prefix = 'mk_preflight_')
    cookie_jar = os.path.join(d, 'jar.txt')
    hdr_path = os.path.join(d, 'last.hdr')
    
    try:
        cmd = [
            'curl',
            '-sL',
            '-m',
            str(timeout_sec),
            '-A',
            ua,
            '-c',
            cookie_jar,
            '-D',
            hdr_path,
            '-o',
            '/dev/null',
            '-w',
            '%{url_effective}',
            start_url]
        r = subprocess.run(cmd, capture_output = True, text = True, timeout = timeout_sec + 10)
        if not r.stdout:
            r.stdout
        effective = ''.strip().split('\n')[-1].strip()
        if not effective.startswith('http'):
            effective = start_url
        (session_key, _) = _parse_last_response_headers(hdr_path)
        cookies = _parse_netscape_cookie_file(cookie_jar) if os.path.isfile(cookie_jar) else []
        if session_key:
            logger.info('session_preflight: ключ получен, url=%s, кук=%s', effective[:80], len(cookies))
        else:
            logger.warning('session_preflight: нет X-Session-Key (url=%s), кук=%s', effective[:80], len(cookies))
        for n in ('jar.txt', 'last.hdr'):
            p = os.path.join(d, n)
            if not os.path.isfile(p):
                continue
            os.unlink(p)
        os.rmdir(d)
        return None
        except OSError:
            return None
    except subprocess.TimeoutExpired:
        logger.warning('session_preflight: таймаут curl')
        
        try:
            for os.path.join(d, n) in ('jar.txt', 'last.hdr'):
                if not os.path.isfile(p):
                    continue
                os.unlink(p)
            os.rmdir(d)
            return None, (None, None, [])
            except OSError:
                return None
            except Exception:
                e = None
                logger.warning('session_preflight: %s', e)
                
                try:
                    del e
                    for None in ('jar.txt', 'last.hdr'):
                        p = os.path.join(d, n)
                        if not os.path.isfile(p):
                            continue
                        os.unlink(p)
                    os.rmdir(d)
                    return None, (None, None, [])
                    except OSError:
                        return None
                    e = None
                    del e
                    
                    try:
                        pass
                    except OSError:
                        pass





