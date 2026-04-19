# Source Generated with Decompyle++
# File: nturl2path.pyc (Python 3.12)

'''Convert a NT pathname to a file URL and vice versa.

This module only exists to provide OS-specific code
for urllib.requests, thus do not use directly.
'''

def url2pathname(url):
    """OS-specific conversion from a relative URL of the 'file' scheme
    to a file system path; not recommended for general use."""
    import string
    import urllib.parse as urllib
    if url[:3] == '///':
        url = url[2:]
    elif url[:12] == '//localhost/':
        url = url[11:]
    if url[:3] == '///':
        url = url[1:]
    url = url.replace(':', '|')
    if '|' not in url:
        return urllib.parse.unquote(url.replace('/', '\\'))
    comp = None.split('|')
    if len(comp) != 2 or comp[0][-1] not in string.ascii_letters:
        error = 'Bad URL: ' + url
        raise OSError(error)
    drive = comp[0][-1].upper()
    tail = urllib.parse.unquote(comp[1].replace('/', '\\'))
    return drive + ':' + tail


def pathname2url(p):
    """OS-specific conversion from a file system path to a relative URL
    of the 'file' scheme; not recommended for general use."""
    import urllib.parse as urllib
    p = p.replace('\\', '/')
    if p[:4] == '//?/':
        p = p[4:]
        if p[:4].upper() == 'UNC/':
            p = '//' + p[4:]
        elif p[1:2] != ':':
            raise OSError('Bad path: ' + p)
    if ':' not in p:
        return urllib.parse.quote(p)
    comp = None.split(':', maxsplit = 2)
    if len(comp) != 2 or len(comp[0]) > 1:
        error = 'Bad path: ' + p
        raise OSError(error)
    drive = urllib.parse.quote(comp[0].upper())
    tail = urllib.parse.quote(comp[1])
    return '///' + drive + ':' + tail

