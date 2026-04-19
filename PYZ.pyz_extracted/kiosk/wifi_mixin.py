# Source Generated with Decompyle++
# File: wifi_mixin.pyc (Python 3.12)

'''Mixin для WiFi-логики KioskWindow: проверка статуса, автоподключение, предложение WiFi.

Выделен из window.py для уменьшения размера KioskWindow.
Предполагает наличие атрибутов:
  self.thread_pool      — QThreadPool
  self.last_wifi_status — dict (последний статус WiFi)
  self.wifi_status_label — QLabel (индикатор ●)
  self.web_view          — QWebEngineView
'''
from PySide6.QtCore import QTimer
from config.state import state
from network import AsyncWorker
from network.status_text import network_status_tooltip_base
from utils.logging_setup import logger

class WiFiMixin:
    '''WiFi-методы для KioskWindow (mixin, не наследует QObject).'''
    
    def _force_wifi_status_update(self, event = (None,)):
        worker = AsyncWorker('check_wifi')
        worker.finished.connect(self._on_wifi_check_finished)
        self.thread_pool.start(worker.run)

    
    def _on_wifi_check_finished(self = None, _success = None, _msg = None, data = ('_success', bool, '_msg', str, 'data', dict)):
        self.last_wifi_status = data
        has_wifi = data.get('has_wifi_connection', False)
        if not bool(data.get('has_ethernet_connection')):
            bool(data.get('has_ethernet_connection'))
        has_eth = bool(data.get('ethernet'))
        if not bool(data.get('network_active')):
            bool(data.get('network_active'))
            if not has_eth:
                has_eth
        network_ok = has_wifi
        tip = network_status_tooltip_base(data) if data else 'Нет подключения к сети'
        if network_ok:
            self.wifi_status_label.setStyleSheet('color: #2ecc71; font-size: 20px;')
            self.wifi_status_label.setToolTip(tip)
            return None
        self.wifi_status_label.setStyleSheet('color: #e74c3c; font-size: 20px;')
        self.wifi_status_label.setToolTip(tip)

    
    def _start_wifi_then_page(self):
        worker = AsyncWorker('auto_connect')
        worker.finished.connect(self._on_wifi_auto_finished)
        self.thread_pool.start(worker.run)

    
    def _on_wifi_auto_finished(self = None, success = None, msg = None, data = ('success', bool, 'msg', str, 'data', dict)):
        pass
    # WARNING: Decompyle incomplete

    
    def _startup_network_check(self):
        '''Проверить сетевое подключение при старте. Если нет ни Ethernet ни WiFi — предложить WiFi.'''
        worker = AsyncWorker('check_wifi')
        worker.finished.connect(self._on_startup_network_checked)
        self.thread_pool.start(worker.run)

    
    def _on_startup_network_checked(self = None, _success = None, _msg = None, data = ('_success', bool, '_msg', str, 'data', dict)):
        '''Обработчик стартовой проверки сети. Предлагает WiFi если нет подключения.'''
        get_ethernet_connection_info = get_ethernet_connection_info
        import network.connection
        has_ethernet = bool(get_ethernet_connection_info())
        has_wifi = data.get('has_wifi_connection', False)
        if not has_ethernet:
            if not has_wifi:
                logger.info('Стартовая проверка: нет активного сетевого подключения — предлагаем WiFi')
                QTimer.singleShot(300, self._offer_wifi_setup)
                return None
            return None

    
    def _offer_wifi_setup(self):
        '''Предложить подключиться к WiFi если нет активного подключения.'''
        WiFiManagementDialog = WiFiManagementDialog
        import admin.panel
        kiosk_frameless_confirm = kiosk_frameless_confirm
        import kiosk.kiosk_frameless_dialog
        if kiosk_frameless_confirm(self, title = 'Нет подключения к сети', message = 'Активное сетевое подключение не найдено.\n\nПредпочитаемая WiFi-сеть не задана или недоступна.\nОткрыть управление WiFi для подключения?', yes_text = 'Открыть', no_text = 'Отмена', default_no = False):
            dlg = WiFiManagementDialog(self)
            dlg.exec()
            return None

    
    def _show_wifi_management(self):
        get_ethernet_connection_info = get_ethernet_connection_info
        import network.connection
        if get_ethernet_connection_info():
            kiosk_frameless_alert = kiosk_frameless_alert
            import kiosk.kiosk_frameless_dialog
            kiosk_frameless_alert(self, 'WiFi недоступен', 'Подключена локальная сеть (Ethernet).\n\nУправление WiFi недоступно при активном проводном подключении.', level = 'info')
            return None
        WiFiManagementDialog = WiFiManagementDialog
        import admin.panel
        dlg = WiFiManagementDialog(self)
        dlg.exec()


