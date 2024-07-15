# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VariableType_IntegerType(UniversalBaseModel):
    type: typing.Literal["integerType"] = "integerType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow


class VariableType_DoubleType(UniversalBaseModel):
    type: typing.Literal["doubleType"] = "doubleType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow


class VariableType_BooleanType(UniversalBaseModel):
    type: typing.Literal["booleanType"] = "booleanType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow


class VariableType_StringType(UniversalBaseModel):
    type: typing.Literal["stringType"] = "stringType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow


class VariableType_CharType(UniversalBaseModel):
    type: typing.Literal["charType"] = "charType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow


class VariableType_ListType(UniversalBaseModel):
    value_type: VariableType = pydantic.Field(alias="valueType")
    is_fixed_length: typing.Optional[bool] = pydantic.Field(alias="isFixedLength", default=None)
    type: typing.Literal["listType"] = "listType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.allow


class VariableType_MapType(UniversalBaseModel):
    key_type: VariableType = pydantic.Field(alias="keyType")
    value_type: VariableType = pydantic.Field(alias="valueType")
    type: typing.Literal["mapType"] = "mapType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.allow


class VariableType_BinaryTreeType(UniversalBaseModel):
    type: typing.Literal["binaryTreeType"] = "binaryTreeType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow


class VariableType_SinglyLinkedListType(UniversalBaseModel):
    type: typing.Literal["singlyLinkedListType"] = "singlyLinkedListType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow


class VariableType_DoublyLinkedListType(UniversalBaseModel):
    type: typing.Literal["doublyLinkedListType"] = "doublyLinkedListType"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            extra = pydantic.Extra.allow


VariableType = typing.Union[
    VariableType_IntegerType,
    VariableType_DoubleType,
    VariableType_BooleanType,
    VariableType_StringType,
    VariableType_CharType,
    VariableType_ListType,
    VariableType_MapType,
    VariableType_BinaryTreeType,
    VariableType_SinglyLinkedListType,
    VariableType_DoublyLinkedListType,
]
