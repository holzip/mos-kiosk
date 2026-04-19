# Source Generated with Decompyle++
# File: state.pyc (Python 3.12)

__doc__ = '\nГлобальное состояние из конфига и константы UI.\nПосле загрузки конфига вызывается apply_config(config).\n'
from PySide6.QtCore import Qt
from config.browser_defaults import DEFAULT_BROWSER_USER_AGENT

class ConfigState:
    '''Хранилище настроек из конфига (заполняется через apply_config).

    Сессионные флаги (не из конфига, сбрасываются при перезапуске):
      service_mode_active — сервисное меню разблокировано в текущей сессии.
      CONFIG_FILE_PATH    — путь к загруженному файлу конфига (для сохранения).
    '''
    service_mode_active: bool = False
    CONFIG_FILE_PATH: str = ''
    CONFIG_OVERRIDE_PATH: str = ''
    RUN_MODE: str = 'kiosk'
    LAUNCH_CONTEXT: str = 'manual'
    KWIN_META_DISABLE_FOR_SESSION = None

state = ConfigState()
MIN_BUTTON_HEIGHT = 30
URL_SELECTOR_MAX_WIDTH = 350
PRINT_BUTTON_WIDTH = 70
RESTART_BUTTON_WIDTH = 150
TECHSUPPORT_BUTTON_WIDTH = 130
EXIT_BUTTON_WIDTH = 90
CONTROL_PANEL_SPACING = 3
TIME_LABEL_WIDTH = 180
LAYOUT_BUTTON_WIDTH = 60
EXIT_COMBO_MODIFIERS = Qt.ControlModifier
EXIT_COMBO_KEY = Qt.Key_Q
REBOOT_COMBO_MODIFIERS = Qt.ControlModifier | Qt.ShiftModifier
REBOOT_COMBO_KEY = Qt.Key_R
POWEROFF_COMBO_KEY = Qt.Key_F13
# WARNING: Decompyle incomplete
