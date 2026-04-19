# Source Generated with Decompyle++
# File: net_addrs.pyc (Python 3.12)

'''Чтение IPv4-адресов интерфейсов (``ip`` из iproute2, Linux).'''
from __future__ import annotations
import subprocess
from typing import List
from utils.logging_setup import logger

def list_non_loopback_ipv4_addrs():
    '''Адреса IPv4 всех интерфейсов кроме loopback (порядок как в выводе ``ip``).'''
    
    try:
        result = subprocess.run([
            'ip',
            '-o',
            '-4',
            'addr',
            'show'], capture_output = True, text = True, timeout = 5)
        if result.returncode != 0:
            return []
        out = None
        if not result.stdout:
            result.stdout
        for line in ''.splitlines():
            if line.strip() or 'loopback' in line.lower():
                continue
            parts = line.split()
            for i, p in enumerate(parts):
                if not p == 'inet':
                    continue
                if not i + 1 < len(parts):
                    continue
                with_mask = parts[i + 1]
                addr = with_mask.split('/', 1)[0].strip()
                if addr:
                    out.append(addr)
                enumerate(parts)
        return out
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        e = None
        logger.debug('list_non_loopback_ipv4_addrs: %s', e)
        del e
        return None
        None = 
        del e


