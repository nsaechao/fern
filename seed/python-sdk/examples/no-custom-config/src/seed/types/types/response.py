# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..identifier import Identifier


class Response(UniversalBaseModel):
    """
    Examples
    --------
    from seed import Identifier, Response

    Response(
        response="Initializing...",
        identifiers=[
            Identifier(
                type="primitive",
                value="example",
                label="Primitive",
            ),
            Identifier(
                type="unknown",
                value="{}",
                label="Unknown",
            ),
        ],
    )
    """

    response: typing.Any
    identifiers: typing.List[Identifier]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
