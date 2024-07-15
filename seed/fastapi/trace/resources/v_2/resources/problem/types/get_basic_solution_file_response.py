# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....commons.types.language import Language
from .file_info_v_2 import FileInfoV2


class GetBasicSolutionFileResponse(UniversalBaseModel):
    solution_file_by_language: typing.Dict[Language, FileInfoV2] = pydantic.Field(alias="solutionFileByLanguage")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.forbid
