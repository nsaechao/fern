# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import typing
class Cat(UniversalBaseModel):
    name: str
    likes_to_meow: bool = pydantic.Field(alias="likesToMeow")
    
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")
    else:
        class Config:
            allow_population_by_field_name = True
            extra = pydantic.Extra.forbid
