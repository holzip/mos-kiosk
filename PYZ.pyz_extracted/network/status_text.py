# Source Generated with Decompyle++
# File: status_text.pyc (Python 3.12)

'''Тексты статуса сети для индикатора (без Qt).'''

def network_status_tooltip_base(data = None):
    '''Краткий текст статуса активной сети по данным AsyncWorker «check_wifi».

    Приоритет отображения: проводная сеть, затем Wi-Fi (как в индикаторе на панели).
    '''
    if not data.get('ethernet'):
        data.get('ethernet')
    eth_info = { }
    if not bool(data.get('has_ethernet_connection')):
        bool(data.get('has_ethernet_connection'))
    has_eth = bool(eth_info)
    has_wifi = data.get('has_wifi_connection', False)
    if not data.get('ssid'):
        data.get('ssid')
    ssid = ''.strip()
    wifi_present = data.get('wifi_enabled', False)
    if has_eth:
        if not eth_info.get('device'):
            eth_info.get('device')
        dev = ''.strip()
        if not eth_info.get('connection_name'):
            eth_info.get('connection_name')
        conn = ''.strip()
        if conn and dev:
            return f'''Локальная сеть: {conn} ({dev})'''
        if None:
            return f'''Локальная сеть ({dev})'''
    if has_wifi and ssid:
        return f'''Wi-Fi: {ssid}'''
    if None:
        return 'Wi-Fi подключён'
    if wifi_present:
        return 'Wi-Fi без активного подключения'
    return 'Нет подключения к сети'

