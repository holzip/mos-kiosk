# Source Generated with Decompyle++
# File: windows.pyc (Python 3.12)

'''Windows.'''
from __future__ import annotations
import os
import sys
from functools import lru_cache
from typing import TYPE_CHECKING
from api import PlatformDirsABC
if TYPE_CHECKING:
    from collections.abc import Callable

class Windows(PlatformDirsABC):
    '''
    `MSDN on where to store app data files <https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid>`_.

    Makes use of the `appname <platformdirs.api.PlatformDirsABC.appname>`, `appauthor
    <platformdirs.api.PlatformDirsABC.appauthor>`, `version <platformdirs.api.PlatformDirsABC.version>`, `roaming
    <platformdirs.api.PlatformDirsABC.roaming>`, `opinion <platformdirs.api.PlatformDirsABC.opinion>`, `ensure_exists
    <platformdirs.api.PlatformDirsABC.ensure_exists>`.

    '''
    user_data_dir = (lambda self = None: const = 'CSIDL_APPDATA' if self.roaming else 'CSIDL_LOCAL_APPDATA'path = os.path.normpath(get_win_folder(const))self._append_parts(path))()
    
    def _append_parts(self = None, path = None, *, opinion_value):
        params = []
    # WARNING: Decompyle incomplete

    site_data_dir = (lambda self = None: path = os.path.normpath(get_win_folder('CSIDL_COMMON_APPDATA'))self._append_parts(path))()
    user_config_dir = (lambda self = None: self.user_data_dir)()
    site_config_dir = (lambda self = None: self.site_data_dir)()
    user_cache_dir = (lambda self = None: path = os.path.normpath(get_win_folder('CSIDL_LOCAL_APPDATA'))self._append_parts(path, opinion_value = 'Cache'))()
    site_cache_dir = (lambda self = None: path = os.path.normpath(get_win_folder('CSIDL_COMMON_APPDATA'))self._append_parts(path, opinion_value = 'Cache'))()
    user_state_dir = (lambda self = None: self.user_data_dir)()
    user_log_dir = (lambda self = None: path = self.user_data_dirif self.opinion:
path = os.path.join(path, 'Logs')self._optionally_create_directory(path)path)()
    user_documents_dir = (lambda self = None: os.path.normpath(get_win_folder('CSIDL_PERSONAL')))()
    user_downloads_dir = (lambda self = None: os.path.normpath(get_win_folder('CSIDL_DOWNLOADS')))()
    user_pictures_dir = (lambda self = None: os.path.normpath(get_win_folder('CSIDL_MYPICTURES')))()
    user_videos_dir = (lambda self = None: os.path.normpath(get_win_folder('CSIDL_MYVIDEO')))()
    user_music_dir = (lambda self = None: os.path.normpath(get_win_folder('CSIDL_MYMUSIC')))()
    user_desktop_dir = (lambda self = None: os.path.normpath(get_win_folder('CSIDL_DESKTOPDIRECTORY')))()
    user_runtime_dir = (lambda self = None: path = os.path.normpath(os.path.join(get_win_folder('CSIDL_LOCAL_APPDATA'), 'Temp'))self._append_parts(path))()
    site_runtime_dir = (lambda self = None: self.user_runtime_dir)()


def get_win_folder_from_env_vars(csidl_name = None):
    '''Get folder from environment variables.'''
    result = get_win_folder_if_csidl_name_not_env_var(csidl_name)
# WARNING: Decompyle incomplete


def get_win_folder_if_csidl_name_not_env_var(csidl_name = None):
    '''Get a folder for a CSIDL name that does not exist as an environment variable.'''
    if csidl_name == 'CSIDL_PERSONAL':
        return os.path.join(os.path.normpath(os.environ['USERPROFILE']), 'Documents')
    if None == 'CSIDL_DOWNLOADS':
        return os.path.join(os.path.normpath(os.environ['USERPROFILE']), 'Downloads')
    if None == 'CSIDL_MYPICTURES':
        return os.path.join(os.path.normpath(os.environ['USERPROFILE']), 'Pictures')
    if None == 'CSIDL_MYVIDEO':
        return os.path.join(os.path.normpath(os.environ['USERPROFILE']), 'Videos')
    if None == 'CSIDL_MYMUSIC':
        return os.path.join(os.path.normpath(os.environ['USERPROFILE']), 'Music')


def get_win_folder_from_registry(csidl_name = None):
    """
    Get folder from the registry.

    This is a fallback technique at best. I'm not sure if using the registry for these guarantees us the correct answer
    for all CSIDL_* names.

    """
    shell_folder_name = {
        'CSIDL_APPDATA': 'AppData',
        'CSIDL_COMMON_APPDATA': 'Common AppData',
        'CSIDL_LOCAL_APPDATA': 'Local AppData',
        'CSIDL_PERSONAL': 'Personal',
        'CSIDL_DOWNLOADS': '{374DE290-123F-4565-9164-39C4925E467B}',
        'CSIDL_MYPICTURES': 'My Pictures',
        'CSIDL_MYVIDEO': 'My Video',
        'CSIDL_MYMUSIC': 'My Music' }.get(csidl_name)
# WARNING: Decompyle incomplete


def get_win_folder_via_ctypes(csidl_name = None):
    '''Get folder with ctypes.'''
    import ctypes
    csidl_const = {
        'CSIDL_APPDATA': 26,
        'CSIDL_COMMON_APPDATA': 35,
        'CSIDL_LOCAL_APPDATA': 28,
        'CSIDL_PERSONAL': 5,
        'CSIDL_MYPICTURES': 39,
        'CSIDL_MYVIDEO': 14,
        'CSIDL_MYMUSIC': 13,
        'CSIDL_DOWNLOADS': 40,
        'CSIDL_DESKTOPDIRECTORY': 16 }.get(csidl_name)
# WARNING: Decompyle incomplete


def _pick_get_win_folder():
    
    try:
        import ctypes
        if hasattr(ctypes, 'windll'):
            return get_win_folder_via_ctypes
        
        try:
            import winreg
            return get_win_folder_from_registry
            except ImportError:
                continue
        except ImportError:
            return 



get_win_folder = lru_cache(maxsize = None)(_pick_get_win_folder())
__all__ = [
    'Windows']
