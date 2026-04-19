# Source Generated with Decompyle++
# File: load_finished_spurious.pyc (Python 3.12)

'''
Эвристика для Qt WebEngine: ложный loadFinished(False) при рабочей главной странице.

Не импортирует config/Qt — можно тестировать без PySide6.
'''

def document_urls_match_for_same_navigation(a = None, b = None):
    '''Совпадают ли URL как «один и тот же документ» для проверки загрузки (без # и ?).

    Логика согласована с нормализацией в ``KioskWindow.go_home`` (путь без хвостового ``/``).
    '''
    
    def norm(u = None):
        if not u:
            u
        return ''.split('?')[0].split('#')[0].strip().rstrip('/')

    nb = norm(b)
    na = norm(a)
    if not na.startswith(('http://', 'https://')):
        return False
    if not nb.startswith(('http://', 'https://')):
        return False
    return na == nb


def should_ignore_load_finished_false_as_spurious(success, is_chrome_error, requested_url = None, current_url = None, page_loaded = None, page_load_got_100 = ('success', bool, 'is_chrome_error', bool, 'requested_url', str, 'current_url', str, 'page_loaded', bool, 'page_load_got_100', bool, 'return', bool)):
    '''Нужно ли не считать ``loadFinished(False)`` фатальной ошибкой главного документа.

    Chromium/Qt иногда шлют ``success=False`` при сбое **вложенного** фрейма или вторичной
    подгрузке, при этом URL вкладки остаётся целевым (не ``chrome-error://``). Тогда
    показ «сайт не открылся» и retry ложны.

    Условия: URL вкладки совпадает с последним запрошенным http(s) **и** уже был успех **или**
    до этого дошли до ``loadProgress(100)`` в этом цикле загрузки.
    '''
    if success or is_chrome_error:
        return False
    if not document_urls_match_for_same_navigation(requested_url, current_url):
        return False
    if not page_loaded:
        page_loaded
    return page_load_got_100

