# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bar import Bar as types_types_bar_Bar
from .foo import Foo as types_types_foo_Foo

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def foo(self, value: types_types_foo_Foo) -> UnionWithoutKey:
        return UnionWithoutKey(_UnionWithoutKey.Foo(**value.dict(exclude_unset=True), type="foo"))

    def bar(self, value: types_types_bar_Bar) -> UnionWithoutKey:
        return UnionWithoutKey(_UnionWithoutKey.Bar(**value.dict(exclude_unset=True), type="bar"))


if IS_PYDANTIC_V2:

    class _UnionWithoutKeyBase(UniversalBaseModel, pydantic.RootModel):

        root: typing_extensions.Annotated[
            typing.Union[_UnionWithoutKey.Foo, _UnionWithoutKey.Bar], pydantic.Field(discriminator="type")
        ]

        def get_as_union(self) -> typing.Union[_UnionWithoutKey.Foo, _UnionWithoutKey.Bar]:
            return self.root

else:

    class _UnionWithoutKeyBase(UniversalBaseModel):

        __root__: typing_extensions.Annotated[
            typing.Union[_UnionWithoutKey.Foo, _UnionWithoutKey.Bar], pydantic.Field(discriminator="type")
        ]

        def get_as_union(self) -> typing.Union[_UnionWithoutKey.Foo, _UnionWithoutKey.Bar]:
            return self.__root__


class UnionWithoutKey(_UnionWithoutKeyBase):
    factory: typing.ClassVar[_Factory] = _Factory()

    def visit(
        self,
        foo: typing.Callable[[types_types_foo_Foo], T_Result],
        bar: typing.Callable[[types_types_bar_Bar], T_Result],
    ) -> T_Result:
        if self.get_as_union().type == "foo":
            return foo(types_types_foo_Foo(**self.get_as_union().dict(exclude_unset=True, exclude={"type"})))
        if self.get_as_union().type == "bar":
            return bar(types_types_bar_Bar(**self.get_as_union().dict(exclude_unset=True, exclude={"type"})))


class _UnionWithoutKey:
    class Foo(types_types_foo_Foo):
        type: typing.Literal["foo"] = "foo"

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
        else:

            class Config:
                frozen = True
                smart_union = True
                allow_population_by_field_name = True

    class Bar(types_types_bar_Bar):
        type: typing.Literal["bar"] = "bar"

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
        else:

            class Config:
                frozen = True
                smart_union = True
                allow_population_by_field_name = True
