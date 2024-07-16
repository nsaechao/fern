# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def date(self, value: typing.Optional[dt.date]) -> UnionWithOptionalTime:
        return UnionWithOptionalTime(__root__=_UnionWithOptionalTime.Date(type="date", value=value))

    def dateimte(self, value: typing.Optional[dt.datetime]) -> UnionWithOptionalTime:
        return UnionWithOptionalTime(__root__=_UnionWithOptionalTime.Dateimte(type="dateimte", value=value))


class UnionWithOptionalTime(pydantic_v1.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_UnionWithOptionalTime.Date, _UnionWithOptionalTime.Dateimte]:
        return self.__root__

    def visit(
        self,
        date: typing.Callable[[typing.Optional[dt.date]], T_Result],
        dateimte: typing.Callable[[typing.Optional[dt.datetime]], T_Result],
    ) -> T_Result:
        if self.__root__.type == "date":
            return date(self.__root__.value)
        if self.__root__.type == "dateimte":
            return dateimte(self.__root__.value)

    __root__: typing_extensions.Annotated[
        typing.Union[_UnionWithOptionalTime.Date, _UnionWithOptionalTime.Dateimte],
        pydantic_v1.Field(discriminator="type"),
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _UnionWithOptionalTime:
    class Date(pydantic_v1.BaseModel):
        type: typing.Literal["date"] = "date"
        value: typing.Optional[dt.date] = None

    class Dateimte(pydantic_v1.BaseModel):
        type: typing.Literal["dateimte"] = "dateimte"
        value: typing.Optional[dt.datetime] = None


UnionWithOptionalTime.update_forward_refs()
