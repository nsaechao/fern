# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def value(self, value: int) -> UnionWithTime:
        return UnionWithTime(_UnionWithTime.Value(type="value", value=value))

    def date(self, value: dt.date) -> UnionWithTime:
        return UnionWithTime(_UnionWithTime.Date(type="date", value=value))

    def datetime(self, value: dt.datetime) -> UnionWithTime:
        return UnionWithTime(_UnionWithTime.Datetime(type="datetime", value=value))


if IS_PYDANTIC_V2:

    class _UnionWithTimeBase(UniversalBaseModel, pydantic.RootModel):

        root: typing_extensions.Annotated[
            typing.Union[_UnionWithTime.Value, _UnionWithTime.Date, _UnionWithTime.Datetime],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_UnionWithTime.Value, _UnionWithTime.Date, _UnionWithTime.Datetime]:
            return self.root

else:

    class _UnionWithTimeBase(UniversalBaseModel):

        __root__: typing_extensions.Annotated[
            typing.Union[_UnionWithTime.Value, _UnionWithTime.Date, _UnionWithTime.Datetime],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_UnionWithTime.Value, _UnionWithTime.Date, _UnionWithTime.Datetime]:
            return self.__root__


class UnionWithTime(_UnionWithTimeBase):
    factory: typing.ClassVar[_Factory] = _Factory()

    def visit(
        self,
        value: typing.Callable[[int], T_Result],
        date: typing.Callable[[dt.date], T_Result],
        datetime: typing.Callable[[dt.datetime], T_Result],
    ) -> T_Result:
        if self.get_as_union().type == "value":
            return value(self.get_as_union().value)
        if self.get_as_union().type == "date":
            return date(self.get_as_union().value)
        if self.get_as_union().type == "datetime":
            return datetime(self.get_as_union().value)


class _UnionWithTime:
    class Value(UniversalBaseModel):
        type: typing.Literal["value"] = "value"
        value: int

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
        else:

            class Config:
                frozen = True
                smart_union = True

    class Date(UniversalBaseModel):
        type: typing.Literal["date"] = "date"
        value: dt.date

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
        else:

            class Config:
                frozen = True
                smart_union = True

    class Datetime(UniversalBaseModel):
        type: typing.Literal["datetime"] = "datetime"
        value: dt.datetime

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
        else:

            class Config:
                frozen = True
                smart_union = True
