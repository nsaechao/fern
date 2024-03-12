# This file was auto-generated by Fern from our API Definition.

import typing
import datetime as dt

from .trace_response_v_2 import TraceResponseV2
from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore
            
class TraceResponsesPageV2(pydantic.BaseModel):
    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    If present, use this to load subseqent pages.
    The offset is the id of the next trace response to load.
    """
    
    trace_responses: typing.List[TraceResponseV2] = pydantic.Field(alias="traceResponses")
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
