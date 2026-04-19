# Source Generated with Decompyle++
# File: android.pyc (Python 3.12)

'''Android.'''
from __future__ import annotations
import os
import re
import sys
from functools import lru_cache
from typing import TYPE_CHECKING, cast
from api import PlatformDirsABC

class Android(PlatformDirsABC):
    '''
    Follows the guidance `from here <https://android.stackexchange.com/a/216132>`_.

    Makes use of the `appname <platformdirs.api.PlatformDirsABC.appname>`, `version
    <platformdirs.api.PlatformDirsABC.version>`, `ensure_exists <platformdirs.api.PlatformDirsABC.ensure_exists>`.

    '''
    user_data_dir = (lambda self = None: self._append_app_name_and_version(cast(str, _android_folder()), 'files'))()
    site_data_dir = (lambda self = None: self.user_data_dir)()
    user_config_dir = (lambda self = None: self._append_app_name_and_version(cast(str, _android_folder()), 'shared_prefs'))()
    site_config_dir = (lambda self = None: self.user_config_dir)()
    user_cache_dir = (lambda self = None: self._append_app_name_and_version(cast(str, _android_folder()), 'cache'))()
    site_cache_dir = (lambda self = None: self.user_cache_dir)()
    user_state_dir = (lambda self = None: self.user_data_dir)()
    user_log_dir = (lambda self = None: path = self.user_cache_dirif self.opinion:
path = os.path.join(path, 'log')path)()
    user_documents_dir = (lambda self = None: _android_documents_folder())()
    user_downloads_dir = (lambda self = None: _android_downloads_folder())()
    user_pictures_dir = (lambda self = None: _android_pictures_folder())()
    user_videos_dir = (lambda self = None: _android_videos_folder())()
    user_music_dir = (lambda self = None: _android_music_folder())()
    user_desktop_dir = (lambda self = None: '/storage/emulated/0/Desktop')()
    user_runtime_dir = (lambda self = None: path = self.user_cache_dirif self.opinion:
path = os.path.join(path, 'tmp')path)()
    site_runtime_dir = (lambda self = None: self.user_runtime_dir)()

_android_folder = (lambda : result = None# WARNING: Decompyle incomplete
)()
_android_documents_folder = (lambda : try:
autoclass = autoclassimport jniuscontext = autoclass('android.content.Context')environment = autoclass('android.os.Environment')documents_dir = context.getExternalFilesDir(environment.DIRECTORY_DOCUMENTS).getAbsolutePath()documents_direxcept Exception:
documents_dir = '/storage/emulated/0/Documents'documents_dir)()
_android_downloads_folder = (lambda : try:
autoclass = autoclassimport jniuscontext = autoclass('android.content.Context')environment = autoclass('android.os.Environment')downloads_dir = context.getExternalFilesDir(environment.DIRECTORY_DOWNLOADS).getAbsolutePath()downloads_direxcept Exception:
downloads_dir = '/storage/emulated/0/Downloads'downloads_dir)()
_android_pictures_folder = (lambda : try:
autoclass = autoclassimport jniuscontext = autoclass('android.content.Context')environment = autoclass('android.os.Environment')pictures_dir = context.getExternalFilesDir(environment.DIRECTORY_PICTURES).getAbsolutePath()pictures_direxcept Exception:
pictures_dir = '/storage/emulated/0/Pictures'pictures_dir)()
_android_videos_folder = (lambda : try:
autoclass = autoclassimport jniuscontext = autoclass('android.content.Context')environment = autoclass('android.os.Environment')videos_dir = context.getExternalFilesDir(environment.DIRECTORY_DCIM).getAbsolutePath()videos_direxcept Exception:
videos_dir = '/storage/emulated/0/DCIM/Camera'videos_dir)()
_android_music_folder = (lambda : try:
autoclass = autoclassimport jniuscontext = autoclass('android.content.Context')environment = autoclass('android.os.Environment')music_dir = context.getExternalFilesDir(environment.DIRECTORY_MUSIC).getAbsolutePath()music_direxcept Exception:
music_dir = '/storage/emulated/0/Music'music_dir)()
__all__ = [
    'Android']
