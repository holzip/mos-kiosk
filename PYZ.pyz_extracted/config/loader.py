# Source Generated with Decompyle++
# File: loader.pyc (Python 3.12)

'''Загрузка, создание и сохранение конфигурации киоска.

Порядок загрузки при старте (main_parser):
  1. Парсинг --config и --profile
  2. load_config()  → читаем JSON с диска
  3. База профиля: config/profiles/<profile>.json — сверка SHA-256 с config/profile_hashes.py
     (пересбор после правок: python3 tools/gen_profile_hashes.py)
  4. Поверх базы данные из файла --config (для mcko из файла — только kiosk_smc и kiosk_ss)
  5. vault.migrate_config_fields() → ENC|v0| → ENC|v1| при первом запуске на АРМ
  6. vault.decode_sensitive_fields() → декодируем ENC|v1|... поля (соль, пароли)
  7. validate_config() → проверка структуры; ошибки → диалог + завершение
  8. apply_config() → применяем в state.*

Чувствительные поля (kiosk_ss, kiosk_smc, wifi_password) могут храниться
в закодированном виде (ENC|v1|...) с помощью config/vault.py.
Для кодирования/декодирования на конкретном АРМ:
    python3 config/vault.py encode "значение"
'''
import argparse
import getpass
import grp
import hashlib
import json
import os
import sys
import pwd
import shutil
import stat
import subprocess
import tempfile
import time
from PySide6.QtWidgets import QApplication, QMessageBox
from utils.qt_message_box_style import apply_kiosk_qmessagebox_style
from config.browser_defaults import DEFAULT_BROWSER_USER_AGENT
from config.state import _DEFAULTS, apply_config
from config.vault import decode, decode_sensitive_fields, is_encoded, migrate_config_fields
from utils.logging_setup import logger
_PROFILE_KIOSK = 'kiosk'
_PROFILE_MCKO = 'mcko'
_SUPPORTED_PROFILES = (_PROFILE_KIOSK, _PROFILE_MCKO)
_PROTECTED_OVERRIDE_KEYS = {
    'kiosk_ss',
    'kiosk_smc'}

def _config_package_dir():
