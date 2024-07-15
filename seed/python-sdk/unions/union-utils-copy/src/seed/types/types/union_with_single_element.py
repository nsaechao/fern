# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .foo import Foo as types_types_foo_Foo

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def foo(self, value: types_types_foo_Foo) -> UnionWithSingleElement:
        return UnionWithSingleElement(_UnionWithSingleElement.Foo(**value.dict(exclude_unset=True), type="foo"))


if IS_PYDANTIC_V2:

    class _UnionWithSingleElementBase(UniversalBaseModel, pydantic.RootModel):

        root: typing.Union[_UnionWithSingleElement.Foo]

        def get_as_union(self) -> typing.Union[_UnionWithSingleElement.Foo]:
            return self.root

else:

    class _UnionWithSingleElementBase(UniversalBaseModel):

        __root__: typing.Union[_UnionWithSingleElement.Foo]

        def get_as_union(self) -> typing.Union[_UnionWithSingleElement.Foo]:
            return self.__root__


class UnionWithSingleElement(_UnionWithSingleElementBase):
    factory: typing.ClassVar[_Factory] = _Factory()

    def visit(self, foo: typing.Callable[[types_types_foo_Foo], T_Result]) -> T_Result:
        if self.get_as_union().type == "foo":
            return foo(types_types_foo_Foo(**self.get_as_union().dict(exclude_unset=True, exclude={"type"})))


class _UnionWithSingleElement:
    class Foo(types_types_foo_Foo):
        type: typing.Literal["foo"] = "foo"

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
        else:

            class Config:
                frozen = True
                smart_union = True
                allow_population_by_field_name = True
