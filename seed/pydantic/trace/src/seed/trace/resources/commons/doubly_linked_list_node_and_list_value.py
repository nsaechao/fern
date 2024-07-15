# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doubly_linked_list_value import DoublyLinkedListValue
from .node_id import NodeId


class DoublyLinkedListNodeAndListValue(UniversalBaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    full_list: DoublyLinkedListValue = pydantic.Field(alias="fullList")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.allow
