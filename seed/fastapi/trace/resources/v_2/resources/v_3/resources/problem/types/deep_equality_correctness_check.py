# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ........core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parameter_id import ParameterId


class DeepEqualityCorrectnessCheck(UniversalBaseModel):
    expected_value_parameter_id: ParameterId = pydantic.Field(alias="expectedValueParameterId")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.forbid
