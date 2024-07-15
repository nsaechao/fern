# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...commons.types.language import Language
from .workspace_files import WorkspaceFiles


class WorkspaceStarterFilesResponse(UniversalBaseModel):
    files: typing.Dict[Language, WorkspaceFiles]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            extra = pydantic.Extra.forbid
