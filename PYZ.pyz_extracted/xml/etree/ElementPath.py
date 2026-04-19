# Source Generated with Decompyle++
# File: ElementPath.pyc (Python 3.12)

import re
xpath_tokenizer_re = re.compile('(\'[^\']*\'|\\"[^\\"]*\\"|::|//?|\\.\\.|\\(\\)|!=|[/.*:\\[\\]\\(\\)@=])|((?:\\{[^}]+\\})?[^/\\[\\]\\(\\)@!=\\s]+)|\\s+')

def xpath_tokenizer(pattern, namespaces = (None,)):
    pass
# WARNING: Decompyle incomplete


def get_parent_map(context):
    parent_map = context.parent_map
# WARNING: Decompyle incomplete


def _is_wildcard_tag(tag):
    if not tag[:3] == '{*}':
        tag[:3] == '{*}'
    return tag[-2:] == '}*'


def _prepare_tag(tag):
    pass
# WARNING: Decompyle incomplete


def prepare_child(next, token):
    pass
# WARNING: Decompyle incomplete


def prepare_star(next, token):
    
    def select(context, result):
        pass
    # WARNING: Decompyle incomplete

    return select


def prepare_self(next, token):
    
    def select(context, result):
        pass
    # WARNING: Decompyle incomplete

    return select


def prepare_descendant(next, token):
    pass
# WARNING: Decompyle incomplete


def prepare_parent(next, token):
    
    def select(context, result):
        pass
    # WARNING: Decompyle incomplete

    return select


def prepare_predicate(next, token):
    pass
# WARNING: Decompyle incomplete

ops = {
    '': prepare_child,
    '*': prepare_star,
    '.': prepare_self,
    '..': prepare_parent,
    '//': prepare_descendant,
    '[': prepare_predicate }
_cache = { }

class _SelectorContext:
    parent_map = None
    
    def __init__(self, root):
        self.root = root



def iterfind(elem, path, namespaces = (None,)):
    if path[-1:] == '/':
        path = path + '*'
    cache_key = (path,)
    if namespaces:
        cache_key += tuple(sorted(namespaces.items()))
    
    try:
        selector = _cache[cache_key]
        result = [
            elem]
        context = _SelectorContext(elem)
        for select in selector:
            result = select(context, result)
        return result
    except KeyError:
        if len(_cache) > 100:
            _cache.clear()
        if path[:1] == '/':
            raise SyntaxError('cannot use absolute path on element')
        next = iter(xpath_tokenizer(path, namespaces)).__next__
        token = next()
    except StopIteration:
        return None

    selector = []
    selector.append(ops[token[0]](next, token))


def find(elem, path, namespaces = (None,)):
    return next(iterfind(elem, path, namespaces), None)


def findall(elem, path, namespaces = (None,)):
    return list(iterfind(elem, path, namespaces))


def findtext(elem, path, default, namespaces = (None, None)):
    pass
# WARNING: Decompyle incomplete

