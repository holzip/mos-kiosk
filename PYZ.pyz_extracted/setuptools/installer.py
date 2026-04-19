# Source Generated with Decompyle++
# File: installer.pyc (Python 3.12)

from __future__ import annotations
import glob
import os
import subprocess
import sys
import tempfile
from functools import partial
from pkg_resources import Distribution
from  import _reqs
from _reqs import _StrOrIter
from warnings import SetuptoolsDeprecationWarning
from wheel import Wheel
from distutils import log
from distutils.errors import DistutilsError

def _fixup_find_links(find_links):
    '''Ensure find-links option end-up being a list of strings.'''
    if isinstance(find_links, str):
        return find_links.split()
# WARNING: Decompyle incomplete


def fetch_build_egg(dist, req):
    '''Fetch an egg needed for building.

    Use pip/wheel to fetch/build a wheel.'''
    _DeprecatedInstaller.emit()
    _warn_wheel_not_available(dist)
    return _fetch_build_egg_no_warn(dist, req)


def _fetch_build_eggs(dist = None, requires = None):
    import pkg_resources
    _DeprecatedInstaller.emit(stacklevel = 3)
    _warn_wheel_not_available(dist)
    resolved_dists = pkg_resources.working_set.resolve(_reqs.parse(requires, pkg_resources.Requirement), installer = partial(_fetch_build_egg_no_warn, dist), replace_conflicting = True)
    for dist in resolved_dists:
        pkg_resources.working_set.add(dist, replace = True)
    return resolved_dists


def _fetch_build_egg_no_warn(dist, req):
    import pkg_resources
    req = strip_marker(req)
    opts = dist.get_option_dict('easy_install')
    if 'allow_hosts' in opts:
        raise DistutilsError('the `allow-hosts` option is not supported when using pip to install requirements.')
    if 'PIP_QUIET' not in os.environ:
        'PIP_QUIET' not in os.environ
    quiet = 'PIP_VERBOSE' not in os.environ
    if 'PIP_INDEX_URL' in os.environ:
        index_url = None
    elif 'index_url' in opts:
        index_url = opts['index_url'][1]
    else:
        index_url = None
    find_links = _fixup_find_links(opts['find_links'][1])[:] if 'find_links' in opts else []
    if dist.dependency_links:
        find_links.extend(dist.dependency_links)
    eggs_dir = os.path.realpath(dist.get_egg_cache_dir())
    environment = pkg_resources.Environment()
    for egg_dist in pkg_resources.find_distributions(eggs_dir):
        if not egg_dist in req:
            continue
        if not environment.can_add(egg_dist):
            continue
        
        return pkg_resources.find_distributions(eggs_dir), egg_dist
    [
        sys.executable,
        '-m',
        'pip',
        '--disable-pip-version-check',
        'wheel',
        '--no-deps',
        '-w',
        tmpdir] = tempfile.TemporaryDirectory()
    if quiet:
        cmd.append('--quiet')
# WARNING: Decompyle incomplete


def strip_marker(req):
    '''
    Return a new requirement without the environment marker to avoid
    calling pip with something like `babel; extra == "i18n"`, which
    would always be ignored.
    '''
    import pkg_resources
    req = pkg_resources.Requirement.parse(str(req))
    req.marker = None
    return req


def _warn_wheel_not_available(dist):
    import pkg_resources
    
    try:
        pkg_resources.get_distribution('wheel')
        return None
    except pkg_resources.DistributionNotFound:
        dist.announce('WARNING: The wheel package is not available.', log.WARN)
        return None



class _DeprecatedInstaller(SetuptoolsDeprecationWarning):
    _SUMMARY = 'setuptools.installer and fetch_build_eggs are deprecated.'
    _DETAILS = '\n    Requirements should be satisfied by a PEP 517 installer.\n    If you are using pip, you can try `pip install --use-pep517`.\n    '

