# Source Generated with Decompyle++
# File: x_alert.pyc (Python 3.12)

'''Заголовок ``X-Alert``: битовая маска событий за сессию процесса.

Маска сбрасывается при перезапуске браузера в киоске, смене сайта и сбросе URL
(см. ``x_alert_reset_session``); после сброса снова выставляется только бит VM (если актуален).

Биты (OR, десятичное значение в заголовке):
    0  — штатно (маска 0; заголовок ``X-Alert: 0``).
    1  — попытка снимка экрана (зарезервировано).
    2  — во время открытой «Диагностика / Лог»: уход фокуса с приложения
         (``ApplicationDeactivate``) или деактивация главного окна киоска
         (``WindowDeactivate`` при модальном диалоге — без смены приложения).
    4  — подозрение на удалённое управление / анализ мыши (зарезервировано).
    8  — запуск в виртуальной машине (Linux), см. ``utils.vm_detect``.

Пример: сработали биты 1 и 4 → ``X-Alert: 5``.

После срабатывания бит «залипает» до конца процесса; каждый следующий
навигационный запрос (main frame) отдаёт актуальную маску в заголовке.
'''
from __future__ import annotations
import threading
_lock = threading.Lock()
_mask = 0
X_ALERT_SCREENSHOT_ATTEMPT = 1
X_ALERT_FOCUS_LOSS_DIAGNOSTICS = 2
X_ALERT_REMOTE_CONTROL_MOUSE = 4
X_ALERT_VIRTUALIZATION = 8

def x_alert_get_mask():
    '''Текущая маска для заголовка X-Alert (целое число).'''
    _lock
    None(None, None)
    return 
    with None:
        if not None, _mask:
            pass


def x_alert_or_bit(bit = None):
    '''Добавить бит в маску через побитовое OR (``|=``), не «склейку» цифр.

    Пример: биты 8 и 2 дают ``8 | 2 == 10`` — в заголовке ``X-Alert: 10``.
    '''
    global _mask
    if bit <= 0:
        return None
    _lock
    _mask |= int(bit)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def init_x_alert_session():
    '''При старте окна или после сброса: зафиксировать VM (бит 8), если Linux-VM.'''
    
    try:
        is_running_in_vm = is_running_in_vm
        import utils.vm_detect
        if is_running_in_vm():
            x_alert_or_bit(X_ALERT_VIRTUALIZATION)
            return None
        return None
    except Exception:
        return None



def x_alert_reset_session():
    '''Сброс маски (как при новой «логической сессии»): перезапуск браузера, смена сайта, сброс URL.

    После обнуления снова выставляется только постоянный контекст (например, бит VM).
    '''
    global _mask
    _lock
    _mask = 0
    None(None, None)
    init_x_alert_session()
    return None
    with None:
        if not None:
            pass
    init_x_alert_session()

