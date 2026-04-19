# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

'''
Utilities for determining application-specific dirs.

See <https://github.com/platformdirs/platformdirs> for details and usage.

'''
from __future__ import annotations
import os
import sys
from typing import TYPE_CHECKING
from api import PlatformDirsABC
from version import __version__
from version import __version_tuple__ as __version_info__
if TYPE_CHECKING:
    from pathlib import Path
    from typing import Literal

def _set_platform_dir_class():
    if sys.platform == 'win32':
        Result = Windows
        import platformdirs.windows
    elif sys.platform == 'darwin':
        Result = MacOS
        import platformdirs.macos
    else:
        Result = Unix
        import platformdirs.unix
# WARNING: Decompyle incomplete

PlatformDirs = _set_platform_dir_class()
AppDirs = PlatformDirs

def user_data_dir(appname = None, appauthor = None, version = None, roaming = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'roaming', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data directory tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, roaming = roaming, ensure_exists = ensure_exists).user_data_dir


def site_data_dir(appname = None, appauthor = None, version = None, multipath = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'multipath', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data directory shared by users
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, multipath = multipath, ensure_exists = ensure_exists).site_data_dir


def user_config_dir(appname = None, appauthor = None, version = None, roaming = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'roaming', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config directory tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, roaming = roaming, ensure_exists = ensure_exists).user_config_dir


def site_config_dir(appname = None, appauthor = None, version = None, multipath = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'multipath', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config directory shared by the users
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, multipath = multipath, ensure_exists = ensure_exists).site_config_dir


def user_cache_dir(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache directory tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).user_cache_dir


def site_cache_dir(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache directory tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).site_cache_dir


def user_state_dir(appname = None, appauthor = None, version = None, roaming = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'roaming', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: state directory tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, roaming = roaming, ensure_exists = ensure_exists).user_state_dir


def user_log_dir(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: log directory tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).user_log_dir


def user_documents_dir():
    ''':returns: documents directory tied to the user'''
    return PlatformDirs().user_documents_dir


def user_downloads_dir():
    ''':returns: downloads directory tied to the user'''
    return PlatformDirs().user_downloads_dir


def user_pictures_dir():
    ''':returns: pictures directory tied to the user'''
    return PlatformDirs().user_pictures_dir


def user_videos_dir():
    ''':returns: videos directory tied to the user'''
    return PlatformDirs().user_videos_dir


def user_music_dir():
    ''':returns: music directory tied to the user'''
    return PlatformDirs().user_music_dir


def user_desktop_dir():
    ''':returns: desktop directory tied to the user'''
    return PlatformDirs().user_desktop_dir


def user_runtime_dir(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime directory tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).user_runtime_dir


def site_runtime_dir(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'str')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime directory shared by users
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).site_runtime_dir


def user_data_path(appname = None, appauthor = None, version = None, roaming = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'roaming', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data path tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, roaming = roaming, ensure_exists = ensure_exists).user_data_path


def site_data_path(appname = None, appauthor = None, version = None, multipath = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'multipath', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `multipath <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: data path shared by users
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, multipath = multipath, ensure_exists = ensure_exists).site_data_path


def user_config_path(appname = None, appauthor = None, version = None, roaming = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'roaming', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config path tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, roaming = roaming, ensure_exists = ensure_exists).user_config_path


def site_config_path(appname = None, appauthor = None, version = None, multipath = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'multipath', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param multipath: See `roaming <platformdirs.api.PlatformDirsABC.multipath>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: config path shared by the users
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, multipath = multipath, ensure_exists = ensure_exists).site_config_path


def site_cache_path(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache directory tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).site_cache_path


def user_cache_path(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: cache path tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).user_cache_path


def user_state_path(appname = None, appauthor = None, version = None, roaming = (None, None, None, False, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'roaming', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param roaming: See `roaming <platformdirs.api.PlatformDirsABC.roaming>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: state path tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, roaming = roaming, ensure_exists = ensure_exists).user_state_path


def user_log_path(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `roaming <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: log path tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).user_log_path


def user_documents_path():
    ''':returns: documents a path tied to the user'''
    return PlatformDirs().user_documents_path


def user_downloads_path():
    ''':returns: downloads path tied to the user'''
    return PlatformDirs().user_downloads_path


def user_pictures_path():
    ''':returns: pictures path tied to the user'''
    return PlatformDirs().user_pictures_path


def user_videos_path():
    ''':returns: videos path tied to the user'''
    return PlatformDirs().user_videos_path


def user_music_path():
    ''':returns: music path tied to the user'''
    return PlatformDirs().user_music_path


def user_desktop_path():
    ''':returns: desktop path tied to the user'''
    return PlatformDirs().user_desktop_path


def user_runtime_path(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime path tied to the user
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).user_runtime_path


def site_runtime_path(appname = None, appauthor = None, version = None, opinion = (None, None, None, True, False), ensure_exists = ('appname', 'str | None', 'appauthor', 'str | None | Literal[False]', 'version', 'str | None', 'opinion', 'bool', 'ensure_exists', 'bool', 'return', 'Path')):
    '''
    :param appname: See `appname <platformdirs.api.PlatformDirsABC.appname>`.
    :param appauthor: See `appauthor <platformdirs.api.PlatformDirsABC.appauthor>`.
    :param version: See `version <platformdirs.api.PlatformDirsABC.version>`.
    :param opinion: See `opinion <platformdirs.api.PlatformDirsABC.opinion>`.
    :param ensure_exists: See `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.
    :returns: runtime path shared by users
    '''
    return PlatformDirs(appname = appname, appauthor = appauthor, version = version, opinion = opinion, ensure_exists = ensure_exists).site_runtime_path

__all__ = [
    'AppDirs',
    'PlatformDirs',
    'PlatformDirsABC',
    '__version__',
    '__version_info__',
    'site_cache_dir',
    'site_cache_path',
    'site_config_dir',
    'site_config_path',
    'site_data_dir',
    'site_data_path',
    'site_runtime_dir',
    'site_runtime_path',
    'user_cache_dir',
    'user_cache_path',
    'user_config_dir',
    'user_config_path',
    'user_data_dir',
    'user_data_path',
    'user_desktop_dir',
    'user_desktop_path',
    'user_documents_dir',
    'user_documents_path',
    'user_downloads_dir',
    'user_downloads_path',
    'user_log_dir',
    'user_log_path',
    'user_music_dir',
    'user_music_path',
    'user_pictures_dir',
    'user_pictures_path',
    'user_runtime_dir',
    'user_runtime_path',
    'user_state_dir',
    'user_state_path',
    'user_videos_dir',
    'user_videos_path']
