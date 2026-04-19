# Source Generated with Decompyle++
# File: device.pyc (Python 3.12)

'''Идентификация устройства: machine-id, MAC-адрес, hostname.

Используется:
  - config/vault.py  → device-bound ключ шифрования (ENC|v1|)
  - network/session_auth.py → X-Kiosk-ID (UUID v5)
  - modules/incoming_connections_monitor.py → поля ``host_kiosk_id`` / ``host_device_raw_id``

Цепочка fallback:
  1. /etc/machine-id  — world-readable (0444), 32 hex-символа
  2. MAC первого физического интерфейса (wired > wireless)
  3. hostname — крайний fallback (не уникален)
'''
import os
import socket
import uuid
from typing import Optional
from utils.logging_setup import logger
_KIOSK_UUID_NAMESPACE = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')

def read_machine_id():
    '''/etc/machine-id — world-readable (0444), 32 hex-символа.

    Генерируется systemd/dbus при установке ОС, стабилен между перезагрузками.
    /var/lib/dbus/machine-id — обычно симлинк на тот же файл.
    '''
    pass
# WARNING: Decompyle incomplete


def get_mac_fallback():
    '''MAC первого физического интерфейса. Приоритет: wired > wireless.

    Читает /sys/class/net/ (world-readable, без root).
    Фильтрует: пропускает lo, виртуальные (нет /device), type != 1.
    Определяет wireless по наличию /wireless/ или /phy80211.
    '''
    sys_net = '/sys/class/net'
    wired_macs = []
    wireless_macs = []
# WARNING: Decompyle incomplete


def get_hostname_fallback():
    '''Последний fallback — hostname (не уникален, только если всё выше недоступно).'''
    return socket.gethostname()


def get_device_raw_id():
    '''Стабильный «сырой» идентификатор устройства (цепочка как для X-Kiosk-ID).

    Возвращает machine-id либо MAC либо hostname — всегда непустая строка.
    '''
    raw = read_machine_id()
    if raw:
        return raw
    raw = None()
    if raw:
        return raw
    return None()


def get_kiosk_uuid():
    '''Постоянный UUID киоска в том же виде, что ``X-Kiosk-ID`` (UUID v5 от raw id).'''
    return str(uuid.uuid5(_KIOSK_UUID_NAMESPACE, get_device_raw_id()))

