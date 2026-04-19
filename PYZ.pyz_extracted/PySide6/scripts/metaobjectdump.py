# Source Generated with Decompyle++
# File: metaobjectdump.pyc (Python 3.12)

from __future__ import annotations
import ast
import json
import os
import sys
import tokenize
from argparse import ArgumentParser, RawTextHelpFormatter
from pathlib import Path
from typing import Union
DESCRIPTION = 'Parses Python source code to create QObject metatype\ninformation in JSON format for qmltyperegistrar.'
REVISION = 68
CPP_TYPE_MAPPING = {
    'str': 'QString' }
QML_IMPORT_NAME = 'QML_IMPORT_NAME'
QML_IMPORT_MAJOR_VERSION = 'QML_IMPORT_MAJOR_VERSION'
QML_IMPORT_MINOR_VERSION = 'QML_IMPORT_MINOR_VERSION'
QT_MODULES = 'QT_MODULES'
ITEM_MODELS = [
    'QAbstractListModel',
    'QAbstractProxyModel',
    'QAbstractTableModel',
    'QConcatenateTablesProxyModel',
    'QFileSystemModel',
    'QIdentityProxyModel',
    'QPdfBookmarkModel',
    'QPdfSearchModel',
    'QSortFilterProxyModel',
    'QSqlQueryModel',
    'QStandardItemModel',
    'QStringListModel',
    'QTransposeProxyModel',
    'QWebEngineHistoryModel']
QOBJECT_DERIVED = [
    'QObject',
    'QQuickItem',
    'QQuickPaintedItem'] + ITEM_MODELS
AstDecorator = Union[(ast.Name, ast.Call)]
AstPySideTypeSpec = Union[(ast.Name, ast.Constant)]
ClassList = list[dict]
PropertyEntry = dict[(str, Union[(str, int, bool)])]
Argument = dict[(str, str)]
Arguments = list[Argument]
Signal = dict[(str, Union[(str, Arguments)])]
Slot = dict[(str, Union[(str, Arguments)])]

def _decorator(name = None, value = None):
    '''Create a QML decorator JSON entry'''
    return {
        'name': name,
        'value': value }


def _attribute(node = None):
    '''Split an attribute.'''
    return (node.value.id, node.attr)


def _name(node = None):
    '''Return the name of something that is either an attribute or a name,
       such as base classes or call.func'''
    if isinstance(node, ast.Constant):
        return str(node.value)
    if None(node, ast.Attribute):
        (qualifier, name) = _attribute(node)
        return f'''{qualifier}.{node.attr}'''
    return None.id


def _func_name(node = None):
    return _name(node.func)


def _python_to_cpp_type(type = None):
    '''Python to C++ type'''
    c = CPP_TYPE_MAPPING.get(type)
    if c:
        return c


def _parse_property_kwargs(keywords = None, prop = None):
    '''Parse keyword arguments of @Property'''
    for k in keywords:
        if not k.arg == 'notify':
            continue
        prop['notify'] = _name(k.value)


def _parse_assignment(node = None):
    '''Parse an assignment and return a tuple of name, value.'''
    if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        var_name = node.targets[0].id
        return (var_name, node.value)


def _parse_pyside_type(type_spec = None):
    '''Parse type specification of a Slot/Property decorator. Usually a type,
       but can also be a string constant with a C++ type name.'''
    if isinstance(type_spec, ast.Constant):
        return type_spec.value
    return None(_name(type_spec))


def _parse_call_args(call = None):
    '''Parse arguments of a Signal call/Slot decorator (type list).'''
    result = []
    for n, arg in enumerate(call.args):
        par_name = f'''a{n + 1}'''
        par_type = _parse_pyside_type(arg)
        result.append({
            'name': par_name,
            'type': par_type })
    return result


def _parse_slot(func_name = None, call = None):
    """Parse a 'Slot' decorator."""
    return_type = 'void'
    for kwarg in call.keywords:
        if not kwarg.arg == 'result':
            continue
        return_type = _python_to_cpp_type(_name(kwarg.value))
        call.keywords
    return {
        'access': 'public',
        'name': func_name,
        'arguments': _parse_call_args(call),
        'returnType': return_type }


class VisitorContext:
    '''Stores a list of QObject-derived classes encountered in order to find
       out which classes inherit QObject.'''
    
    def __init__(self):
        self.qobject_derived = QOBJECT_DERIVED



class MetaObjectDumpVisitor(ast.NodeVisitor):
    pass
# WARNING: Decompyle incomplete


def create_arg_parser(desc = None):
    parser = ArgumentParser(description = desc, formatter_class = RawTextHelpFormatter)
    parser.add_argument('--compact', '-c', action = 'store_true', help = 'Use compact format')
    parser.add_argument('--suppress-file', '-s', action = 'store_true', help = 'Suppress inputFile entry (for testing)')
    parser.add_argument('--quiet', '-q', action = 'store_true', help = 'Suppress warnings')
    parser.add_argument('files', type = str, nargs = '+', help = 'Python source file')
    parser.add_argument('--out-file', '-o', type = str, help = 'Write output to file rather than stdout')
    return parser


def parse_file(file = None, context = None, suppress_file = None):
    '''Parse a file and return its json data'''
    ast_tree = MetaObjectDumpVisitor.create_ast(file)
    visitor = MetaObjectDumpVisitor(context)
    visitor.visit(ast_tree)
    class_list = visitor.json_class_list()
    if not class_list:
        return None
    result = {
        'classes': class_list,
        'outputRevision': REVISION }
    if visitor.qml_import_name():
        result[QML_IMPORT_NAME] = visitor.qml_import_name()
    qml_import_version = visitor.qml_import_version()
    if qml_import_version[0]:
        result[QML_IMPORT_MAJOR_VERSION] = qml_import_version[0]
        result[QML_IMPORT_MINOR_VERSION] = qml_import_version[1]
    qt_modules = visitor.qt_modules()
    if qt_modules:
        result[QT_MODULES] = qt_modules
    if not suppress_file:
        result['inputFile'] = os.fspath(file).replace('\\', '/')
    return result

if __name__ == '__main__':
    arg_parser = create_arg_parser(DESCRIPTION)
    args = arg_parser.parse_args()
    context = VisitorContext()
    json_list = []
    for file_name in args.files:
        file = Path(file_name).resolve()
        if not file.is_file():
            print(f'''{file_name} does not exist or is not a file.''', file = sys.stderr)
            sys.exit(-1)
        json_data = parse_file(file, context, args.suppress_file)
        if json_data:
            json_list.append(json_data)
        elif not args.quiet:
            print(f'''No classes found in {file_name}''', file = sys.stderr)
    continue
    indent = None if args.compact else 4
    if args.out_file:
        f = open(args.out_file, 'w')
        json.dump(json_list, f, indent = indent)
        None(None, None)
        return None
    json.dump(json_list, sys.stdout, indent = indent)
    return None
return None
except (AttributeError, SyntaxError):
    e = None
    reason = str(e)
    print(f'''Error parsing {file_name}: {reason}''', file = sys.stderr)
    raise 
    e = None
    del e
with None:
    if not None:
        pass
