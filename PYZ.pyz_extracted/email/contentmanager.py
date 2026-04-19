# Source Generated with Decompyle++
# File: contentmanager.pyc (Python 3.12)

import binascii
import email.charset as email
import email.message as email
import email.errors as email
from email import quoprimime

class ContentManager:
    
    def __init__(self):
        self.get_handlers = { }
        self.set_handlers = { }

    
    def add_get_handler(self, key, handler):
        self.get_handlers[key] = handler

    
    def get_content(self, msg, *args, **kw):
        content_type = msg.get_content_type()
    # WARNING: Decompyle incomplete

    
    def add_set_handler(self, typekey, handler):
        self.set_handlers[typekey] = handler

    
    def set_content(self, msg, obj, *args, **kw):
        if msg.get_content_maintype() == 'multipart':
            raise TypeError('set_content not valid on multipart')
        handler = self._find_set_handler(msg, obj)
        msg.clear_content()
    # WARNING: Decompyle incomplete

    
    def _find_set_handler(self, msg, obj):
        full_path_for_error = None
    # WARNING: Decompyle incomplete


raw_data_manager = ContentManager()

def get_text_content(msg, errors = ('replace',)):
    content = msg.get_payload(decode = True)
    charset = msg.get_param('charset', 'ASCII')
    return content.decode(charset, errors = errors)

raw_data_manager.add_get_handler('text', get_text_content)

def get_non_text_content(msg):
    return msg.get_payload(decode = True)

for maintype in 'audio image video application'.split():
    raw_data_manager.add_get_handler(maintype, get_non_text_content)
del maintype

def get_message_content(msg):
    return msg.get_payload(0)

for subtype in 'rfc822 external-body'.split():
    raw_data_manager.add_get_handler('message/' + subtype, get_message_content)
del subtype

def get_and_fixup_unknown_message_content(msg):
    return bytes(msg.get_payload(0))

raw_data_manager.add_get_handler('message', get_and_fixup_unknown_message_content)

def _prepare_set(msg, maintype, subtype, headers):
    msg['Content-Type'] = '/'.join((maintype, subtype))
# WARNING: Decompyle incomplete


def _finalize_set(msg, disposition, filename, cid, params):
    pass
# WARNING: Decompyle incomplete


def _encode_base64(data, max_line_length):
    encoded_lines = []
    unencoded_bytes_per_line = (max_line_length // 4) * 3
    for i in range(0, len(data), unencoded_bytes_per_line):
        thisline = data[i:i + unencoded_bytes_per_line]
        encoded_lines.append(binascii.b2a_base64(thisline).decode('ascii'))
    return ''.join(encoded_lines)


def _encode_text(string, charset, cte, policy):
    pass
# WARNING: Decompyle incomplete


def set_text_content(msg, string, subtype, charset, cte, disposition, filename, cid, params, headers = ('plain', 'utf-8', None, None, None, None, None, None)):
    _prepare_set(msg, 'text', subtype, headers)
    (cte, payload) = _encode_text(string, charset, cte, msg.policy)
    msg.set_payload(payload)
    msg.set_param('charset', email.charset.ALIASES.get(charset, charset), replace = True)
    msg['Content-Transfer-Encoding'] = cte
    _finalize_set(msg, disposition, filename, cid, params)

raw_data_manager.add_set_handler(str, set_text_content)

def set_message_content(msg, message, subtype, cte, disposition, filename, cid, params, headers = ('rfc822', None, None, None, None, None, None)):
    if subtype == 'partial':
        raise ValueError('message/partial is not supported for Message objects')
# WARNING: Decompyle incomplete

raw_data_manager.add_set_handler(email.message.Message, set_message_content)

def set_bytes_content(msg, data, maintype, subtype, cte, disposition, filename, cid, params, headers = ('base64', None, None, None, None, None)):
    _prepare_set(msg, maintype, subtype, headers)
    if cte == 'base64':
        data = _encode_base64(data, max_line_length = msg.policy.max_line_length)
    elif cte == 'quoted-printable':
        data = binascii.b2a_qp(data, istext = False, header = False, quotetabs = True)
        data = data.decode('ascii')
    elif cte == '7bit':
        data = data.decode('ascii')
    elif cte in ('8bit', 'binary'):
        data = data.decode('ascii', 'surrogateescape')
    msg.set_payload(data)
    msg['Content-Transfer-Encoding'] = cte
    _finalize_set(msg, disposition, filename, cid, params)

for typ in (bytes, bytearray, memoryview):
    raw_data_manager.add_set_handler(typ, set_bytes_content)
del typ
