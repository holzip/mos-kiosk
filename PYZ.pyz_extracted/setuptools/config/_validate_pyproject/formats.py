# Source Generated with Decompyle++
# File: formats.pyc (Python 3.12)

'''
The functions in this module are used to validate schemas with the
`format JSON Schema keyword
<https://json-schema.org/understanding-json-schema/reference/string#format>`_.

The correspondence is given by replacing the ``_`` character in the name of the
function with a ``-`` to obtain the format name and vice versa.
'''
import builtins
import logging
import os
import re
import string
import typing
from itertools import chain as _chain
if typing.TYPE_CHECKING:
    from typing_extensions import Literal
_logger = logging.getLogger(__name__)
VERSION_PATTERN = '\n    v?\n    (?:\n        (?:(?P<epoch>[0-9]+)!)?                           # epoch\n        (?P<release>[0-9]+(?:\\.[0-9]+)*)                  # release segment\n        (?P<pre>                                          # pre-release\n            [-_\\.]?\n            (?P<pre_l>alpha|a|beta|b|preview|pre|c|rc)\n            [-_\\.]?\n            (?P<pre_n>[0-9]+)?\n        )?\n        (?P<post>                                         # post release\n            (?:-(?P<post_n1>[0-9]+))\n            |\n            (?:\n                [-_\\.]?\n                (?P<post_l>post|rev|r)\n                [-_\\.]?\n                (?P<post_n2>[0-9]+)?\n            )\n        )?\n        (?P<dev>                                          # dev release\n            [-_\\.]?\n            (?P<dev_l>dev)\n            [-_\\.]?\n            (?P<dev_n>[0-9]+)?\n        )?\n    )\n    (?:\\+(?P<local>[a-z0-9]+(?:[-_\\.][a-z0-9]+)*))?       # local version\n'
VERSION_REGEX = re.compile('^\\s*' + VERSION_PATTERN + '\\s*$', re.X | re.I)

def pep440(version = None):
    """See :ref:`PyPA's version specification <pypa:version-specifiers>`
    (initially introduced in :pep:`440`).
    """
    return VERSION_REGEX.match(version) is not None

PEP508_IDENTIFIER_PATTERN = '([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])'
PEP508_IDENTIFIER_REGEX = re.compile(f'''^{PEP508_IDENTIFIER_PATTERN}$''', re.I)

def pep508_identifier(name = None):
    """See :ref:`PyPA's name specification <pypa:name-format>`
    (initially introduced in :pep:`508#names`).
    """
    return PEP508_IDENTIFIER_REGEX.match(name) is not None


try:
    from packaging import requirements as _req
    
    try:
        
        def pep508(value = None):
            """See :ref:`PyPA's dependency specifiers <pypa:dependency-specifiers>`
        (initially introduced in :pep:`508`).
        """
            
            try:
                _req.Requirement(value)
                return True
            except _req.InvalidRequirement:
                return False


        
        def pep508_versionspec(value = None):
            """Expression that can be used to specify/lock versions (including ranges)
    See ``versionspec`` in :ref:`PyPA's dependency specifiers
    <pypa:dependency-specifiers>` (initially introduced in :pep:`508`).
    """
            pass
        # WARNING: Decompyle incomplete

        
        def pep517_backend_reference(value = None):
            """See PyPA's specification for defining build-backend references
    introduced in :pep:`517#source-trees`.

    This is similar to an entry-point reference (e.g., ``package.module:object``).
    """
            (module, _, obj) = value.partition(':')
            identifiers = _chain(module.split('.'), obj.split('.'))()
            return (lambda .0: pass# WARNING: Decompyle incomplete
)(identifiers())

        
        def _download_classifiers():
            import ssl
            Message = Message
            import email.message
            urlopen = urlopen
            import urllib.request
            url = 'https://pypi.org/pypi?:action=list_classifiers'
            context = ssl.create_default_context()
            response = urlopen(url, context = context)
            headers = Message()
            headers['content_type'] = response.getheader('content-type', 'text/plain')
            None(None, None)
            return 
            with None:
                if not None, response.read().decode(headers.get_param('charset', 'utf-8')):
                    pass

        
        class _TroveClassifier:
            downloaded: typing.Union[(None, 'Literal[False]', typing.Set[str])] = "The ``trove_classifiers`` package is the official way of validating classifiers,\n    however this package might not be always available.\n    As a workaround we can still download a list from PyPI.\n    We also don't want to be over strict about it, so simply skipping silently is an\n    option (classifiers will be validated anyway during the upload to PyPI).\n    "
            
            def __init__(self = None):
                self.downloaded = None
                self._skip_download = False
                self.__name__ = 'trove_classifier'

            
            def _disable_download(self = None):
                self._skip_download = True

            
            def __call__(self = None, value = None):
                if self.downloaded is False or self._skip_download is True:
                    return True
                if os.getenv('NO_NETWORK') or os.getenv('VALIDATE_PYPROJECT_NO_NETWORK'):
                    self.downloaded = False
                    msg = 'Install ``trove-classifiers`` to ensure proper validation. Skipping download of classifiers list from PyPI (NO_NETWORK).'
                    _logger.debug(msg)
                    return True
            # WARNING: Decompyle incomplete


        
        try:
            from trove_classifiers import classifiers as _trove_classifiers
            
            def trove_classifier(value = None):
                '''See https://pypi.org/classifiers/'''
                if not value in _trove_classifiers:
                    value in _trove_classifiers
                return value.lower().startswith('private ::')

            
            def pep561_stub_name(value = None):
                '''Name of a directory containing type stubs.
    It must follow the name scheme ``<package>-stubs`` as defined in
    :pep:`561#stub-only-packages`.
    '''
                pass
            # WARNING: Decompyle incomplete

            
            def url(value = None):
                '''Valid URL (validation uses :obj:`urllib.parse`).
    For maximum compatibility please make sure to include a ``scheme`` prefix
    in your URL (e.g. ``http://``).
    '''
                urlparse = urlparse
                import urllib.parse
                
                try:
                    parts = urlparse(value)
                    if not parts.scheme:
                        _logger.warning(f'''For maximum compatibility please make sure to include a `scheme` prefix in your URL (e.g. \'http://\'). Given value: {value}''')
                        if not value.startswith('/') and value.startswith('\\') and '@' in value:
                            parts = urlparse(f'''http://{value}''')
                    if parts.scheme:
                        parts.scheme
                    return bool(parts.netloc)
                except Exception:
                    return False


            ENTRYPOINT_PATTERN = '[^\\[\\s=]([^=]*[^\\s=])?'
            ENTRYPOINT_REGEX = re.compile(f'''^{ENTRYPOINT_PATTERN}$''', re.I)
            RECOMMEDED_ENTRYPOINT_PATTERN = '[\\w.-]+'
            RECOMMEDED_ENTRYPOINT_REGEX = re.compile(f'''^{RECOMMEDED_ENTRYPOINT_PATTERN}$''', re.I)
            ENTRYPOINT_GROUP_PATTERN = '\\w+(\\.\\w+)*'
            ENTRYPOINT_GROUP_REGEX = re.compile(f'''^{ENTRYPOINT_GROUP_PATTERN}$''', re.I)
            
            def python_identifier(value = None):
                '''Can be used as identifier in Python.
    (Validation uses :obj:`str.isidentifier`).
    '''
                return value.isidentifier()

            
            def python_qualified_identifier(value = None):
                '''
    Python "dotted identifier", i.e. a sequence of :obj:`python_identifier`
    concatenated with ``"."`` (e.g.: ``package.module.submodule``).
    '''
                if value.startswith('.') or value.endswith('.'):
                    return False
                return (lambda .0: pass# WARNING: Decompyle incomplete
)(value.split('.')())

            
            def python_module_name(value = None):
                '''Module name that can be used in an ``import``-statement in Python.
    See :obj:`python_qualified_identifier`.
    '''
                return python_qualified_identifier(value)

            
            def python_module_name_relaxed(value = None):
                '''Similar to :obj:`python_module_name`, but relaxed to also accept
    dash characters (``-``) and cover special cases like ``pip-run``.

    It is recommended, however, that beginners avoid dash characters,
    as they require advanced knowledge about Python internals.

    The following are disallowed:

    * names starting/ending in dashes,
    * names ending in ``-stubs`` (potentially collide with :obj:`pep561_stub_name`).
    '''
                if value.startswith('-') or value.endswith('-'):
                    return False
                if value.endswith('-stubs'):
                    return False
                return python_module_name(value.replace('-', '_'))

            
            def python_entrypoint_group(value = None):
                """See ``Data model > group`` in the :ref:`PyPA's entry-points specification
    <pypa:entry-points>`.
    """
                return ENTRYPOINT_GROUP_REGEX.match(value) is not None

            
            def python_entrypoint_name(value = None):
                """See ``Data model > name`` in the :ref:`PyPA's entry-points specification
    <pypa:entry-points>`.
    """
                if not ENTRYPOINT_REGEX.match(value):
                    return False
                if not RECOMMEDED_ENTRYPOINT_REGEX.match(value):
                    msg = f'''Entry point `{value}` does not follow recommended pattern: '''
                    msg += RECOMMEDED_ENTRYPOINT_PATTERN
                    _logger.warning(msg)
                return True

            
            def python_entrypoint_reference(value = None):
                """Reference to a Python object using in the format::

        importable.module:object.attr

    See ``Data model >object reference`` in the :ref:`PyPA's entry-points specification
    <pypa:entry-points>`.
    """
                (module, _, rest) = value.partition(':')
                module_parts = module.split('.')
                identifiers = _chain(module_parts, obj.split('.')) if rest else module_parts
                return (lambda .0: pass# WARNING: Decompyle incomplete
)(identifiers())

            
            def uint8(value = None):
                '''Unsigned 8-bit integer (:math:`0 \\leq x < 2^8`)'''
                if  <= 0, value:
                     <= 0, value
                    return 0, value < 256
                 <= 0, value
                return 0, value

            
            def uint16(value = None):
                '''Unsigned 16-bit integer (:math:`0 \\leq x < 2^{16}`)'''
                if  <= 0, value:
                     <= 0, value
                    return 0, value < 65536
                 <= 0, value
                return 0, value

            
            def uint(value = None):
                '''Unsigned 64-bit integer (:math:`0 \\leq x < 2^{64}`)'''
                if  <= 0, value:
                     <= 0, value
                    return 0, value < 0x10000000000000000
                 <= 0, value
                return 0, value

            
            def int(value = None):
                '''Signed 64-bit integer (:math:`-2^{63} \\leq x < 2^{63}`)'''
                if  <= -0x8000000000000000, value:
                     <= -0x8000000000000000, value
                    return -0x8000000000000000, value < 0x8000000000000000
                 <= -0x8000000000000000, value
                return -0x8000000000000000, value

            return None
            except ImportError:
                from setuptools._vendor.packaging import requirements as _req
                
                try:
                    continue
                    
                    try:
                        pass
                    except ImportError:
                        _logger.warning('Could not find an installation of `packaging`. Requirements, dependencies and versions might not be validated. To enforce validation, please install `packaging`.')
                        
                        def pep508(value = None):
                            return True

                        continue
                        except ImportError:
                            trove_classifier = _TroveClassifier()
                            continue





