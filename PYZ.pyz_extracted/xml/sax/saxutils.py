# Source Generated with Decompyle++
# File: saxutils.pyc (Python 3.12)

'''A library of useful helper classes to the SAX classes, for the
convenience of application and driver writers.
'''
import os
import urllib.parse as urllib
import urllib.request as urllib
import io
import codecs
from  import handler
from  import xmlreader

def __dict_replace(s, d):
    '''Replace substrings of a string using a dictionary.'''
    for key, value in d.items():
        s = s.replace(key, value)
    return s


def escape(data, entities = ({ },)):
    '''Escape &, <, and > in a string of data.

    You can escape other strings of data by passing a dictionary as
    the optional entities parameter.  The keys and values must all be
    strings; each key will be replaced with its corresponding value.
    '''
    data = data.replace('&', '&amp;')
    data = data.replace('>', '&gt;')
    data = data.replace('<', '&lt;')
    if entities:
        data = __dict_replace(data, entities)
    return data


def unescape(data, entities = ({ },)):
    '''Unescape &amp;, &lt;, and &gt; in a string of data.

    You can unescape other strings of data by passing a dictionary as
    the optional entities parameter.  The keys and values must all be
    strings; each key will be replaced with its corresponding value.
    '''
    data = data.replace('&lt;', '<')
    data = data.replace('&gt;', '>')
    if entities:
        data = __dict_replace(data, entities)
    return data.replace('&amp;', '&')


def quoteattr(data, entities = ({ },)):
    '''Escape and quote an attribute value.

    Escape &, <, and > in a string of data, then quote it for use as
    an attribute value.  The " character will be escaped as well, if
    necessary.

    You can escape other strings of data by passing a dictionary as
    the optional entities parameter.  The keys and values must all be
    strings; each key will be replaced with its corresponding value.
    '''
    pass
# WARNING: Decompyle incomplete


def _gettextwriter(out, encoding):
    pass
# WARNING: Decompyle incomplete


class XMLGenerator(handler.ContentHandler):
    
    def __init__(self, out, encoding, short_empty_elements = (None, 'iso-8859-1', False)):
        handler.ContentHandler.__init__(self)
        out = _gettextwriter(out, encoding)
        self._write = out.write
        self._flush = out.flush
        self._ns_contexts = [
            { }]
        self._current_context = self._ns_contexts[-1]
        self._undeclared_ns_maps = []
        self._encoding = encoding
        self._short_empty_elements = short_empty_elements
        self._pending_start_element = False

    
    def _qname(self, name):
