# Source Generated with Decompyle++
# File: _requirestxt.pyc (Python 3.12)

'''Helper code used to generate ``requires.txt`` files in the egg-info directory.

The ``requires.txt`` file has an specific format:
    - Environment markers need to be part of the section headers and
      should not be part of the requirement spec itself.

See https://setuptools.pypa.io/en/latest/deprecated/python_eggs.html#requires-txt
'''
from __future__ import annotations
import io
from collections import defaultdict
from collections.abc import Mapping
from itertools import filterfalse
from typing import TypeVar
from jaraco.text import yield_lines
from packaging.requirements import Requirement
from  import _reqs
from _reqs import _StrOrIter
_T = TypeVar('_T')
_Ordered = dict[(_T, None)]

def _prepare(install_requires = None, extras_require = None):
    '''Given values for ``install_requires`` and ``extras_require``
    create modified versions in a way that can be written in ``requires.txt``
    '''
    extras = _convert_extras_requirements(extras_require)
    return _move_install_requirements_markers(install_requires, extras)


def _convert_extras_requirements(extras_require = None):
    '''
    Convert requirements in `extras_require` of the form
    `"extra": ["barbazquux; {marker}"]` to
    `"extra:{marker}": ["barbazquux"]`.
    '''
    output = defaultdict[(str, _Ordered[Requirement])](dict)
    for section, v in extras_require.items():
        output[section]
        for r in _reqs.parse(v):
            output[section + _suffix_for(r)].setdefault(r)
    return output


def _move_install_requirements_markers(install_requires = None, extras_require = None):
    '''
    The ``requires.txt`` file has an specific format:
        - Environment markers need to be part of the section headers and
          should not be part of the requirement spec itself.

    Move requirements in ``install_requires`` that are using environment
    markers ``extras_require``.
    '''
    inst_reqs = list(_reqs.parse(install_requires))
    simple_reqs = filter(_no_marker, inst_reqs)
    complex_reqs = filterfalse(_no_marker, inst_reqs)
    simple_install_requires = list(map(str, simple_reqs))
    for r in complex_reqs:
        extras_require[':' + str(r.marker)].setdefault(r)
    expanded_extras = (lambda .0: pass# WARNING: Decompyle incomplete
)(extras_require.items()())
    return (simple_install_requires, expanded_extras)


def _suffix_for(req):
    """Return the 'extras_require' suffix for a given requirement."""
    if req.marker:
        return ':' + str(req.marker)


def _clean_req(req):
    '''Given a Requirement, remove environment markers and return it'''
    r = Requirement(str(req))
    r.marker = None
    return r


def _no_marker(req):
    return not (req.marker)


def _write_requirements(stream, reqs):
    if not reqs:
        reqs
    lines = yield_lines(())
    
    def append_cr(line):
        return line + '\n'

    lines = map(append_cr, lines)
    stream.writelines(lines)


def write_requirements(cmd, basename, filename):
    dist = cmd.distribution
    data = io.StringIO()
    if not dist.install_requires:
        dist.install_requires
    if not dist.extras_require:
        dist.extras_require
    (install_requires, extras_require) = _prepare((), { })
    _write_requirements(data, install_requires)
# WARNING: Decompyle incomplete


def write_setup_requirements(cmd, basename, filename):
    data = io.StringIO()
    _write_requirements(data, cmd.distribution.setup_requires)
    cmd.write_or_delete_file('setup-requirements', filename, data.getvalue())

