# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .migration_status import MigrationStatus


class Migration(UniversalBaseModel):
    """
    Examples
    --------
    from seed.examples import Migration, MigrationStatus

    Migration(
        name="001_init",
        status=MigrationStatus.RUNNING,
    )
    """

    name: str
    status: MigrationStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:

        class Config:
            extra = pydantic.Extra.forbid
