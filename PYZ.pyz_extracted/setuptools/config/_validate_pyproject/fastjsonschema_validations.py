# Source Generated with Decompyle++
# File: fastjsonschema_validations.pyc (Python 3.12)

VERSION = '2.20.0'
from decimal import Decimal
import re
from fastjsonschema_exceptions import JsonSchemaValueException
REGEX_PATTERNS = {
    '^.*$': re.compile('^.*$'),
    '.+': re.compile('.+'),
    '^.+$': re.compile('^.+$'),
    'idn-email_re_pattern': re.compile('^[^@]+@[^@]+\\.[^@]+\\Z') }
NoneType = type(None)

def validate(data, custom_formats, name_prefix = ({ }, None)):
    if not name_prefix:
        name_prefix
    validate_https___packaging_python_org_en_latest_specifications_declaring_build_dependencies(data, custom_formats, 'data' + '')
    return data


def validate_https___packaging_python_org_en_latest_specifications_declaring_build_dependencies(data, custom_formats, name_prefix = ({ }, None)):
    pass
# WARNING: Decompyle incomplete


def validate_https___setuptools_pypa_io_en_latest_userguide_pyproject_config_html(data, custom_formats, name_prefix = ({ }, None)):
    pass
# WARNING: Decompyle incomplete


def validate_https___setuptools_pypa_io_en_latest_userguide_pyproject_config_html__definitions_file_directive_properties_file(data, custom_formats, name_prefix = ({ }, None)):
    data_one_of_count7 = 0
# WARNING: Decompyle incomplete


def validate_https___setuptools_pypa_io_en_latest_userguide_pyproject_config_html__definitions_file_directive_for_dependencies(data, custom_formats, name_prefix = ({ }, None)):
    if not name_prefix:
        name_prefix
    validate_https___setuptools_pypa_io_en_latest_userguide_pyproject_config_html__definitions_file_directive(data, custom_formats, 'data' + '')
    return data


def validate_https___setuptools_pypa_io_en_latest_userguide_pyproject_config_html__definitions_file_directive(data, custom_formats, name_prefix = ({ }, None)):
    if not isinstance(data, dict):
        if not name_prefix:
            name_prefix
        if not name_prefix:
            name_prefix
        raise JsonSchemaValueException('' + 'data' + ' must be object', value = data, name = '' + 'data' + '', definition = {
            '$id': '#/definitions/file-directive',
            'title': "'file:' directive",
            'description': 'Value is read from a file (or list of files and then concatenated)',
            'type': 'object',
            'additionalProperties': False,
            'properties': {
                'file': {
                    'oneOf': [
                        {
                            'type': 'string' },
                        {
                            'type': 'array',
                            'items': {
                                'type': 'string' } }] } },
            'required': [
                'file'] }, rule = 'type')
    data_is_dict = isinstance(data, dict)
# WARNING: Decompyle incomplete


def validate_https___setuptools_pypa_io_en_latest_userguide_pyproject_config_html__definitions_attr_directive(data, custom_formats, name_prefix = ({ }, None)):
    if not isinstance(data, dict):
        if not name_prefix:
            name_prefix
        if not name_prefix:
            name_prefix
        raise JsonSchemaValueException('' + 'data' + ' must be object', value = data, name = '' + 'data' + '', definition = {
            'title': "'attr:' directive",
            '$id': '#/definitions/attr-directive',
            '$$description': [
                'Value is read from a module attribute. Supports callables and iterables;',
                'unsupported types are cast via ``str()``'],
            'type': 'object',
            'additionalProperties': False,
            'properties': {
                'attr': {
                    'type': 'string',
                    'format': 'python-qualified-identifier' } },
            'required': [
                'attr'] }, rule = 'type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data__missing_keys = set([
            'attr']) - data.keys()
        if data__missing_keys:
            if not name_prefix:
                name_prefix
            if not name_prefix:
                name_prefix
            raise JsonSchemaValueException('' + 'data' + ' must contain ' + str(sorted(data__missing_keys)) + ' properties', value = data, name = '' + 'data' + '', definition = {
                'title': "'attr:' directive",
                '$id': '#/definitions/attr-directive',
                '$$description': [
                    'Value is read from a module attribute. Supports callables and iterables;',
                    'unsupported types are cast via ``str()``'],
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'attr': {
                        'type': 'string',
                        'format': 'python-qualified-identifier' } },
                'required': [
                    'attr'] }, rule = 'required')
        data_keys = set(data.keys())
        if 'attr' in data_keys:
            data_keys.remove('attr')
            data__attr = data['attr']
            if not isinstance(data__attr, str):
                if not name_prefix:
                    name_prefix
                if not name_prefix:
                    name_prefix
                raise JsonSchemaValueException('' + 'data' + '.attr must be string', value = data__attr, name = '' + 'data' + '.attr', definition = {
                    'type': 'string',
                    'format': 'python-qualified-identifier' }, rule = 'type')
            if not isinstance(data__attr, str) and custom_formats['python-qualified-identifier'](data__attr):
                if not name_prefix:
                    name_prefix
                if not name_prefix:
                    name_prefix
                raise JsonSchemaValueException('' + 'data' + '.attr must be python-qualified-identifier', value = data__attr, name = '' + 'data' + '.attr', definition = {
                    'type': 'string',
                    'format': 'python-qualified-identifier' }, rule = 'format')
        if data_keys:
            if not name_prefix:
                name_prefix
            if not name_prefix:
                name_prefix
            raise JsonSchemaValueException('' + 'data' + ' must not contain ' + str(data_keys) + ' properties', value = data, name = '' + 'data' + '', definition = {
                'title': "'attr:' directive",
                '$id': '#/definitions/attr-directive',
                '$$description': [
                    'Value is read from a module attribute. Supports callables and iterables;',
                    'unsupported types are cast via ``str()``'],
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'attr': {
                        'type': 'string',
                        'format': 'python-qualified-identifier' } },
                'required': [
                    'attr'] }, rule = 'additionalProperties')
    return data


def validate_https___setuptools_pypa_io_en_latest_userguide_pyproject_config_html__definitions_ext_module(data, custom_formats, name_prefix = ({ }, None)):
    pass
# WARNING: Decompyle incomplete


def validate_https___setuptools_pypa_io_en_latest_userguide_pyproject_config_html__definitions_find_directive(data, custom_formats, name_prefix = ({ }, None)):
    if not isinstance(data, dict):
        if not name_prefix:
            name_prefix
        if not name_prefix:
            name_prefix
        raise JsonSchemaValueException('' + 'data' + ' must be object', value = data, name = '' + 'data' + '', definition = {
            '$id': '#/definitions/find-directive',
            'title': "'find:' directive",
            'type': 'object',
            'additionalProperties': False,
            'properties': {
                'find': {
                    'type': 'object',
                    '$$description': [
                        'Dynamic `package discovery',
                        '<https://setuptools.pypa.io/en/latest/userguide/package_discovery.html>`_.'],
                    'additionalProperties': False,
                    'properties': {
                        'where': {
                            'description': 'Directories to be searched for packages (Unix-style relative path)',
                            'type': 'array',
                            'items': {
                                'type': 'string' } },
                        'exclude': {
                            'type': 'array',
                            '$$description': [
                                'Exclude packages that match the values listed in this field.',
                                "Can container shell-style wildcards (e.g. ``'pkg.*'``)"],
                            'items': {
                                'type': 'string' } },
                        'include': {
                            'type': 'array',
                            '$$description': [
                                'Restrict the found packages to just the ones listed in this field.',
                                "Can container shell-style wildcards (e.g. ``'pkg.*'``)"],
                            'items': {
                                'type': 'string' } },
                        'namespaces': {
                            'type': 'boolean',
                            '$$description': [
                                'When ``True``, directories without a ``__init__.py`` file will also',
                                'be scanned for :pep:`420`-style implicit namespaces'] } } } } }, rule = 'type')
    data_is_dict = isinstance(data, dict)
# WARNING: Decompyle incomplete


def validate_https___setuptools_pypa_io_en_latest_userguide_pyproject_config_html__definitions_package_name(data, custom_formats, name_prefix = ({ }, None)):
    if not isinstance(data, str):
        if not name_prefix:
            name_prefix
        if not name_prefix:
            name_prefix
        raise JsonSchemaValueException('' + 'data' + ' must be string', value = data, name = '' + 'data' + '', definition = {
            '$id': '#/definitions/package-name',
            'title': 'Valid package name',
            'description': 'Valid package name (importable or :pep:`561`).',
            'type': 'string',
            'anyOf': [
                {
                    'type': 'string',
                    'format': 'python-module-name-relaxed' },
                {
                    'type': 'string',
                    'format': 'pep561-stub-name' }] }, rule = 'type')
    data_any_of_count10 = 0
    if not data_any_of_count10:
        
        try:
            if not isinstance(data, str):
                if not name_prefix:
                    name_prefix
                if not name_prefix:
                    name_prefix
                raise JsonSchemaValueException('' + 'data' + ' must be string', value = data, name = '' + 'data' + '', definition = {
                    'type': 'string',
                    'format': 'python-module-name-relaxed' }, rule = 'type')
            if not isinstance(data, str) and custom_formats['python-module-name-relaxed'](data):
                if not name_prefix:
                    name_prefix
                if not name_prefix:
                    name_prefix
                raise JsonSchemaValueException('' + 'data' + ' must be python-module-name-relaxed', value = data, name = '' + 'data' + '', definition = {
                    'type': 'string',
                    'format': 'python-module-name-relaxed' }, rule = 'format')
            data_any_of_count10 += 1
            if not data_any_of_count10:
                
                try:
                    if not isinstance(data, str):
                        if not name_prefix:
                            name_prefix
                        if not name_prefix:
                            name_prefix
                        raise JsonSchemaValueException('' + 'data' + ' must be string', value = data, name = '' + 'data' + '', definition = {
                            'type': 'string',
                            'format': 'pep561-stub-name' }, rule = 'type')
                    if not isinstance(data, str) and custom_formats['pep561-stub-name'](data):
                        if not name_prefix:
                            name_prefix
                        if not name_prefix:
                            name_prefix
                        raise JsonSchemaValueException('' + 'data' + ' must be pep561-stub-name', value = data, name = '' + 'data' + '', definition = {
                            'type': 'string',
                            'format': 'pep561-stub-name' }, rule = 'format')
                    data_any_of_count10 += 1
                    if not data_any_of_count10:
                        if not name_prefix:
                            name_prefix
                        if not name_prefix:
                            name_prefix
                        raise JsonSchemaValueException('' + 'data' + ' cannot be validated by any definition', value = data, name = '' + 'data' + '', definition = {
                            '$id': '#/definitions/package-name',
                            'title': 'Valid package name',
                            'description': 'Valid package name (importable or :pep:`561`).',
                            'type': 'string',
                            'anyOf': [
                                {
                                    'type': 'string',
                                    'format': 'python-module-name-relaxed' },
                                {
                                    'type': 'string',
                                    'format': 'pep561-stub-name' }] }, rule = 'anyOf')
                    return data
                    except JsonSchemaValueException:
                        continue
                except JsonSchemaValueException:
                    continue




def validate_https___setuptools_pypa_io_en_latest_deprecated_distutils_configfile_html(data, custom_formats, name_prefix = ({ }, None)):
    if not isinstance(data, dict):
        if not name_prefix:
            name_prefix
        if not name_prefix:
            name_prefix
        raise JsonSchemaValueException('' + 'data' + ' must be object', value = data, name = '' + 'data' + '', definition = {
            '$schema': 'http://json-schema.org/draft-07/schema#',
            '$id': 'https://setuptools.pypa.io/en/latest/deprecated/distutils/configfile.html',
            'title': '``tool.distutils`` table',
            '$$description': [
                '**EXPERIMENTAL** (NOT OFFICIALLY SUPPORTED): Use ``tool.distutils``',
                'subtables to configure arguments for ``distutils`` commands.',
                'Originally, ``distutils`` allowed developers to configure arguments for',
                '``setup.py`` commands via `distutils configuration files',
                '<https://setuptools.pypa.io/en/latest/deprecated/distutils/configfile.html>`_.',
                'See also `the old Python docs <https://docs.python.org/3.11/install/>_`.'],
            'type': 'object',
            'properties': {
                'global': {
                    'type': 'object',
                    'description': 'Global options applied to all ``distutils`` commands' } },
            'patternProperties': {
                '.+': {
                    'type': 'object' } },
            '$comment': 'TODO: Is there a practical way of making this schema more specific?' }, rule = 'type')
    data_is_dict = isinstance(data, dict)
# WARNING: Decompyle incomplete


def validate_https___packaging_python_org_en_latest_specifications_pyproject_toml(data, custom_formats, name_prefix = ({ }, None)):
    pass
# WARNING: Decompyle incomplete


def validate_https___packaging_python_org_en_latest_specifications_pyproject_toml___definitions_dependency(data, custom_formats, name_prefix = ({ }, None)):
    if not isinstance(data, str):
        if not name_prefix:
            name_prefix
        if not name_prefix:
            name_prefix
        raise JsonSchemaValueException('' + 'data' + ' must be string', value = data, name = '' + 'data' + '', definition = {
            '$id': '#/definitions/dependency',
            'title': 'Dependency',
            'type': 'string',
            'description': 'Project dependency specification according to PEP 508',
            'format': 'pep508' }, rule = 'type')
    if not isinstance(data, str) and custom_formats['pep508'](data):
        if not name_prefix:
            name_prefix
        if not name_prefix:
            name_prefix
        raise JsonSchemaValueException('' + 'data' + ' must be pep508', value = data, name = '' + 'data' + '', definition = {
            '$id': '#/definitions/dependency',
            'title': 'Dependency',
            'type': 'string',
            'description': 'Project dependency specification according to PEP 508',
            'format': 'pep508' }, rule = 'format')
    return data


def validate_https___packaging_python_org_en_latest_specifications_pyproject_toml___definitions_entry_point_group(data, custom_formats, name_prefix = ({ }, None)):
    if not isinstance(data, dict):
        if not name_prefix:
            name_prefix
        if not name_prefix:
            name_prefix
        raise JsonSchemaValueException('' + 'data' + ' must be object', value = data, name = '' + 'data' + '', definition = {
            '$id': '#/definitions/entry-point-group',
            'title': 'Entry-points',
            'type': 'object',
            '$$description': [
                'Entry-points are grouped together to indicate what sort of capabilities they',
                'provide.',
                'See the `packaging guides',
                '<https://packaging.python.org/specifications/entry-points/>`_',
                'and `setuptools docs',
                '<https://setuptools.pypa.io/en/latest/userguide/entry_point.html>`_',
                'for more information.'],
            'propertyNames': {
                'format': 'python-entrypoint-name' },
            'additionalProperties': False,
            'patternProperties': {
                '^.+$': {
                    'type': 'string',
                    '$$description': [
                        'Reference to a Python object. It is either in the form',
                        '``importable.module``, or ``importable.module:object.attr``.'],
                    'format': 'python-entrypoint-reference',
                    '$comment': 'https://packaging.python.org/specifications/entry-points/' } } }, rule = 'type')
    data_is_dict = isinstance(data, dict)
# WARNING: Decompyle incomplete


def validate_https___packaging_python_org_en_latest_specifications_pyproject_toml___definitions_author(data, custom_formats, name_prefix = ({ }, None)):
    if not isinstance(data, dict):
        if not name_prefix:
            name_prefix
        if not name_prefix:
            name_prefix
        raise JsonSchemaValueException('' + 'data' + ' must be object', value = data, name = '' + 'data' + '', definition = {
            '$id': '#/definitions/author',
            'title': 'Author or Maintainer',
            '$comment': 'https://peps.python.org/pep-0621/#authors-maintainers',
            'type': 'object',
            'additionalProperties': False,
            'properties': {
                'name': {
                    'type': 'string',
                    '$$description': [
                        'MUST be a valid email name, i.e. whatever can be put as a name, before an',
                        'email, in :rfc:`822`.'] },
                'email': {
                    'type': 'string',
                    'format': 'idn-email',
                    'description': 'MUST be a valid email address' } } }, rule = 'type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_keys = set(data.keys())
        if 'name' in data_keys:
            data_keys.remove('name')
            data__name = data['name']
            if not isinstance(data__name, str):
                if not name_prefix:
                    name_prefix
                if not name_prefix:
                    name_prefix
                raise JsonSchemaValueException('' + 'data' + '.name must be string', value = data__name, name = '' + 'data' + '.name', definition = {
                    'type': 'string',
                    '$$description': [
                        'MUST be a valid email name, i.e. whatever can be put as a name, before an',
                        'email, in :rfc:`822`.'] }, rule = 'type')
        if 'email' in data_keys:
            data_keys.remove('email')
            data__email = data['email']
            if not isinstance(data__email, str):
                if not name_prefix:
                    name_prefix
                if not name_prefix:
                    name_prefix
                raise JsonSchemaValueException('' + 'data' + '.email must be string', value = data__email, name = '' + 'data' + '.email', definition = {
                    'type': 'string',
                    'format': 'idn-email',
                    'description': 'MUST be a valid email address' }, rule = 'type')
            if not isinstance(data__email, str) and REGEX_PATTERNS['idn-email_re_pattern'].match(data__email):
                if not name_prefix:
                    name_prefix
                if not name_prefix:
                    name_prefix
                raise JsonSchemaValueException('' + 'data' + '.email must be idn-email', value = data__email, name = '' + 'data' + '.email', definition = {
                    'type': 'string',
                    'format': 'idn-email',
                    'description': 'MUST be a valid email address' }, rule = 'format')
        if data_keys:
            if not name_prefix:
                name_prefix
            if not name_prefix:
                name_prefix
            raise JsonSchemaValueException('' + 'data' + ' must not contain ' + str(data_keys) + ' properties', value = data, name = '' + 'data' + '', definition = {
                '$id': '#/definitions/author',
                'title': 'Author or Maintainer',
                '$comment': 'https://peps.python.org/pep-0621/#authors-maintainers',
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'name': {
                        'type': 'string',
                        '$$description': [
                            'MUST be a valid email name, i.e. whatever can be put as a name, before an',
                            'email, in :rfc:`822`.'] },
                    'email': {
                        'type': 'string',
                        'format': 'idn-email',
                        'description': 'MUST be a valid email address' } } }, rule = 'additionalProperties')
    return data

