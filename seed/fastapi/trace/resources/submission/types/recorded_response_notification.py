# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .submission_id import SubmissionId


class RecordedResponseNotification(UniversalBaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    trace_responses_size: int = pydantic.Field(alias="traceResponsesSize")
    test_case_id: typing.Optional[str] = pydantic.Field(alias="testCaseId", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.forbid
