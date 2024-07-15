# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class DebugMapValue(UniversalBaseModel):
    key_value_pairs: typing.List[DebugKeyValuePairs] = pydantic.Field(alias="keyValuePairs")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.forbid


from .debug_key_value_pairs import DebugKeyValuePairs  # noqa: E402

update_forward_refs(DebugMapValue)
