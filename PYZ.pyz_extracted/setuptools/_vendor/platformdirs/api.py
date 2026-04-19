# Source Generated with Decompyle++
# File: api.pyc (Python 3.12)

'''Base API.'''
from __future__ import annotations
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterator, Literal

class PlatformDirsABC(ABC):
    '''Abstract base class for platform directories.'''
    
    def __init__(self, appname, appauthor, version = None, roaming = None, multipath = None, opinion = (None, None, None, False, False, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'roaming', 'bool', 'multipath', 'bool', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'None')):
        '''
        Create a new platform directory.

        :param appname: See `appname`.
        :param appauthor: See `appauthor`.
        :param version: See `version`.
        :param roaming: See `roaming`.
        :param multipath: See `multipath`.
        :param opinion: See `opinion`.
        :param ensure_exists: See `ensure_exists`.

        '''
        self.appname = appname
        self.appauthor = appauthor
        self.version = version
        self.roaming = roaming
        self.multipath = multipath
        self.opinion = opinion
        self.ensure_exists = ensure_exists

    
    def _append_app_name_and_version(self = None, *base):
        params = list(base[1:])
        if self.appname:
            params.append(self.appname)
            if self.version:
                params.append(self.version)
    # WARNING: Decompyle incomplete

    
    def _optionally_create_directory(self = None, path = None):
        if self.ensure_exists:
            Path(path).mkdir(parents = True, exist_ok = True)
            return None

    user_data_dir = (lambda self = None: pass)()()
    site_data_dir = (lambda self = None: pass)()()
    user_config_dir = (lambda self = None: pass)()()
    site_config_dir = (lambda self = None: pass)()()
    user_cache_dir = (lambda self = None: pass)()()
    site_cache_dir = (lambda self = None: pass)()()
    user_state_dir = (lambda self = None: pass)()()
    user_log_dir = (lambda self = None: pass)()()
    user_documents_dir = (lambda self = None: pass)()()
    user_downloads_dir = (lambda self = None: pass)()()
    user_pictures_dir = (lambda self = None: pass)()()
    user_videos_dir = (lambda self = None: pass)()()
    user_music_dir = (lambda self = None: pass)()()
    user_desktop_dir = (lambda self = None: pass)()()
    user_runtime_dir = (lambda self = None: pass)()()
    site_runtime_dir = (lambda self = None: pass)()()
    user_data_path = (lambda self = None: Path(self.user_data_dir))()
    site_data_path = (lambda self = None: Path(self.site_data_dir))()
    user_config_path = (lambda self = None: Path(self.user_config_dir))()
    site_config_path = (lambda self = None: Path(self.site_config_dir))()
    user_cache_path = (lambda self = None: Path(self.user_cache_dir))()
    site_cache_path = (lambda self = None: Path(self.site_cache_dir))()
    user_state_path = (lambda self = None: Path(self.user_state_dir))()
    user_log_path = (lambda self = None: Path(self.user_log_dir))()
    user_documents_path = (lambda self = None: Path(self.user_documents_dir))()
    user_downloads_path = (lambda self = None: Path(self.user_downloads_dir))()
    user_pictures_path = (lambda self = None: Path(self.user_pictures_dir))()
    user_videos_path = (lambda self = None: Path(self.user_videos_dir))()
    user_music_path = (lambda self = None: Path(self.user_music_dir))()
    user_desktop_path = (lambda self = None: Path(self.user_desktop_dir))()
    user_runtime_path = (lambda self = None: Path(self.user_runtime_dir))()
    site_runtime_path = (lambda self = None: Path(self.site_runtime_dir))()
    
    def iter_config_dirs(self = None):
        ''':yield: all user and site configuration directories.'''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_data_dirs(self = None):
        ''':yield: all user and site data directories.'''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_cache_dirs(self = None):
        ''':yield: all user and site cache directories.'''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_runtime_dirs(self = None):
        ''':yield: all user and site runtime directories.'''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_config_paths(self = None):
        ''':yield: all user and site configuration paths.'''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_data_paths(self = None):
        ''':yield: all user and site data paths.'''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_cache_paths(self = None):
        ''':yield: all user and site cache paths.'''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_runtime_paths(self = None):
        ''':yield: all user and site runtime paths.'''
        pass
    # WARNING: Decompyle incomplete


