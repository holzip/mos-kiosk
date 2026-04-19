# Source Generated with Decompyle++
# File: tags.pyc (Python 3.12)

from __future__ import annotations
import email.policy as email
import itertools
import os
from collections.abc import Iterable
from email.parser import BytesParser
from wheelfile import WheelFile

def _compute_tags(original_tags = None, new_tags = None):
    '''Add or replace tags. Supports dot-separated tags'''
    pass
# WARNING: Decompyle incomplete


def tags(wheel, python_tags = None, abi_tags = None, platform_tags = None, build_tag = (None, None, None, None, False), remove = ('wheel', 'str', 'python_tags', 'str | None', 'abi_tags', 'str | None', 'platform_tags', 'str | None', 'build_tag', 'str | None', 'remove', 'bool', 'return', 'str')):
    '''Change the tags on a wheel file.

    The tags are left unchanged if they are not specified. To specify "none",
    use ["none"]. To append to the previous tags, a tag should start with a
    "+".  If a tag starts with "-", it will be removed from existing tags.
    Processing is done left to right.

    :param wheel: The paths to the wheels
    :param python_tags: The Python tags to set
    :param abi_tags: The ABI tags to set
    :param platform_tags: The platform tags to set
    :param build_tag: The build tag to set
    :param remove: Remove the original wheel
    '''
    f = WheelFile(wheel, 'r')
# WARNING: Decompyle incomplete

