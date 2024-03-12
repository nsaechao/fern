# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .tag import Tag
from .metadata import Metadata

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore
            
class EventInfo_Metadata(Metadata):
    type: typing.Literal["metadata"]
    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
class EventInfo_Tag(pydantic.BaseModel):
    type: typing.Literal["tag"]
    value: Tag
    class Config:
        frozen = True
        smart_union = True
"""
from seed.resources.commons import EventInfo_Metadata
EventInfo_Metadata(type="metadata", id="metadata-alskjfg8", data={"one": "two"}, json_string='{"one": "two"}', )
"""
EventInfo = typing.Union[EventInfo_Metadata, EventInfo_Tag]
