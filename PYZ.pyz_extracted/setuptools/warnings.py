# Source Generated with Decompyle++
# File: warnings.pyc (Python 3.12)

'''Provide basic warnings used by setuptools modules.

Using custom classes (other than ``UserWarning``) allow users to set
``PYTHONWARNINGS`` filters to run tests and prepare for upcoming changes in
setuptools.
'''
from __future__ import annotations
import os
import warnings
from datetime import date
from inspect import cleandoc
from textwrap import indent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing_extensions import TypeAlias
_DueDate: 'TypeAlias' = tuple[(int, int, int)]
_INDENT = '        '
_TEMPLATE = f'''{'********************************************************************************'}\n{{details}}\n{'********************************************************************************'}'''

class SetuptoolsWarning(UserWarning):
    '''Base class in ``setuptools`` warning hierarchy.'''
    emit = (lambda cls, summary, details = None, due_date = None, see_docs = classmethod, see_url = (None, None, None, None, None, 2), stacklevel = ('summary', 'str | None', 'details', 'str | None', 'due_date', '_DueDate | None', 'see_docs', 'str | None', 'see_url', 'str | None', 'stacklevel', 'int', 'return', 'None'): if not summary:
summaryif not getattr(cls, '_SUMMARY', None):
getattr(cls, '_SUMMARY', None)summary_ = ''if not details:
detailsif not getattr(cls, '_DETAILS', None):
getattr(cls, '_DETAILS', None)details_ = ''if not due_date:
due_datedue_date = getattr(cls, '_DUE_DATE', None)if not see_docs:
see_docsdocs_ref = getattr(cls, '_SEE_DOCS', None)if docs_ref:
docs_refdocs_url = f'''https://setuptools.pypa.io/en/latest/{docs_ref}'''if not see_url:
see_urlsee_url = getattr(cls, '_SEE_URL', None)# WARNING: Decompyle incomplete
)()
    _format = (lambda cls, summary = None, details = None, due_date = classmethod, see_url = (None, None, None), format_args = ('summary', 'str', 'details', 'str', 'due_date', 'date | None', 'see_url', 'str | None', 'format_args', 'dict | None', 'return', 'str'): today = date.today()if not format_args:
format_argssummary = cleandoc(summary).format_map({ })if not format_args:
format_argspossible_parts = [
cleandoc(details).format_map({ }),
f'''\nBy {due_date:%Y-%b-%d}, you need to update your project and remove deprecated calls\nor your builds will no longer be supported.''' if due_date and due_date > today else None,
'\nThis deprecation is overdue, please update your project and remove deprecated\ncalls to avoid build errors in the future.' if due_date and due_date < today else None,
f'''\nSee {see_url} for details.''' if see_url else None]# WARNING: Decompyle incomplete
)()


class InformationOnly(SetuptoolsWarning):
    '''Currently there is no clear way of displaying messages to the users
    that use the setuptools backend directly via ``pip``.
    The only thing that might work is a warning, although it is not the
    most appropriate tool for the job...

    See pypa/packaging-problems#558.
    '''
    pass


class SetuptoolsDeprecationWarning(SetuptoolsWarning):
    '''
    Base class for warning deprecations in ``setuptools``

    This class is not derived from ``DeprecationWarning``, and as such is
    visible by default.
    '''
    pass


def _should_enforce():
    enforce = os.getenv('SETUPTOOLS_ENFORCE_DEPRECATION', 'false').lower()
    return enforce in ('true', 'on', 'ok', '1')

