# Source Generated with Decompyle++
# File: _core_metadata.pyc (Python 3.12)

__doc__ = '\nHandling of Core Metadata for Python packages (including reading and writing).\n\nSee: https://packaging.python.org/en/latest/specifications/core-metadata/\n'
from __future__ import annotations
import os
import stat
import textwrap
from email import message_from_file
from email.message import Message
from tempfile import NamedTemporaryFile
from packaging.markers import Marker
from packaging.requirements import Requirement
from packaging.utils import canonicalize_name, canonicalize_version
from packaging.version import Version
from  import _normalization, _reqs
from _static import is_static
from warnings import SetuptoolsDeprecationWarning
from distutils.util import rfc822_escape

def get_metadata_version(self):
    mv = getattr(self, 'metadata_version', None)
# WARNING: Decompyle incomplete


def rfc822_unescape(content = None):
    '''Reverse RFC-822 escaping by removing leading whitespaces from content.'''
    lines = content.splitlines()
    if len(lines) == 1:
        return lines[0].lstrip()
    return None.join((lines[0].lstrip(), textwrap.dedent('\n'.join(lines[1:]))))


def _read_field_from_msg(msg = None, field = None):
    '''Read Message header field.'''
    value = msg[field]
    if value == 'UNKNOWN':
        return None
    return value


def _read_field_unescaped_from_msg(msg = None, field = None):
    '''Read Message header field and apply rfc822_unescape.'''
    value = _read_field_from_msg(msg, field)
# WARNING: Decompyle incomplete


def _read_list_from_msg(msg = None, field = None):
    '''Read Message header field and return all results as list.'''
    values = msg.get_all(field, None)
    if values == []:
        return None
    return values


def _read_payload_from_msg(msg = None):
    value = str(msg.get_payload()).strip()
    if not value == 'UNKNOWN' or value:
        return None
    return value


def read_pkg_file(self, file):
    '''Reads the metadata values from a file object.'''
    msg = message_from_file(file)
    self.metadata_version = Version(msg['metadata-version'])
    self.name = _read_field_from_msg(msg, 'name')
    self.version = _read_field_from_msg(msg, 'version')
    self.description = _read_field_from_msg(msg, 'summary')
    self.author = _read_field_from_msg(msg, 'author')
    self.maintainer = None
    self.author_email = _read_field_from_msg(msg, 'author-email')
    self.maintainer_email = None
    self.url = _read_field_from_msg(msg, 'home-page')
    self.download_url = _read_field_from_msg(msg, 'download-url')
    self.license = _read_field_unescaped_from_msg(msg, 'license')
    self.long_description = _read_field_unescaped_from_msg(msg, 'description')
# WARNING: Decompyle incomplete


def single_line(val):
    '''
    Quick and dirty validation for Summary pypa/setuptools#1390.
    '''
    if '\n' in val:
        msg = 'newlines are not allowed in `summary` and will break in the future'
        SetuptoolsDeprecationWarning.emit('Invalid config.', msg)
        val = val.strip().split('\n')[0]
    return val


def write_pkg_info(self, base_dir):
    '''Write the PKG-INFO file into the release tree.'''
    temp = ''
    final = os.path.join(base_dir, 'PKG-INFO')
    
    try:
        f = NamedTemporaryFile('w', encoding = 'utf-8', dir = base_dir, delete = False)
        temp = f.name
        self.write_pkg_file(f)
        
        try:
            None(None, None)
            permissions = stat.S_IMODE(os.lstat(temp).st_mode)
            os.chmod(temp, permissions | stat.S_IRGRP | stat.S_IROTH)
            os.replace(temp, final)
            if temp:
                if os.path.exists(temp):
                    os.remove(temp)
                    return None
                return None
            return None
            with None:
                if not None:
                    pass
            
            try:
                continue
            except:
                if temp:
                    if os.path.exists(temp):
                        os.remove(temp)





def write_pkg_file(self, file):
    '''Write the PKG-INFO format data to a file object.'''
    pass
# WARNING: Decompyle incomplete


def _write_requirements(self, file):
    for req in _reqs.parse(self.install_requires):
        file.write(f'''Requires-Dist: {req}\n''')
    processed_extras = { }
    for augmented_extra, reqs in self.extras_require.items():
        (unsafe_extra, _, condition) = augmented_extra.partition(':')
        unsafe_extra = unsafe_extra.strip()
        extra = _normalization.safe_extra(unsafe_extra)
        if extra:
            _write_provides_extra(file, processed_extras, extra, unsafe_extra)
        for req in _reqs.parse_strings(reqs):
            r = _include_extra(req, extra, condition.strip())
            file.write(f'''Requires-Dist: {r}\n''')
    return processed_extras


def _include_extra(req = None, extra = None, condition = None):
    r = Requirement(req)
    parts = (f'''({r.marker})''' if r.marker else None, f'''({condition})''' if condition else None, f'''extra == {extra!r}''' if extra else None)
    r.marker = ' and '.join((lambda .0: pass# WARNING: Decompyle incomplete
)(parts()))
    return r


def _write_provides_extra(file, processed_extras, safe, unsafe):
    previous = processed_extras.get(safe)
    if previous == unsafe:
        SetuptoolsDeprecationWarning.emit('Ambiguity during "extra" normalization for dependencies.', f'''\n            {previous!r} and {unsafe!r} normalize to the same value:\n\n                {safe!r}\n\n            In future versions, setuptools might halt the build process.\n            ''', see_url = 'https://peps.python.org/pep-0685/')
        return None
    processed_extras[safe] = unsafe
    file.write(f'''Provides-Extra: {safe}\n''')


def get_fullname(self):
    return _distribution_fullname(self.get_name(), self.get_version())


def _distribution_fullname(name = None, version = None):
    """
    >>> _distribution_fullname('setup.tools', '1.0-2')
    'setup_tools-1.0.post2'
    >>> _distribution_fullname('setup-tools', '1.2post2')
    'setup_tools-1.2.post2'
    >>> _distribution_fullname('setup-tools', '1.0-r2')
    'setup_tools-1.0.post2'
    >>> _distribution_fullname('setup.tools', '1.0.post')
    'setup_tools-1.0.post0'
    >>> _distribution_fullname('setup.tools', '1.0+ubuntu-1')
    'setup_tools-1.0+ubuntu.1'
    """
    return '{}-{}'.format(canonicalize_name(name).replace('-', '_'), canonicalize_version(version, strip_trailing_zero = False))

# WARNING: Decompyle incomplete
