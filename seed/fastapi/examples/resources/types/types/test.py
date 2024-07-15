# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, UniversalRootModel

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def and_(self, value: bool) -> Test:
        return Test(_Test.And(type="and", value=value))

    def or_(self, value: bool) -> Test:
        return Test(_Test.Or(type="or", value=value))


class Test(UniversalRootModel):
    """
    Examples
    --------
    from seed.examples import Test_And

    Test_And(value=True)
    """

    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[typing.Union[_Test.And, _Test.Or], pydantic.Field(discriminator="type")]

        def get_as_union(self) -> typing.Union[_Test.And, _Test.Or]:
            return self.root

    else:
        __root__: typing_extensions.Annotated[typing.Union[_Test.And, _Test.Or], pydantic.Field(discriminator="type")]

        def get_as_union(self) -> typing.Union[_Test.And, _Test.Or]:
            return self.__root__

    def visit(self, and_: typing.Callable[[bool], T_Result], or_: typing.Callable[[bool], T_Result]) -> T_Result:
        if self.get_as_union().type == "and":
            return and_(self.get_as_union().value)
        if self.get_as_union().type == "or":
            return or_(self.get_as_union().value)


class _Test:
    class And(UniversalBaseModel):
        type: typing.Literal["and"] = "and"
        value: bool

    class Or(UniversalBaseModel):
        type: typing.Literal["or"] = "or"
        value: bool
