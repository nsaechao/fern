# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_info import FileInfo


class File(UniversalBaseModel):
    """
    Examples
    --------
    from seed import File

    File(
        name="file.txt",
        contents="...",
        info="REGULAR",
    )
    """

    name: str
    contents: str
    info: FileInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
