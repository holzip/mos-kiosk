# Source Generated with Decompyle++
# File: unpack.pyc (Python 3.12)

from __future__ import annotations
from pathlib import Path
from wheelfile import WheelFile

def unpack(path = None, dest = None):
    '''Unpack a wheel.

    Wheel content will be unpacked to {dest}/{name}-{ver}, where {name}
    is the package name and {ver} its version.

    :param path: The path to the wheel.
    :param dest: Destination directory (default to current directory).
    '''
    wf = WheelFile(path)
    namever = wf.parsed_filename.group('namever')
    destination = Path(dest) / namever
    print(f'''Unpacking to: {destination}...''', end = '', flush = True)
    for zinfo in wf.filelist:
        wf.extract(zinfo, destination)
        permissions = zinfo.external_attr >> 16 & 511
        destination.joinpath(zinfo.filename).chmod(permissions)
    None(None, None)
    print('OK')
    return None
    with None:
        if not None:
            pass
    continue

