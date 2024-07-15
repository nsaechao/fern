# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .node_id import NodeId


class DoublyLinkedListNodeValue(UniversalBaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    val: float
    next: typing.Optional[NodeId] = None
    prev: typing.Optional[NodeId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.allow
