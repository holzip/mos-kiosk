# Source Generated with Decompyle++
# File: _reqs.pyc (Python 3.12)

from __future__ import annotations
from collections.abc import Iterable, Iterator
from functools import lru_cache
from typing import TYPE_CHECKING, Callable, TypeVar, Union, overload
from jaraco.text import text
from packaging.requirements import Requirement
if TYPE_CHECKING:
    from typing_extensions import TypeAlias
_T = TypeVar('_T')
_StrOrIter: 'TypeAlias' = Union[(str, Iterable[str])]
parse_req: 'Callable[[str], Requirement]' = lru_cache()(Requirement)

def parse_strings(strs = None):
    '''
    Yield requirement strings for each specification in `strs`.

    `strs` must be a string, or a (possibly-nested) iterable thereof.
    '''
    return text.join_continuation(map(text.drop_comment, text.yield_lines(strs)))

parse = (lambda strs = None: pass)()
parse = (lambda strs = None, parser = None: pass)()

def parse(strs = None, parser = None):
    '''
    Replacement for ``pkg_resources.parse_requirements`` that uses ``packaging``.
    '''
    return map(parser, parse_strings(strs))

