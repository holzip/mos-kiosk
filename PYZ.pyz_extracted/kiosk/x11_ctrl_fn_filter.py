# Source Generated with Decompyle++
# File: x11_ctrl_fn_filter.pyc (Python 3.12)

'''Linux/X11: F11/F12 и Ctrl+F1…F12 до Chromium (QWebEngine часто мимо Qt eventFilter).'''
from __future__ import annotations
import struct
import sys
from typing import Any
_F1_F10 = frozenset(range(67, 77))
_F11_F12 = frozenset((95, 96))
XCB_KEY_PRESS = 2
XCB_MOD_MASK_CONTROL = 4

def _try_install(app = None):
    if sys.platform != 'linux':
        return False
    
    try:
        QAbstractNativeEventFilter = QAbstractNativeEventFilter
        import PySide6.QtCore
        
        class _Filter(QAbstractNativeEventFilter):
            
            def nativeEventFilter(self = None, event_type = None, message = None):
                
                try:
                    et = event_type
                    if isinstance(et, bytes):
                        et_s = et.decode('latin-1', errors = 'replace')
                    else:
                        et_s = str(et)
                    if 'xcb' not in et_s.lower():
                        return (False, 0)
                        
                        try:
                            data = bytes(message)
                            if len(data) < 32:
                                return (False, 0)
                                
                                try:
                                    if data[0] & 127 != XCB_KEY_PRESS:
                                        return (False, 0)
                                        
                                        try:
                                            keycode = data[1]
                                            state = struct.unpack_from('<H', data, 28)[0]
                                            has_ctrl = state & XCB_MOD_MASK_CONTROL != 0
                                            if keycode in _F11_F12:
                                                return (True, 0)
                                                
                                                try:
                                                    if keycode in _F1_F10 and has_ctrl:
                                                        return (True, 0)
                                                    return (False, 0)
                                                except Exception:
                                                    return (False, 0)







        f = _Filter()
        app.installNativeEventFilter(f)
        app._kiosk_x11_ctrl_fn_filter = f
        return True
    except ImportError:
        return False



def install_x11_ctrl_fn_block_filter(app = None):
    '''Вызывать сразу после QApplication(). Безопасно на Wayland (тип события не xcb).'''
    
    try:
        if _try_install(app):
            logger = logger
            import utils.logging_setup
            logger.info('X11: фильтр F11/F12 и Ctrl+F1…F12 для WebEngine')
            return None
        return None
    except Exception:
        return None


