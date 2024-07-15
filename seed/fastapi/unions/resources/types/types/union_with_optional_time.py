# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, UniversalRootModel

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def date(self, value: typing.Optional[dt.date]) -> UnionWithOptionalTime:
        return UnionWithOptionalTime(_UnionWithOptionalTime.Date(type="date", value=value))

    def dateimte(self, value: typing.Optional[dt.datetime]) -> UnionWithOptionalTime:
        return UnionWithOptionalTime(_UnionWithOptionalTime.Dateimte(type="dateimte", value=value))


class UnionWithOptionalTime(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[_UnionWithOptionalTime.Date, _UnionWithOptionalTime.Dateimte],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_UnionWithOptionalTime.Date, _UnionWithOptionalTime.Dateimte]:
            return self.root

    else:
        __root__: typing_extensions.Annotated[
            typing.Union[_UnionWithOptionalTime.Date, _UnionWithOptionalTime.Dateimte],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_UnionWithOptionalTime.Date, _UnionWithOptionalTime.Dateimte]:
            return self.__root__

    def visit(
        self,
        date: typing.Callable[[typing.Optional[dt.date]], T_Result],
        dateimte: typing.Callable[[typing.Optional[dt.datetime]], T_Result],
    ) -> T_Result:
        if self.get_as_union().type == "date":
            return date(self.get_as_union().value)
        if self.get_as_union().type == "dateimte":
            return dateimte(self.get_as_union().value)


class _UnionWithOptionalTime:
    class Date(UniversalBaseModel):
        type: typing.Literal["date"] = "date"
        value: typing.Optional[dt.date] = None

    class Dateimte(UniversalBaseModel):
        type: typing.Literal["dateimte"] = "dateimte"
        value: typing.Optional[dt.datetime] = None
