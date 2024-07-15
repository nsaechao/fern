# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2


class WorkspaceRunDetails(UniversalBaseModel):
    exception_v_2: typing.Optional[ExceptionV2] = pydantic.Field(alias="exceptionV2", default=None)
    exception: typing.Optional[ExceptionInfo] = None
    stdout: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.allow
