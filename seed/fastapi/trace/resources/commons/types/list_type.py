# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class ListType(UniversalBaseModel):
    value_type: VariableType = pydantic.Field(alias="valueType")
    is_fixed_length: typing.Optional[bool] = pydantic.Field(alias="isFixedLength", default=None)
    """
    Whether this list is fixed-size (for languages that supports fixed-size lists). Defaults to false.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.forbid


from .variable_type import VariableType  # noqa: E402

update_forward_refs(ListType)
