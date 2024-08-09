# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, UniversalRootModel

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def value(self, value: int) -> UnionWithTime:
        if IS_PYDANTIC_V2:
            return UnionWithTime(root=_UnionWithTime.Value(type="value", value=value))
        else:
            return UnionWithTime(__root__=_UnionWithTime.Value(type="value", value=value))

    def date(self, value: dt.date) -> UnionWithTime:
        if IS_PYDANTIC_V2:
            return UnionWithTime(root=_UnionWithTime.Date(type="date", value=value))
        else:
            return UnionWithTime(__root__=_UnionWithTime.Date(type="date", value=value))

    def datetime(self, value: dt.datetime) -> UnionWithTime:
        if IS_PYDANTIC_V2:
            return UnionWithTime(root=_UnionWithTime.Datetime(type="datetime", value=value))
        else:
            return UnionWithTime(__root__=_UnionWithTime.Datetime(type="datetime", value=value))


class UnionWithTime(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[_UnionWithTime.Value, _UnionWithTime.Date, _UnionWithTime.Datetime],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_UnionWithTime.Value, _UnionWithTime.Date, _UnionWithTime.Datetime]:
            return self.root

    else:
        __root__: typing_extensions.Annotated[
            typing.Union[_UnionWithTime.Value, _UnionWithTime.Date, _UnionWithTime.Datetime],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_UnionWithTime.Value, _UnionWithTime.Date, _UnionWithTime.Datetime]:
            return self.__root__

    def visit(
        self,
        value: typing.Callable[[int], T_Result],
        date: typing.Callable[[dt.date], T_Result],
        datetime: typing.Callable[[dt.datetime], T_Result],
    ) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "value":
            return value(unioned_value.value)
        if unioned_value.type == "date":
            return date(unioned_value.value)
        if unioned_value.type == "datetime":
            return datetime(unioned_value.value)


class _UnionWithTime:
    class Value(UniversalBaseModel):
        type: typing.Literal["value"] = "value"
        value: int

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
        else:

            class Config:
                frozen = True
                smart_union = True

    class Date(UniversalBaseModel):
        type: typing.Literal["date"] = "date"
        value: dt.date

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
        else:

            class Config:
                frozen = True
                smart_union = True

    class Datetime(UniversalBaseModel):
        type: typing.Literal["datetime"] = "datetime"
        value: dt.datetime

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
        else:

            class Config:
                frozen = True
                smart_union = True
