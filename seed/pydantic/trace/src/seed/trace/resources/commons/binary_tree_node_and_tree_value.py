# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .binary_tree_value import BinaryTreeValue
from .node_id import NodeId


class BinaryTreeNodeAndTreeValue(UniversalBaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    full_tree: BinaryTreeValue = pydantic.Field(alias="fullTree")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")
    else:

        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.allow
