# This file was auto-generated by Fern from our API Definition.

import typing
import datetime as dt

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore
            
class ExceptionInfo(pydantic.BaseModel):
    """
    from seed import ExceptionInfo
    ExceptionInfo(exception_type="Unavailable", exception_message="This component is unavailable!", exception_stacktrace="<logs>", )
    """
    exception_type: str = pydantic.Field(alias="exceptionType")
    exception_message: str = pydantic.Field(alias="exceptionMessage")
    exception_stacktrace: str = pydantic.Field(alias="exceptionStacktrace")
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
