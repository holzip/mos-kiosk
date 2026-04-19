# Source Generated with Decompyle++
# File: version.pyc (Python 3.12)

'''Версия приложения: читается из установленного RPM-пакета.'''
import subprocess
_FALLBACK = 'dev'

def get_version():
    """Получить версию из RPM: rpm -q --qf '%{VERSION}-%{RELEASE}' mostech-kiosk."""
    
    try:
        result = subprocess.run([
            'rpm',
            '-q',
            '--qf',
            '%{VERSION}-%{RELEASE}',
            'mostech-kiosk'], capture_output = True, text = True, timeout = 3)
        if result.returncode == 0 and result.stdout.strip():
            ver = result.stdout.strip()
            parts = ver.split('.')
            if '-' in ver:
                (base, release_full) = ver.rsplit('-', 1)
                release_num = release_full.split('.')[0]
                return f'''{base}-{release_num}'''
            return None
        return None
    except Exception:
        return _FALLBACK


VERSION = get_version()
