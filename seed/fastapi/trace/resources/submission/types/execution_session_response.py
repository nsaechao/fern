# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...commons.types.language import Language
from .execution_session_status import ExecutionSessionStatus


class ExecutionSessionResponse(UniversalBaseModel):
    session_id: str = pydantic.Field(alias="sessionId")
    execution_session_url: typing.Optional[str] = pydantic.Field(alias="executionSessionUrl", default=None)
    language: Language
    status: ExecutionSessionStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.forbid
