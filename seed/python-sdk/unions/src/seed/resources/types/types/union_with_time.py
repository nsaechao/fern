# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing
import datetime as dt

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore
            
class UnionWithTime_Value(pydantic.BaseModel):
    type: typing.Literal["value"]
    value: int
    class Config:
        frozen = True
        smart_union = True
class UnionWithTime_Date(pydantic.BaseModel):
    type: typing.Literal["date"]
    value: dt.date
    class Config:
        frozen = True
        smart_union = True
class UnionWithTime_Datetime(pydantic.BaseModel):
    type: typing.Literal["datetime"]
    value: dt.datetime
    class Config:
        frozen = True
        smart_union = True
UnionWithTime = typing.Union[UnionWithTime_Value, UnionWithTime_Date, UnionWithTime_Datetime]
