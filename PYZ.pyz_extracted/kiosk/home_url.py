# Source Generated with Decompyle++
# File: home_url.pyc (Python 3.12)

'''
Домашний URL киоска: первая ссылка из ``allowed_sites`` для выбранного сайта или по хосту.

Без Qt — тестируется без PySide6.
'''
from __future__ import annotations
from urllib.parse import urlparse

def _norm_host(host = None):
    if not host:
        host
    return ''.strip().lower()


def host_matches_allowed_site(host = None, site_netloc = None):
    '''Совпадает ли хост навигации с базовым хостом записи из конфига (включая поддомены).'''
    h = _norm_host(host)
    p = _norm_host(site_netloc)
    if not h or p:
        return False
    if h == p:
        return True
    return h.endswith('.' + p)


def config_first_url_for_site(allowed_domains = None, site_name = None):
    '''Первый URL из ``allowed_sites`` для имени сайта (как в комбобоксе).'''
    if not site_name or isinstance(allowed_domains, dict):
        return ''
    if site_name not in allowed_domains:
        return ''
    value = allowed_domains[site_name]
    primary = value[0] if isinstance(value, list) else value
    if not isinstance(primary, str):
        return ''
    return primary.strip()


def config_first_url_for_http_hint(allowed_domains = None, hint_url = None):
    '''Первая ссылка из конфига для того же «сайта», что и ``hint_url`` (по netloc).

    Например, для ``https://demo.mcko.ru/test/`` и записи ``MCKO: ["https://mcko.ru/"]``
    вернёт ``https://mcko.ru/``.
    '''
    if not hint_url:
        hint_url
    hint = ''.strip()
    if not hint.startswith(('http://', 'https://')):
        return ''
    
    try:
        host = urlparse(hint).netloc
        if not host:
            return ''
        if not isinstance(allowed_domains, dict):
            return ''
        for _name, value in allowed_domains.items():
            primary = value[0] if isinstance(value, list) else value
            if not isinstance(primary, str):
                continue
            primary = primary.strip()
            if not primary.startswith(('http://', 'https://')):
                continue
            site_host = urlparse(primary).netloc
            if not site_host:
                continue
            if not host_matches_allowed_site(host, site_host):
                continue
            
            return allowed_domains.items(), primary
        return ''
    except Exception:
        return ''
        except Exception:
            continue



def resolve_input_mode_home_url(remembered_url = None, web_view_url = None, allowed_domains = None):
    '''Домашний URL в режиме ручного ввода (``URL_SELECTOR_MODE == "input"``).

    1. Если пользователь уже ввёл адрес (запоминается при первом успешном Enter) — **всегда** он
       (точный URL, без подмены на «первую ссылку из конфига»).
    2. Иначе — как раньше: по текущему документу ищем первую ссылку из ``allowed_sites`` для того же хоста.
    '''
    if not remembered_url:
        remembered_url
    mem = ''.strip()
    if mem:
        return mem
    if not None:
        pass
    hint = ''.strip()
    canon = config_first_url_for_http_hint(allowed_domains, hint)
    if canon:
        return canon

