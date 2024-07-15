# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .object_with_optional_field import ObjectWithOptionalField


class NestedObjectWithOptionalField(UniversalBaseModel):
    string: typing.Optional[str] = None
    nested_object: typing.Optional[ObjectWithOptionalField] = pydantic.Field(alias="NestedObject", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            allow_population_by_field_name = True
            extra = pydantic.Extra.allow
