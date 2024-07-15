# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...v_2.resources.problem.types.test_case_id import TestCaseId


class RecordedTestCaseUpdate(UniversalBaseModel):
    test_case_id: TestCaseId = pydantic.Field(alias="testCaseId")
    trace_responses_size: int = pydantic.Field(alias="traceResponsesSize")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.forbid
