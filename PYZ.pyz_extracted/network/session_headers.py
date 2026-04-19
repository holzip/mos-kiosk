# Source Generated with Decompyle++
# File: session_headers.pyc (Python 3.12)

'''Единая точка расчёта заголовков сессии от X-Session-Key.

В проде: вызывайте с одним аргументом (ключ) — соль читается из ``config.state.KIOSK_SS``
после vault (без соли конструктора :class:`KioskSessionContext`).

Опционально можно передать соль явно (тесты, утилиты) — см. параметр ``kiosk_ss``.

Кеширование по ключу выполняется в :meth:`KioskSessionContext.materialize_session_http_headers`.
'''
from __future__ import annotations
from typing import Any, Optional
from network.session_protocol import normalize_session_key_for_md5, session_client_from_key_and_salt

def calculate_session_dependent_headers(raw_session_key = None, *, kiosk_ss):
    '''По ключу сессии и соли посчитать данные для **X-Session-Client** (и соль в ответе).

    **Вход:** ``raw_session_key`` — как пришёл/будет в заголовке (trim внутри).

    **Соль:** если ``kiosk_ss is None`` — из ``state.KIOSK_SS``; иначе используется переданная
    строка (не читаем ``state``).

    **Выход** — словарь:
    - ``x_session_key`` — trim ключа
    - ``x_session_client`` — hex MD5 или ``""``
    - ``kiosk_ss_used`` — соль, реально участвовавшая в MD5

    Короткое имя: :func:`calculate_headers` (то же самое).
    '''
    pass
# WARNING: Decompyle incomplete

calculate_headers = calculate_session_dependent_headers
