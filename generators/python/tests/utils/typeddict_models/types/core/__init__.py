# This file was auto-generated by Fern from our API Definition.

from .datetime_utils import serialize_datetime
from .pydantic_utilities import (
    IS_PYDANTIC_V2,
    UniversalBaseModel,
    UniversalRootModel,
    deep_union_pydantic_dicts,
    parse_obj_as,
    universal_field_validator,
    universal_root_validator,
    update_forward_refs,
)
from .serialization import FieldMetadata
from .unchecked_base_model import UncheckedBaseModel, UnionMetadata, construct_type

__all__ = [
    "FieldMetadata",
    "IS_PYDANTIC_V2",
    "UncheckedBaseModel",
    "UnionMetadata",
    "UniversalBaseModel",
    "UniversalRootModel",
    "construct_type",
    "deep_union_pydantic_dicts",
    "parse_obj_as",
    "serialize_datetime",
    "universal_field_validator",
    "universal_root_validator",
    "update_forward_refs",
]
