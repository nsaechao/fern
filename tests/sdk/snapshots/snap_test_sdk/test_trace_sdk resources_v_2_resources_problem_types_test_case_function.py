# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .....commons.types.list_type import ListType
from .....commons.types.map_type import MapType
from .....commons.types.variable_type import VariableType
from .test_case_with_actual_result_implementation import TestCaseWithActualResultImplementation
from .void_function_definition import VoidFunctionDefinition


class TestCaseFunction_WithActualResult(TestCaseWithActualResultImplementation):
    type: typing_extensions.Literal["withActualResult"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class TestCaseFunction_Custom(VoidFunctionDefinition):
    type: typing_extensions.Literal["custom"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


TestCaseFunction = typing_extensions.Annotated[
    typing.Union[TestCaseFunction_WithActualResult, TestCaseFunction_Custom], pydantic.Field(discriminator="type")
]
TestCaseFunction_WithActualResult.update_forward_refs(ListType=ListType, MapType=MapType, VariableType=VariableType)
TestCaseFunction_Custom.update_forward_refs(ListType=ListType, MapType=MapType, VariableType=VariableType)
