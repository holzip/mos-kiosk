# Source Generated with Decompyle++
# File: wifi_worker.pyc (Python 3.12)

'''Асинхронный воркер WiFi. Подключение только через network.connection.connect_to_wifi
(единая логика nmcli dev wifi connect). Не добавлять сюда параллельные команды connect.'''
import subprocess
import time
from typing import Any, Dict, List
from PySide6.QtCore import QObject, Signal
from config.state import state
from network.connection import connect_to_wifi, ensure_wifi_adapter_ready, get_active_wifi_connection, get_ethernet_connection_info, is_wifi_adapter_present
from utils.logging_setup import logger

class AsyncWorker(QObject):
    pass
# WARNING: Decompyle incomplete

