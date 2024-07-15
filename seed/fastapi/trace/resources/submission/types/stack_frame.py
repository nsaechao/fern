# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scope import Scope


class StackFrame(UniversalBaseModel):
    method_name: str = pydantic.Field(alias="methodName")
    line_number: int = pydantic.Field(alias="lineNumber")
    scopes: typing.List[Scope]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.forbid
