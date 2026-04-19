# Source Generated with Decompyle++
# File: pack.pyc (Python 3.12)

from __future__ import annotations
import email.policy as email
import os.path as os
import re
from email.generator import BytesGenerator
from email.parser import BytesParser
from wheel.cli import WheelError
from wheel.wheelfile import WheelFile
DIST_INFO_RE = re.compile('^(?P<namever>(?P<name>.+?)-(?P<ver>\\d.*?))\\.dist-info$')

def pack(directory = None, dest_dir = None, build_number = None):
    '''Repack a previously unpacked wheel directory into a new wheel file.

    The .dist-info/WHEEL file must contain one or more tags so that the target
    wheel file name can be determined.

    :param directory: The unpacked wheel directory
    :param dest_dir: Destination directory (defaults to the current directory)
    '''
    pass
# WARNING: Decompyle incomplete


def compute_tagline(tags = None):
    '''Compute a tagline from a list of tags.

    :param tags: A list of tags
    :return: A tagline
    '''
    pass
# WARNING: Decompyle incomplete

