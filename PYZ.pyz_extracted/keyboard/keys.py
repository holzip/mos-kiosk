# Source Generated with Decompyle++
# File: keys.pyc (Python 3.12)

__doc__ = 'Отключение/восстановление сервисных клавиш через xmodmap (Alt, Win, Ctrl, Fn, F1–F12 кроме F5).\n\nF5 оставляем в X: в киоске — обновление страницы (как кнопка «↻»).\n\nПереключение раскладки (us/ru): setxkbmap + повторная блокировка xmodmap выполняются\nв **фоновом потоке**, чтобы не блокировать GUI. Подписи EN/RU на кнопках обновляются\nсразу по выбранной раскладке (без лишнего setxkbmap -query на каждый клик).\n'
import subprocess
import threading
from utils.logging_setup import logger
# WARNING: Decompyle incomplete
