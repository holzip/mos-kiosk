# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.12)

'''
Wheel command-line utility.
'''
from __future__ import annotations
import argparse
import os
import sys
from argparse import ArgumentTypeError

class WheelError(Exception):
    pass


def unpack_f(args):
    unpack = unpack
    import unpack
    unpack(args.wheelfile, args.dest)


def pack_f(args):
    pack = pack
    import pack
    pack(args.directory, args.dest_dir, args.build_number)


def convert_f(args):
    convert = convert
    import convert
    convert(args.files, args.dest_dir, args.verbose)


def tags_f(args):
    pass
# WARNING: Decompyle incomplete


def version_f(args):
    __version__ = __version__
    import 
    print('wheel %s' % __version__)


def parse_build_tag(build_tag = None):
    if not build_tag and build_tag[0].isdigit():
        raise ArgumentTypeError('build tag must begin with a digit')
    if '-' in build_tag:
        raise ArgumentTypeError("invalid character ('-') in build tag")
    return build_tag

TAGS_HELP = 'Make a new wheel with given tags. Any tags unspecified will remain the same.\nStarting the tags with a "+" will append to the existing tags. Starting with a\n"-" will remove a tag (use --option=-TAG syntax). Multiple tags can be\nseparated by ".". The original file will remain unless --remove is given.  The\noutput filename(s) will be displayed on stdout for further processing.\n'

def parser():
    pass
# WARNING: Decompyle incomplete


def main():
    p = parser()
    args = p.parse_args()
    if not hasattr(args, 'func'):
        p.print_help()
        return 1
    
    try:
        args.func(args)
        return 0
    except WheelError:
        e = None
        print(e, file = sys.stderr)
        e = None
        del e
        return 1
        e = None
        del e


