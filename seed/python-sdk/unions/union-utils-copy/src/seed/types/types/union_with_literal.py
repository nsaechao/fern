# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def fern(self, value: typing.Literal["fern"]) -> UnionWithLiteral:
        return UnionWithLiteral(_UnionWithLiteral.Fern(type="fern", value=value))


if IS_PYDANTIC_V2:

    class _UnionWithLiteralBase(UniversalBaseModel, pydantic.RootModel):

        root: typing.Union[_UnionWithLiteral.Fern]

        def get_as_union(self) -> typing.Union[_UnionWithLiteral.Fern]:
            return self.root

else:

    class _UnionWithLiteralBase(UniversalBaseModel):

        __root__: typing.Union[_UnionWithLiteral.Fern]

        def get_as_union(self) -> typing.Union[_UnionWithLiteral.Fern]:
            return self.__root__


class UnionWithLiteral(_UnionWithLiteralBase):
    factory: typing.ClassVar[_Factory] = _Factory()

    def visit(self, fern: typing.Callable[[typing.Literal["fern"]], T_Result]) -> T_Result:
        if self.get_as_union().type == "fern":
            return fern(self.get_as_union().value)


class _UnionWithLiteral:
    class Fern(UniversalBaseModel):
        type: typing.Literal["fern"] = "fern"
        value: typing.Literal["fern"]

        if IS_PYDANTIC_V2:
            model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
        else:

            class Config:
                frozen = True
                smart_union = True
