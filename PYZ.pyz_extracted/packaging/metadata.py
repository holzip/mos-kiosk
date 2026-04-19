# Source Generated with Decompyle++
# File: metadata.pyc (Python 3.12)

from __future__ import annotations
import email.feedparser as email
import email.header as email
import email.message as email
import email.parser as email
import email.policy as email
import keyword
import pathlib
import sys
import typing
from typing import Any, Callable, Generic, Literal, TypedDict, cast
from  import licenses, requirements, specifiers, utils
from  import version as version_module
if typing.TYPE_CHECKING:
    from licenses import NormalizedLicenseExpression
T = typing.TypeVar('T')

class InvalidMetadata(ValueError):
    pass
# WARNING: Decompyle incomplete


def RawMetadata():
    '''RawMetadata'''
    import_namespaces: 'list[str]' = 'A dictionary of raw core metadata.\n\n    Each field in core metadata maps to a key of this dictionary (when data is\n    provided). The key is lower-case and underscores are used instead of dashes\n    compared to the equivalent core metadata field. Any core metadata field that\n    can be specified multiple times or can hold multiple values in a single\n    field have a key with a plural name. See :class:`Metadata` whose attributes\n    match the keys of this dictionary.\n\n    Core metadata fields that can be specified multiple times are stored as a\n    list or dict depending on which is appropriate for the field. Any fields\n    which hold multiple values in a single field are stored as a list.\n\n    '

RawMetadata = <NODE:27>(RawMetadata, 'RawMetadata', TypedDict, total = False)
_STRING_FIELDS = {
    'name',
    'author',
    'license',
    'summary',
    'version',
    'home_page',
    'maintainer',
    'description',
    'author_email',
    'download_url',
    'requires_python',
    'maintainer_email',
    'metadata_version',
    'license_expression',
    'description_content_type'}
_LIST_FIELDS = {
    'dynamic',
    'provides',
    'requires',
    'obsoletes',
    'platforms',
    'classifiers',
    'import_names',
    'license_files',
    'provides_dist',
    'requires_dist',
    'obsoletes_dist',
    'provides_extra',
    'import_namespaces',
    'requires_external',
    'supported_platforms'}
_DICT_FIELDS = {
    'project_urls'}

def _parse_keywords(data = None):
    '''Split a string of comma-separated keywords into a list of keywords.'''
    pass
# WARNING: Decompyle incomplete


def _parse_project_urls(data = None):
    '''Parse a list of label/URL string pairings separated by a comma.'''
    urls = { }
    for pair in data:
        (label, _, url) = pair.partition(',')()
        if label in urls:
            raise KeyError('duplicate labels in project urls')
        urls[label] = url
    return urls


def _get_payload(msg = None, source = None):
    '''Get the body of the message.'''
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
