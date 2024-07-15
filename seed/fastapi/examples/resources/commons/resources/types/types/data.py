# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, UniversalRootModel

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def string(self, value: str) -> Data:
        return Data(_Data.String(type="string", value=value))

    def base_64(self, value: str) -> Data:
        return Data(_Data.Base64(type="base64", value=value))


class Data(UniversalRootModel):
    """
    Examples
    --------
    from seed.examples.resources.commons import Data_String

    Data_String(value="data")
    """

    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[_Data.String, _Data.Base64], pydantic.Field(discriminator="type")
        ]

        def get_as_union(self) -> typing.Union[_Data.String, _Data.Base64]:
            return self.root

    else:
        __root__: typing_extensions.Annotated[
            typing.Union[_Data.String, _Data.Base64], pydantic.Field(discriminator="type")
        ]

        def get_as_union(self) -> typing.Union[_Data.String, _Data.Base64]:
            return self.__root__

    def visit(self, string: typing.Callable[[str], T_Result], base_64: typing.Callable[[str], T_Result]) -> T_Result:
        if self.get_as_union().type == "string":
            return string(self.get_as_union().value)
        if self.get_as_union().type == "base64":
            return base_64(self.get_as_union().value)


class _Data:
    class String(UniversalBaseModel):
        type: typing.Literal["string"] = "string"
        value: str

    class Base64(UniversalBaseModel):
        type: typing.Literal["base64"] = "base64"
        value: str
