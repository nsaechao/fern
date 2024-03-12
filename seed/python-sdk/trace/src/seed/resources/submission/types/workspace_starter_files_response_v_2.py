# This file was auto-generated by Fern from our API Definition.

import typing
import datetime as dt

from ....core.datetime_utils import serialize_datetime
from ...commons.types.language import Language
from ...v_2.resources.problem.types.files import Files

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore
            
class WorkspaceStarterFilesResponseV2(pydantic.BaseModel):
    files_by_language: typing.Dict[Language, Files] = pydantic.Field(alias="filesByLanguage")
    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = { "by_alias": True, "exclude_unset": True, **kwargs }
        return super().json(**kwargs_with_defaults)
    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = { "by_alias": True, "exclude_unset": True, **kwargs }
        return super().dict(**kwargs_with_defaults)
    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
