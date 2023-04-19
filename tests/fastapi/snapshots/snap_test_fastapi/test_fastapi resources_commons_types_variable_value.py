# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .binary_tree_value import BinaryTreeValue as resources_commons_types_binary_tree_value_BinaryTreeValue
from .doubly_linked_list_value import (
    DoublyLinkedListValue as resources_commons_types_doubly_linked_list_value_DoublyLinkedListValue,
)
from .singly_linked_list_value import (
    SinglyLinkedListValue as resources_commons_types_singly_linked_list_value_SinglyLinkedListValue,
)

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def integer_value(self, value: int) -> VariableValue:
        return VariableValue(__root__=_VariableValue.IntegerValue(type="integerValue", value=value))

    def boolean_value(self, value: bool) -> VariableValue:
        return VariableValue(__root__=_VariableValue.BooleanValue(type="booleanValue", value=value))

    def double_value(self, value: float) -> VariableValue:
        return VariableValue(__root__=_VariableValue.DoubleValue(type="doubleValue", value=value))

    def string_value(self, value: str) -> VariableValue:
        return VariableValue(__root__=_VariableValue.StringValue(type="stringValue", value=value))

    def char_value(self, value: str) -> VariableValue:
        return VariableValue(__root__=_VariableValue.CharValue(type="charValue", value=value))

    def map_value(self, value: resources_commons_types_map_value_MapValue) -> VariableValue:
        return VariableValue(__root__=_VariableValue.MapValue(**value.dict(exclude_unset=True), type="mapValue"))

    def list_value(self, value: typing.List[VariableValue]) -> VariableValue:
        return VariableValue(__root__=_VariableValue.ListValue(type="listValue", value=value))

    def binary_tree_value(self, value: resources_commons_types_binary_tree_value_BinaryTreeValue) -> VariableValue:
        return VariableValue(
            __root__=_VariableValue.BinaryTreeValue(**value.dict(exclude_unset=True), type="binaryTreeValue")
        )

    def singly_linked_list_value(
        self, value: resources_commons_types_singly_linked_list_value_SinglyLinkedListValue
    ) -> VariableValue:
        return VariableValue(
            __root__=_VariableValue.SinglyLinkedListValue(
                **value.dict(exclude_unset=True), type="singlyLinkedListValue"
            )
        )

    def doubly_linked_list_value(
        self, value: resources_commons_types_doubly_linked_list_value_DoublyLinkedListValue
    ) -> VariableValue:
        return VariableValue(
            __root__=_VariableValue.DoublyLinkedListValue(
                **value.dict(exclude_unset=True), type="doublyLinkedListValue"
            )
        )

    def null_value(self) -> VariableValue:
        return VariableValue(__root__=_VariableValue.NullValue(type="nullValue"))


class VariableValue(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _VariableValue.IntegerValue,
        _VariableValue.BooleanValue,
        _VariableValue.DoubleValue,
        _VariableValue.StringValue,
        _VariableValue.CharValue,
        _VariableValue.MapValue,
        _VariableValue.ListValue,
        _VariableValue.BinaryTreeValue,
        _VariableValue.SinglyLinkedListValue,
        _VariableValue.DoublyLinkedListValue,
        _VariableValue.NullValue,
    ]:
        return self.__root__

    def visit(
        self,
        integer_value: typing.Callable[[int], T_Result],
        boolean_value: typing.Callable[[bool], T_Result],
        double_value: typing.Callable[[float], T_Result],
        string_value: typing.Callable[[str], T_Result],
        char_value: typing.Callable[[str], T_Result],
        map_value: typing.Callable[[resources_commons_types_map_value_MapValue], T_Result],
        list_value: typing.Callable[[typing.List[VariableValue]], T_Result],
        binary_tree_value: typing.Callable[[resources_commons_types_binary_tree_value_BinaryTreeValue], T_Result],
        singly_linked_list_value: typing.Callable[
            [resources_commons_types_singly_linked_list_value_SinglyLinkedListValue], T_Result
        ],
        doubly_linked_list_value: typing.Callable[
            [resources_commons_types_doubly_linked_list_value_DoublyLinkedListValue], T_Result
        ],
        null_value: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self.__root__.type == "integerValue":
            return integer_value(self.__root__.value)
        if self.__root__.type == "booleanValue":
            return boolean_value(self.__root__.value)
        if self.__root__.type == "doubleValue":
            return double_value(self.__root__.value)
        if self.__root__.type == "stringValue":
            return string_value(self.__root__.value)
        if self.__root__.type == "charValue":
            return char_value(self.__root__.value)
        if self.__root__.type == "mapValue":
            return map_value(self.__root__)
        if self.__root__.type == "listValue":
            return list_value(self.__root__.value)
        if self.__root__.type == "binaryTreeValue":
            return binary_tree_value(self.__root__)
        if self.__root__.type == "singlyLinkedListValue":
            return singly_linked_list_value(self.__root__)
        if self.__root__.type == "doublyLinkedListValue":
            return doubly_linked_list_value(self.__root__)
        if self.__root__.type == "nullValue":
            return null_value()

    __root__: typing_extensions.Annotated[
        typing.Union[
            _VariableValue.IntegerValue,
            _VariableValue.BooleanValue,
            _VariableValue.DoubleValue,
            _VariableValue.StringValue,
            _VariableValue.CharValue,
            _VariableValue.MapValue,
            _VariableValue.ListValue,
            _VariableValue.BinaryTreeValue,
            _VariableValue.SinglyLinkedListValue,
            _VariableValue.DoublyLinkedListValue,
            _VariableValue.NullValue,
        ],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @VariableValue.Validators.validate
            def validate(value: typing.Union[_VariableValue.IntegerValue, _VariableValue.BooleanValue, _VariableValue.DoubleValue, _VariableValue.StringValue, _VariableValue.CharValue, _VariableValue.MapValue, _VariableValue.ListValue, _VariableValue.BinaryTreeValue, _VariableValue.SinglyLinkedListValue, _VariableValue.DoublyLinkedListValue, _VariableValue.NullValue]) -> typing.Union[_VariableValue.IntegerValue, _VariableValue.BooleanValue, _VariableValue.DoubleValue, _VariableValue.StringValue, _VariableValue.CharValue, _VariableValue.MapValue, _VariableValue.ListValue, _VariableValue.BinaryTreeValue, _VariableValue.SinglyLinkedListValue, _VariableValue.DoublyLinkedListValue, _VariableValue.NullValue]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _VariableValue.IntegerValue,
                            _VariableValue.BooleanValue,
                            _VariableValue.DoubleValue,
                            _VariableValue.StringValue,
                            _VariableValue.CharValue,
                            _VariableValue.MapValue,
                            _VariableValue.ListValue,
                            _VariableValue.BinaryTreeValue,
                            _VariableValue.SinglyLinkedListValue,
                            _VariableValue.DoublyLinkedListValue,
                            _VariableValue.NullValue,
                        ]
                    ],
                    typing.Union[
                        _VariableValue.IntegerValue,
                        _VariableValue.BooleanValue,
                        _VariableValue.DoubleValue,
                        _VariableValue.StringValue,
                        _VariableValue.CharValue,
                        _VariableValue.MapValue,
                        _VariableValue.ListValue,
                        _VariableValue.BinaryTreeValue,
                        _VariableValue.SinglyLinkedListValue,
                        _VariableValue.DoublyLinkedListValue,
                        _VariableValue.NullValue,
                    ],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [
                    typing.Union[
                        _VariableValue.IntegerValue,
                        _VariableValue.BooleanValue,
                        _VariableValue.DoubleValue,
                        _VariableValue.StringValue,
                        _VariableValue.CharValue,
                        _VariableValue.MapValue,
                        _VariableValue.ListValue,
                        _VariableValue.BinaryTreeValue,
                        _VariableValue.SinglyLinkedListValue,
                        _VariableValue.DoublyLinkedListValue,
                        _VariableValue.NullValue,
                    ]
                ],
                typing.Union[
                    _VariableValue.IntegerValue,
                    _VariableValue.BooleanValue,
                    _VariableValue.DoubleValue,
                    _VariableValue.StringValue,
                    _VariableValue.CharValue,
                    _VariableValue.MapValue,
                    _VariableValue.ListValue,
                    _VariableValue.BinaryTreeValue,
                    _VariableValue.SinglyLinkedListValue,
                    _VariableValue.DoublyLinkedListValue,
                    _VariableValue.NullValue,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[
                _VariableValue.IntegerValue,
                _VariableValue.BooleanValue,
                _VariableValue.DoubleValue,
                _VariableValue.StringValue,
                _VariableValue.CharValue,
                _VariableValue.MapValue,
                _VariableValue.ListValue,
                _VariableValue.BinaryTreeValue,
                _VariableValue.SinglyLinkedListValue,
                _VariableValue.DoublyLinkedListValue,
                _VariableValue.NullValue,
            ],
            values.get("__root__"),
        )
        for validator in VariableValue.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


from .key_value_pair import KeyValuePair  # noqa: E402
from .map_value import MapValue as resources_commons_types_map_value_MapValue  # noqa: E402


class _VariableValue:
    class IntegerValue(pydantic.BaseModel):
        type: typing_extensions.Literal["integerValue"]
        value: int

    class BooleanValue(pydantic.BaseModel):
        type: typing_extensions.Literal["booleanValue"]
        value: bool

    class DoubleValue(pydantic.BaseModel):
        type: typing_extensions.Literal["doubleValue"]
        value: float

    class StringValue(pydantic.BaseModel):
        type: typing_extensions.Literal["stringValue"]
        value: str

    class CharValue(pydantic.BaseModel):
        type: typing_extensions.Literal["charValue"]
        value: str

    class MapValue(resources_commons_types_map_value_MapValue):
        type: typing_extensions.Literal["mapValue"]

        class Config:
            allow_population_by_field_name = True

    class ListValue(pydantic.BaseModel):
        type: typing_extensions.Literal["listValue"]
        value: typing.List[VariableValue]

    class BinaryTreeValue(resources_commons_types_binary_tree_value_BinaryTreeValue):
        type: typing_extensions.Literal["binaryTreeValue"]

        class Config:
            allow_population_by_field_name = True

    class SinglyLinkedListValue(resources_commons_types_singly_linked_list_value_SinglyLinkedListValue):
        type: typing_extensions.Literal["singlyLinkedListValue"]

        class Config:
            allow_population_by_field_name = True

    class DoublyLinkedListValue(resources_commons_types_doubly_linked_list_value_DoublyLinkedListValue):
        type: typing_extensions.Literal["doublyLinkedListValue"]

        class Config:
            allow_population_by_field_name = True

    class NullValue(pydantic.BaseModel):
        type: typing_extensions.Literal["nullValue"]


_VariableValue.MapValue.update_forward_refs(
    KeyValuePair=KeyValuePair, MapValue=resources_commons_types_map_value_MapValue, VariableValue=VariableValue
)
VariableValue.update_forward_refs()
