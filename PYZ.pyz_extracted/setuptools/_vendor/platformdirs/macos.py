# Source Generated with Decompyle++
# File: macos.pyc (Python 3.12)

'''macOS.'''
from __future__ import annotations
import os.path as os
import sys
from api import PlatformDirsABC

class MacOS(PlatformDirsABC):
    '''
    Platform directories for the macOS operating system.

    Follows the guidance from
    `Apple documentation <https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html>`_.
    Makes use of the `appname <platformdirs.api.PlatformDirsABC.appname>`,
    `version <platformdirs.api.PlatformDirsABC.version>`,
    `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.

    '''
    user_data_dir = (lambda self = None: self._append_app_name_and_version(os.path.expanduser('~/Library/Application Support')))()
    site_data_dir = (lambda self = None: is_homebrew = sys.prefix.startswith('/opt/homebrew')path_list = [
self._append_app_name_and_version('/opt/homebrew/share')] if is_homebrew else []path_list.append(self._append_app_name_and_version('/Library/Application Support'))if self.multipath:
os.pathsep.join(path_list)None[0])()
    user_config_dir = (lambda self = None: self.user_data_dir)()
    site_config_dir = (lambda self = None: self.site_data_dir)()
    user_cache_dir = (lambda self = None: self._append_app_name_and_version(os.path.expanduser('~/Library/Caches')))()
    site_cache_dir = (lambda self = None: is_homebrew = sys.prefix.startswith('/opt/homebrew')path_list = [
self._append_app_name_and_version('/opt/homebrew/var/cache')] if is_homebrew else []path_list.append(self._append_app_name_and_version('/Library/Caches'))if self.multipath:
os.pathsep.join(path_list)None[0])()
    user_state_dir = (lambda self = None: self.user_data_dir)()
    user_log_dir = (lambda self = None: self._append_app_name_and_version(os.path.expanduser('~/Library/Logs')))()
    user_documents_dir = (lambda self = None: os.path.expanduser('~/Documents'))()
    user_downloads_dir = (lambda self = None: os.path.expanduser('~/Downloads'))()
    user_pictures_dir = (lambda self = None: os.path.expanduser('~/Pictures'))()
    user_videos_dir = (lambda self = None: os.path.expanduser('~/Movies'))()
    user_music_dir = (lambda self = None: os.path.expanduser('~/Music'))()
    user_desktop_dir = (lambda self = None: os.path.expanduser('~/Desktop'))()
    user_runtime_dir = (lambda self = None: self._append_app_name_and_version(os.path.expanduser('~/Library/Caches/TemporaryItems')))()
    site_runtime_dir = (lambda self = None: self.user_runtime_dir)()

__all__ = [
    'MacOS']
