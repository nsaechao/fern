# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..v_2.resources.problem.test_case_id import TestCaseId
from .test_case_grade import TestCaseGrade


class GradedTestCaseUpdate(UniversalBaseModel):
    test_case_id: TestCaseId = pydantic.Field(alias="testCaseId")
    grade: TestCaseGrade

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.allow
