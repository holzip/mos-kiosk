# Source Generated with Decompyle++
# File: unix.pyc (Python 3.12)

'''Unix.'''
from __future__ import annotations
import os
import sys
from configparser import ConfigParser
from pathlib import Path
from typing import Iterator, NoReturn
from api import PlatformDirsABC
if sys.platform == 'win32':
    
    def getuid():
        msg = 'should only be used on Unix'
        raise RuntimeError(msg)

else:
    from os import getuid

class Unix(PlatformDirsABC):
    '''
    On Unix/Linux, we follow the `XDG Basedir Spec <https://specifications.freedesktop.org/basedir-spec/basedir-spec-
    latest.html>`_.

    The spec allows overriding directories with environment variables. The examples shown are the default values,
    alongside the name of the environment variable that overrides them. Makes use of the `appname
    <platformdirs.api.PlatformDirsABC.appname>`, `version <platformdirs.api.PlatformDirsABC.version>`, `multipath
    <platformdirs.api.PlatformDirsABC.multipath>`, `opinion <platformdirs.api.PlatformDirsABC.opinion>`, `ensure_exists
    <platformdirs.api.PlatformDirsABC.ensure_exists>`.

    '''
    user_data_dir = (lambda self = None: path = os.environ.get('XDG_DATA_HOME', '')if not path.strip():
path = os.path.expanduser('~/.local/share')self._append_app_name_and_version(path))()
    _site_data_dirs = (lambda self = None: path = os.environ.get('XDG_DATA_DIRS', '')if not path.strip():
path = f'''/usr/local/share{os.pathsep}/usr/share'''# WARNING: Decompyle incomplete
)()
    site_data_dir = (lambda self = None: dirs = self._site_data_dirsif not self.multipath:
dirs[0]None.pathsep.join(dirs))()
    user_config_dir = (lambda self = None: path = os.environ.get('XDG_CONFIG_HOME', '')if not path.strip():
path = os.path.expanduser('~/.config')self._append_app_name_and_version(path))()
    _site_config_dirs = (lambda self = None: path = os.environ.get('XDG_CONFIG_DIRS', '')if not path.strip():
path = '/etc/xdg'# WARNING: Decompyle incomplete
)()
    site_config_dir = (lambda self = None: dirs = self._site_config_dirsif not self.multipath:
dirs[0]None.pathsep.join(dirs))()
    user_cache_dir = (lambda self = None: path = os.environ.get('XDG_CACHE_HOME', '')if not path.strip():
path = os.path.expanduser('~/.cache')self._append_app_name_and_version(path))()
    site_cache_dir = (lambda self = None: self._append_app_name_and_version('/var/cache'))()
    user_state_dir = (lambda self = None: path = os.environ.get('XDG_STATE_HOME', '')if not path.strip():
path = os.path.expanduser('~/.local/state')self._append_app_name_and_version(path))()
    user_log_dir = (lambda self = None: path = self.user_state_dirif self.opinion:
path = os.path.join(path, 'log')self._optionally_create_directory(path)path)()
    user_documents_dir = (lambda self = None: _get_user_media_dir('XDG_DOCUMENTS_DIR', '~/Documents'))()
    user_downloads_dir = (lambda self = None: _get_user_media_dir('XDG_DOWNLOAD_DIR', '~/Downloads'))()
    user_pictures_dir = (lambda self = None: _get_user_media_dir('XDG_PICTURES_DIR', '~/Pictures'))()
    user_videos_dir = (lambda self = None: _get_user_media_dir('XDG_VIDEOS_DIR', '~/Videos'))()
    user_music_dir = (lambda self = None: _get_user_media_dir('XDG_MUSIC_DIR', '~/Music'))()
    user_desktop_dir = (lambda self = None: _get_user_media_dir('XDG_DESKTOP_DIR', '~/Desktop'))()
    user_runtime_dir = (lambda self = None: path = os.environ.get('XDG_RUNTIME_DIR', '')if not path.strip():
if sys.platform.startswith(('freebsd', 'openbsd', 'netbsd')):
path = f'''/var/run/user/{getuid()}'''if not Path(path).exists():
path = f'''/tmp/runtime-{getuid()}'''else:
path = f'''/run/user/{getuid()}'''self._append_app_name_and_version(path))()
    site_runtime_dir = (lambda self = None: path = os.environ.get('XDG_RUNTIME_DIR', '')if not path.strip():
if sys.platform.startswith(('freebsd', 'openbsd', 'netbsd')):
path = '/var/run'else:
path = '/run'self._append_app_name_and_version(path))()
    site_data_path = (lambda self = None: self._first_item_as_path_if_multipath(self.site_data_dir))()
    site_config_path = (lambda self = None: self._first_item_as_path_if_multipath(self.site_config_dir))()
    site_cache_path = (lambda self = None: self._first_item_as_path_if_multipath(self.site_cache_dir))()
    
    def _first_item_as_path_if_multipath(self = None, directory = None):
        if self.multipath:
            directory = directory.split(os.pathsep)[0]
        return Path(directory)

    
    def iter_config_dirs(self = None):
        ''':yield: all user and site configuration directories.'''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_data_dirs(self = None):
        ''':yield: all user and site data directories.'''
        pass
    # WARNING: Decompyle incomplete



def _get_user_media_dir(env_var = None, fallback_tilde_path = None):
    media_dir = _get_user_dirs_folder(env_var)
# WARNING: Decompyle incomplete


def _get_user_dirs_folder(key = None):
    '''
    Return directory from user-dirs.dirs config file.

    See https://freedesktop.org/wiki/Software/xdg-user-dirs/.

    '''
    user_dirs_config_path = Path(Unix().user_config_dir) / 'user-dirs.dirs'
    if user_dirs_config_path.exists():
        parser = ConfigParser()
        stream = user_dirs_config_path.open()
        parser.read_string(f'''[top]\n{stream.read()}''')
        None(None, None)
        if key not in parser['top']:
            return None
        path = parser['top'][key].strip('"')
        return path.replace('$HOME', os.path.expanduser('~'))
    with None:
        if not None:
            pass
    continue

__all__ = [
    'Unix']
