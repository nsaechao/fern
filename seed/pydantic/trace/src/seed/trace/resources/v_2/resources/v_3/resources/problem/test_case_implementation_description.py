# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from .......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .test_case_implementation_description_board import TestCaseImplementationDescriptionBoard


class TestCaseImplementationDescription(UniversalBaseModel):
    boards: typing.List[TestCaseImplementationDescriptionBoard]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow
