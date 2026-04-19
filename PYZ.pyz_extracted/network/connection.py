# Source Generated with Decompyle++
# File: connection.pyc (Python 3.12)

'''Проверка сети и WiFi через nmcli.

Единая точка подключения к WiFi — функция connect_to_wifi().
Во всём KIOSK_v3 не должно быть других вызовов «nmcli … wifi connect» и не должно
быть ручного создания профиля через «nmcli connection add …» перед подключением:
только «nmcli dev wifi connect <SSID> [password …]». Отключение от чужой сети —
«nmcli connection down id …» (см. force_disconnect_ssid).

Админка, автоподключение при старте и любые будущие сценарии — только через
connect_to_wifi(); дублировать логику nmcli в других модулях запрещено.
'''
import subprocess
import time
import urllib.request as urllib
import ssl
from typing import Optional, Tuple
from utils.logging_setup import logger
from utils.net_addrs import list_non_loopback_ipv4_addrs

def check_network_has_ip():
    '''Проверка наличия IP у сетевых адаптеров (кроме loopback).'''
    return bool(list_non_loopback_ipv4_addrs())


def _parse_nmcli_device_status_line(line = None):
    '''
    Парсит одну строку вывода nmcli -t -f DEVICE,TYPE,STATE,CONNECTION device status.
    Возвращает (device, dtype, state, connection_name) или None.
    '''
    if not line or line.strip():
        return None
    parts = line.split(':')
    if len(parts) < 4:
        return None
    device = parts[0]
    dtype = parts[1].lower()
    state = parts[2].lower()
    connection_name = ':'.join(parts[3:]).strip()
    return (device, dtype, state, connection_name)


def _is_wifi_device_type(dtype = None):
    '''Проверка, что тип устройства — WiFi (wifi, 802-11-wireless, wireless).'''
    if not dtype:
        return False
    d = dtype.lower()
    if not d == 'wifi':
        d == 'wifi'
        if not d == '802-11-wireless':
            d == '802-11-wireless'
    return 'wireless' in d


def _get_active_wifi_from_connection_show():
    '''Активное WiFi-подключение из nmcli connection show --active. Возвращает имя или None.'''
    
    try:
        result = subprocess.run([
            'nmcli',
            '-t',
            '-f',
            'NAME,TYPE',
            'connection',
            'show',
            '--active'], capture_output = True, text = True, timeout = 2)
        if not result.stdout:
            result.stdout
        for line in ''.strip().split('\n'):
            if not line:
                continue
            parts = line.split(':')
            if not len(parts) >= 2:
                continue
                
                try:
                    name = ':'.join(parts[:-1]).strip()
                    if not parts[-1]:
                        parts[-1]
                    typ = ''.lower()
                    if not _is_wifi_device_type(typ):
                        continue
                        
                        try:
                            if not name:
                                continue
                                
                                try:
                                    if not name != '--':
                                        continue
                                        
                                        try:
                                            
                                            return ''.strip().split('\n'), name
                                            
                                            try:
                                                return None
                                            except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
                                                return None








def get_active_wifi_connection():
    '''Возвращает имя (SSID/connection) активного WiFi-подключения, или None.

    Сначала проверяет nmcli device status, затем fallback через connection show --active.
    '''
    
    try:
        result = subprocess.run([
            'nmcli',
            '-t',
            '-f',
            'DEVICE,TYPE,STATE,CONNECTION',
            'device',
            'status'], capture_output = True, text = True, timeout = 3)
        if not result.stdout:
            result.stdout
        for line in ''.strip().split('\n'):
            parsed = _parse_nmcli_device_status_line(line)
            if not parsed:
                continue
                
                try:
                    (_dev, dtype, connection_state, connection_name) = parsed
                    if not _is_wifi_device_type(dtype):
                        continue
                        
                        try:
                            if not connection_state in ('connected', 'connecting'):
                                continue
                                
                                try:
                                    if not connection_name:
                                        continue
                                        
                                        try:
                                            if not connection_name != '--':
                                                continue
                                                
                                                try:
                                                    
                                                    return ''.strip().split('\n'), connection_name
                                                    
                                                    try:
                                                        return _get_active_wifi_from_connection_show()
                                                    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
                                                        return _get_active_wifi_from_connection_show()









def is_wifi_adapter_present():
    '''Проверяет, есть ли хотя бы один WiFi-адаптер в системе.'''
    
    try:
        result = subprocess.run([
            'nmcli',
            '-t',
            '-f',
            'DEVICE,TYPE,STATE,CONNECTION',
            'device',
            'status'], capture_output = True, text = True, timeout = 3)
        if not result.stdout:
            result.stdout
        for line in ''.strip().split('\n'):
            parsed = _parse_nmcli_device_status_line(line)
            if not parsed:
                continue
                
                try:
                    if not _is_wifi_device_type(parsed[1]):
                        continue
                        
                        try:
                            ''.strip().split('\n')
                            return True
                            
                            try:
                                return False
                            except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
                                return False






def ensure_wifi_adapter_ready(max_wait_sec = None):
    '''
    Включить WiFi-радио и дождаться, пока адаптер станет активен.
    Возвращает True, если адаптер готов.
    '''
    
    try:
        subprocess.run([
            'nmcli',
            'radio',
            'wifi',
            'on'], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL, timeout = 5)
        time.sleep(1)
        deadline = time.time() + max_wait_sec
        if time.time() < deadline:
            result = subprocess.run([
                'nmcli',
                '-t',
                '-f',
                'DEVICE,TYPE,STATE',
                'device',
                'status'], capture_output = True, text = True, timeout = 3)
            if not result.stdout:
                result.stdout
            for line in ''.strip().split('\n'):
                if line or 'wifi' not in line.lower():
                    continue
                parts = line.split(':')
                if not len(parts) >= 3:
                    continue
                    
                    try:
                        state = parts[2].strip().lower()
                        if not state in ('disconnected', 'connected', 'connecting'):
                            continue
                            
                            try:
                                ''.strip().split('\n')
                                return True
                                
                                try:
                                    time.sleep(1)
                                    if time.time() < deadline:
                                        continue
                                    return False
                                except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
                                    return False






def connect_to_wifi(ssid = None, password = None, force_disconnect_ssid = None, auto_enable_wifi = ('', None, True)):
    '''Подключение: одна команда ``nmcli dev wifi connect`` (без предварительного
    ``nmcli connection add``). Пароль опционален для открытых сетей.

    NetworkManager после успеха может сохранить соединение у себя — это не отдельный
    шаг киоска; в коде нет ручной сборки профиля.

    Returns:
        (success, message)
    '''
    if not ssid or ssid.strip():
        return (False, 'Не указан SSID')
    if force_disconnect_ssid:
        
        try:
            subprocess.run([
                'nmcli',
                'connection',
                'down',
                'id',
                force_disconnect_ssid], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL, timeout = 5)
            time.sleep(1)
            if not auto_enable_wifi and ensure_wifi_adapter_ready(max_wait_sec = 12):
                logger.warning('WiFi адаптер не стал активен за отведённое время')
            if password:
                cmd = [
                    'nmcli',
                    '--wait',
                    '45',
                    'dev',
                    'wifi',
                    'connect',
                    ssid,
                    'password',
                    password]
            else:
                cmd = [
                    'nmcli',
                    '--wait',
                    '45',
                    'dev',
                    'wifi',
                    'connect',
                    ssid]
            
            try:
                result = subprocess.run(cmd, capture_output = True, text = True, timeout = 50)
                if result.returncode == 0:
                    logger.info('Подключен к %s', ssid)
                    return (True, f'''Подключен к {ssid}''')
                if not None.stderr:
                    None.stderr
                    if not result.stdout:
                        result.stdout
                err = ''.strip()
                if not err:
                    err
                return (False, 'Ошибка подключения к WiFi')
                except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
                    e = None
                    logger.warning('Ошибка при отключении от %s: %s', force_disconnect_ssid, e)
                    e = None
                    del e
                    continue
                    e = None
                    del e
            except subprocess.TimeoutExpired:
                logger.warning('WiFi подключение: таймаут nmcli (%s)', ssid)
                return (False, 'Таймаут подключения к WiFi')
                except OSError:
                    e = None
                    logger.warning('WiFi подключение: ошибка запуска nmcli: %s', e)
                    del e
                    return None
                    None = 
                    del e




def get_ethernet_connection_info():
    '''Проверка подключения по Ethernet. Возвращает dict (device, connection_name, ip_list) или None.'''
    pass
# WARNING: Decompyle incomplete


def check_internet_connection_unified(timeout_internal = None, timeout_external = None):
    '''Проверка "интернет есть".

    Логика:
    - если нет IP ни на одном интерфейсе → интернета точно нет
    - если IP есть → короткая HTTP(S) проверка достижимости (в фоне)

    timeout_internal: reserved (совместимость), сейчас не используется
    timeout_external: таймаут HTTP(S) проверки
    '''
    if not check_network_has_ip():
        return False
    test_url = 'https://ya.ru'
    
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(test_url, method = 'GET', headers = {
            'User-Agent': 'mostech-kiosk/3' })
        resp = urllib.request.urlopen(req, timeout = timeout_external, context = ctx)
        code = getattr(resp, 'status', 200)
        if  <= 200, int(code):
             <= 200, int(code)
        else:
            
            
            try:
                None(None, None)
                return 
                with None:
                    if not None, None, 200, int(code) < 500:
                        pass
                
                try:
                    return None
                    
                    try:
                        pass
                    except Exception:
                        logger.debug('internet check failed: %s', e)
                        None = None
                        del e
                        return False
                        e = None
                        del e





