# Source Generated with Decompyle++
# File: vm_detect.pyc (Python 3.12)

'''Детект виртуальной машины и решение о тихом завершении процесса (Linux).

Назначение
    В продакшене киоск не должен работать в гостевой ОС (лицензирование, среда
    не соответствует целевому железу). Точка входа (mt_kiosk) вызывает
    ``should_exit_silently_on_vm()`` до создания QApplication: при срабатывании
    процесс завершается с кодом 0, без окон и сообщений.

Как определяется VM (достаточно одного срабатывания)
    * ``systemd-detect-virt`` — не ``none``;
    * флаг ``hypervisor`` в строке ``flags`` в ``/proc/cpuinfo``;
    * DMI: ``/sys/class/dmi/id/{product_name,sys_vendor,board_vendor,chassis_vendor}``
      содержит типичные для гипервизоров подстроки (KVM, QEMU, VMware, VirtualBox и т.д.).

Платформа
    Проверка только при ``sys.platform == "linux"``. На Windows и macOS VM
    не детектится, завершения из-за VM нет.

Разрешить запуск в VM (тестирование)
    1. Окружение: ``KIOSK_ALLOW_VM=1`` (или ``true`` / ``yes`` / ``on``).
    2. Конфиг: ``"allow_vm": true`` в ``mostech-kiosk.json`` (путь как у
       ``--config``, по умолчанию рядом с mt_kiosk.py).
    3. Пользовательский слой: ``~/.config/mostech-kiosk/overrides.json`` —
       если в файле явно заданы ключи ``allow_vm`` или ``kiosk_allow_vm``,
       они перекрывают базовый конфиг для этой проверки.

По умолчанию ключ ``allow_vm`` в конфиге отсутствует или ``false`` — на VM
запуск считается запрещённым.

Ограничения
    Детект эвристический; возможны ложные срабатывания и обход. При ошибке
    чтения конфига/импорта модуля вызывающий код может пропустить проверку
    (см. mt_kiosk).
'''
from __future__ import annotations
import json
import os
import re
import subprocess
import sys
_VM_HINTS = re.compile('vmware|virtualbox|qemu|kvm|xen|microsoft|parallels|bochs|innotek|virtual.?machine|standard.?pc.*qemu|openstack|nutanix|proxmox', re.I)

def _read_first_line(path = None, max_len = None):
    pass
# WARNING: Decompyle incomplete


def _systemd_detect_virt():
    
    try:
        r = subprocess.run([
            'systemd-detect-virt'], capture_output = True, text = True, timeout = 3)
        if r.returncode != 0:
            return False
            
            try:
                if not r.stdout:
                    r.stdout
                out = ''.strip().lower()
                if out:
                    out
                return bool(out != 'none')
            except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
                return False




def _cpu_hypervisor_flag():
    pass
# WARNING: Decompyle incomplete


def _dmi_looks_like_vm():
    base = '/sys/class/dmi/id'
    for name in ('product_name', 'sys_vendor', 'board_vendor', 'chassis_vendor'):
        val = _read_first_line(os.path.join(base, name))
        if not val:
            continue
        if not _VM_HINTS.search(val):
            continue
        ('product_name', 'sys_vendor', 'board_vendor', 'chassis_vendor')
        return True
    return False


def _resolve_config_path(project_root = None):
    '''Путь к JSON-конфигу (как у mt_kiosk: --config или mostech-kiosk.json).'''
    args = sys.argv[1:]
    i = 0
    if i < len(args):
        if args[i] == '--config' and i + 1 < len(args):
            p = args[i + 1].strip()
            if os.path.isabs(p):
                return p
            return None.path.normpath(os.path.join(project_root, p))
        if None[i].startswith('--config='):
            p = args[i].split('=', 1)[1].strip()
            if os.path.isabs(p):
                return p
            return None.path.normpath(os.path.join(project_root, p))
        None += 1
        if i < len(args):
            continue
    return os.path.join(project_root, 'mostech-kiosk.json')

_OVERRIDES_PATH = os.path.join(os.path.expanduser('~'), '.config', 'mostech-kiosk', 'overrides.json')

def _read_allow_vm_flag(path = None):
    pass
# WARNING: Decompyle incomplete


def vm_testing_allowed(project_root = None):
    '''Разрешён ли запуск приложения в виртуальной машине.

    Args:
        project_root: корень установки (каталог mt_kiosk.py), для разрешения
            пути к JSON при относительном ``--config``.

    Returns:
        True — блокировку VM не применять (тесты, разработка).
        False — если ни переменная окружения, ни конфиг не разрешают VM.

    Порядок проверки:
        1. ``KIOSK_ALLOW_VM`` ∈ {1, true, yes, on} → True.
        2. Если существует ``~/.config/mostech-kiosk/overrides.json`` и в нём
           есть ключ ``allow_vm`` или ``kiosk_allow_vm`` → значение из файла.
        3. Иначе читается основной конфиг (поля ``allow_vm`` / ``kiosk_allow_vm``).
    '''
    ev = os.environ.get('KIOSK_ALLOW_VM', '').strip().lower()
    if ev in ('1', 'true', 'yes', 'on'):
        return True
    cfg_main = _resolve_config_path(project_root)
# WARNING: Decompyle incomplete


def is_running_in_vm():
    '''Похоже ли текущее окружение на гостевую Linux-VM.

    Returns:
        True — хотя бы один из индикаторов (systemd-detect-virt, CPU flags,
        DMI) указывает на виртуализацию.
        False — не Linux, или признаков VM не найдено.

    Не учитывает конфиг и окружение ``KIOSK_ALLOW_VM``; только «сырой» детект.
    '''
    if sys.platform != 'linux':
        return False
    if _systemd_detect_virt():
        return True
    if _cpu_hypervisor_flag():
        return True
    if _dmi_looks_like_vm():
        return True
    return False


def should_exit_silently_on_vm(project_root = None):
    '''Нужно ли завершить процесс без UI до инициализации Qt.

    Args:
        project_root: каталог установки; см. параметр у ``vm_testing_allowed``.

    Returns:
        True — обнаружена VM и запуск в ней не разрешён конфигом/окружением;
            вызывающий код должен сделать ``return 0``.
        False — не VM, или ``vm_testing_allowed`` == True.

    Используется в ``mt_kiosk.main()`` сразу после проверки single-instance.
    '''
    if vm_testing_allowed(project_root):
        return False
    return is_running_in_vm()

