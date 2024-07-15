# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invalid_request_cause import InvalidRequestCause
from .submission_request import SubmissionRequest


class InvalidRequestResponse(UniversalBaseModel):
    request: SubmissionRequest
    cause: InvalidRequestCause

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow
