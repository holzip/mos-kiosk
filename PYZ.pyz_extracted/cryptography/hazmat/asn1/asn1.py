# Source Generated with Decompyle++
# File: asn1.pyc (Python 3.12)

from __future__ import annotations
import dataclasses
import sys
import typing
if sys.version_info < (3, 11):
    import typing_extensions
    if sys.version_info < (3, 9):
        get_type_hints = typing_extensions.get_type_hints
    else:
        get_type_hints = typing.get_type_hints
else:
    get_type_hints = typing.get_type_hints
from cryptography.hazmat.bindings._rust import declarative_asn1
T = typing.TypeVar('T', covariant = True)
U = typing.TypeVar('U')
encode_der = declarative_asn1.encode_der

def _normalize_field_type(field_type = None, field_name = None):
    annotation = declarative_asn1.Annotation()
    if hasattr(field_type, '__asn1_root__'):
        annotated_root = field_type.__asn1_root__
        if not isinstance(annotated_root, declarative_asn1.AnnotatedType):
            raise TypeError(f'''unsupported root type: {annotated_root}''')
        return annotated_root
    rust_field_type = None.non_root_python_to_rust(field_type)
    return declarative_asn1.AnnotatedType(rust_field_type, annotation)


def _annotate_fields(raw_fields = None):
    fields = { }
    for field_name, field_type in raw_fields.items():
        annotated_field_type = _normalize_field_type(field_type, field_name)
        fields[field_name] = annotated_field_type
    return fields


def _register_asn1_sequence(cls = None):
    raw_fields = get_type_hints(cls, include_extras = True)
    root = declarative_asn1.AnnotatedType(declarative_asn1.Type.Sequence(cls, _annotate_fields(raw_fields)), declarative_asn1.Annotation())
    setattr(cls, '__asn1_root__', root)

if sys.version_info < (3, 11):
    sequence = (lambda cls = None: if sys.version_info >= (3, 10):
dataclass_cls = dataclasses.dataclass(repr = False, eq = False, match_args = False, kw_only = True)(cls)else:
dataclass_cls = dataclasses.dataclass(repr = False, eq = False)(cls)_register_asn1_sequence(dataclass_cls)dataclass_cls)()
    return None
sequence = (lambda cls = None: dataclass_cls = dataclasses.dataclass(repr = False, eq = False, match_args = False, kw_only = True)(cls)_register_asn1_sequence(dataclass_cls)dataclass_cls)()
